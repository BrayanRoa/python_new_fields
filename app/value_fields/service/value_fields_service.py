from app.container import unitow_imp
from app.value_fields.schema.value_fields_schema import list_value_fields_schema

class ValueFieldsService():
    
    def get_all(self, page, per_page):
        value_fields = unitow_imp.value_fields.list(page,per_page)
        data = list_value_fields_schema.dump(value_fields[0])
        return {"code":200, "data":data}