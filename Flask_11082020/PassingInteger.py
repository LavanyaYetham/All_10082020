#!/root/All_10082020/Flask_11082020/venv/bin/python3.8
from flask import *
app=Flask(__name__)
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return "Blog Number is %d " % postID
@app.route('/rev/<float:revNo>')
def revision(revNo):
    return "Revision Number %f " % revNo
if __name__ == "__main__":
    app.run(host="192.168.1.110",port="9090",debug=True)

