from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    with open("test/index.html", "r") as file:
        html = file.read()
    return html, 200

app.run("0.0.0.0", 5000)