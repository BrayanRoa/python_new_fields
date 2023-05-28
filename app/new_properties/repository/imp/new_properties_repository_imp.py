from app.new_properties.repository.new_properties_repository import INewPropertiesRepository
from app.repository.imp.repository import Repository
from app.db import db
from app.new_properties.entity.new_properties_entity import NewPropertiesEntity

class NewPropertiesRepositoryImplementation(INewPropertiesRepository, Repository):
    
    def __init__(self):
        self.session = db.session
        self.model_cls = NewPropertiesEntity
        self.model_cls.start_mapper()