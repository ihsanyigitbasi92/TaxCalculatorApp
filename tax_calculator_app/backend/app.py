from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from config import Config
from routes import auth, tax, profile

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
jwt = JWTManager(app)

app.register_blueprint(auth.bp)
app.register_blueprint(tax.bp)
app.register_blueprint(profile.bp)

if __name__ == '__main__':
    app.run()