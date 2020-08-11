#!/root/All_10082020/Flask_11082020/venv/bin/python3.8
from flask import *
app=Flask(__name__)
@app.route('/add/<num1>/<num2>')
def add(num1,num2):
    total=int(num1)+int(num2)
    return "The total of {} and {} is {}".format(num1,num2,total)
if __name__ == "__main__":
    app.run(host="192.168.1.103",port="9090",debug=True)
    
