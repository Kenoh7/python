from flask import render_template,redirect,session,request
from flask_app import app
from flask_app.models.task import Task
from flask_app.models.user import User

# display route --------------------------------------------------------------
@app.route('/task/add')
def add_task():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('add_task.html',user=User.get_by_id(data))

@app.route('/task/complete/<int:id>')
def complete_task(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Task.complete(data)
    return redirect('/dashboard')

@app.route('/task/edit/<int:id>')
def edit_task(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_task.html",edit=Task.get_one(data),user=User.get_by_id(user_data))

@app.route('/task/delete/<int:id>')
def delete_task(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Task.delete(data)
    return redirect('/dashboard')

@app.route('/task/update',methods=['POST'])
def update_task():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Task.is_valid (request.form):
        return redirect(f'/task/edit/{request.form["id"]}')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "due_date": request.form["due_date"],
        "id": request.form['id']
    }
    Task.update(data)
    return redirect('/dashboard')

@app.route('/task/completed',methods=['POST'])
def completed_task2():
    data = {
        "id": request.form['id'],
        "completed": request.form['completed']
    }
    Task.update2(data)
    return redirect('/dashboard')

@app.route('/task/view/<int:id>')
def view_task(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("view_task.html",task=Task.onetask_to_user(data),user=User.get_by_id(user_data))
# active route --------------------------------------------------------------

@app.route('/task/create',methods=['POST'])
def create_task():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Task.is_valid(request.form):
        return redirect('/task/add')
    data = {
        "user_id": session["user_id"],
        "name": request.form["name"],
        "description": request.form["description"],
        "due_date": request.form["due_date"]
    }
    Task.save(data)
    return redirect('/dashboard')

