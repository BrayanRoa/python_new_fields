from flask import Blueprint, request
from app.wheat_production.service.wheat_production_service import WheatProductionService

wheat_production = Blueprint("wheat_production", __name__)
wheat_service = WheatProductionService()

@wheat_production.route("/")
def get_all():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 15, type=int)
    return wheat_service.get_all(page, per_page)

@wheat_production.route("/new_propertie", methods=['POST'])
def new_properties():
    data = request.get_json()
    return wheat_service.new_properties(data)