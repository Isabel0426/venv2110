from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hola tripulantes 2022-2</h1>"