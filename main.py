from api import *
from models import *

if __name__ == '__main__':
    db.connect()
    db.create_tables([User])
    app.run(host='0.0.0.0',
            debug=True,
            port=8080)