from flask import Flask

app =Flask(__name__)
@app.route('/')
def index():
    return "Hi"
@app.route('/name')
def name():
    return " Shahzaib Yaqoob"
if __name__ == "__main__":
    app.run(debug= True)


