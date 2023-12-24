# main.py
from fastapi import FastAPI
from router.router_mysql import router as mysql_router
from router.router_normal import router as sqlite_router
app = FastAPI()
app.include_router(mysql_router, prefix="/mysql_api", tags=["mysql_api"])
app.include_router(sqlite_router, prefix="/normal", tags=["default"])