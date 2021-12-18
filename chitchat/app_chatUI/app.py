"""
    对训练好的模型进行测试
    运行此文件开始与机器人聊天
    注意只能进行中文聊天
"""

from flask import Flask, jsonify, render_template, request

# webapp
app = Flask(__name__, static_folder='templates', static_url_path='')


'''
request.json
一维数组，784个特征
[255, 161, 0, 0,....]
'''
@app.route('/')
def main():
    return render_template('index.html')
    # return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
