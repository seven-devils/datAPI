#!/datAPI/flask/bin/python

"""
This is the actual API to listen for requests.

This simply needs to be run in order to begin the listen state.
Default port is 5000, so ensure it's open in the firewall.
"""


from flask import Flask, jsonify
from fibo import restfib

api = Flask(__name__)


@api.route('/')
def index():
    return "The Fibonacci sequence API.\nSend POST/GET to /fibo/api/v1.0/<int>\n"


@api.route('/fibo/api/v1.0/<steps>', methods=['POST', 'GET'])
def do_fibo(steps):
    try:
        steps = int(steps)
    except ValueError:
        return jsonify(
            {"result": {"Error01": "You must submit a whole number!"}})
    obj = restfib()
    result = obj.san_number(steps)
    if result is True:
        result = obj.make_list(steps)
    return jsonify({'result': result})

if __name__ == '__main__':
    api.run(host='0.0.0.0')
