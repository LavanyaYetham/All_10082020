#!/root/All_10082020/Flask_11082020/venv/bin/python3.8
from flask import *
app=Flask(__name__)
def hello_world():
    return '<h1>hello world</h1>'
app.add_url_rule('/','Hello',hello_world)
if __name__ == "__main__":
    app.run(host="192.168.1.110",port="9090",debug=True)
