from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.magazine import Magazine

# ! ////// CREATE  //////
# TODO CREATE REQUIRES TWO ROUTES:
# TODO ONE TO DISPLAY THE FORM:
@app.route('/magazine/new')
def new():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("new_magazine.html")

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/magazine/create',methods=['POST'])
def create():
    print(request.form)
    # if there are errors:
    # We call the staticmethod on Magazine magazine to validate
    if not Magazine.validate_magazine(request.form):
        # redirect to the route where the magazine form is rendered.
        return redirect('/magazine/new')
    # else no errors:
    id = Magazine.save(request.form)
    print(id)
    return redirect(f'/magazine/show/{id}')

# ! ////// READ/RETRIEVE //////
# TODO ROOT ROUTE


# TODO READ ALL
@app.route('/magazines')
def magazines():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("magazines.html",magazines=Magazine.get_all_with_user())

# TODO READ ONE
@app.route('/magazine/show/<int:id>')
def show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ 
        "id":id
    }
    return render_template("show_magazine.html",magazine=Magazine.get_one(data))

# ! ///// UPDATE /////
# TODO UPDATE REQUIRES TWO ROUTES
# TODO ONE TO SHOW THE FORM
# @app.route('/magazine/edit/<int:id>')
# def edit(id):
#     data ={ 
#         "id":id
#     }
#     return render_template("edit_magazine.html",magazine=Magazine.get_one(data))

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/magazine/update',methods=['POST'])
def update():
    Magazine.update(request.form)
    return redirect('/magazines')

# ! ///// DELETE //////
@app.route('/magazine/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Magazine.destroy(data)
    return redirect('/magazines')


