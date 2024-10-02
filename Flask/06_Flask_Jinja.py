from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/<uname>/')
def hello_name(uname):
    return render_template("06_Flask_Jinja.html", name=uname)


app.run(debug=True)