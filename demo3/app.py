#encoding:utf-8
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '这是url传参演示!'
@app.route('/user/<name>')
def list_name(name):
    return "接收到的名字为： %s" % name
@app.route('/news/<int:id>')
def list_news(id):
    return "接收到的id为： %s" % id
if __name__ == '__main__':
    app.run(debug=True)
