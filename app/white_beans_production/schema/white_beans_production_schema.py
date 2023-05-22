from app.ext import ma
from marshmallow import fields

class WhiteBeansProductionSchema(ma.Schema):
    
    id = fields.Integer(dump_only=True)
    variety=fields.String()
    ontario_acres=fields.Integer()
    intake_ont=fields.Integer()
    pending=fields.Integer()
    intake=fields.Integer()
    dumped=fields.Integer()
    estimate_planted=fields.Integer()
    percentage_of_sales=fields.Integer()
    
white_beans_production = WhiteBeansProductionSchema()
list_white_beans_production = WhiteBeansProductionSchema(many=True)