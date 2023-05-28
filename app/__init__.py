from flask import Flask
from .db import db
from .ext import ma, migrate
from flasgger import Swagger
from flask_cors import CORS
from app.productions.controller.production import production_bp
from app.property_tables.controller.property_tables_controller import property_tables
from app.new_properties.controller.new_properties_controller import new_properties_bp
from app.white_beans_production.controller.white_beans_production_controller import white_beans_production
from app.type_entity.controller.type_entity_controler import type_entity_bp
from app.value_fields.controller.value_fields_controller import value_fields_bp
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
    app.register_blueprint(type_entity_bp, url_prefix=f"{prefix}/type_entity")
    app.register_blueprint(production_bp, url_prefix=f"{prefix}/productions")
    app.register_blueprint(property_tables, url_prefix=f"{prefix}/property_tables")
    app.register_blueprint(new_properties_bp, url_prefix=f"{prefix}/new_properties")
    app.register_blueprint(value_fields_bp, url_prefix=f"{prefix}/value_fields")
    
    app.register_blueprint(white_beans_production, url_prefix=f"{prefix}/white_beans_production")
    return app