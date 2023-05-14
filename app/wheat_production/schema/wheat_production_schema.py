from app.ext import ma
from marshmallow import fields

class WheatProductionSchema(ma.Schema):
    
    id = fields.Integer(dump_only=True)
    variety = fields.String()
    ontario_acres = fields.Integer()
    intake_ont = fields.Integer()
    pending = fields.Integer()
    intake = fields.Integer()
    
wheat_production_schema = WheatProductionSchema()
list_wheat_production_schema = WheatProductionSchema(many=True)
