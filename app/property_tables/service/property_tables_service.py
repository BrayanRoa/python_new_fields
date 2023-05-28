from app.db import collections, mongo_db

class PropertyTablesService():

    def new_properties(self, data, table):
        if table not in collections:
            mongo_db.create_collection(table)
        new_document = {
            "name": data["name"], 
            "type": data["type"], 
            "formula": data["formula"]
        }            
        mongo_db[table].insert_one(new_document)
        return {
            "code":201, 
            "data":f"new properties added succesfully to {table}"
        }
    
    def concat_data(self, data, properties):
        for obj in data:
            for formula in properties:
                resultado = eval(formula["form"],{}, obj)
                obj[formula["name"]] = resultado
        return data