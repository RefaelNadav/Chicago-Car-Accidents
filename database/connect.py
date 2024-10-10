from pymongo import MongoClient


client = MongoClient('localhost', 27017)
chicago_car_accidents_db = client['chicago_car_accidents']


accidents = chicago_car_accidents_db['accidents']
