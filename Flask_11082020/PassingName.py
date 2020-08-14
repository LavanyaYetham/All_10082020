#!/root/All_10082020/Flask_11082020/venv/bin/python3.8
from flask import *
app=Flask(__name__)
@app.route('/hello/<name>')
def hello(name):
    return "Hello %s!!"%name
if __name__ == "__main__":
    app.run(host="192.168.1.110",port="9090",debug=True)
