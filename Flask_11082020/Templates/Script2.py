#!/root/All_10082020/Flask_11082020/Templates/venv/bin/python3.8
from flask import *
app=Flask(__name__)
@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)
if __name__ == "__main__":
    app.run(host="192.168.1.110",port="9090",debug=True)
