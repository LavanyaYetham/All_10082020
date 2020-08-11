#!/root/All_10082020/Flask_11082020/venv/bin/python3.8
from flask import *
app=Flask(__name__)
@app.route('/')
def home():
    return "Hello World!!"
@app.route('/hello')
def hello():
    return "<h1>Hello World!!</h1>"
if __name__ == "__main__":
    app.run(host="192.168.1.103",port="9090",debug=True)
