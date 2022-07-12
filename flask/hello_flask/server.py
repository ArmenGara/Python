from flask import Flask, render_template, request, redirect, session # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "keep it secret, keep it safe"


@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response


@app.route('/users', methods=['POST'])
def create_user():
    print(request.form)
    session['form_data'] = request.form['data']
    session['user'] = request.form['user_name']
    return redirect('/')



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)