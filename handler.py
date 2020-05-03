import json


def webhook(event, context):
    response = {
        "statusCode": 200,
        "body": json.dumps({"message": 'ok'})
    }

    return response
