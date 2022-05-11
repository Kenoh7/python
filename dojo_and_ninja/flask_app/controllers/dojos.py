from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route("/")
def re_direct():
    return redirect('/dojos')

@app.route("/dojos")
def home():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos)

@app.route("/ninja")
def ninja():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos=dojos)

@app.route('/dojos/create', methods=["POST"])
def create_dojo():
    data = {
        "name": request.form["name"],
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("dojo_show.html",dojo=Dojo.get_one(data), ninjas=Ninja.get_one(data))

@app.route('/create_ninja',methods=["POST"])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/dojos')