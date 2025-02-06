import logging

from fastapi import FastAPI, Request
import schema, mongoDB_crud
from functions import calculate_size_by_item
from plot import create_svg_source
from bson.objectid import ObjectId 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change "*" to a specific origin for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def home():
    return {'status': 'OK'}


@app.post('/add_new_item_to_db')
async def add_new_item_to_database(new_item: schema.AddNewItemSchema):
    try:
        document_id = mongoDB_crud.add_new_item_to_db(**new_item.model_dump())
        return {'status': 'OK', 'document_id': str(document_id)}
    except Exception as e:
        return {'status': 'Error', 'error_type': type(e), 'error_reason': str(e)}


@app.post('/find_first_item')
async def find_first_item(item_condition: schema.ItemCondition):
    try:
        item_id = ObjectId(item_condition.item_id)
        item = mongoDB_crud.find_one_item(item_id)

        if item:
            width, height, length = calculate_size_by_item(item, item_condition.weight_in_gram)
            svg_plot = create_svg_source(width, height, length)
            print(svg_plot)
            return {
                'status': 'OK',
                'width': width,
                'height': height,
                'length': length,
                'svg_plot': svg_plot
            }

        return {'status': 'NOK', 'detail': 'there is no item with this specification'}
    except KeyError as e:
        return {
            'status': 'Error',
            'error_type': type(e),
            'error_reason': f"item doesn't have required field. {str(e)}"
        }
    except Exception as e:
        return {'status': 'Error', 'error_type': str(type(e)), 'error_reason': str(e)}


@app.post('/find_items')
async def find_items(item_condition: schema.ItemCondition):
    try:
        cleand_data = {k: v for k, v in item_condition.model_dump().items() if v is not None}
        items = mongoDB_crud.find_items(cleand_data, {})
        if items:
            items_list = []
            for item in items:
                item['_id'] = str(item['_id'])
                items_list.append(item)
            return {'status': 'OK', 'items': items_list}
        return {'status': 'NOK', 'detail': 'there is no item with this specification'}
    except Exception as e:
        return {'status': 'Error', 'error_type': type(e), 'error_reason': str(e)}