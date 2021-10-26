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

## Publishing To PyPI

Reference:
- https://docs.streamlit.io/library/components/publish
- https://packaging.python.org/

1. Need to install the packages below in you environment

```bash
pip install wheel twine
```

2. Preparing the upload

Refer to [upload.sh](./vite-template/upload.sh) file on how the commands are run. The script will also echo the pre-requisites (to run this on windows, use git bash)

Setup `.pypirc` file in your `$HOME` or `~` directory with the contents below

```
[distutils]
index-servers =
  pypi
  testpypi

[pypi]
username = __token__
password = <your pypi API Key>

[testpypi]
username = __token__
password = <your testpypi API Key>
repository = https://test.pypi.org/legacy/
```

3. To deploy to pypi test

```bash
./upload.sh test
```

4. To deploy to pypi

```bash
./upload.sh production
```

5. To install from pypi test for use in your streamlit application

```bash
pip install -i https://test.pypi.org/simple/ streamlit-sidemenu==<version number>
```
