from fastapi import FastAPI, Request
import schema, mongoDB_crud

app = FastAPI()

@app.get('/')
async def home():
    return {'status': 'OK'}

@app.post('/add_new_item_to_db')
async def add_new_item_to_database(new_item: schema.AddNewItemSchema):
    mongoDB_crud.add_new_item_to_db(new_item.dict())

@app.get('/find_first_item')
async def find_first_item():
    pass

@app.get('f/ind_items')
async def find_items():
    pass
