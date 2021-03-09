from jose import jwt
from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer, APIKeyHeader

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
apiKeyHeader_scheme = APIKeyHeader(name="Authorization")

# oauth2_scheme, apiKeyHeader_scheme
async def auth_user(token: str = Depends(apiKeyHeader_scheme)):
  credentials_exception = HTTPException(
      status_code=401,
      detail="Could not validate credentials",
      headers={"WWW-Authenticate": "Bearer"},
  )
  try:
      decoded = jwt.decode(token, "secret", algorithms=["HS256"])
      username = decoded.get("sub")
      # if username is None:
      #     raise credentials_exception
      # token_data = TokenData(username=username)
  except jwt.JWTError:
      raise credentials_exception
  return { "username": username }
  
