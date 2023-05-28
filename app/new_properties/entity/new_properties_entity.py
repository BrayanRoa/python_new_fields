from app.db import db
from sqlalchemy.orm import mapper
from app.new_properties.model.new_properties_model import NewPropertiesModel

class NewPropertiesEntity(db.Model):
    
    __tablename__="new_properties"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    is_calculated = db.Column(db.Boolean)
    form = db.Column(db.String)
    is_required = db.Column(db.Boolean)    
    condition = db.Column(db.String)
    description = db.Column(db.String)
    
    type_entity_id = db.Column(db.Integer, db.ForeignKey("type_entity.id"))
    type_ent = db.relationship("TypeEntity", back_populates="new_properties")

    value_field = db.relationship("ValueFieldsEntity", back_populates="new_propertie")
    
    def start_mapper():
        mapper(NewPropertiesModel, NewPropertiesEntity)