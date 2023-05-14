from app.container import unitow_imp
from app.wheat_production.schema.wheat_production_schema import list_wheat_production_schema
from app.db import mongo_db
from app.property_tables.service.property_tables_service import PropertyTablesService


class WheatProductionService():

    def __init__(self) -> None:
        self.property_tables = PropertyTablesService()
    
    def get_all(self, page, per_page):
        wheat = unitow_imp.wheat_production.list(page, per_page)
        data = list_wheat_production_schema.dump(wheat[0])
        properties = list(mongo_db.wheat_production.find())
        result = self.property_tables.concat_data(data, properties)
        return {
            "code":200, 
            "data":result,
            "meta":wheat[1]
        }
        
    #! OJO, DEBEMOS VALIDAR QUE NO SE INGRESEN DATOS MALICIOSOS
    #! LIMPIAR LOS ESPACIOS EN BLANCO
    # def concatenar_data(self, data, properties):
    #     for obj in data:
    #         for formula in properties:
    #             resultado = eval(formula["formula"],{}, obj)
    #             obj[formula["nombre"]] = resultado
    #     return data
    
    # def new_properties(self, data, table):
    #     if table not in colecciones:
    #         mongo_db.create_collection(table)
        
    #     new_document = {
    #         "nombre": data["nombre"], 
    #         "tipo": data["tipo"], 
    #         "formula": data["formula"]
    #     }            
    #     mongo_db[table].insert_one(new_document)
    #     return {"code":201, "data":"model_data"}
