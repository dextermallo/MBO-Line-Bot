import datetime
import uuid


class Daily_task():

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

        self. daily_task_id = str(uuid.uuid1())
        self.user_display_name = user_display_name
        self.user_id = user_id
        self.date = f'{now.year}/{now.month}/{now.day}'
        self.status = 'to-do'
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
