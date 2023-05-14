from dependency_injector import containers
from dependency_injector import containers, providers
from app.unity_of_work.imp.unity_of_work_imp import UnitOfWork

class Container(containers.DeclarativeContainer):
    unitow = providers.Singleton(UnitOfWork)

container = Container()
unitow_imp = container.unitow()
