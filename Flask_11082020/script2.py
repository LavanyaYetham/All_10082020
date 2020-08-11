#!/root/All_10082020/Flask_11082020/venv/bin/python3.8
from flask import *
app=Flask(__name__)
@app.route('/home/<num1>/<num2>')
def home(num1,num2):
    return ("My First Argument {} and My second Argument {}".format(num1,num2))
if __name__ == "__main__":
    app.run(host="192.168.1.103",port="9090",debug=True)
