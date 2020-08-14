#!/root/All_10082020/Flask_11082020/venv/bin/python3.8
from flask import *
app=Flask(__name__)
@app.route('/python')
def one():
    return "Hello Python!!"
@app.route('/flask')
def two():
    return "Hello Flask!!"
if __name__ == "__main__":
    app.run(host="192.168.1.110",port="9090",debug=True)
