"""
Created by tz on 2021/1/10 
"""

__author__ = 'tz'

from nltk.tokenize import word_tokenize
import jieba
# isalpha() 判断是否为字母 不区分大小写
import re
import os
pattern = re.compile(r'\d*,\d*')

current_path = os.path.dirname(__file__)
# 全局变量
wrong_word_set = set()
# 过滤不正常单词，集合
# with open(os.path.join(current_path,'wrong_word_list.txt'), 'r', encoding='utf-8') as f:
#     data = f.readlines()
#     for w in data:
#         wrong_word_set.add(w.strip())
#     print('wrong word set 构造成功')

# print(wrong_word_set)
def filter_wrong_words(sentence):
    """过滤不正常单词"""

    # 对几个特殊的单词固定规则
    if 'assembly' in sentence:
        sentence = sentence.replace('assembly','assembly ')
    if 'aperiod' in sentence:
        sentence = sentence.replace('aperiod', 'a period ')
    if 'voltagethe' in sentence:
        sentence = sentence.replace('voltagethe','voltage the')
    if 'tighten' in sentence:
        sentence = sentence.replace('tighten',' tighten')
    if 'industrial' in sentence:
        sentence = sentence.replace('industrial',' industrial')
    if 'catalyst' in sentence:
        sentence = sentence.replace('catalyst',' catalyst')
    if 'crimp' in sentence:
        sentence = sentence.replace('crimp', ' crimp')
    if 'removal' in sentence:
        sentence = sentence.replace('removal', ' removal')

    # 其余的按照wrong_word_list中的单词进行替换。
    for r in wrong_word_set:

        if r in sentence:
            # print(r)
            sentence = sentence.replace(r,' '+r+' ')
    return sentence



# def en_digit_process(s):
#     # 对英文数字 10,000 的处理
#     num = re.findall(pattern, s)
#     if num:
#         s = re.sub(pattern, num[0].replace(',',''),s)
#     return s


def is_chinese(uchar):
    """判断单个字符是否是中文"""
    if uchar >= u'\u4e00' and uchar <= u'\u9fa5':
        return True
    else:
        return False

def is_normal(s):
    """正常为True"""
    first = any([s[0].isdigit(), s[0].isalpha(), is_chinese(s[0]), s[0]=='('])
    last = any([s[-1].isdigit(), s[-1].isalpha(), is_chinese(s[-1]), s[-1]==')'])
    return first, last
def first_last_special_c(s):
    """去掉一句话收尾特殊字符"""
    first, last = is_normal(s)
    while  (not first) or  (not last):
        if not first:
            # s = s.replace(s[0],'')
            s = s[1:]
        if not last:
            # s = s.replace(s[-1],'')
            s = s[:-1]
        first, last = is_normal(s)
    return s


def is_all_chinese(strs):
    """判断所有字符是否是中文"""
    for _char in strs:
        if not '\u4e00' <= _char <= '\u9fa5':
            return False
    return True

def special_char(s,char):
    #
    if char == '/':
        s = s.replace('/',' / ')

    return s

def cn_trans_to_en(string):
    """将中文标点符号转化为英文。"""
    E_pun = u';:,.!?[]()<>""\'\''
    C_pun = u'；：，。！？【】（）《》“”‘’'
    table= {ord(f):ord(t) for f,t in zip(C_pun, E_pun)}
    return string.translate(table)

def filter_blank(w):
    """过滤分词列表中存在的空格"""
    if w == ' ' or w == '   ' or w=='  ' or w=='    ':
        return False
    else:
        return True

def proper_nouns(cn_file, only_read=False):
    """对中文语料特殊名词进行提取，存储到文件中
    only_read: 直接读取set，已经提取过之后使用，默认False
    """
    # 提取文件中的所有句子为一个列表

    if not only_read:
        perper_file = open('proper_nouns.txt', 'a+', encoding='utf-8')
        w_list = set()
        with open(cn_file, 'r', encoding='utf-8') as cn_f:
            for s in cn_f.readlines():
                word_l = s.split(' ')
                for word in word_l:
                    if is_chinese(word) or word.isdigit() or word in './\\#();；- 、:"*<>·':
                        pass
                    else:
                        # print(word)
                        w_list.add(word)
        for w in list(w_list):
            perper_file.write(w + '\n')
        print('proper_nouns.txt文件保存完成')

        perper_file.close()
    else:
        perper_file = open(cn_file, 'r', encoding='utf-8')
        set_word = set(list(filter(filter_blank, [w.strip() for w in perper_file.readlines()])))
        perper_file.close()
        return set_word

# 摄氏度替换
def cf_replace(s):
    s.replace('°c',' °c ')
    s.replace('° c', ' °c ')
    s.replace('°f', ' °f ')
    s.replace('° f', ' °f ')
    return s

# 替换 2for 2to 2and
# s = '7in 4from'
def digitword(s):
    tmp = re.findall(r'(\d+)and',s)
    if tmp:
        s = s.replace(tmp[0],tmp[0]+' ')

    tmp = re.findall(r'(\d+)for', s)
    if tmp:
        s = s.replace(tmp[0], tmp[0] + ' ')

    tmp = re.findall(r'(\d+)to', s)
    if tmp:
        s = s.replace(tmp[0], tmp[0] + ' ')

    tmp = re.findall(r'(\d+)from', s)
    if tmp:
        s = s.replace(tmp[0], tmp[0] + ' ')
    for i in ['horn','aec','rotate','bucket','with','coolant', 'away','unless','inlet','in']:
        tmp = re.findall(r'(\d+)'+i, s)
        if tmp:
            s = s.replace(tmp[0], tmp[0] + ' ')
    return s


# print(digitword(s))

set1 = set()
# aaa = 'Commercial Heavy-Duty Coolant/Antifreeze that meets "ASTM D4985".'
def english_process(s):
    """输入一句话，进行分词"""
    # set_word = proper_nouns(cn_file='proper_nouns.txt', only_read=True)
    s = special_char(s,'/')  # 对/的单词进行拆分 a/b => a / b
    s = s.replace('"','') # 消除引号
    s = first_last_special_c(s) # 去除首位特殊字符 非数字，字母，汉字
    # s = en_digit_process(s)  # 对特殊数字进行处理
    s = s.lower()
    # 摄氏度替换
    s = filter_wrong_words(s) # 过滤特殊错误单词
    s = digitword(s) # 过滤数字+单词的错误形式
    tmp_l = word_tokenize(s)
    # tmp_l = [w.lower() if w not in set_word else w for w in tmp_l ]
    # return " ".join(tmp_l)
    return tmp_l
# test
# print(english_process(aaa))


def chinese_process(s):
    """中文处理"""
    # print(s)
    s = cn_trans_to_en(s)  # 将中文标点符号转化为英文
    s = s.replace('\\','').strip()
    s = s.replace('、', ',').strip()
    s = s.replace('"', '')
    s = first_last_special_c(s) # 去除首位特殊字符 非数字，字母，汉字
    s = s.lower()
    s = filter_wrong_words(s) # 过滤特殊格式错误单词
    s = digitword(s)  # 过滤数字+单词的错误形式
    # s = en_digit_process(s)  # 处理英文字符
    s = list(filter(filter_blank,list(jieba.cut(s,HMM=True))))
    return s
# test
# print(chinese_process(s))
# Cat ET 将 显示 Test ECM Mode ( 测试 ECM 模式 ) 的 状态 和 Test ECM Mode ( 测试 ECM 模式 ) 的 剩余时间 .


# with open('en.txt','r',encoding='utf-8') as f:
#     for s in f:
#         s = cn_trans_to_en(s)
#         s = english_process(s)

# 对中文预料进行分词,生成新文件

# 提取数据到新文件
# with open('cn_1.txt', 'a+', encoding='utf-8') as writer:
#     with open('cn.txt','r',encoding='utf-8') as reader:
#         for s in reader:
#             s = chinese_process(s)
#             print(s)
#             writer.write(s+'\n')

# 提取数据到新文件


# with open('en_1.txt','a+',encoding='utf-8') as writer:
#     with open('en.txt','r',encoding='utf-8') as reader:
#         for s in reader:
#             s = english_process(s)
#             print(s)
#             writer.write(s+'\n')
# with open('dict.txt','a+',encoding='utf-8') as f:
#     for i in set1:
#         f.write(i + '\n')


# 生成验证集
def generate_valid_data(folder,src,tgt,train_data_size,valid_data_size):
    import numpy as np
    np.random.seed(123)
    random_idx = np.random.randint(0,train_data_size,size=valid_data_size)
    print(random_idx)


    src_f = open(folder + f'/train/{src}.txt','r',encoding='utf-8')
    tgt_f = open(folder + f'/train/{tgt}.txt', 'r', encoding='utf-8')

    valid_src = open(folder + f'/valid/valid_{src}.txt','a+',encoding='utf-8')
    valid_tgt = open(folder + f'/valid/valid_{tgt}.txt','a+',encoding='utf-8')

    src_data = src_f.readlines()
    tgt_data = tgt_f.readlines()

    for idx in random_idx:
        valid_src.write(src_data[idx])
        valid_tgt.write(tgt_data[idx])

    src_f.close()
    tgt_f.close()
    valid_src.close()
    valid_tgt.close()
    return 'success'

# 对英文测试文件的预处理
# with open('test_en.txt','a+',encoding='utf-8') as writer:
#     with open('test_en_raw.txt','r',encoding='utf-8') as reader:
#         for s in reader:
#             s = english_process(s)
#             print(s)
#             writer.write(s+'\n')


### 对原始数据进行处理
def raw_file_process(raw_file, train_file_1, train_file_2):
    f_1 = open(train_file_1, 'w', encoding='utf-8')
    f_2 = open(train_file_2, 'w', encoding='utf-8')

    file_1_name = os.path.basename(train_file_1)
    file_1_name = file_1_name.split('.')[0]
    file_2_name = os.path.basename(train_file_2)
    file_2_name = file_2_name.split('.')[0]

    with open(raw_file, 'r', encoding='UTF-16') as f:
        data = f.read()
        next(data)
        data_list = data.split('\n')
        raw_1 = []
        raw_2 = []
        for s in data_list[1:]:
            # print(s)
            raw_1.append(s.split('\t')[0])
            raw_2.append(s.split('\t')[1])

    zh_data = (raw_1,f_1) if 'zh' == file_1_name else (raw_2,f_2)
    en_data = (raw_1,f_1) if 'en' == file_1_name else (raw_2,f_2)

    process_1 = []
    process_2 = []
    for data_cn in zh_data[0]:
        tmp_cn = chinese_process(data_cn)
        if len(tmp_cn) > 300:
            continue
        tmp_s_cn = ' '.join(tmp_cn)
        process_1.append(tmp_s_cn + '\n')
    for data_en in en_data[0]:
        tmp_en = english_process(data_en)
        if len(tmp_cn) > 300:
            continue
        tmp_s_en = ' '.join(tmp_en)
        process_2.append(tmp_s_en + '\n')

    zh_data[1].writelines(process_1)
    en_data[1].writelines(process_2)

    f_1.close()
    f_2.close()

    return 'done'

