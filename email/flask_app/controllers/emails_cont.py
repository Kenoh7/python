from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.email import Email

# display routes ------------------------------
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/success')
def result():
    return render_template('success.html', emails=Email.get_all())

# active routes ------------------------------
@app.route("/create", methods=["POST"])
def create():
    if not Email.is_valid(request.form):
        return redirect('/')
    Email.save(request.form)
    return redirect('/success')