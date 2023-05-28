from app.ext import ma
from marshmallow import fields

class NewPropertiesSchema(ma.Schema):
    
    id = fields.Integer(dump_only=True)
    name = fields.String()
    type = fields.String()
    is_calculated = fields.Boolean()
    form = fields.String()
    is_required = fields.Boolean()   
    condition = fields.String()
    description = fields.String()
    type_entity_id = fields.Integer()
    
new_properties_schema=NewPropertiesSchema()
list_new_properties_schema=NewPropertiesSchema(many=True)