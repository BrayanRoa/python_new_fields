from app.ext import ma
from marshmallow import fields
from app.productions.schema.production_schema import ProductionSchema

class TypeEntitySchema(ma.Schema):
    
    id = fields.Integer(dump_only=True)
    name = fields.String()
    productions = fields.Nested(ProductionSchema, many=True)
    
type_entity_schema = TypeEntitySchema() 
list_type_entity_schema = TypeEntitySchema(many=True) 