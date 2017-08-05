from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Flask is working!'

app.run(host='127.0.0.1', port=3000, debug=True)
