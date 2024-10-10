
from database.connect import accidents, chicago_car_accidents_db

def get_total_accidents_by_region(region):
    total_accidents = chicago_car_accidents_db.accidents.count_documents({'beat_of_occurrence': region})
    return total_accidents


def get_total_accidents_by_time_from_db(region, start_date1, end_date1):

    total_accidents = chicago_car_accidents_db.accidents.count_documents({
        "beat_of_occurrence": region,
        "crash_date": {"$gte": start_date1, "$lt": end_date1}
    })
    return total_accidents


def group_accidents_by_prim_cause(region):
    result = list(chicago_car_accidents_db.accidents.aggregate([
        { '$match': {'beat_of_occurrence': region}},
        { '$group': {'_id': "$injuries",
                     'total_accidents': { '$sum': 1 } } }

    ]))
    return result


def injuries_stats_by_region(region):
    result = list(chicago_car_accidents_db.accidents.aggregate([
        {'$match': {'beat_of_occurrence': region}},
        {'$group': {'_id': "$beat_of_occurrence",
                    'total_injuries': {'$sum': '$injuries.injuries_total'},
                    'total_injuries_fatal': {'$sum': '$injuries.injuries_fatal'},
                    'total_injuries_non_fatal': {'$sum': '$injuries.injuries_non_fatal'}
                    }}
    ]))
    return result