from app import app
from config import *

app.secret_key = SECRET_KEY
app.run(host='0.0.0.0', port=8080, debug=DEBUG)
