import os
from app import create_app

PORT = int(os.getenv('PYDIARY_PORT', '8080'))
app = create_app('config.DevelopmentConfig')
app.run(host='127.0.0.1', port=PORT)
