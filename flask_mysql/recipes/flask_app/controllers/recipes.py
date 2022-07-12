from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

# ! ////// CREATE  //////
# TODO CREATE REQUIRES TWO ROUTES:
# TODO ONE TO DISPLAY THE FORM:
@app.route('/recipe/new')
def new():
    return render_template("new_recipe.html")

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/recipe/create',methods=['POST'])
def create():
    print(request.form)
    # if there are errors:
    # We call the staticmethod on Recipe recipe to validate
    if not Recipe.validate_recipe(request.form):
        # redirect to the route where the recipe form is rendered.
        return redirect('/recipe/new')
    # else no errors:
    id = Recipe.save(request.form)
    print(id)
    return redirect(f'/recipe/show/{id}')

# ! ////// READ/RETRIEVE //////
# TODO ROOT ROUTE


# TODO READ ALL
@app.route('/recipes')
def recipes():
    if 'user_id' not in session:
        return redirect('/logout')
    return render_template("recipes.html",recipes=Recipe.get_all())

# TODO READ ONE
@app.route('/recipe/show/<int:id>')
def show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ "id":id}
    return render_template("show_recipe.html",recipe=Recipe.get_one(data))

# ! ///// UPDATE /////
# TODO UPDATE REQUIRES TWO ROUTES
# TODO ONE TO SHOW THE FORM
@app.route('/recipe/edit/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data ={ "id":id }
    return render_template("edit_recipe.html",recipe=Recipe.get_one(data))

# TODO ONE TO HANDLE THE DATA FROM THE FORM
@app.route('/recipe/update',methods=['POST'])
def update():
    Recipe.update(request.form)
    return redirect('/recipes')

# ! ///// DELETE //////
@app.route('/recipe/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Recipe.destroy(data)
    return redirect('/recipes')