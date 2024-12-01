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

def find_one_item(condition):
    return item_collection.find_one(condition)

def find_items(condition:dict, includes_parameter:dict):
    return item_collection.find(condition, includes_parameter)

def search_in_items(search, **kwargs):
    return item_collection.aggregate([
        {
            '$search': {
                search
            }
        },
        kwargs
    ])