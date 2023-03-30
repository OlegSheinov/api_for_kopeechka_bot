from pydantic.main import BaseModel


class EmailNameData(BaseModel):
    email: str


class EmailIDData(BaseModel):
    email_id: int
