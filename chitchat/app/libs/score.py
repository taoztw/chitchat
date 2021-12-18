"""
Created by tz on 2020/11/18
"""

__author__ = 'tz'

from nltk.translate.bleu_score import sentence_bleu,corpus_bleu

# 单个句子
# reference = [['this', 'is', 'small', 'test']]
# candidate = ['this', 'is', 'a', 'test']
# score = sentence_bleu(reference, candidate,weights=(1,0.5,0.5,0.5))

# 多个句子
def read_references(ref_file):
    """
    语料的references计算
    :return: [ [['word','word'],['word','word']]   ]
    """
    result = []
    r_sentences = []

    f = open(ref_file,'r',encoding='utf-8')
    sentences = f.readlines()
    for s in sentences:
        references = []
        references.append(s.strip().split(' '))
        result.append(references)
    f.close()
    return result

def read_candidates(can_file):
    """模型翻译译文"""
    result = []
    file = open(can_file,'r',encoding='utf-8')
    sentences = file.readlines()
    for s in sentences:
        result.append(s.strip().split(' '))
    file.close()
    return result

# references = [[['this', 'is', 'small', 'test']]]
# candidates = [['this', 'is', 'a', 'test']]
if __name__ == '__main__':

    references = read_references()
    candidates = read_candidates()
    score = corpus_bleu(references, candidates,weights=(0.25,0.25,0.25,0.25))

    print(score)


def get_score(ref_file, can_file):
    references = read_references(ref_file)
    candidates = read_candidates(can_file)
    score = corpus_bleu(references, candidates,weights=(0.4,0.3,0.2,0.1))
    return score