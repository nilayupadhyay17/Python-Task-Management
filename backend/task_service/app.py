from flask import Flask
from flask_jwt_extended import JWTManager
from db import db
from routes import task_bp
import config

print("DB_HOST in app.py:", os.getenv("DB_HOST"))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["JWT_SECRET_KEY"] = config.JWT_SECRET_KEY

db.init_app(app)
jwt = JWTManager(app)

app.register_blueprint(task_bp, url_prefix="/tasks")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5002, debug=True)
