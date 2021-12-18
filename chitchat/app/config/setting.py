import os
from app import data
from app import config

TOKEN_EXPIRATION = 30 * 24 * 3600 * 3600

# 数据路径
DATA_FOLDER = os.path.dirname(data.__file__)   # data目录绝对路径

# 模型初始化配置文件目录
MODEL_CONFIG = os.path.dirname(config.__file__) # 初始化配置文件绝对路径

# tensorboard_log_dir
TENSORBOARD_LOG_DIR = os.path.join(DATA_FOLDER,'output')

# 最大长度
MAX_CONTENT_LENGTH = 1 * 1024 * 1024 * 1024  # 1G


## 训练文件
# train file save
TRAIN_FOLDER = DATA_FOLDER + '/train'
# valid file save
VALID_FOLDER = DATA_FOLDER + '/valid'
# test file save
TEST_FOLDER = DATA_FOLDER + '/test'
# raw file save
RAW_FOLDER = DATA_FOLDER + '/raw_data'
# model file save
MODEL_FOLDER = DATA_FOLDER + '/model'

# train
SUBWORD = False

## 单独文件路径
# wrong_word_list.txt

# 解码参数
