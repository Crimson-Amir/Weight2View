from fastapi import FastAPI, Request
import schema, mongoDB_crud

app = FastAPI()

@app.get('/')
async def home():
    return {'status': 'OK'}

@app.post('/add_new_item_to_db')
async def add_new_item_to_database(new_item: schema.AddNewItemSchema):
    try:
        document_id = mongoDB_crud.add_new_item_to_db(**new_item.model_dump())
        return {'status': 'OK', 'document_id': document_id}
    except Exception as e:
        return {'status': 'Error', 'error_type': type(e), 'error_reason': str(e)}

@app.post('/find_first_item')
async def find_first_item(item_condition: schema.ItemCondition):
    try:
        cleand_data = {k: v for k, v in item_condition.model_dump().items() if v is not None}
        item = mongoDB_crud.find_one_item(cleand_data)
        if item:
            item['_id'] = str(item['_id'])
            return {'status': 'OK', 'item': dict(item)}
        return {'status': 'NOK', 'detail': 'there is no item with this specification'}
    except Exception as e:
        return {'status': 'Error', 'error_type': type(e), 'error_reason': str(e)}


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