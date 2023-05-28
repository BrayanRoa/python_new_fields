

class NewPropertiesModel():
    
    def __init__(self, name=None, type=None, is_calculated=None, form=None, is_required=None,condition=None,description=None, type_entity_id=None) -> None:
        self.name = name
        self.type = type
        self.is_calculated = is_calculated
        self.form = form
        self.is_required = is_required    
        self.condition = condition
        self.description = description
        self.type_entity_id = type_entity_id
        
    def __str__(self):
        return {
            "name": self.name,
            "type": self.type,
            "is_calculated": self.is_calculated,
            "form": self.form,
            "is_required": self.is_required,
            "condition": self.condition,
            "description": self.description,
            "type_entity_id": self.type_entity_id
        }
