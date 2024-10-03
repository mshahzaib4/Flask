from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"
@app.route('/<float:date>')
def date(date):
    return "Hello, World! %s" % date
