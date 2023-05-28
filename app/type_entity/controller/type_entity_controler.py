from flask import Blueprint, request
from app.type_entity.service.type_entity_service import TypeEntityService

type_entity_bp=Blueprint("type_entity", __name__)
type_entity_service=TypeEntityService()


@type_entity_bp.route("/")
def get_all():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 15, type=int)
    return type_entity_service.get_all(page, per_page)