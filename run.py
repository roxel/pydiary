from app import create_app

app = create_app('config.DevelopmentConfig')
app.run(host='0.0.0.0', port=8080)
