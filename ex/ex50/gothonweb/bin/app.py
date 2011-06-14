from flask import Flask
from flask import render_template

app = Flask(".")
app.debug = True

@app.route("/")
def hello():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)

if __name__ == "__main__":
    app.run()

