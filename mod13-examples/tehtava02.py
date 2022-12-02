
# Toteuta taustapalvelu,
# joka palauttaa annettua lentokentän ICAO-koodia vastaavan lentokentän nimen ja kaupungin JSON-muodossa.
# Tiedot haetaan opintojaksolla käytetystä lentokenttätietokannasta.
# Esimerkiksi EFHK-koodia vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/kenttä/EFHK.
# Vastauksen on oltava muodossa: {"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}.

""""
from flask import Flask, request, Response
import json
import mysql.connector


def connect_database():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='user',
        password='password',
        autocommit=True
    )


connection = connect_database()
app = Flask(__name__)


@app.route('/airport/<icao>')
def icao_code(icao):
    args = request.args
    try:
        str(args.get(icao))
        sql = f"SELECT name, municipality from airport where ident='{icao}';"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            response_dic = {"ICAO": icao, "Name": i[0], "Municipality": i[1]}
            response_json = json.dumps(response_dic)
            return Response(response=response_json, status=200, mimetype="application/json")

    except TypeError:
        response_json = json.dumps({"message": "Invalid parameter: missing?", "status": "404 bad request"})
        return Response(response=response_json, status=400, mimetype="application/json")

    except ValueError:
        response_json = json.dumps({"message": "Invalid parameter value, not a number", "status": "404 bad request"})
        return Response(response=response_json, status=400, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(error):
    # convert exception object (error) to string
    error_text = str(error)
    response_json = json.dumps({"error": error_text})
    return Response(response=response_json, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

"""

# Sama kuin komenti ulhaalla
import mysql.connector
from flask import Flask  # , request, Response
from flask_cors import CORS


def connect_db():
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='user',
        password='password',
        autocommit=True
    )


def get_airport(icao):
    sql = f"select ident, name, municipality from airport where ident='{icao}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result_set = cursor.fetchone()
    if cursor.rowcount > 0:
        return {"ICAO": result_set[0], "name": result_set[1], "municipality": result_set[2]}
    else:
        return {"Error": "No results."}


connection = connect_db()
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/airport/<icao>')
def airport(icao):
    response = get_airport(icao)
    return response


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)