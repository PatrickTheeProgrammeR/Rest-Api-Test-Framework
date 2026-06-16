from pydantic import BaseModel

class UserData(BaseModel):
    id : int
    email : str
    first_name : str
    last_name : str


class UserResponse(BaseModel):
    data : UserData
