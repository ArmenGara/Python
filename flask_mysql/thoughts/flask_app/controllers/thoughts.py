from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.thought import Thought

# ! ////// CREATE  //////
# TODO CREATE REQUIRES TWO ROUTES:
# TODO ONE TO DISPLAY THE FORM:
@app.route('/thought/new')
def new():
    return render_template("new_thought.html")

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/thought/create',methods=['POST'])
def create():
    print(request.form)
    # if there are errors:
    # We call the staticmethod on Thought thought to validate
    if not Thought.validate_thought(request.form):
        # redirect to the route where the thought form is rendered.
        return redirect('/thought/new')
    # else no errors:
    id = Thought.save(request.form)
    print(id)
    return redirect('/thoughts')

# ! ////// READ/RETRIEVE //////
# TODO ROOT ROUTE


# TODO READ ALL
@app.route('/thoughts')
def thoughts():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("thoughts.html",thoughts=Thought.get_all_with_user())

# # TODO READ ONE
# @app.route('/thought/show/<int:id>')
# def show(id):
#     data ={ 
#         "id":id
#     }
#     return render_template("show_thought.html",thought=Thought.get_one(data))

# ! ///// UPDATE /////
# TODO UPDATE REQUIRES TWO ROUTES
# TODO ONE TO SHOW THE FORM
@app.route('/thought/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_thought.html",thought=Thought.get_one(data))

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/thought/update',methods=['POST'])
def update():
    Thought.update(request.form)
    return redirect('/thoughts')

@app.route('/like/<int:id>')
def like(id):
    data = { 'id': id}
    Thought.update(data)
    return redirect('/thoughts')

@app.route('/unlike/<int:id>')
def unlike(id):
    data = { 'id': id}
    Thought.downdate(data)
    return redirect('/thoughts')

# ! ///// DELETE //////
@app.route('/thought/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Thought.destroy(data)
    return redirect('/thoughts')