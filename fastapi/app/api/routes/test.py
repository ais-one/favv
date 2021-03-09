# either in one file or put in folder...
from fastapi import APIRouter, Depends
import subprocess
from services.db import get_db

router = APIRouter(tags=["api_test"], prefix="/test")

@router.get("/another-spawn")
async def spawn_test():
  subprocess.Popen(
      ["python", "test_model.py"],    # program and arguments
      # stdout=subprocess.PIPE,  # capture stdout
      # check=True               # raise exception if program fails
  )
  # print(result.stdout)         # result.stdout contains a byte-string
  return { "Where": "test-spawn" }

@router.get("/another-db")
async def db_test():
  result = get_db().execute("select * from books")
  names = [row[1] for row in result]
  print(names)
  return { "Where": "test-another-db", "test": names }
