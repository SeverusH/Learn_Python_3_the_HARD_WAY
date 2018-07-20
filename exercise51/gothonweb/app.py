from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello", methods = ['POST', 'GET'])
def index():
    #greet = request.args.get('greeting', 'Hello')
    #name = request.args.get('name', 'Nobody')
    if request.method == 'POST':
        greet = request.form.get('greeting', 'Hello')
        name = request.form.get('name', 'Nobody')

        if greet:
            greeting = f"{greet} "
        else:
            greeting = "Hello "

        if name:
            greeting += name
        else:
            greeting += "World"

        return render_template("index_laid_out.html", greeting = greeting, app=repr(app.__dict__))
    else:
        return render_template("hello_form_laid_out.html")


if __name__ == '__main__':
    app.run()
