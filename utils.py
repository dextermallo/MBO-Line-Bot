import re
import datetime


def get_today():
    now = datetime.datetime.now()
    return f'{now.year}/{now.month}/{now.day}'


def get_str_first_line(s):
    return s.partition('\n')[0]


def split_text_to_orders(s, start_line=0):
    orders = []
    for idx in range(start_line, len(s)):
        orders.append({
            'order': int(s[idx][0]),
            'description': s[idx][3:],
        })
    return orders


def remove_leading_and_trailing_whitespace(s):
    return re.sub(r"^\s+|\s+$", "", s)
