from flask import Blueprint, jsonify, request

from database.connect import accidents
from repository.csv_repository import init_chicago_car_accidents

accidents_blueprint = Blueprint("accidents", __name__)


@accidents_blueprint.route("/initialize", methods=["POST"])

def initialize_db():
    try:
        init_chicago_car_accidents()
        return jsonify({ "message": "data created successfully"}), 201
    except Exception as e:
        return jsonify({'error': repr(e)}), 500