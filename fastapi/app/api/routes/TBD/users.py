from fastapi import APIRouter

from typing import Optional, Dict, List, Union
from pydantic import BaseModel # , EmailStr

router = APIRouter(
  prefix="/users",
  tags=["api-common-users"],
  # dependencies=[Depends(get_token_header)],
  responses={404: {"description": "Not found"}},
)

class UserIn2(BaseModel):
  username: str
  password: str
  email: str # EmailStr
  full_name: Optional[str] = None
  level: int = 1


class UserOut2(BaseModel):
  username: str
  email: str # EmailStr
  full_name: Optional[str] = None
  level: int = 1


@router.post("/user/", response_model=UserOut2, response_model_exclude_unset=True)
# also...
# response_model_exclude_defaults=True
# response_model_exclude_none=True
# response_model_exclude=["username"]
# response_model_include=["username", "email"]
async def create_user(user: UserIn2):
  return user

@router.get("/users/")
async def read_users():
  return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/users/me")
async def read_user_me():
  return {"username": "fakecurrentuser"}


@router.get("/users/{username}")
async def read_user(username: str):
  return {"username": username}


### Extra Models

# reduce duplication
class UserBase(BaseModel):
  username: str
  email: str
  full_name: Optional[str] = None

class UserIn(UserBase):
  password: str

class UserOut(UserBase):
  pass

class UserInDB(UserBase):
  hashed_password: str

def fake_password_hasher(raw_password: str):
  return "supersecret" + raw_password

def fake_save_user(user_in: UserIn):
  hashed_password = fake_password_hasher(user_in.password)
  user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password) # ** is like destructuring in JS
  print("User saved! ..not really")
  return user_in_db

@router.post("/user-reduce-dup/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

# Union
class BaseItem(BaseModel):
  description: str
  type: str

class CarItem(BaseItem):
  type = "car"

class PlaneItem(BaseItem):
  type = "plane"
  size: int

bitems = {
    "item1": {"description": "All my friends drive a low rider", "type": "car"},
    "item2": {
        "description": "Music is my aeroplane, it's my aeroplane",
        "type": "plane",
        "size": 5,
    },
}

@router.get("/bitems/{item_id}", response_model=Union[PlaneItem, CarItem])
async def read_bitem(item_id: str):
  return bitems[item_id]

# list of models
class Item3(BaseModel):
  name: str
  description: str

items3 = [
  {"name": "Foo", "description": "There comes my hero"},
  {"name": "Red", "description": "It's my aeroplane"},
]

@router.get("/items3/", response_model=List[Item3])
async def read_items3():
  return items3

# arbitrary Dict
@router.get("/keyword-weights/", response_model=Dict[str, float])
async def read_keyword_weights():
  return {"foo": 2.3, "bar": 3.4}
