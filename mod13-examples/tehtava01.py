
# Toteuta Flask-taustapalvelu, joka ilmoittaa, onko parametrina saatu luku alkuluku vai ei.
# Hyödynnä toteutuksessa aiempaa tehtävää, jossa alkuluvun testaus tehtiin.
# Esimerkiksi lukua 31 vastaava GET-pyyntö annetaan muodossa: http://127.0.0.1:3000/alkuluku/31.
# Vastauksen on oltava muodossa: {"Number":31, "isPrime":true}.


from flask import Flask, request, Response
import json

app = Flask(__name__)


@app.route('/is-prime')
def is_prime():
    args = request.args
    try:
        num = int(args.get("number"))
        prime_num = True
        for i in range(2, num):
            if num % i == 0: prime_num = False

        response_dic = {"Number": num, "isPrime": prime_num}
        response_json = json.dumps(response_dic)
        return Response(response=response_json, status=200, mimetype="application/json")

    except TypeError:
        response_json = json.dumps({"message": "Invalid parameter: missing?", "status": "404 bad request Balde"})
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