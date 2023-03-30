from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from api.handler import get_email_id_handler, get_code_from_id_handler
from api.utils.pydantic_models import EmailNameData, EmailIDData

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/get_email_id/")
async def get_email_id(data: EmailNameData):
    return jsonable_encoder(await get_email_id_handler(data.email))


@app.get("/get_code_from_id/")
async def get_code_from_message(data: EmailIDData):
    return jsonable_encoder(await get_code_from_id_handler(data.email_id))
