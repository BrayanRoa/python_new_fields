from flask import request, Blueprint
from ..service.white_beans_production_service import WhiteBeansProductionService

white_beans_production = Blueprint("white_beans_production",__name__)
white_beans_production_service = WhiteBeansProductionService()

@white_beans_production.route("/")
def get_all():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 15, type=int)
    return white_beans_production_service.get_all(page, per_page)