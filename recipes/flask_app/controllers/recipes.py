from flask import render_template,redirect,session,request
from flask_app import app
from flask_app.models.recipe import Recipe
from flask_app.models.user import User

# display route --------------------------------------------------------------
@app.route('/recipe/add')
def add_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('add_recipe.html',user=User.get_by_id(data))

@app.route('/recipe/edit/<int:id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_recipe.html",edit=Recipe.get_one(data),user=User.get_by_id(user_data))

@app.route('/recipe/delete/<int:id>')
def delete_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Recipe.delete(data)
    return redirect('/dashboard')

@app.route('/recipe/update',methods=['POST'])
def update_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.is_validate(request.form):
        return redirect(f'/recipe/edit/{request.form["id"]}')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under_30": request.form["under_30"],
        "date_made": request.form["date_made"],
        "id": request.form['id']
    }
    Recipe.update(data)
    return redirect('/dashboard')

@app.route('/recipe/view/<int:id>')
def view_recipe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("view_recipe.html",recipe=Recipe.get_one(data),user=User.get_by_id(user_data))
# active route --------------------------------------------------------------

@app.route('/recipe/create',methods=['POST'])
def create_recipe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Recipe.is_validate(request.form):
        return redirect('/recipe/add')
    data = {
        "user_id": session["user_id"],
        "name": request.form["name"],
        "description": request.form["description"],
        "instructions": request.form["instructions"],
        "under_30": request.form["under_30"],
        "date_made": request.form["date_made"]
    }
    Recipe.save(data)
    return redirect('/dashboard')

