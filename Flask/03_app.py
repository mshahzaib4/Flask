from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/name')
def hello_name():
    return 'What is your name!'

@app.route('/user/<name>')
def hello_name_red(name):
    if name.lower() == "shahzaib":  
        return redirect(url_for('hello_name')) 
if __name__ == "__main__":
    app.run(debug=True)
