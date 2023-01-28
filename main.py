from typing import Optional
import pandas as pd
from fastapi import FastAPI
import psycopg2
from pydantic import BaseModel
import pandas.io.sql as psql

class Item(BaseModel):
    pincode: str

app = FastAPI()
conn = psycopg2.connect(host="localhost",dbname="postgres", user="postgres" ,password="Satya@268")
cur = conn.cursor()
@app.post("/", status_code=200)
async def create_item(item: Item):
    pincode = item.pincode
    sql = f"""select * from private.t_state_code tsc where pincode = '{pincode}';"""
    datas =  psql.read_sql(sql, conn)
    datas = datas.drop(columns=['id'])
    return datas.to_dict(orient="records")