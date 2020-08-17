#!/root/All_10082020/Flask_11082020/Templates/venv/bin/python3.8
from flask import *
app=Flask(__name__)
@app.route('/')
def index():
    return "<html><body><h1>Hello World!!!</h1></body></html>"
if __name__ == "__main__":
    app.run(host="192.168.1.110",port="9090",debug=True)
