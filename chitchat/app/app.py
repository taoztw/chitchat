from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from datetime import date

from app.libs.error_code import ServerError


class JSONEncoder(_JSONEncoder):
    def default(self, o):  # 如何把对象转化为一个字典
        if hasattr(o, 'keys') and hasattr('o', '__getitem__'):
            return dict(o)  # 存在问题： 类变量不会存储到__dict__中
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder

