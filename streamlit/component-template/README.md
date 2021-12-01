# Streamlit Custom Components

This project shows how to architecture multiple component_groups with multiple custom streamlit components

e.g.

+-streamlit-antv (component_group)
| +- g2 (component)
| |  +- frontend
| +- g2plot
| |  +- frontend
| +- g6
|    +- frontend
+-streamlit-xui
  +- sidemenu
  |  +- frontend
  +- hidden
     +- frontend

The packaging tool [Vite](https://github.com/vitejs/vite), is used to create React, Vue or Vanilla JS frontends.

NPM workspace features is used

## Requirements

- NodeJS 16+
- NPM 8+
- Python 3.8+

## References

- [Streamlit](https://streamlit.io)
- Streamlit component [README.md](https://github.com/streamlit/component-template#readme)
- dev.to [article](https://dev.to/aisone/streamlit-custom-components-vite-4bj7) for more information on the motivation and why Vite is used.


## Quick Test

Test `vanilla_component` in `streamlit-vite` component_group folder

1. Install and run frontend component run dev server

From `<project root>/streamlit/component-tamplate` folder

```
npm i --workspace=streamlit-vite/vanilla_component
npm run dev --workspace=streamlit-vite/vanilla_component
```

2. Run python side

From `<project root>/streamlit` folder

**Note:** ensure `venv` set is set and python libraries such as `streamlit` are installed.

```cmd
python -m venv dev
dev\Scripts\activate.bat
pip install -r requirements.txt
```

From `<project root>/streamlit/component-tamplate/streamlit-vite` (component_group) folder

```bash
streamlit run vanilla_component/__init__.py
```

**Note:** make sure `_RELEASE = False` in `__init__.py` file


3. View on browser

Navigate to URL indicated by streamlit (usually http://localhost:8501)


---

## Create new component_group and component in the component_group

Refer to [README-CREATE.md](README-CREATE.md)

## Publish to PyPI

Refer to [README-PUBLISH.md](README-PUBLISH.md)

## NPM Workspace Notes

```bash
# install all
npm i -- <script arguments if any>

# build all in a workspace (a component group)
npm run build --workspace=streamlit-vite/* -- <script arguments if any>

# run dev a project (component) in a workspace
npm run dev --workspace=streamlit-vite/vanilla_component -- <script arguments if any>
```
