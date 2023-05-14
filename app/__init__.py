from flask import Flask
from .db import db
from .ext import ma, migrate
from flasgger import Swagger
from flask_cors import CORS
from app.wheat_production.controller.wheat_production import wheat_production
from app.property_tables.controller.property_tables_controller import property_tables

prefix="/api/v1"

def create_app(settings_module):
    app = Flask(__name__)
    
    app.config.from_object(settings_module)
    host = app.config.get("SITE_HOST")
    
    swagger_template = {
        "info": {
            'title': 'Api Python Test',
            'version': '0.1',
            'description': 'This document contains the list of API services '
                           'with Python.',
        },
        "host": host,
        "schemes":["http" , "https"],
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "Authorization: Bearer {token}"
            }   
        },
        "security": [
            {
                "Bearer": []
            }
        ]
    }
    CORS(app, supports_credentials=False)
    Swagger(app, template=swagger_template)
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app)
    
    #* BLUEPRINTS
    app.register_blueprint(wheat_production, url_prefix=f"{prefix}/wheat_production")
    app.register_blueprint(property_tables, url_prefix=f"{prefix}/property_tables")
    return app