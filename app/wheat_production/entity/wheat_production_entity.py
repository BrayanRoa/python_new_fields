from app.db import db
from sqlalchemy.orm import mapper
from app.wheat_production.model.wheat_production_model import WheatProductionModel

class WheatProductionEntity(db.Model):
    
    __tablename__="wheat"
    
    id=db.Column(db.Integer, primary_key=True)
    variety = db.Column(db.String)
    ontario_acres = db.Column(db.Integer)
    intake_ont = db.Column(db.Integer)
    pending = db.Column(db.Integer)
    intake = db.Column(db.Integer)
    
    def start_mappers():
        mapper(WheatProductionModel, WheatProductionEntity)
        
    def __str__(self):
        return {
            "id":self.id,
            "variety":self.variety,
            "ontario_acres":self.ontario_acres,
            "intake_ont":self.intake_ont,
            "pending":self.pending,
            "intake":self.intake
        }
        
        