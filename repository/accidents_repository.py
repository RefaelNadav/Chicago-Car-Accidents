from datetime import datetime, timedelta
from database.connect import accidents, chicago_car_accidents_db

def get_total_accidents_by_region(region):
    total_accidents = chicago_car_accidents_db.accidents.count_documents({'beat_of_occurrence': region})
    return total_accidents


def parse_date(date_str: str):
    has_seconds = len(date_str.split(' ')) > 2
    date_format = '%m/%d/%Y %H:%M:%S %p' if has_seconds else '%m/%d/%Y %H:%M'
    return datetime.strptime(date_str, date_format)

def get_total_accidents_by_period(start_date, period):
    pass