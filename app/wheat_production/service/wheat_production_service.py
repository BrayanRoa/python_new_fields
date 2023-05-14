from app.container import unitow_imp
from app.wheat_production.schema.wheat_production_schema import list_wheat_production_schema
# from app.db import tabla_collection
from app.db import colecciones, mongo_db

class WheatProductionService():
    
    def get_all(self, page, per_page):
        wheat = unitow_imp.wheat_production.list(page, per_page)
        data = list_wheat_production_schema.dump(wheat[0])
        documents = list(mongo_db.wheat_production.find())
        for obj in data:
            for formula in documents:
                resultado = eval(formula["formula"],{}, obj)
                obj[formula["nombre"]] = resultado
        return {
            "code":200, 
            "data":data, 
            "meta":wheat[1]
        }
        
    def new_properties(self, data):
        if "wheat_production" not in colecciones:
            mongo_db.wheat_production
        else:
            new_document = {
                    "nombre": data["nombre"], 
                    "tipo": data["tipo"], 
                    "formula": data["formula"]
            }            
            mongo_db["wheat_production"].insert_one(new_document)
        return {"code":201, "data":"model_data"}
