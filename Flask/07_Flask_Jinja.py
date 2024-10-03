from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def Subject():
    result = {'Maths': 80, 'programming': 90, 'Urdu': 80}
    return render_template('07_Flask_jinja.html', result=result)

app.run(debug=True)