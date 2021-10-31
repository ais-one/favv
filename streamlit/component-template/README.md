# Streamlit Custom Components

## Introduction

The folder contains template and example code for creating [Streamlit](https://streamlit.io) Components using
- [Vite](https://github.com/vitejs/vite).
- Create React App

Refer to this [article](https://dev.to/aisone/streamlit-custom-components-vite-4bj7) for more information on the motivation and why Vite is used and how this repo was created.

If you are not familiar with creating a streamlit custom component, refer to the [README.md](https://github.com/streamlit/component-template#readme) document of [https://github.com/streamlit/component-template](https://github.com/streamlit/component-template) where this repo is derived from.


## NPM Usage (NPM 8+)

```bash
# everything
npm <command> -- <script arguments>

# per component group
npm <command> --workspace=sample -- <script arguments>

# per component
npm <command> --workspace=sample/vue_component -- <script arguments>
```


## Creation

Refer to [README-CREATE.md](README-CREATE.md)

## Publish to PyPI

Refer to [README-PUBLISH.md](README-PUBLISH.md)


## Development - Vite Vanilla Component - TBD

Use `sample` folder as reference for creating a group of components

### npm 6.x

```
cd <component_name_vanilla>
npm init vite@latest frontend --template vanilla
cd <component_name_vue>
npm init vite@latest frontend --template vue
```

### npm 8+

```
cd <component_name>
npm init vite@latest frontend -- --template vanilla
```

```
cd frontend
npm i streamlit-component-lib
```

take note of vite.config.js



1. Frontend - Install dependencies and run

From `sample` folder

```
cd vite_vanilla_compoent
cd frontend
npm i
npm run dev
```

2. Backend - Install dependencies and run

From `sample` folder

Create and activate your venv

```
pip install -r requirements.txt
streamlit run vanilla_component/__init__.py
```

3. Test

Navigate to URL indicated by streamlit (usually http://localhost:8501)



npm i
npm run build --workspace=sample/*
npm run dev --workspace=sample/vanilla_component

