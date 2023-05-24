from pydantic import BaseModel, EmailStr


class Profile(BaseModel):
    email: EmailStr
    phone_number: str
