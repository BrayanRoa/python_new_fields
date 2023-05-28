from app.ext import ma
from marshmallow import fields
from app.new_properties.schema.new_properties_schema import NewPropertiesSchema

class ValueFieldsSchema(ma.Schema):
    
    id = fields.Integer(dump_only=True)
    value = fields.String()
    new_propertie = fields.Nested(NewPropertiesSchema)
    
value_fields_schema = ValueFieldsSchema()
list_value_fields_schema = ValueFieldsSchema(many=True)