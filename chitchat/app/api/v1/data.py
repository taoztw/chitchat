"""
Created by tz on 2021/1/18 
"""

__author__ = 'tz'

import os
from flask import current_app, request

from app.libs.data_pre import raw_file_process
from app.libs.error_code import RawFileProcessError, Success
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from config.model_config import DATA_DIR

api = Redprint('data')

@api.route('/preprocessing',methods=['POST'])
@auth.login_required
def preprocessing():
    """
    请求参数：raw_data文件名，en_zh ,第一列是英文，第二列是中文

    处理：对原始数据进行处理，保存训练数据
    :return:
    """
    data = request.get_json(silent=True)
    print(data['file_name'])
    raw_data_path = os.path.join(current_app.config['RAW_FOLDER'], data['file_name']+'.txt')
    if '.' in data['file_name']:
        tmp_1, tmp_2 = data['file_name'].split('.')[0].split('_')
    else:
        tmp_1, tmp_2 = data['file_name'].split('_')
    # raw_file = _path
    tmp_1_file = os.path.join(current_app.config['TRAIN_FOLDER'], tmp_1+'.txt')
    tmp_2_file = os.path.join(current_app.config['TRAIN_FOLDER'], tmp_2+'.txt')
    try:
        # 根据预处理逻辑对训练文件进行处理
        flag = raw_file_process(raw_data_path, tmp_1_file, tmp_2_file)
        if current_app.config['SUBWORD']:
            from app.libs.model_train_lib import subword_data
            # subword_data(train_folder=os.path.join(current_app.config['TRAIN_FOLDER'],f'{tmp_src}2{tmp_tgt}_{tmp_folder}'),
            #              train_src_file=tmp_1_file,
            #              train_tgt_file=tmp_2_file)
        # 构造词典

        return Success()
    except:
        print('原始文件处理出错')
        return RawFileProcessError()



