from app.container import unitow_imp
from app.new_properties.schema.new_properties_schema import list_new_properties_schema

class NewPropertiesService():
    
    def get_all(self, page,per_page):
        new_properties = unitow_imp.new_properties.list(page, per_page)
        data = list_new_properties_schema.dump(new_properties[0])
        return {"code":200, "data":data}