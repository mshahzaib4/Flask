from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<html><body><h1>Hello, World!</h1></body></html>'

@app.route('/template')
def template():
    return render_template('04.html')

if __name__ == "__main__":
    app.run(debug=True)
