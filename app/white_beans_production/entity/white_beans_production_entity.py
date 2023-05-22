from app.db import db
from sqlalchemy.orm import mapper
from ..model.white_beans_production_model import WhiteBeansProductionModel

class WhiteBeansEntity(db.Model):
    
    __tablename__="white_beans"
    
    id = db.Column(db.Integer, primary_key=True)
    variety=db.Column(db.String)
    ontario_acres=db.Column(db.Integer)
    intake_ont=db.Column(db.Integer)
    pending=db.Column(db.Integer)
    intake=db.Column(db.Integer)
    dumped=db.Column(db.Integer)
    estimate_planted=db.Column(db.Integer)
    percentage_of_sales=db.Column(db.Integer)
    
    def start_mapper():
        mapper(WhiteBeansProductionModel, WhiteBeansEntity)
        
    def __str__(self):
        return {
            "id":self.id,
            "variety":self.variety,
            "ontario_acres":self.ontario_acres,
            "intake_ont":self.intake_ont,
            "pending":self.pending,
            "intake":self.intake,
            "dumped":self.dumped,
            "estimate_planted":self.estimate_planted,
            "percentage_of_sales":self.percentage_of_sales
        }
        