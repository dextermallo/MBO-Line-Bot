import datetime
import uuid
import json

from .line_bot.models import UserMessage
from .aws.database import db


class DailyTask:

    daily_task_id: str
    user_display_name: str
    user_id: str
    date: str
    status: str
    order: int
    description: str

    def __init__(self, user_display_name, user_id, order, description):

        # default to tomorrow
        now = datetime.datetime.now() + datetime.timedelta(days=1)

        self.daily_task_id = str(uuid.uuid1())
        self.user_display_name = user_display_name
        self.user_id = user_id
        self.date = f'{now.year}/{now.month}/{now.day}'
        self.status = 'todo'
        self.order = order
        self.description = description

    def to_dict(self):
        return {
            'daily_task_id': self.daily_task_id,
            'user_display_name': self.user_display_name,
            'user_id': self.user_id,
            'date': self.date,
            'status': self.status,
            'order': self.order,
            'description': self.description
        }

    def save(self):
        table = db().Table('daily_task')
        table.put_item(Item=self.to_dict())


class DailyTaskSummary:
    daily_task: list
    user_id: str

    def __init__(self):
        self.daily_task = []
        self.user_id = ''

    def save(self, message: UserMessage):

        daily_task = []

        for msg in message.clean_msg:

            task = DailyTask(
                user_display_name=message.user_display_name,
                user_id=message.user_id,
                order=msg['order'],
                description=msg['description']
            )

            task.save()
            daily_task.append(task)

        self.daily_task = daily_task

    def on_create_msg(self):

        ret = '紀錄成功😎\n明天目標如下：\n'
        for task in self.daily_task:
            ret += '{order}: {description}\n'.format(**task.to_dict())

        return ret.rstrip('\n')


# Loader for message to reply user.
class ReplyLoader:
    data: json

    def __init__(self):
        with open('res/config.json') as config_file:
            self.data = json.load(config_file)
