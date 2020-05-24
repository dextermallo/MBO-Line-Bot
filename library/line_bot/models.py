import os
import requests
import abc

from utils import get_str_first_line, remove_leading_and_trailing_whitespace


class LINEMessage(metaclass=abc.ABCMeta):
    user_id: str
    message: str
    reply_token: str
    timestamp: str
    user_display_name: str

    @abc.abstractmethod
    def identify_msg_type(self, msg):
        return NotImplemented

    @abc.abstractmethod
    def msg_cleaner(self):
        return NotImplemented

    def get_user_display_name(self):

        channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']

        headers = {'Authorization': 'Bearer ' + channel_access_token}
        profile = requests.get(
            f'https://api.line.me/v2/bot/profile/{self.user_id}',
            headers=headers
        )

        self.user_display_name = eval(profile.text)['displayName']

    @abc.abstractmethod
    def to_dict(self):
        return NotImplemented


class UserMessage(LINEMessage):
    message_type: str
    clean_msg: []

    def __init__(self, event):
        self.user_id = event['source']['userId']
        self.message = event['message']['text']
        self.reply_token = event['replyToken']
        self.timestamp = event['timestamp']
        self.get_user_display_name()
        self.identify_msg_type()
        self.msg_cleaner()

    def identify_msg_type(self):
        self.message_type = get_str_first_line(self.message)

    def msg_cleaner(self):
        if self.message_type == 'help':
            self.clean_msg = [{'1': 'test'}]
        elif self.message_type == '明天目標':
            self.clean_msg = []
            for sub_str in self.message.split('\n')[1:]:
                task = {
                    'order': int(sub_str[:sub_str.find('.')]),
                    'task_name': remove_leading_and_trailing_whitespace(sub_str[sub_str.find('.')+1:])
                }

                self.clean_msg.append(task)
        elif self.message_type == '完成':
            for sub_str in self.message.split('\n')[1:]:
                task = {
                    'order': int(sub_str[:sub_str.find('.')]),
                    'task_name': remove_leading_and_trailing_whitespace(sub_str[sub_str.find('.')+1:])
                }

                self.clean_msg.append(task)
        else:
            self.clean_msg = None

    def to_dict(self):
        return {
            # Inherit
            'user_id': self.user_id,
            'message': self.message,
            'reply_token': self.reply_token,
            'timestamp': self.timestamp,
            'user_display_name': self.user_display_name,
            # Extension
            'message_type': self.message_type,
            'clean_msg': self.clean_msg,
        }
