from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.user import User

@app.route("/")
def index():
    users = User.get_all()
    return render_template("home.html", users=users)

@app.route("/add")
def user():
    return render_template("add.html")


@app.route('/create', methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    User.save(data)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html",user=User.get_one(data))

@app.route('/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show.html",user=User.get_one(data))

@app.route('/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    User.delete(data)
    return redirect('/')