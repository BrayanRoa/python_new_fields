from bson import ObjectId, schema

user_schema = schema.Schema({
    'nombre': str,
    'tipo': str,
    'formula': int,
})