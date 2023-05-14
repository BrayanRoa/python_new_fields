from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
from config.development import MONGO_CONNECTION

db = SQLAlchemy()

client = MongoClient(MONGO_CONNECTION)
mongo_db = client['prisma_test']
collections = mongo_db.list_collection_names()

# print(mongo_db["wheat_production"])
# tabla_collection = mongo_db.pruebaaaaaa

# tabla_schema = {
#     "nombre": {
#         "type": "string", 
#         "required": True
#     },
#     "columnas": [{
#             "nombre": {
#                 "type": "string", 
#                 "required": True
#             },
#             "tipo": {
#                 "type": "string", 
#                 "required": True
#             },
#             "formula": {
#                 "type": "string", 
#                 "required": False}
#             }
#     ]
# }

# tabla_collection.insert_one(tabla_schema)
# mongo_db.usuarios.insert_one({'nombre': 'Juan', 'edad': 30})

# print(colecciones)