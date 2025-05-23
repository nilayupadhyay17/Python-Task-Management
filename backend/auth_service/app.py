from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy
from db import db
from models import User 
from routes import auth_bp
from flask_migrate import Migrate
import config
import os

print("DB_HOST in app.py:", os.getenv("DB_HOST"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY
app.config['DEBUG'] = True

print(config.SQLALCHEMY_DATABASE_URI)
db.init_app(app)
jwt = JWTManager(app)
migrate = Migrate(app,db)
app.register_blueprint(auth_bp, url_prefix="/auth")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5001)
