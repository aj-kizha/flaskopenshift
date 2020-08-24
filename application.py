from flask import Flask

application = Flask(__name__)

@app.route('/')
def hello():
    return "hello woorld"

application.run()