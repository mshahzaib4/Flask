from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/05_app', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usname = request.form["uname"]
        pword = request.form["pword"]
        if usname == "Shahzaib" and pword == "0000":
            return "Welcome, Shahzaib"
        else:
            return "Invalid username or password"
    return render_template('05.html')

if __name__ == '__main__':
    app.run(debug=True)
