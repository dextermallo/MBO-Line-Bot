import json

from library.line_bot.helper import message_handler
from library.line_bot.models import Message


def webhook(event, context):
    """
    webhook handler for LINE bot.
    """

    msg = json.loads(event['body'])

    # LINE server will send mutli-msg at once, so catch messages with loops.
    for event in msg['events']:
        message = Message(event)
        print(message.to_dict())
        message_handler(message)

    # quick response for webhook.
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": 'ok'})
    }

    return response
