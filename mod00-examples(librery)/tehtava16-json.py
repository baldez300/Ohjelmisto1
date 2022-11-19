
# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.

"""from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/sum')
def get_sum():
    args = request.args
    # print(args)
    try:
        num1 = float(args.get("number1"))
        num2 = float(args.get("number2"))
        sum_of_nums = num1 + num2
        response_dic = {"num1": num1, "num2": num2, "sum": sum_of_nums}
        response_json = json.dumps(response_dic)
        return Response(response=response_json, status=200, mimetype="application/json")

    except TypeError:
        response_json = json.dumps({"message": "Invalid parameter: missing?", "status": "404 bad request"})
        return Response(response=response_json, status=400, mimetype="application/json")

    except ValueError:
        # TODO: convert response to json & fix mimetype
        return "Invalid parameter value, not a number"


@app.route('/moro')
def do_somthing_else():
    return 'Moro taas!'


@app.errorhandler(404)
def page_not_found(error):
    # convert exception object (error) to string
    error_text = str(error)
    # print(type(error_text))
    response_json = json.dumps({"error": error_text})
    return Response(response=response_json, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000) """
# =============================================================================
""""
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/sum')
def get_sum():
    args = request.args
    # print(args)
    try:
        num1 = float(args.get("number1"))
        num2 = float(args.get("number2"))
        sum_of_nums = num1 + num2
        response_dic = {"num1": num1, "num2": num2, "sum": sum_of_nums}
        response_json = json.dumps(response_dic)
        return Response(response=response_json, status=200, mimetype="application/json")

    except TypeError:
        response_json = json.dumps({"message": "Invalid parameter: missing?", "status": "404 bad request Balde"})
        return Response(response=response_json, status=400, mimetype="application/json")

    except ValueError:
        # TODO: convert response to json & fix mimetype
        # return "Invalid parameter value, not a number"
        response_json = json.dumps({"message": "Invalid parameter value, not a number", "status": "404 bad request"})
        return Response(response=response_json, status=400, mimetype="application/json")


@app.route('/moro/<yourname>/<location>')
def do_somthing_else(yourname, location):
    return f"Moro! {yourname} olet paikassa {location}"


@app.errorhandler(404)
def page_not_found(error):
    # convert exception object (error) to string
    error_text = str(error)
    # print(type(error_text))
    response_json = json.dumps({"error": error_text})
    return Response(response=response_json, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000) """
# =====================================

"""
from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/Is-prime')
def is_prime():
    args = request.args
    try:
        num = int(args.get('num1'))
        prime_num = True
        for i in range(2, num):
            if num % i == 0: prime_num = False

        response_dic = {"Number": num, "isPrime": prime_num}
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
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
    """
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
# app = Flask(__name__)


# @app.route('/airport/<icao>')
def icao_code(icao):
    # args = request.args
    try:
        sql = f"SELECT name, municipality from airport where ident='{icao}';"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            response_dic = {"ICAO": icao, "Name": i[0], "Municipality": i[1]}
            print(i[0], i[1])
            # print(i[1])
    except:
        return 'Hello'


airportIcaoCode = input("Valitse yllä olevista satunnaisista lentokentistä kirjoittamalla ICAO-koodi: ")
icao_code(airportIcaoCode)