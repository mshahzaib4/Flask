from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def registeration_page():
    return render_template("09_registeration_page.html")
@app.route('/success', methods = ['POST'])
def success1():
    result = request.form
    return render_template("registeration_page_output.html", result = result)
    
if __name__ == "__main__":
    app.run(debug= True)