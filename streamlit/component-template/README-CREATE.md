# Creation

## Create The Component Group Folder


```bash
mkdir streamlit-<component_group_name>
```

Copy the `LICENSE`, `MANIFEST.in`, `setup.py`, `README.md` files from [streamlit-antv](streamlit-antv) as an example

You will need to modify all files later except `LICENSE`

## Creating the vanilla component using vite js

```bash
mkdir vanilla_component
cd vanilla_component
npm init vite@latest frontend --template vanilla
```
# npm 6.x

```
cd <component_name_vanilla>
cd <component_name_vue>
npm init vite@latest frontend --template vue
```

# npm 7+

```
cd <component_name>
npm init vite@latest frontend -- --template vanilla
```

```
cd frontend
npm i streamlit-component-lib
```

take note of vite.config.js

