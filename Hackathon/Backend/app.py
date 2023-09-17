from flask import Flask
from flask_cors import CORS
from db import mongo_connection  # Assuming you have a db.py file with the dbConnection function
from routes.auth import auth_blueprint  # Assuming you have a routes/auth.py file with auth_blueprint

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database connection
mongo_connection()

# Register blueprints for routes
app.register_blueprint(auth_blueprint, url_prefix='/api/auth')

@app.route('/')
def hello_world():
    return 'Hello World From Backend'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
