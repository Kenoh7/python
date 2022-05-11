from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Welcome to Playground, type /play to the url"
@app.route('/play')
def boxes():
    return render_template("playground.html", times=3,color="aqua")
@app.route('/play/<int:times>')
def num_box(times):
    return render_template("playground.html",times=times,color="aqua")
@app.route('/play/<int:times>/<string:color>')
def color(times, color):
    return render_template("playground.html",times=times, color=color)
if __name__=="__main__":
    app.run(debug=True)