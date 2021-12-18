"""
Created bt tz on 2020/12/18 
"""

__author__ = 'tz'

from flask import request,current_app
from flask_cors import cross_origin
from app.libs.error import APIException
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.validators.forms import TranslateForm
from app.libs.data_pre import chinese_process, english_process
import os
from chat_api import chat
import sys
from app.libs.spa.classifiers import DictClassifier

ds = DictClassifier()

sys.path.append(r'E:\nmt\chitchat')
# from app.libs.data_pre import jieba
# import ctranslate2

api = Redprint('chat')

max_history_len = 5
max_len = 25
repetition_penalty = 1.0  # 重复惩罚系数
temperature = 1
topk = 8
topp = 0.8


@api.route('',methods=['POST'])
# @auth.login_required
@cross_origin(supports_credentials=True)
def translate():
    # data = TranslateForm().validate_for_api()
    # dict_path = os.path.join(current_app.config['DATA_FOLDER'], 'dict.txt')
    # jieba.load_userdict(dict_path)
    data = request.get_json(silent=True)

    msg = data.get('text',None)

    if not msg:
        return APIException(msg='SOMETHING ERROR', code=500, error_code=0)
    if len(msg)==1 and msg in '^%$#@&':
        return APIException(msg='SOMETHING ERROR', code=500, error_code=0)
    print(topk)
    msg = chat(msg, max_history_len, max_len, topk, topp, repetition_penalty, temperature)

    spa_cls = ds.analyse_sentence(msg)
    msg = msg + "\t" + str(spa_cls)
    return APIException(msg=msg,code=200, error_code=0)


@api.route('/parameter',methods=['POST'])
# @auth.login_required
@cross_origin(supports_credentials=True)
def parameter():

    data = request.get_json(silent=True)

    global max_history_len
    global max_len
    global temperature
    global topp
    global topk
    global repetition_penalty

    max_history_len = data.get('max_history_len',5)
    max_len = data.get('max_len', 25)
    repetition_penalty = data.get('repetition_penalty', 1.0)
    temperature = data.get('temperature', 1)
    topk = data.get('topk', 8)
    topp = data.get('topp', 0.8)

    if max_history_len:
        max_history_len = int(max_history_len)
    else:
        max_history_len = 5
    if max_len:
        max_len = int(max_len)
    else:
        max_len = 25

    if repetition_penalty:
        repetition_penalty = float(repetition_penalty)
    else:
        repetition_penalty = 1.0

    if temperature:
        temperature = float(temperature)
    else:
        temperature = 1

    if topp:
        topp = float(topp)
    else:
        topp = 0.8

    if topk:
        topk = int(topk)
    else:
        topk = 1
    print(topk)
    return APIException(msg='设置成功',code=200, error_code=0)
# 加载模型
