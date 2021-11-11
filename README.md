# About FAVV (FastAPI+ViteVue)

FastAPI Python backend (BE) and Vite + VueJS + Ant Design frontend (FE) template... for your API and Web application needs.

The difference between this project and [https://github.com/ais-one/cookbook](https://github.com/ais-one/cookbook) is described [here](https://github.com/ais-one/cookbook/blob/master/README.md#about)

Also includes some samples in streamlit

## Considerations

The following are considerations for the project. The aim is to allow things to be built faster and reduce maintenence overhead.

- code reusability
- application segregation **inject your own frontend and backend project**
- ease of template upgrade
- ci/cd and container friendly
- microservices friendly
- up to date dependencies
- reducing technical debt
- scalability

## Roadmap & Updates

See [CHANGELOG.md](./CHANGELOG.md)

## Development - Setup and Run

### Backend

> python: 3.8.5, pip: 20.1.1

```bash
cd fastapi

# create environment called dev
python -m venv dev # python3 -m venv /path/to/new/virtual/env

# copy .env.example to .env, adjust your own custom env settings here
cp ./app/.env.example ./app/.env # common environment
cp ./app/.env.local.example ./app/.env.local # for local machine deployment
cp ./app/.env.docker-compose.example ./app/.env.docker-compose # for docker compose deployment

# copy requirements.txt.example to copy requirements.txt (point to your own custom requirements.txt inside)
cp ./requirements.txt.example ./requirements.txt
```
### activate env in windows

```
# cmd 
dev\Scripts\activate
dev\Scripts\deactivate

# powershell
dev\Scripts\Activate.ps1
deactivate
```
### activate env in linux

```
source dev/bin/activate 
```

# Installing / Upgrading python packages

## For framework

run **fastapi/install.sh**

## For your own applications

Manage packages using **fastapi/app/<custom_app>/requirements.txt**

Or run **fastapi/app/<custom_app>/install.sh**


# Run App & Task Quque (requires redis)

```bash
cd app

# fastapi application
python main.py # OPTION 1 - running using python
uvicorn main:app --reload --host=0.0.0.0 --port=3000 --access-log --log-level=debug --header server:none # OPTION 2 - running uvicorn

# HTTPS
# if using SSL include the following to uvicorn, also set USE_HTTPS in environment file
# --ssl-keyfile <path> - SSL key file --ssl-certfile <path> - SSL certificate file

# huey task queue consumer 
huey_consumer custom_app.models.tasks.huey

```

Navigate to - http://127.0.0.1:3000/api-docs

**Note:** if you use https and self-signed cert you may need to allow on browser

## HTTPS

Generate your private key and...

Create a self-signed cert, or get a signed cert

```bash
openssl req -x509 -newkey rsa:4096 -keyout local.key.pem -out local.cert.pem -days 365 -nodes -subj '/CN=127.0.0.1'
```

## Production Run (Docker)

```bash
cd ../fastapi
docker build -t <your-image-name>:<tag> .
docker run -it <your-image-name>:<tag>
```

### Frontend

- VueJS 3
- Vite 2 [https://github.com/vuejs/vite](https://github.com/vuejs/vite)
- Ant Design 2

refer to [vitevue/README.md](vitevue/README.md)

### Streamlit

See [streamlit/README.md](streamlit/README.md) for more information

---


# Customization

## Structure - Files / Folders For Customisation Or Use

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
  | + .env: environment state, custom app name and version
  | + .env.<your-environment>: environment specific info
  | + Dockerfile.example: DO NOT TOUCH THIS, use this as an example for your own Dockerfile
  | + install.sh: DO NOT TOUCH THIS 
  | + requirements.base.txt: DO NOT TOUCH THIS
  + streamlit/
  | + app/ : demo application
  | + component-template/ : streamlit custom components
  |   + streamlit-antv: using antv charts on streamlit
  |   + streamlit-vite: basic example of using vite to build streamlit-components
  |   + streamlit-xui: extended UI components for streamlit
  + vitevue/
    + README.md
```

**NOTES**
- All folders and files prefixed with TBD can be ignored, they are not implemented and used for reference

## Backend Customization Notes

Setting up your custom backend

```bash
# in favv/fastapi/app/
# note that project name must end with suffix "_app"
git clone <your backend project e.g. example_app>
```

- use **favv/fastapi/app/custom_app/** as reference on your custom backend
  - on working with your custom endpoints, using db, s3, file services
  - working with files in **favv/fastapi/app/custom_app/uploads/** folder
  - running subprocess in **favv/fastapi/app/custom_app/models/** folder
- set the APP, to the folder name of your custom app in **favv/fastapi/app/.env**
  - specify the VERSION and the ENVIRONMENT state (local, docker-compose, production, <your-environment-name> etc...)
  - specify APP which is your custom application, UPLOAD_FOLDER and MODEL_FOLDER is directly inside your custom app folder
  - set uour environment specific information in **favv/fastapi/app/.env.<your-environment-name>**
- application path is **favv/fastapi/app/** as **main.py** is run from there (either using python or uvicorn)
- test endpoints in **favv/fastapi/app/api/routes/test.py** will not be available in production environment
- NOTE: update **favv/fastapi/app/config.py** when **.env** entries change
- NOTE: any code outside **favv/fastapi/app** will not auto reload

## Notes

- use **fastapi/install.sh** to update python libraries
- for favv/fastapi .env host is **redis** if using docker compose **127.0.0.1** otherwise
