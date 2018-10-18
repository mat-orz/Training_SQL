from flask import Flask, jsonify
from flask_cors import CORS
import datetime
import argparse
import pymssql
import json

# parser options
parser = argparse.ArgumentParser()
parser.add_argument("db_ip")
parser.add_argument("db_port")
parser.add_argument("db_instance")
parser.add_argument("db_name")
parser.add_argument("db_user")
parser.add_argument("db_password")
args = parser.parse_args()
print(args)

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })


@app.route('/date', methods=['GET'])
def get_date():
    return jsonify(datetime.datetime.now().isoformat())

@app.route('/athletes', methods=['GET'])
def get_athletes():

    column_fields = ['Athlete Nick Name',
                                'Athlete Name',
                                'Athlete Surname',
                                'Division',
                                'Birth Date']
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * from dbo.T_cfg_Athletes")
    values = cursor.fetchall()
    conn.close()

    athletesData = []
    for value in values:
        athletesData.append({column_fields[0]: value[0],
                             column_fields[1]: value[1],
                             column_fields[2]: value[2],
                             column_fields[3]: value[3],
                             column_fields[4]: value[4]})

    json_values = jsonify({'fields': column_fields, 'athletes': athletesData})

    return json_values



def get_connection():
    return pymssql.connect(host=args.db_ip, server=args.db_instance, user=args.db_user, password=args.db_password,
                           database=args.db_name, port=args.db_port)

if __name__ == '__main__':

    app.run()
