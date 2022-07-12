from unittest import result
from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)


@app.route('/')
def index():
    friends = User.get_all()
    print(friends)
    return render_template("index.html", friends=friends)


@app.route('/newuser')
def hello_world():
    return render_template('page2.html')

@app.route('/create_users', methods=["POST"])
def create_users():
    print(request.form)
    User.save(request.form)
    return redirect("/")





if __name__ == "__main__":
    app.run(debug=True)