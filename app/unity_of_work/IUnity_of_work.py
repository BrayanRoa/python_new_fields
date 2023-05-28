from app.productions.repository.production_repository import IProductionRepository
from app.white_beans_production.repository.white_beans_production_repository import IWhiteBeansProductionRepository
from app.type_entity.repository.type_entity_repositoty import ITypeEntityRepository
from app.new_properties.repository.new_properties_repository import INewPropertiesRepository
from app.value_fields.repository.value_fields_repositoty import IValueFieldsRepository

class IUnityOfWork():
    production = IProductionRepository
    type_entity = ITypeEntityRepository
    new_properties = INewPropertiesRepository
    value_fields = IValueFieldsRepository
    white_beans_production = IWhiteBeansProductionRepository