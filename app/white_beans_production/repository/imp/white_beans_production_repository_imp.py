from app.white_beans_production.repository.white_beans_production_repository import IWhiteBeansProductionRepository
from app.repository.imp.repository import Repository
from app.db import db
from ...entity.white_beans_production_entity import WhiteBeansEntity

class WhiteBeansProductionRepositoryImp(IWhiteBeansProductionRepository, Repository):
    
    def __init__(self):
        self.session = db.session
        self.model_cls = WhiteBeansEntity
        self.model_cls.start_mapper()