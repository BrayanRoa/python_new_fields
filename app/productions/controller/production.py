from flask import Blueprint, request
from app.productions.service.production_service import ProductionService

production_bp = Blueprint("production", __name__)
production_service = ProductionService()

@production_bp.route("/<int:id>")
def get_all(id):
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 15, type=int)
    return production_service.get_all(page, per_page, id)

# @wheat_production.route("/new_propertie/<table>", methods=['POST'])
# def new_properties(table):
#     data = request.get_json()
#     return wheat_service.new_properties(data, table)