from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep secretbruh'



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')

@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)
    session['form_data'] = request.form['data']
    session['user_name'] = request.form['user_name']
    return redirect('/hello')



if __name__=="__main__":
    app.run(debug=True)  