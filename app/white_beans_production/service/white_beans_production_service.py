from app.property_tables.service.property_tables_service import PropertyTablesService
from app.container import unitow_imp
from ..schema.white_beans_production_schema import list_white_beans_production
from app.db import mongo_db 

class WhiteBeansProductionService():
    
    def __init__(self) -> None:
        self.property_tables = PropertyTablesService()
    
    def get_all(self, page, per_page):
        wheat = unitow_imp.white_beans_production.list(page, per_page)
        data = list_white_beans_production.dump(wheat[0])
        properties = list(mongo_db.white_beans.find())
        result = self.property_tables.concat_data(data, properties)
        return {
            "code":200, 
            "data":result,
            "meta":wheat[1]
        }