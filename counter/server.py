from flask import Flask,render_template,redirect, session
app = Flask(__name__)
app.secret_key = 'dont share my secret key'

@app.route('/')
def index():
    return "Welcome! Lets Count Views Together!!"

# Display ----------------------------------------
@app.route('/count')
def count():
    if 'count' not in session:
        session['count'] = 1
    session['count'] += 1
    return render_template('index.html', count=session['count'])
# Active -----------------------------------------
@app.route('/destroy_session',methods=['POST'])
def destroy_session():
    session['count'] = 1
    return redirect('/count')

if __name__=="__main__":
    app.run(debug=True)