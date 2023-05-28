from app.value_fields.repository.value_fields_repositoty import IValueFieldsRepository
from app.repository.imp.repository import Repository
from app.db import db
from app.value_fields.entity.value_fields_entity import ValueFieldsEntity


class ValueFieldsRepositoryImplementation(IValueFieldsRepository, Repository):
    
    def __init__(self):
        self.session = db.session
        self.model_cls = ValueFieldsEntity
        self.model_cls.start_mapper()