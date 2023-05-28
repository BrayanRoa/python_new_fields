from app.db import db
from sqlalchemy.orm import mapper
from app.value_fields.model.value_fields_model import ValueFieldsModel

class ValueFieldsEntity(db.Model):
    
    __tablaname__="value_fields"
    
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String)
    
    production_id = db.Column(db.Integer, db.ForeignKey("production.id"))
    production = db.relationship("ProductionEntity", back_populates="value_field")

    new_propertie_id = db.Column(db.Integer, db.ForeignKey("new_properties.id"))
    new_propertie = db.relationship("NewPropertiesEntity", back_populates="")

    def start_mapper():
        mapper(ValueFieldsModel, ValueFieldsEntity)