from app.productions.repository.production_repository import IProductionRepository
from app.repository.imp.repository import Repository
from app.db import db
from app.productions.entity.production_entity import ProductionEntity

class ProductionImplementation(IProductionRepository, Repository):
    def __init__(self):
        self.session = db.session
        self.model_cls = ProductionEntity
        self.model_cls.start_mappers()
