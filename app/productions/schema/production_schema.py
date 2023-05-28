from app.ext import ma
from marshmallow import fields
from app.value_fields.schema.value_fields_schema import ValueFieldsSchema

class ProductionSchema(ma.Schema):
    
    id = fields.Integer(dump_only=True)
    variety = fields.String()
    ontario_acres = fields.Integer()
    intake_ont = fields.Integer()
    pending = fields.Integer() 
    intake = fields.Integer()
    dumped = fields.String()
    on_60_lbs=fields.String()
    porcentage_sold=fields.String()
    acres=fields.String()
    shrink=fields.String()
    seed_rate=fields.String()
    estimate_acres=fields.String()
    yieldd=fields.String()
    source=fields.String()
    comment=fields.String()
    new_breeder_seed_in=fields.String()
    
    value_field = fields.Nested(ValueFieldsSchema, many=True)
        
production_schema = ProductionSchema()
list_production_schema = ProductionSchema(many=True)
