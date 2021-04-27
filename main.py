from api import *
from models import *
import os
port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    db.connect()
    db.create_tables([User])
    app.run(host='0.0.0.0',
            debug=True,
            port=port)