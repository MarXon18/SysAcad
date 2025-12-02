import logging
from flask import Flask
import os
from flask_migrate import Migrate
from app.config import config
from flask_sqlalchemy import SQLAlchemy

#extensiones adicionales
from flask_marshmallow import Marshmallow
from flask_hashids import Hashids

db = SQLAlchemy()
migrate = Migrate()
#agregue:
ma = Marshmallow()
hashids = Hashids()

def create_app() -> Flask:
    """
    Using an Application Factory
    Ref: Book Flask Web Development Page 78
    """
    app = Flask(__name__)
    app_context = os.getenv('FLASK_CONTEXT')
    #https://flask.palletsprojects.com/en/stable/api/#flask.Flask
    #app = Flask(__name__)
    f = config.factory(app_context if app_context else 'development') 
    app.config.from_object(f)

    #inicializacion de extensiones
    db.init_app(app)
    migrate.init_app(app,db)
    hashids.init_app(app) 
    ma.init_app(app) 

    #registro de rutas
    from app.resources import init_routes
    init_routes(app)


    @app.shell_context_processor    
    def ctx():
        return {"app": app}
    
    return app
