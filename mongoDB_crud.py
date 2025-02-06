from pymongo import MongoClient
from setting import mongodb_atlas_url

client = MongoClient(mongodb_atlas_url)
weight2view_db = client.weight2view
item_collection = weight2view_db.items

def add_new_item_to_db(**kwargs):
    """
    item_name: str,
    weight_in_gram: float,
    height_mm: float,
    width_mm: float,
    length_mm: float
    """
    post_id = item_collection.insert_one(kwargs).inserted_id
    return post_id

def find_one_item(item_id):
    return item_collection.find_one(item_id)

def find_items(name_filter, limit_value):
    pipeline = [
        {"$match": {"item_name": {"$regex": name_filter, "$options": "i"}}},
        {"$project": {"item_name": 1, "_id": 1}},
        {"$limit": limit_value}
    ]
    return item_collection.aggregate(pipeline)