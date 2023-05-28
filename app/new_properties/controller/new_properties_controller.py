from flask import Blueprint, request
from app.new_properties.service.new_properties_service import NewPropertiesService

new_properties_bp = Blueprint("new_properties", __name__)
new_properties_service = NewPropertiesService()


@new_properties_bp.route("/<int:id>")
def get_all_entity(id):
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 15, type=int)
    return new_properties_service.get_all(page, per_page, id)

@new_properties_bp.route("/",methods=["POST"])
def create():
    data = request.get_json()
    return new_properties_service.create(data)