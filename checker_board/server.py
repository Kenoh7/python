from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Welcome to CheckerBoard, type /view to the url"

@app.route('/view')
def color():
    return render_template("index.html",rows=4,columns=4,color1="black",color2="white")

@app.route('/view/<int:rows>/<int:columns>/<string:color1>/<string:color2>')
def columns_only(rows,columns,color1,color2):
    return render_template('index.html',rows=rows,columns=columns,color1=color1,color2=color2)

if __name__=="__main__":
    app.run(debug=True)