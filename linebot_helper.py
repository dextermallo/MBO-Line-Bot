from linebot.models import TextSendMessage

import database
from models import Daily_task

INVAILD_MESSAGE = '您輸入的功能不存在耶！\n 請檢查有沒有輸入錯誤，\n或輸入 "# help" 查看功能集。'
JOIN_MESSAGE = '嗨！我是目標管理の工具人(`・ω・´)，\n請輸入 "# help" 查看功能集，\n或聯絡開發者 Dexter'
HELP_MESSAGE = '''指令集施工中 σ`∀´)σ
目前指令：
#指令集
#明天目標
#確認
#完成'''
WAITING_MESSAGE = '本功能還沒實裝呦 ┐(´д`)┌！'

STATUS_DONE = '✅'
STATUS_TODO = '❌'

METHODS = [
    '指令集', '點名',
    '明天目標', '確認', '完成',
    '下月目標', '本月確認', '本月完成',
    ]


def message_contain_service(message, line_bot_api, token):

    result = {
        'status': False,
        'method': None,
        'lines': [],
    }

    if message[0] == '#':
        first_line = message.partition('\n')[0]
        first_line = first_line[1:]
        if first_line not in METHODS:
            line_bot_api.reply_message(token,
                                       TextSendMessage(text=INVAILD_MESSAGE))
        else:
            result['status'] = True
            result['method'] = first_line
            result['lines'] = message.split('\n')

    return result


def reply_message_handler(message_formatter, user_info, line_bot_api, token):

    method = message_formatter['method']

    if method == '指令集':
        line_bot_api.reply_message(token, TextSendMessage(text=HELP_MESSAGE))
    elif method == '明天目標':
        try:
            daily_goals = split_goals(message_formatter['lines'])
            post_tomorrow_goals(daily_goals, user_info)
            # text = '嗨{user_display_name}！\n收到你的明天目標囉😁'.format(**user_info)
            # line_bot_api.reply_message(token, TextSendMessage(text=text))
        except Exception as e:
            error_class = e.__class__.__name__  # 取得錯誤類型
            detail = e.args[0]  # 取得詳細內容
            print(error_class, detail)

            err_msg = '你的目標格式好像怪怪的哦！請參考指令集'
            line_bot_api.reply_message(token, TextSendMessage(text=err_msg))
    elif method == '確認':
        try:
            daily_goals = database.get_today_task(user_info['user_id'])
            if len(daily_goals) == 0:
                msg = '目前沒有任何本日目標哦'
                line_bot_api.reply_message(token, TextSendMessage(text=msg))
            else:
                msg = '嗨{user_display_name}！\n你的本日目標如下：\n'.format(**user_info)
                for daily_goal in daily_goals:
                    if daily_goal['status'] == 'to-do':
                        msg += f'{STATUS_TODO}' + '{order}:{description}\n'.format(**daily_goal)
                    elif daily_goal['status'] == 'done':
                        msg += f'{STATUS_DONE}' + '{order}:{description}\n'.format(**daily_goal)

                msg.rstrip()
                line_bot_api.reply_message(token, TextSendMessage(text=msg))
        except Exception as e:
            err_msg = '好像哪裡怪怪的哦！請聯繫 Dexter'
            error_class = e.__class__.__name__  # 取得錯誤類型
            detail = e.args[0]  # 取得詳細內容
            print(error_class, detail)
            line_bot_api.reply_message(token, TextSendMessage(text=err_msg))
    elif method == '完成':
        try:
            finished_task_orders = message_formatter['lines'][1]
            finished_task_orders = [int(order) for order in finished_task_orders.split()]
            msg = 'Congrats!🎉你完成了🎉\n'

            for order in finished_task_orders:
                resp = database.set_today_task(user_info['user_id'], order)
            #     if resp['exists'] is True:
            #         msg += '{description}\n'.format(**resp)
            #     else:
            #         msg += '今日目標 {order}不存在耶！\n'
            # msg.rstrip()
            # line_bot_api.reply_message(token, TextSendMessage(text=msg))

        except Exception as e:
            err_msg = '好像哪裡怪怪的哦！請聯繫 Dexter'
            error_class = e.__class__.__name__  # 取得錯誤類型
            detail = e.args[0]  # 取得詳細內容
            print(error_class, detail)
            line_bot_api.reply_message(token, TextSendMessage(text=err_msg))
    else:
        line_bot_api.reply_message(token, TextSendMessage(text=WAITING_MESSAGE))


def reply_join_message(line_bot_api, token):
    line_bot_api.reply_message(token, TextSendMessage(text=JOIN_MESSAGE))


def split_goals(messages):
    goals = []
    for idx in range(1, len(messages)):
        goals.append({
            'order': int(messages[idx][0]),
            'description': messages[idx][3:],
        })
    return goals


def post_tomorrow_goals(daily_goals, user_info):
    for daily_goal in daily_goals:

        task = Daily_task(
            user_info['user_display_name'],
            user_info['user_id'],
            daily_goal['order'],
            daily_goal['description'])

        database.post_daily_task(task)

    return
