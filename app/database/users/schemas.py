import re

import pydantic
from pydantic import BaseModel, validator


class User(BaseModel):
    id: int
    redirect_url: pydantic.HttpUrl = "https://google.com"
    address: str = ""


class TgUser(User):
    @validator("address", always=True)
    def get_address(cls, address: str, values: dict[str, object]) -> str:
        if address == "":
            return str(values["id"])

        assert re.fullmatch(r"^[^_]\w+[^_]$", address)
        return address

    class Config:
        validate_assignment = True
