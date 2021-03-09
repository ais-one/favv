## Dependency Injection

https://levelup.gitconnected.com/dependency-injection-in-fastapi-111e3e7aad28

```python
from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()

class CommonQueryParams:
    def __init__(self, id: str, name: str, age: int):
        self.id = id
        self.name = name
        self.age = age

async def verify_age(commons: CommonQueryParams = Depends(CommonQueryParams)):
    if commons.age < 18:
        raise HTTPException(status_code=400, detail="Requires adult supervision")

async def verify_admin(commons: CommonQueryParams = Depends(CommonQueryParams)):
    if commons.id != 'ID0001':
        raise HTTPException(status_code=400, detail="Requires admin access")

@app.get("/user/", dependencies=[Depends(verify_age)])
async def user():
    return {"message": "Successfully accessed user page"}

@app.get("/admin/", dependencies=[Depends(verify_admin), Depends(verify_age)])
async def admin():
    return {"message": "Successfully accessed admin page"}
```
