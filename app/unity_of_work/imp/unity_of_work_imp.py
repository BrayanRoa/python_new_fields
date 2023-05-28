
from app.unity_of_work.IUnity_of_work import IUnityOfWork
from app.productions.repository.imp.production_repository_imp import ProductionImplementation
from app.white_beans_production.repository.imp.white_beans_production_repository_imp import WhiteBeansProductionRepositoryImp
from app.type_entity.repository.imp.type_entity_repository_imp import TypeEntityImplementation
from app.new_properties.repository.imp.new_properties_repository_imp import NewPropertiesRepositoryImplementation
from app.value_fields.repository.imp.value_fields_repository_imp import ValueFieldsRepositoryImplementation 
class UnitOfWork(IUnityOfWork):
    def __init__(self):
        self.production = ProductionImplementation()
        self.type_entity = TypeEntityImplementation()
        self.new_properties = NewPropertiesRepositoryImplementation()
        self.value_fields = ValueFieldsRepositoryImplementation()
        self.white_beans_production = WhiteBeansProductionRepositoryImp()