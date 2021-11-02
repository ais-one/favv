## Publishing To PyPI

Reference:
- https://docs.streamlit.io/library/components/publish
- https://packaging.python.org/


## Prerequisite

1. Build Frontend

```
npm run build --workspace=<component_group>/<component>
```

```
npm run build --workspace=./streamlit-vite/vanilla_component
npm run build --workspace=./streamlit-vite/vue_component
```

2. Set _RELEASE Flag in `__init__.py` == `True`

## Setup For PyPY publishing

1. Need to install the packages below in you environment

```bash
pip install wheel twine
```

2. Preparing the upload

Refer to [upload.sh](./streamlit-xui/upload.sh) file on how the commands are run. The script will also echo the pre-requisites (to run this on windows, use git bash)

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

## Perform Deployment

3. To deploy to pypi test

```bash
./upload.sh <component_group> test
```

4. To deploy to pypi

```bash
./upload.sh <component_group> production
```

5. To install from pypi test for use in your streamlit application

```bash
pip install -i https://test.pypi.org/simple/ streamlit-xui==<version number>
```
