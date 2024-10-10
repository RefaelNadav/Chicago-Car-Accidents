
from database.connect import chicago_car_accidents_db, accidents
import csv
import os


def read_csv(csv_path):
   with open(csv_path, 'r') as file:
       csv_reader = csv.DictReader(file)
       for row in csv_reader:
           yield row

def validate_and_convert_int(value):
    if value == '':
        return 0
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def init_chicago_car_accidents():
   accidents.drop()


   for row in read_csv('data/Traffic_Crashes_-_Crashes - 20k rows.csv'):
       injuries = {
           'injuries_total': validate_and_convert_int(row['INJURIES_TOTAL']),
           'injuries_fatal': validate_and_convert_int(row['INJURIES_FATAL']),
           'injuries_non_fatal': validate_and_convert_int(row['INJURIES_TOTAL']) - \
                                 validate_and_convert_int(row['INJURIES_FATAL'])

       }


       accident = {
           'beat_of_occurrence': row['BEAT_OF_OCCURRENCE'],
           'crash_date': row['CRASH_DATE'].split(' ')[0],
           'prim_contributory_cause': row['PRIM_CONTRIBUTORY_CAUSE'],
           'injuries': injuries
       }

       accidents.insert_one(accident)
