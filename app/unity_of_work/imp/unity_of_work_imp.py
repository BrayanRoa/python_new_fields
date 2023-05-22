
from app.unity_of_work.IUnity_of_work import IUnityOfWork
from app.wheat_production.repository.imp.wheat_production_repository_imp import WhaetProductionImplementation
from app.white_beans_production.repository.imp.white_beans_production_repository_imp import WhiteBeansProductionRepositoryImp
class UnitOfWork(IUnityOfWork):
    def __init__(self):
        self.wheat_production = WhaetProductionImplementation()
        self.white_beans_production = WhiteBeansProductionRepositoryImp()