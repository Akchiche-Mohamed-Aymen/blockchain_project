from pydantic import BaseModel, Field, field_validator
from typing import Literal
import re


class UserRegister(BaseModel):
    username: str = Field(
        ...,
        min_length=4,
        max_length=50
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=128
    )
    email: str
    role: Literal["admin", "client", "freelancer"] = Field(default="client")

    @field_validator("username")
    @classmethod
    def validate_username(cls, value):
        if not re.fullmatch(r"[a-zA-Z0-9_]+", value):
            raise ValueError(
                "Username can only contain letters, numbers and underscores"
            )
        return value

    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain an uppercase letter")

        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain a lowercase letter")

        if not re.search(r"\d", value):
            raise ValueError("Password must contain a number")

        return value




class UserLogin(BaseModel):
    username: str = Field(
        ...,
        min_length=4,
        max_length=50
    )

    password: str = Field(
        ...,
        min_length=8,
        max_length=128
    )
    @field_validator("username")
    @classmethod
    def validate_username(cls, value):
        if not re.fullmatch(r"[a-zA-Z0-9_]+", value):
            raise ValueError(
                    "Username can only contain letters, numbers and underscores"
            )
        return value
