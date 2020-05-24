import json

from library.line_bot.helper import user_message_handler, group_message_handler
from library.line_bot.models import UserMessage


def webhook(event, context):
    """
    webhook handler for LINE bot.
    """

    msg = json.loads(event['body'])

    # LINE server will send mutli-msg at once, so catch messages with loops.
    for event in msg['events']:
        if event['source']['type'] == 'user':
            user_message = UserMessage(event)
            print(user_message.to_dict())
            user_message_handler(user_message)
        if event['source']['type'] == 'group':
            group_message = UserMessage(event)
            group_message_handler(group_message)

    # quick response for webhook.
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": 'ok'})
    }

    return response
