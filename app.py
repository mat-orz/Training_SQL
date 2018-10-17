from flask import Flask, jsonify
from flask_cors import CORS
import datetime


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/date', methods=['GET'])
def get_date():
    return jsonify(datetime.datetime.now().isoformat())


if __name__ == '__main__':
    app.run()