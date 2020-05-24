import os
from linebot.models import TextSendMessage, FlexSendMessage
from linebot import LineBotApi

from library.models import ReplyLoader, DailyTaskSummary


def reply_msg(token, msg):
    """
    create instance for line api connection
    """
    channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']
    LineBotApi(channel_access_token).reply_message(token, msg)


def user_message_handler(message):
    """
    deal with user (console) chat.
    """

    if message.message_type == "功能表":  # TODO
        msg = TextSendMessage(text='hi')
        reply_msg(message.reply_token, msg)
    elif message.message_type == "明天目標":
        daily_task_summary = DailyTaskSummary()
        daily_task_summary.save(message=message)
        msg = TextSendMessage(text=daily_task_summary.on_create_msg())
        reply_msg(message.reply_token, msg)
    elif message.message_type == '進度':  # TODO
        msg = TextSendMessage(text='進度')
        reply_msg(message.reply_token, msg)
    elif message.message_type == '本月進度':  # TODO
        msg = TextSendMessage(text='本月進度')
        reply_msg(message.reply_token, msg)
    elif message.message_type == '完成':  # TODO
        reply_loader = ReplyLoader()
        msg = FlexSendMessage(
            alt_text='hello',
            contents=reply_loader.data['user']['response']['daily_progress']
        )
        reply_msg(message.reply_token, msg)


# TODO
def group_message_handler(message):
    """
    deal with group chat.
    """
    if message.message_type == "功能表":
        msg = TextSendMessage(text='hi')
        reply_msg(message.reply_token, msg)
