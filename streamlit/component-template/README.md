# Streamlit Custom Components

## Introduction

The folder contains template and example code for creating [Streamlit](https://streamlit.io) Components using
- [Vite](https://github.com/vitejs/vite).
- Create React App

Refer to this [article](https://dev.to/aisone/streamlit-custom-components-vite-4bj7) for more information on the motivation and why Vite is used and how this repo was created.

If you are not familiar with creating a streamlit custom component, refer to the [README.md](https://github.com/streamlit/component-template#readme) document of [https://github.com/streamlit/component-template](https://github.com/streamlit/component-template) where this repo is derived from.

## Development Usage - Vite Vanilla Component

1. Frontend - Install dependencies and run

From vite-template folder

```
cd vite_vanilla_compoent
cd frontend
npm i
npm run dev
```

2. Backend - Install dependencies and run

From vite-template folder

Create and activate your venv

```
pip install -r requirements.txt
streamlit run vanilla_component/__init__.py
```

3. Test

Navigate to URL indicated by streamlit (usually http://localhost:8501)

