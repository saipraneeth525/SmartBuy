from pydantic import BaseModel, HttpUrl


class ImportProductRequest(BaseModel):
    url: HttpUrl