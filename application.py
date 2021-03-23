from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Lab06 - Devops</h1>\nFIAP - MBA! v2 \o/"
