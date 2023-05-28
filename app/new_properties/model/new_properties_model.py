

class NewPropertiesModel():
    
    def __init__(self, id=None, name=None, type=None, is_calculated=None, form=None, is_required=None,condition=None,description=None, type_entity_id=None) -> None:
        self.id = id
        self.name = name
        self.type = type
        self.is_calculated = is_calculated
        self.form = form
        self.is_required = is_required    
        self.condition = condition
        self.description = description
        self.type_entity_id = type_entity_id
