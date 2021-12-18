"""
Created by tz on 2021/2/1 
"""

__author__ = 'tz'

import os
# import pyonmttok
from app.libs.cmd_execute import subprocess_popen

def subword_data(train_folder, train_src_file, train_tgt_file):
    """
    对数据进行subword
    :param train_folder: 训练目录，用于subword model保存
    :param train_src_file:  src 文件
    :param train_tgt_file:  tgt 文件
    :return:
    """
    tokenizer = pyonmttok.Tokenizer("space", joiner_annotate=True, segment_numbers=True)
    learner = pyonmttok.BPELearner(tokenizer=tokenizer, symbols=32000)

    # subword 保存文件名称
    src_file_name = os.path.basename(train_src_file).split('.')[0]
    tgt_file_name = os.path.basename(train_tgt_file).split('.')[0]

    # 训练src bpe model
    learner.ingest_file(train_src_file)
    tokenizer = learner.learn(os.path.join(train_folder,f"{src_file_name}bpe.model"))

    # 训练 tgt bpe model
    learner.ingest_file(train_tgt_file)
    tokenizer = learner.learn(os.path.join(train_folder,f"{tgt_file_name}bpe.model"))



def detokenization(model_path, sentence):
    tokenizer = pyonmttok.Tokenizer('space', bpe_model_path=model_path)
    print(tokenizer.tokenize(sentence))
    # return tokenizer.tokenize(sentence)

def c_translate(model_path,output_path):
    cmd = f"ct2-opennmt-py-converter --model_path {model_path} --model_spec TransformerBase --output_dir {output_path}"
    subprocess_popen(cmd)
