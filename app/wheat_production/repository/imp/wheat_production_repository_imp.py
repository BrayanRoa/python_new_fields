from app.wheat_production.repository.wheat_production_repository import IWheatProductionRepository
from app.repository.imp.repository import Repository
from app.db import db
from app.wheat_production.entity.wheat_production_entity import WheatProductionEntity

class WhaetProductionImplementation(IWheatProductionRepository, Repository):
    def __init__(self):
        self.session = db.session
        self.model_cls = WheatProductionEntity
        self.model_cls.start_mappers()
