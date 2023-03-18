from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'main.login'
bootstrap = Bootstrap()



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    bootstrap.init_app(app)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp,url_prefix='/api')


    
    return app

from app import models