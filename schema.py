from pydantic import BaseModel


class AddNewItemSchema(BaseModel):
    item_name: str
    weight_in_gram: float
    height_mm: float
    width_mm: float
    length_mm: float

class ItemCondition(BaseModel):
    item_id: str
    weight_in_gram: float
