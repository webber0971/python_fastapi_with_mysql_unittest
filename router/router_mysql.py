from fastapi import APIRouter 
from orm_mysql_model.item import Item
from orm_mysql_model.__init_orm_controller import mysql_client
from input_interface.mainMysql_input_interfac import IWrite

router = APIRouter()
@router.get("/read_data")
def read_data():
    items = mysql_client.read_data()
    mysql_client.close()
    return {"data": items}


@router.post("/write_data_route")
def write_data_route(item: IWrite):
    res = mysql_client.write_data(item=Item(name=item.name, description=item.description))
    mysql_client.close()
    return {"result": res}

@router.get("/read_data_route")
def read_data_route(tableName: str):
    print("------------------")
    print(tableName)
    result={
        "isSuccess":False,
        "data":None
    }
    if tableName == "items":
        items = mysql_client.read(Item,{})
        result={
            "isSuccess":True,
            "data":items
        }
    mysql_client.close()
    return result
