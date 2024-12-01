from pydantic import BaseModel

class AddNewItemSchema(BaseModel):
    item_name: str
    weight_in_gram: float
    height_mm: float
    width_mm: float
    length_mm: float

class ItemCondition(BaseModel):
    item_id: str | None = None
    item_name: str | None = None
    weight_in_gram: float | None = None
    height_mm: float | None = None
    width_mm: float | None = None
    length_mm: float | None = None