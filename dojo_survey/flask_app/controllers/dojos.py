from flask import render_template, request, redirect, session

from flask_app import app
from flask_app.models.dojo import Dojo

# display routes ------------------------------
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html', name=session["name"], location=session["location"], language=session["language"], comment=session["comment"])

# active routes ------------------------------
@app.route("/create", methods=["POST"])
def create_form():
    if not Dojo.validate_dojo(request.form):
        return redirect('/')
    print(request.form)
    session["name"] = request.form["name"]
    session["location"]= request.form["location"]
    session["language"]= request.form["language"]
    session["comment"]= request.form["comment"]
    Dojo.save(request.form)
    return redirect('/result')

@app.route('/create/clear')
def clear():
    session.clear();
    return redirect('/')