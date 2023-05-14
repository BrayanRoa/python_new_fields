from flask import Blueprint, request
from app.property_tables.service.property_tables_service import PropertyTablesService

property_tables = Blueprint("property_tables", __name__)
property_tables_service = PropertyTablesService()

@property_tables.route("/new_properties/<table>", methods=['POST'])
def add_new_properties(table):
    data = request.get_json()
    return property_tables_service.new_properties(data, table)