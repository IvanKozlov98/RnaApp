from fastapi import APIRouter

from app.contracts import Item

router = APIRouter()


@router.get("/")
def read_root():
    """
    Simple printing <Hello world>
    :return:
    """
    return {"Hello": "World"}


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    """Simple query"""
    return {"item_id": item_id}


@router.post("/items/")
async def create_item(item: Item):
    """
    Creating new item with new_name
    :param item: item from contracts
    :return: updating item with new_name
    """
    item_dict = item.dict()
    item_dict.update({"new_name": item.name + item.name})
    return item_dict
