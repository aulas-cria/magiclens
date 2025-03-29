from flask import Flask

app = Flask(__name__)

@app.route('/api/status')
def index():
    return {'message': 'Ok'}
