from flask import  render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users = users)

@app.route('/show')
def show():
    users = User.get_all()
    return render_template('show.html', users=users)

@app.route('/create_friend', methods=['POST'])
def add_user():
    print(request.form)
    User.save(request.form)
    return redirect('/show')


@app.route('/update/<int:id>')
def update(id):
    print(id)
    data = {'id': id}
    return render_template('update.html', user = User.get_one(data))



@app.route('/user_update',methods=['POST'])
def updater():
    User.update(request.form)
    return redirect('/show')

@app.route('/destroy/<int:id>')
def destroy(id):
    data ={'id': id}
    User.destroy(data)
    return redirect('/show')