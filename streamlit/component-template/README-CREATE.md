# Creation

Use `streamlit-vite` folder as reference

## Create The Component Group Folder


```bash
mkdir streamlit-<component_group_name>
cd streamlit-<component_group_name>
```

Copy the `MANIFEST.in`, `setup.py`, `README.md` files from [streamlit-vite](streamlit-vite) and edit accordingly

## Create The Component Folder

In the `streamlit-<component_group_name>` folder

```bash
mkdir <component_name>
cd <component_name>
```

Copy the `__init__.py` file from [streamlit-vite](streamlit-vite) and edit accordingly

## Create the Component

1. Create using vite

Example command for creating a vanilla JS application using Vite

```bash
# npm 6.x
npm init vite@latest frontend --template vanilla

# npm 7+
npm init vite@latest frontend -- --template vanilla

cd frontend
```

You can replace `vanilla` with `vue` or `react`. Refer to [vite documentation](https://vitejs.dev/guide/)

2. Create vite.config.js with the following:

```js
export default {
  base: './'
}
```

3. Set package.json name property

Note this will be used by npm workspaces to identify a workspace

```json
{
  "name": "<component_group_name>_<component_name>"
}
```

3. Install your libraries

```
npm i streamlit-component-lib --workspaces="--workspace=<component_group_name>/<component_name>"
```


