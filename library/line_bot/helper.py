import os
from linebot.models import TextSendMessage
from linebot import LineBotApi


def reply_msg(token, msg):
    """
    create instance for line api connection
    """
    channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
    LineBotApi(channel_access_token).reply_message(token, msg)


def message_handler(message):
    """
    base message switcher for different prop.
    """

    # message no needs to reply
    if message.message_type is None:
        return
    if message.is_group_msg:
        group_message_handler(message)
    else:
        user_message_handler(message)


def group_message_handler(message):
    """
    deal with group chat.
    """
    if message.message_type == "功能表":
        msg = TextSendMessage(text='hi')
        reply_msg(message.reply_token, msg)


def user_message_handler(message):
    """
    deal with user (console) chat.
    """
    if message.message_type == "功能表":
        msg = TextSendMessage(text='hi')
        reply_msg(message.reply_token, msg)

    elif message.message_type == "本月目標":
        print('tmp')
