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


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')



@app.route('/date', methods=['GET'])
def get_date():
    return jsonify(datetime.datetime.now().isoformat())

@app.route('/athletes', methods=['GET'])
def get_athletes():

    column_fields = [ 'Athlete Name',
                      'Athlete Surname',
                                'Division',
                                'Birth Date', 'showDetails']
    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT athleteNickName, athleteName, athleteSurName, divisionDescr, bornDate from dbo.T_cfg_Athletes join T_sys_Divisions on T_cfg_Athletes.division = T_sys_Divisions.division"
    print(query)

    cursor.execute(query)
    values = cursor.fetchall()
    conn.close()

    athletesData = []
    for value in values:
        print(value[0] + ' - ' + value[1]  + value[2] + value[3] + str(value[4]))
        athletesData.append({'AthleteNickName': value[0],
                             column_fields[0]: value[1],
                             column_fields[1]: value[2],
                             column_fields[2]: value[3],
                             column_fields[3]: value[4],
                             '_show_details' : 'true'})

    json_values = jsonify({'fields': column_fields, 'athletes': athletesData})

    return json_values



def get_connection():
    return pymssql.connect(host=args.db_ip, server=args.db_instance, user=args.db_user, password=args.db_password,
                           database=args.db_name, port=args.db_port)

if __name__ == '__main__':

    app.run()
