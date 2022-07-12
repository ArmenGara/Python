from flask import Flask, render_template, session, request, redirect 
app = Flask(__name__)
app.secret_key = 'helloguys'
@app.route('/')
def hello_world():
    if 'count' not in session:
        session['count'] = 0
    else:
        session['count'] += 1
    return render_template("index.html")


@app.route('/clearPage')
def endgame():
    session.clear()
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)