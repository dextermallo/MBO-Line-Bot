import boto3
from boto3.dynamodb.conditions import Key

from utils import get_today


def db():
    dynamodb = boto3.resource(
        'dynamodb',
        region_name='us-east-1'
    )
    return dynamodb


def post_daily_task(daily_task):
    table = db().Table('daily_task')
    table.put_item(Item=daily_task.to_dict())


def get_today_task(user_id):
    table = db().Table('daily_task')

    result = table.query(
        IndexName='user_id-index',
        KeyConditionExpression=Key('user_id').eq(user_id)
    )

    today = get_today()

    today_task = []

    for item in [item for item in result['Items'] if item['date'] == today]:
        today_task.append({
            'status': item['status'],
            'description': item['description'],
            'order': item['order'],
        })

    return today_task


def set_today_task(user_id, order):
    table = db().Table('daily_task')
    query_result = table.query(
        IndexName='user_id-index',
        KeyConditionExpression=Key('user_id').eq(user_id)
    )

    today = get_today()

    resp = {
        'exists': False,
        'description': None,
    }

    for item in [item for item in query_result['Items'] if item['date'] == today and item['order'] == order]:
        resp['exists'] = True
        table.update_item(
            Key={
                'daily_task_id': item['daily_task_id'],
            },
            UpdateExpression="set #status = :val",
            ExpressionAttributeValues={
                ':val': 'done',
            },
            ExpressionAttributeNames={
                "#status": "status",
            }
        )
        resp['description'] = item['description']

    return resp
