# coding: utf-8
"""JWT in httpOnly cookies with OAuth2 password flow.
"""

from calendar import timegm
from datetime import datetime, timedelta
from typing import List

import jwt

from fastapi import Depends, FastAPI, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette.requests import Request
from starlette.responses import JSONResponse

from pydantic import BaseModel


class OAuth2PasswordCookie(OAuth2PasswordBearer):
    """OAuth2 password flow with token in a httpOnly cookie.
    """

    def __init__(self, *args, token_name: str = None, **kwargs):
        super().__init__(*args, **kwargs)
        self._token_name = token_name or "my-jwt-token"

    @property
    def token_name(self) -> str:
        """Get the name of the token's cookie.
        """
        return self._token_name

    async def __call__(self, request: Request) -> str:
        """Extract and return a JWT from the request cookies.

        Raises:
            HTTPException: 403 error if no token cookie is present.
        """
        token = request.cookies.get(self._token_name)
        if not token:
            raise HTTPException(status_code=403, detail="Not authenticated")
        return token


oauth2_scheme = OAuth2PasswordCookie(  # pylint: disable=invalid-name
    tokenUrl="/auth/token", scopes={"user": "User", "admin": "Administrator"}
)

app = FastAPI()  # pylint: disable=invalid-name


def validate_jwt_payload(token: str) -> dict:
    """Decode and validate a JSON web token.

    Args:
        token (str): JWT token.

    Returns:
        dict

    Raises:
        HTTPException: 401 error if the credentials have expired or failed
            validation.
    """
    try:
        payload = jwt.decode(token, "i am a secret", algorithms=["HS256"])
        utc_now = timegm(datetime.utcnow().utctimetuple())
        if payload["exp"] <= utc_now:
            raise HTTPException(401, detail="Credentials have expired")
        return payload
    except jwt.PyJWTError:
        raise HTTPException(401, detail="Could not validate credentials")


class UserData(BaseModel):
    """User name, ID and scopes.
    """

    user: str
    user_id: int
    scopes: List[str]


def is_authenticated(token: str = Security(oauth2_scheme)) -> UserData:
    """Dependency on user being authenticated.
    """
    payload = validate_jwt_payload(token)
    return UserData(
        user=payload["user"], user_id=payload["user_id"], scopes=payload["scopes"]
    )


# dummy users 'database'
_USER_DB = {
    "jeff": {"password": "secret", "scopes": ["user"], "user_id": 0},
    "pete": {"password": "secret", "scopes": ["user", "admin"], "user_id": 0},
}


@app.post("/auth/token")
async def authenticate(form_data: OAuth2PasswordRequestForm = Depends()):
    """Verify login details and issue JWT in httpOnly cookie.

    Raises:
        HTTPException: 401 error if username or password are not recognised.
    """
    user = _USER_DB.get(form_data.username)
    if user["password"] != form_data.password:
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    data = {
        "user": form_data.username,
        "user_id": user["user_id"],
        "scopes": user["scopes"],
    }
    issued_at = datetime.utcnow()
    expire = issued_at + timedelta(minutes=15)
    data.update({"exp": expire, "iat": issued_at, "sub": "jwt-cookies-test"})
    encoded_jwt = jwt.encode(data, "i am a secret", algorithm="HS256").decode("utf-8")
    response = JSONResponse({"status": "authenticated"})
    # NOTE: we should also set secure=True to mark this as a `secure` cookie
    # https://tools.ietf.org/html/rfc6265#section-4.1.2.5
    response.set_cookie(oauth2_scheme.token_name, encoded_jwt, httponly=True)
    return response


@app.get("/")
async def home(_request: Request, user: UserData = Depends(is_authenticated)):
    """Return sample JSON iff the user is authenticated.
    """
    return {"status": "ok", "user": user}