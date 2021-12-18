"""
Created bt tz on 2020/12/19 
"""

__author__ = 'tz'

import subprocess

from flask import request,current_app,jsonify

from app.libs.model_train_lib import c_translate
from app.libs.redprint import Redprint
from app.libs.token_auth import auth
from app.libs.error_code import ModelExist, ModelInitializeSuccess,\
    ModelInitializeFail, TrainFileNotFound,ValidDataGenerateFail,TrainSuccess,\
    ModelTrainFail,ModelTrainSuccess
from app.libs.cmd_execute import subprocess_popen
from app.libs.data_pre import generate_valid_data

from app.libs.score import get_score
from app.libs.error import APIException
import os
import yaml
import shutil
import time
import sys
from shutil import copyfile
from config.model_config import DATA_DIR, LOG_DIR

sys.path.append(r'E:\nmt\chitchat')
from config.model_config import ROOT_DIR
api = Redprint('model')

model_dir = ''
epoch = ''
batch_size = ''

# 保存模型名称，训练src -> tgt模型。
@api.route('/initialize',methods=['POST'])
@auth.login_required
def initialize_model():
    data = request.get_json(silent=True)
    global model_dir
    global epoch
    global batch_size

    model_dir = data['folder']
    epoch = data['epoch']
    batch_size = data['batch_size']
    print(model_dir, epoch, batch_size)
    # 模型目录
    print(ROOT_DIR)
    model_folder = os.path.join(ROOT_DIR, model_dir)

    # # 创建模型数据目录
    # data_dir = os.path.join(model_folder, 'data')


    # 创建模型目录
    if os.path.exists(model_folder):
        return ModelExist()
    else:
        os.makedirs(model_folder)
        copyfile(r'E:\nmt\chitchat\dialogue_model\config.json', os.path.join(model_folder, 'config.json'))
        copyfile(r'E:\nmt\chitchat\dialogue_model\vocab.txt', os.path.join(model_folder, 'vocab.txt'))

    return ModelInitializeSuccess()



@api.route('/train',methods=['POST'])
@auth.login_required
def train_model():
    data = request.get_json(silent=True)
    # print(data)
    # 创建的模型文件名
    model_name = data['folder']

    train_raw_path = os.path.join(DATA_DIR, model_name+'.txt')
    train_tokenized_path = os.path.join(DATA_DIR, model_name+'_token.txt')
    log_path = os.path.join(LOG_DIR, model_name +'_log.txt')
    dialogue_model_output_path = os.path.join(ROOT_DIR, model_name)
    pretrained_model = ''
    if 'finetuning' in model_name:
        pretrained_model = r'E:\nmt\chitchat\dialogue_model'

    print(train_tokenized_path, train_raw_path, log_path, dialogue_model_output_path)

    if not os.path.exists(train_raw_path):
        return TrainFileNotFound()

    #### 执行训练cmd
    cmd = f"python E:\\nmt\chitchat\\train.py --epochs 50 --batch_size 16 --raw --seed 1 --train_raw_path {train_raw_path}" \
          f" --train_tokenized_path {train_tokenized_path} --log_path {log_path} --dialogue_model_output_path {dialogue_model_output_path} "
    # result = subprocess_popen('ping www.baidu.com -t')
    print(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    time.sleep(3.5)

    if p.poll() is None:
        return TrainSuccess()
    else:
        return ModelTrainFail()



@api.route('/visual', methods=['POST'])
@auth.login_required
def visual_model_train():
    # data = request.get_json(silent=True)
    # 获得模型目录文件

    log_file = os.path.join(current_app.config['DATA_FOLDER'],tmp_src+'2'+tmp_tgt+'_'+tmp_folder+'/log.txt')
    log_file = os.path.join(current_app.config['DATA_FOLDER'],'en2zh_en2zh_test_2'+'/log.txt')

    with open(log_file, 'r',encoding='utf-8') as f:

        process_data = 0
        log_data = f.readlines()
        tmp = log_data[-1]
        try:
            steps = tmp.split()[4].replace(';', '').split('/')
            now_step = int(steps[0])
            full_step = int(steps[1])
            process_data = int((now_step / full_step) * 100)
            # return jsonify({'step':int((now_step / full_step) * 100)})
            return APIException(msg=process_data,code=200, error_code=0)
            # return TrainSuccess()
        except:

            # return tmp
            # return jsonify({'step':tmp})
            return APIException(msg=process_data, code=200, error_code=0)


@api.route('/test', methods=['POST'])
@auth.login_required
def find_best_score_model():
    model_file_name = tmp_src + '2' + tmp_tgt + '_' + tmp_folder # 模型文件名称
    model_file_path = os.path.join(current_app.config['DATA_FOLDER'], model_file_name) # 模型所处目录
    file_list = os.listdir(model_file_path)
    model_name_list = [file_name for file_name in file_list if file_name.split('.')[1]=='pt']

    model_score = {}
    src_test_file = os.path.join(current_app.config['TEST_FOLDER'],'test_'+tmp_src+'.txt')
    print(model_name_list)
    # 遍历所有模型文件
    for model in model_name_list:
        model_name = os.path.join(model_file_path, model) # 模型文件

        output_file = os.path.join(model_file_path, 'pred'+model.split('.')[0]+'.txt')
        cmd = f"onmt_translate - model {model_name} - src {src_test_file} - output {output_file} - gpu 0 - verbose - n_best 1 - beam_size 5 - length_penalty avg - coverage_penalty summary"
        cmd_state = subprocess_popen(cmd)
        if cmd_state == 'done':
            model_score[model] = get_score(src_test_file, output_file)
    print('测试成功')

    max_score = max(model_score.values())
    for name,score in model_score.items():
        if score == max_score:
            c_translate(os.path.join(model_file_path,name),os.path.join(current_app.config['MODEL_FOLDER'],name+'ctranslate2'))
            # shutil.move(os.path.join(model_file_path,name), os.path.join(current_app.config['MODEL_FOLDER'],name))
            print('转换模型成功')
        return APIException(msg=f'{name}:{score}',code=200,error_code=0)

