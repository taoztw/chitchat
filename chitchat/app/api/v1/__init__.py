from flask import Blueprint
from app.api.v1 import token, chat, file, model,data
from flask_cors import CORS

def create_blueprint_v1():
    """
    创建蓝图对象，将红图注册到蓝图上。
    :return: 蓝图对象
    """
    bp_v1 = Blueprint('v1', __name__)

    # 和蓝图相似的注册机制，规定url 前缀
    # user.api.register(bp_v1,url_prefix='/user') # 可以省略url_prefix因为，这里url_prefix和红图name重复了


    token.api.register(bp_v1)
    chat.api.register(bp_v1)
    file.api.register(bp_v1)
    model.api.register(bp_v1)
    data.api.register(bp_v1)
    return bp_v1
