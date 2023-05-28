from app.db import db
from sqlalchemy.orm import mapper
from app.type_entity.model.type_entity_model import TypeEntityModel

class TypeEntity(db.Model):
    
    __tablename__ = "type_entity"
    # __table_args__ = {'schema': 'pattern'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    productions = db.relationship("ProductionEntity", back_populates="type_ent")
    new_properties = db.relationship("NewPropertiesEntity", back_populates="type_ent")
    
    def start_mapper():
        mapper(TypeEntityModel,TypeEntity)