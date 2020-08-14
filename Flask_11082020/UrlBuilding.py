#!/root/All_10082020/Flask_11082020/venv/bin/python3.8
from flask import *
app=Flask(__name__)
@app.route('/admin')
def hello_admin():
    return "<h1>Hello Admin</h1>"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello %s as Guest" %guest
@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))
if __name__ == "__main__":
    app.run(host="192.168.1.110",port="9090",debug=True)
