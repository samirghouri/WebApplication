from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route("/add/<int:a>/<int:b>")
def api_info(a, b):
    return str(a+b)


