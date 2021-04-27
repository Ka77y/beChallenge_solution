from flask import Flask, jsonify

# implementacion del servicio
from flask_caching import Cache
from retrieve_users import retrieveUsers

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/bechanllengeapi/user/<username>', methods=['GET'])
@app.route('/bechanllengeapi/user/<username>/<int:page>', methods=['GET'])
@cache.cached(timeout=10)
def retrieveUserByName(username, page=1):
    try:
        per_page = 10
        response = retrieveUsers(username, per_page, page)
        return jsonify(response)
    except Exception:
        return {
            "status": "400",
            "message": "something was wrong :("
        }

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            debug=True,
            port=9200)