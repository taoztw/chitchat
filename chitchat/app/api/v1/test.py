"""
Created by tz on 2021/5/25 
"""

__author__ = 'tz'

from app.libs.spa.classifiers import DictClassifier

s = '我很开心'

ds = DictClassifier()
result = ds.analyse_sentence(s)
print(result)