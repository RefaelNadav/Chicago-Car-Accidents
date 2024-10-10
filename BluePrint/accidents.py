from flask import Blueprint, jsonify, request

from database.connect import accidents
from repository.csv_repository import init_chicago_car_accidents
from repository.accidents_repository import *

accidents_blueprint = Blueprint("accidents", __name__)


@accidents_blueprint.route("/initialize", methods=["POST"])

def initialize_db():
    try:
        init_chicago_car_accidents()
        return jsonify({ "message": "data created successfully"}), 201
    except Exception as e:
        return jsonify({'error': repr(e)}), 500


@accidents_blueprint.route("/accidents/<region>", methods=["GET"])
def get_total_accidents(region):
    total_accidents = get_total_accidents_by_region(region)
    return jsonify({"total_accidents": total_accidents}), 200


@accidents_blueprint.route("/accidents/group_by_cause/<region>", methods=["GET"])
def get_toatl_accidents_by_cause(region):
    result = group_accidents_by_prim_cause(region)
    return jsonify({"accidents": result}), 200