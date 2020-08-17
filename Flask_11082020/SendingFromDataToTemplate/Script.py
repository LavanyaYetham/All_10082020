#!/root/All_10082020/Flask_11082020/SendingFromDataToTemplate/venv/bin/python3.8
from flask import *
app=Flask(__name__)
@app.route('/')
def student():
    return render_template('student.html')
@app.route('/result',methods = ['POST','GET'])
def result():
    if request.method == "POST":
        result=request.form
        return render_template("result.html",result = result)
if __name__ == "__main__":
    app.run(host="192.168.1.110",port="9090",debug=True)
