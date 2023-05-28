from app.type_entity.repository.type_entity_repositoty import ITypeEntityRepository
from app.repository.imp.repository import Repository
from app.db import db
from app.type_entity.entity.type_entity_entity import TypeEntity

class TypeEntityImplementation(ITypeEntityRepository, Repository):
    
    def __init__(self) -> None:
        self.session = db.session
        self.model_cls = TypeEntity
        self.model_cls.start_mapper()