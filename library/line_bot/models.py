import os
import requests

from library.models import ReplyLoader
from utils import get_str_first_line


class Message:

    group_id: str
    user_id: str
    is_group_msg: bool
    message: str
    message_type: str
    reply_token: str
    timestamp: str
    user_display_name: str

    clean_msg: [dict]

    # decompose from LINE event.
    def __init__(self, line_event):

        if line_event['source']['type'] == 'user':
            self.group_id = None
            self.user_id = line_event['source']['userId']
            self.is_group_msg = False
            self.message = line_event['message']['text']
            self.message_type = self.identify_msg_type(
                line_event['message']['text'])
            self.reply_token = line_event['replyToken']
            self.timestamp = line_event['timestamp']
            self.user_display_name = self.get_user_display_name()
            self.msg_cleaner()

        elif line_event['source']['type'] == 'group':
            self.group_id = line_event['source']['groupId']
            self.user_id = line_event['source']['userId']
            self.is_group_msg = True
            self.message = line_event['message']['text']
            self.message_type = self.identify_msg_type(
                line_event['message']['text'])
            self.reply_token = line_event['replyToken']
            self.timestamp = line_event['timestamp']
            self.user_display_name = self.get_user_display_name()
            self.msg_cleaner()

    @staticmethod
    def identify_msg_type(msg):
        loader = ReplyLoader()
        if get_str_first_line(msg) in loader.data['user']['methods']:
            return get_str_first_line(msg)
        return None

    def msg_cleaner(self):
        if self.message_type == '本月獎勵':
            self.clean_msg = [{'1': 'test'}]
        else:
            self.clean_msg = [{'2': 'test2'}]

    def get_user_display_name(self):

        channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']

        headers = {'Authorization': 'Bearer ' + channel_access_token}
        profile = requests.get(
            f'https://api.line.me/v2/bot/profile/{self.user_id}',
            headers=headers
        )

        self.user_display_name = eval(profile.text)['displayName']

    def to_dict(self):
        return {
            'group_id': self.group_id,
            'user_id': self.user_id,
            'is_group_msg': self.is_group_msg,
            'message': self.message,
            'message_type': self.message_type,
            'reply_token': self.reply_token,
            'timestamp': self.timestamp,
            'user_display_name': self.user_display_name,
            'clean_msg': self.clean_msg,
        }
