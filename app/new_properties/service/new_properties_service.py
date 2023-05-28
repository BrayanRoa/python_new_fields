from app.container import unitow_imp
from app.new_properties.schema.new_properties_schema import list_new_properties_schema, new_properties_schema
from app.new_properties.model.new_properties_model import NewPropertiesModel
from marshmallow import ValidationError
from app.new_properties.entity.new_properties_entity import NewPropertiesEntity
from sqlalchemy import and_
class NewPropertiesService():
    
    def get_all(self, page,per_page, id):
        new_properties = unitow_imp.new_properties.list(page, per_page,param=and_(NewPropertiesEntity.type_entity_id==id, NewPropertiesEntity.is_calculated==True))
        data = list_new_properties_schema.dump(new_properties[0])
        return data
    
    def create(self, data):
        new_propertie = None
        try:
            new_propertie = new_properties_schema.load(data)
            unitow_imp.new_properties.add(NewPropertiesModel(
                name=new_propertie["name"],
                condition=new_propertie["condition"],
                description=new_propertie["description"],
                form=new_propertie["form"],
                is_calculated=new_propertie["is_calculated"],
                is_required=new_propertie["is_required"],
                type=new_propertie["type"],
                type_entity_id=new_propertie["type_entity_id"]
            ))
            return {"code":201, "data":"created"}
        except ValidationError as e:
            return {"error":e.args}