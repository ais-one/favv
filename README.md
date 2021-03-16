# About FAVV (FastAPI+ViteVue)

FastAPI Python backend (BE) and Vite + VueJS + Ant Design frontend (FE) template... for your API and Web application needs.

Considerations
- code reusability
- application segregation **inject your own frontend and backend project**
- ease of template upgrade 
- ci/cd and container friendly

## Development - Setup and Run

### Backend

> python: 3.8.5, pip: 20.1.1

```bash
cd fastapi

# create environment called dev
python -m venv dev # python3 -m venv /path/to/new/virtual/env

# rename .env.example to .env
mv ./app/.env.example ./app/.env

# activate it
./dev/Scripts/activate

# install python packages
pip install -r requirements.txt
# pip install fastapi uvicorn[standard] python-multipart SQLAlchemy passlib[bcrypt] python-jose[cryptography] boto3 ? asyncpg ? mongo
# pip freeze > requirements.txt # save libraries installed, done after each pip install

# running the app
cd app
python main.py # OPTION 1 - running using python
uvicorn main:app --reload --host=0.0.0.0 --port=8000 --access-log --log-level=debug --header server:none # OPTION 2 - running uvicorn
```

Navigate to - http://127.0.0.1:8000/api-docs

### Frontend

```bash
cd vitevue
npm i
npm run dev
```

Navigate to - http://127.0.0.1:8080

## Production Run (Docker)

```bash
cd vitevue
deploy.sh
cd ../fastapi
docker build -t <your-image-name>:<tag> .
docker run -it <your-image-name>:<tag>
```

---

# Customization

## Structure

```md
+ favv
  + fastapi/
  | + app/
  | | + .env **backend config**
  | | + *_app/ **folder with suffix "_app" are your custom backend code, models, uploads**
  | |   + models/ 
  | |   + uploads/
  | + Dockerfile
  + vitevue/
    + src
    | + .env.js **frontend config**
    | + .env.vite.js **frontend build config**
    | + *Web/ **folder witht suffix "Web" are your custom frontend code**
    + deploy.sh
```

- NOTE: All folders and files prefixed with TBD can be ignored, they are not implemented and used for reference

## Backend Customization Notes

Setting up your custom backend

```bash
# in favv/fastapi/app/
# note that project name must end with suffix "_app"
git clone <your backend project e.g. example_app>
```

- use **favv/fastapi/app/custom_app/** as reference on your custom backend
  - on working with your custom endpoints, using db, s3, file services
  - working with files in **favv/fastapi/app/custom_app/sample_uploads/** folder
  - running subprocess in **favv/fastapi/app/custom_app/sample_models/** folder
- set the APP, to the folder name of your custom app in **favv/fastapi/app/.env**
  - UPLOAD_FOLDER and MODEL_FOLDER is directly inside your custom app folder
- application path is **favv/fastapi/app/** as **main.py** is run from there (either using python or uvicorn)
- test endpoints in **favv/fastapi/app/api/routes/test.py** will not be available in production environment
- NOTE: update **favv/fastapi/app/config.py** when **.env** entries change
- NOTE: any code outside **favv/fastapi/app** will not auto reload

## Frontend Customization Notes
Setting up your custom backend

```bash
# in favv/vitevue/src/
# note that project name must end with suffix "Web"
git clone <your frontend project e.g. ExampleWeb>
```

- use **favv/vitevue/src/CustomWeb/** as reference on your custom frontend
- see **favv/vitevue/src/.env.js** on the configurations used, especially the ROUTES property
- ROUTES property
  - use kebab-case, will be converted to Capital Case in menu display
  - only up to 1 submenu level
    - /first-level
    - /submenu/second-level
  - paths
    - '~/xxx.js' from **favv/vitevue/src** folder
    - '/xxx.js' from **favv/vitevue** folder
