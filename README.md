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

# copy .env.example to .env, adjust your own custom env settings here
cp ./app/.env.example ./app/.env

# activate it - use \ for windows
dev/Scripts/activate

# pip install fastapi uvicorn[standard] python-multipart SQLAlchemy passlib[bcrypt] python-jose[cryptography] boto3 pymongo redis 
# pip freeze > requirements.txt # save libraries installed, done after each pip install

# install common packages
pip install -r requirements.txt

# install custom app packages
pip install -r app/custom_app/requirements.txt
```

# Run App & Task Quque (requires redis)

```bash
cd app

# fastapi application
python main.py # OPTION 1 - running using python
uvicorn main:app --reload --host=0.0.0.0 --port=8000 --access-log --log-level=debug --header server:none # OPTION 2 - running uvicorn

# huey task queue consumer 
huey_consumer custom_app.models.tasks.huey

```

Navigate to - http://127.0.0.1:8000/api-docs

### Frontend

- VueJS 3
- Vite 2 [https://github.com/vuejs/vite](https://github.com/vuejs/vite)
- Ant Design 2

```bash
# move to the vitevue folder
cd ../../vitevue

# copy the configs
cp src/.env.js.example src/.env.js
cp src/.env.vite.js.example src/.env.vite.js

# install
npm i

# run UI on UI dev server
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
  | | + .env: backend config
  | | + <your-custom-backend>_app/: folder with suffix "_app" are your custom backend code, models, uploads (your backend repo)
  | |   + .gitignore: for your repo
  | |   + base.py: this file name is required, and an FastApi ApiRouter of the name router_<your-custom-backend>_app is needed
  | |   + requirments.txt: your dependencies
  | |   + models/ 
  | |     * tasks.py: custom task queue file
  | |   + uploads/
  | + Dockerfile
  + vitevue/
    + src
    | + .env.js: frontend config (set INITIAL_SECURE_PATH, API_URL - to API server, ROUTES here)
    | + .env.vite.js: frontend build config (set DEV_SERVER_PORT, WEB_BASEPATH here)
    | + .gitignore
    | + <YourCustomFrontend>Web/: folder with suffix "Web" are your custom frontend code (your frontend repo)
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
