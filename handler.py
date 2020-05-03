import json
import requests
from linebot import LineBotApi
import os

import linebot_helper


def webhook(event, context):
    channel_access_token = os.environ['LINE_CHANNEL_ACCESS_TOKEN']

    line_bot_api = LineBotApi(channel_access_token)

    msg = json.loads(event['body'])

    for event in msg['events']:

        if event['type'] == 'join':
            token = event['replyToken']
            linebot_helper.reply_join_message(line_bot_api, token)

        elif event['type'] == 'message':
            user_id = event['source']['userId']
            headers = {'Authorization': 'Bearer ' + channel_access_token}
            profile = requests.get(
                f'https://api.line.me/v2/bot/profile/{user_id}',
                headers=headers
            )

            message = event['message']['text']
            print(profile.text)
            print(profile)
            user_info = {
                'user_id': user_id,
                'user_display_name': eval(profile.text)['displayName'],
            }

            token = event['replyToken']
            message_formatter = linebot_helper.message_contain_service(
                message,
                line_bot_api, token)

            if message_formatter['status']:
                linebot_helper.reply_message_handler(
                    message_formatter,
                    user_info,
                    line_bot_api,
                    token)

    response = {
        "statusCode": 200,
        "body": json.dumps({"message": 'ok'})
    }

    return response
