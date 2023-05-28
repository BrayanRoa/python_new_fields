
from flask import Blueprint, request
from app.value_fields.service.value_fields_service import ValueFieldsService

value_fields_bp = Blueprint("value_fields", __name__)
value_fields_service = ValueFieldsService()


@value_fields_bp.route("/")
def get_all():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 15, type=int)
    return value_fields_service.get_all(page, per_page)