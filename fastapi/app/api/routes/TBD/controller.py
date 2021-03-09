from fastapi import APIRouter # , Depends, HTTPException, status, Security
# from fastapi.security import OAuth2PasswordRequestForm
# from motor.motor_asyncio import AsyncIOMotorClient

# from ..utils.mongodb import get_database
# from ..utils.authentication import *
# from ..models.responses import UsersInResponse, UserInResponse, TokenResponse
# from ..models.user import UserInDB, UserInReq, TokenData

# from app.core import tbd
# import app.core.tbd.xxx
# import tbd

router = APIRouter()

@router.get("/")
async def get_all_users():
  return { 'at': 'api controller' }

# router.include_router(tbd.router, tags=["tbd"])

# @router.get("/", response_model=UsersInResponse)
# async def get_all_users(db: AsyncIOMotorClient = Depends(get_database), token_data: TokenData = Security(verify_token, scopes=['users'])) -> UsersInResponse:
#     """Get all data base Users"""
#     users = [UserInDB(**data) async for data in db['core']['users'].find()]
#     return UsersInResponse(data=users)

# @router.post('/login', response_model=TokenResponse)
# async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncIOMotorClient = Depends(get_database)) -> TokenResponse:
#     """Login"""
#     _user = await db['core']['users'].find_one({'username': form_data.username})

#     invalid_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail='Invalid credentials',
#         headers={
#             'WWW-Authenticate': 'Bearer'})
#     if not _user:
#         raise invalid_exception
#     user = UserInDB(**_user)
#     if not verify_password(form_data.password, user.hashed_password):
#         raise invalid_exception
#     payload = {
#         'sub': str(user.id),
#         'scopes': ['users']
#     }
#     token = get_access_token(payload)
#     return TokenResponse(access_token=token)


# @router.post('/register', response_model=TokenResponse)
# async def register(_user: UserInReq, db: AsyncIOMotorClient = Depends(get_database)) -> TokenResponse:
#     """Register User"""
#     existing_user = await db['core']['users'].find_one({'username': _user.username})
#     if existing_user:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username not available')
#     hashed_password = hash_password(_user.password)
#     user_data = _user.dict()
#     user_data.pop('password')
#     user_data['hashed_password'] = hashed_password
#     _res = await db['core']['users'].insert_one(user_data)
#     payload = {
#         'sub': str(_res.inserted_id),
#         'scopes': []
#     }
#     token = get_access_token(payload)
#     return TokenResponse(access_token=token)