from flask import Blueprint, jsonify
from repository.csv_repository import init_chicago_car_accidents
from repository.accidents_repository import *
from datetime import datetime, timedelta

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


@accidents_blueprint.route("/accidents/total_by_time/<region>/<date>/<period>", methods=["GET"])
def get_total_accidents_by_time(region, date, period):
    time_periods = {
        "day": 1,
        "week": 7,
        "month": 30
    }

    add_date = time_periods.get(period)
    if add_date is None:
        return jsonify({"error": "Invalid time period. Use 'day', 'week', or 'month'."}), 400

    start_date = datetime.strptime(date, '%m-%d-%Y')
    end_date = start_date + timedelta(days=add_date)

    result = get_total_accidents_by_time_from_db(region, start_date, end_date)
    return jsonify({"total_accidents": result}), 200


@accidents_blueprint.route("/accidents/group_by_cause/<region>", methods=["GET"])
def get_toatl_accidents_by_cause(region):
    result = group_accidents_by_prim_cause(region)
    return jsonify({"accidents": result}), 200


@accidents_blueprint.route("/accidents/stats_injuries/<region>", methods=["GET"])
def get_stats_injuries_by_region(region):
    result = injuries_stats_by_region(region)
    return jsonify({"injuries": result}), 200