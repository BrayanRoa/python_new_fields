from app.db import db
from sqlalchemy.orm import mapper
from app.productions.model.production_model import ProductionModel

class ProductionEntity(db.Model):
    
    __tablename__="production"
    # __table_args__ = {'schema': 'pattern'}
    
    id=db.Column(db.Integer, primary_key=True)
    variety = db.Column(db.String)
    ontario_acres = db.Column(db.Integer)
    intake_ont = db.Column(db.Integer)
    pending = db.Column(db.Integer)
    intake = db.Column(db.Integer)
    dumped = db.Column(db.String)
    on_60_lbs = db.Column(db.String)
    porcentage_sold = db.Column(db.String)
    acres = db.Column(db.String)
    shrink = db.Column(db.String)
    seed_rate = db.Column(db.String)
    estimate_acres = db.Column(db.String)
    yieldd = db.Column(db.String)
    source = db.Column(db.String)
    comment = db.Column(db.String)
    new_breeder_seed_in = db.Column(db.String)
    
    type_entity_id = db.Column(db.Integer, db.ForeignKey("type_entity.id"))
    type_ent = db.relationship("TypeEntity", back_populates="productions")

    value_field = db.relationship("ValueFieldsEntity", back_populates="production")
    
    
    def start_mappers():
        mapper(ProductionModel, ProductionEntity)
        
    # def __str__(self):
    #     return {
    #         "id":self.id,
    #         "variety":self.variety,
    #         "ontario_acres":self.ontario_acres,
    #         "intake_ont":self.intake_ont,
    #         "pending":self.pending,
    #         "intake":self.intake
    #     }
        
        