from flask import Flask, render_template, request
from test2 import test

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ner', methods=['POST'])
def getNer():
    source = request.form.get('source')
    return source

@app.route('/test', methods=["POST"])
def getTest():
    source = request.form.get('source')
    return test(source)

@app.route('/other', methods=["POST"])
def getOther():
    source = request.form.get('source')
    return "This step is not handled yet."

if __name__ == '__main__':
    app.run(debug=True, port='5000', host='127.0.0.1')