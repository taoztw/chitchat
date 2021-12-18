"""
Created bt tz on 2020/12/18 
"""

__author__ = 'tz'

import os
from flask import request, current_app, jsonify
from app.libs.error_code import DeleteSuccess, NotFound,\
    FileUploadSuccess, ServerError, ValidDataGenerateFail,RawFileProcessError,FILEEXISTS
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
import sys
sys.path.append(r'E:\nmt\chitchat')
from config.model_config import LOG_DIR
from app.libs.error import APIException

from config.model_config import DATA_DIR

api = Redprint('file')

@api.route('',methods=['POST'])
@auth.login_required
def upload_file():
    # print(request.files)

    try:

        f = request.files['file']
        data_path = os.path.join(DATA_DIR, f.filename)
        if os.path.exists(data_path):
            return FILEEXISTS()
        else:
            f.save(os.path.join(DATA_DIR, f.filename))

        # f.save(os.path.join(current_app.config['UPLOADED_DEST'], secure_filename(f.filename)))

        return FileUploadSuccess()
    except Exception as e:
        print(e)
        return ServerError()


# 展示当前目录文件
@api.route('', methods=['GET'])
@auth.login_required
def list_file():
    file_list = os.listdir(current_app.config['DATA_FOLDER'])
    for i,f in enumerate(file_list):
        if f=='__init__.py' or f=='__pycache__':
            file_list.pop(i)
    result = {
        'code':200,
        'msg':file_list,
        'error_code':0
    }
    return jsonify(result)

# 删除文件
@api.route('', methods=['DELETE'])
@auth.login_required
def delete_file():
    data = request.get_json(silent=True)
    filename = data.get('filename')
    print(filename)
    file_path = os.path.join(current_app.config['UPLOADED_DEST'],filename)
    print(file_path)
    try:
        os.remove(file_path)
        return DeleteSuccess()
    except FileNotFoundError:
        return NotFound()


@api.route('/log', methods=['POST'])
@auth.login_required
def look_log_content():

    data = request.get_json(silent=True)
    # 获得模型目录文件
    # log_file = os.path.join(current_app.config['DATA_FOLDER'],
    #                         data['src'] + '2' + data['tgt'] + '_' + data['folder'] + '/log.txt')

    # 模型目录文件名

    model_name = data.get('folder')

    log_file = os.path.join(LOG_DIR, model_name + '_log.txt')
    with open(log_file,'r',encoding='utf-8') as f:
        content = f.readlines()
        full_content = ''
        for tmp in content:
            full_content += tmp.strip()+'<br/>'
        return APIException(msg=full_content,code=200,error_code=0)
