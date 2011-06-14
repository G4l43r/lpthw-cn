from flask import Flask
app = Flask(".")
app.debug = True

@app.route("/")
def hello():
    greeting = "Hello World"
    return greeting

if __name__ == "__main__":
    app.run()

