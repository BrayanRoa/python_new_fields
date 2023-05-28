from app.container import unitow_imp
from app.type_entity.schema.type_entity_schema import list_type_entity_schema


class TypeEntityService():
    
    def get_all(self, page,per_page):
        type_entity = unitow_imp.type_entity.list(page,per_page)
        data = list_type_entity_schema.dump(type_entity[0])
        return {"code":200, "data":data}