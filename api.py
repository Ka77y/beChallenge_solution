from flask import Flask
import json
from flask_caching import Cache

# implementacion del servicio
from retrieve_users import retrieveUsers

app = Flask(__name__)
#cache = Cache(app, config={'CACHE_TYPE': 'redis', 'CACHE_REDIS_URL': 'redis://localhost:6379/0'})

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/retrieveUser/<username>', methods=['GET'])
@app.route('/retrieveUser/<username>/<int:page>', methods=['GET'])
#@cache.cached(timeout=10)
def retrieveUserByName(username, page=1):
    try:
        per_page = 10
        response = retrieveUsers(username, per_page, page)
        print("paseeeeeotaveeee")
        return json.load(json.dumps(response))
    except Exception as e:
        return "something was wrong :(", e

if __name__ == '__main__':
    app.run(host='0.0.0.0',
            debug=True,
            port=9200)