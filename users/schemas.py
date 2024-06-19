from typing import Annotated

from pydantic import BaseModel, EmailStr
from pydantic import StringConstraints


class SUserCreate(BaseModel):
    name: Annotated[
        str,
        StringConstraints(
            min_length=1, strip_whitespace=True, pattern=r"^[А-Яа-яЁё\s-]+$"
        ),
    ]
    surname: Annotated[
        str,
        StringConstraints(
            min_length=1, strip_whitespace=True, pattern=r"^[А-Яа-яЁё\s-]+$"
        ),
    ]
    patronymic: Annotated[
        str, StringConstraints(strip_whitespace=True, pattern=r"^[А-Яа-яЁё\s-]*$")
    ] = None
    login: Annotated[
        str,
        StringConstraints(
            min_length=1, strip_whitespace=True, pattern=r"^[a-zA-Z0-9-]+$"
        ),
    ]
    email: EmailStr
    phone: Annotated[
        str, StringConstraints(strip_whitespace=True, pattern=r"^\+?[1-9]\d{1,14}$")
    ]
    password: Annotated[str, StringConstraints(min_length=6, strip_whitespace=True)]
    password_repeat: Annotated[
        str, StringConstraints(min_length=6, strip_whitespace=True)
    ]


class SUserAuth(BaseModel):
    login: str
    password: str
