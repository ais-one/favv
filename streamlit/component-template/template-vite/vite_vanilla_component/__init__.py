import os
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
  _component_func = components.declare_component(
    "vite_vanilla_component",
    url="http://localhost:3000", # vite dev server port
  )
else:
  parent_dir = os.path.dirname(os.path.abspath(__file__))
  build_dir = os.path.join(parent_dir, "frontend/dist")
  _component_func = components.declare_component("vite_vanilla_component", path=build_dir)

def my_component(name, config, nodes, edges, key=None):
  component_value = _component_func(name=name, config=config, nodes=nodes, edges=edges, key=key, default=0)
  return component_value

if not _RELEASE:
  import streamlit as st
  import pandas as pd

  print("START COMPONENT")

  @st.cache
  def load_dataset(csv_file_path):
    dataset = pd.read_csv(csv_file_path, index_col=0)
    return dataset

  df = load_dataset("vite_vanilla_component/g6test.txt")
  nodes = []
  edges = []
  for col in df.columns:
    print(col)
    nodes.append({ "id": col, "label": col })
  for i in range(df.shape[0]): #iterate over rows
    # nodes.append
    for j in range(df.shape[1]): #iterate over columns
      value = df.iat[i, j] # get cell value
      # if value != 0:
      edge = { "source": df.columns[i], "target": df.columns[j], "label": value }
      if i > j: # , it is return
        edge["return"] = True
      elif i == j: #, it is loop
        edge["type"] = "loop"
      # print(f'{i}, {j} = {value}', end="\t")
      print(edge)
      edges.append(edge)
    print()
  st.write(df.shape)
  st.dataframe(df)

  # nodes = [
  #   { "id": "node1", "x": 50, "y": 350, "label": "A", },
  #   { "id": "node2", "x": 250, "y": 150, "label": "B", },
  #   { "id": "node3", "x": 450, "y": 350, "label": "C", },
  # ]
  # edges = []

  # for x in range(8):
  #   edges.append({ "source": "node1", "target": "node2", "label": f'{x}th edge of A-B', })
  # for x in range(5):
  #   edges.append({ "source": "node2", "target": "node3", "label": f'{x}th edge of B-C', })

  config = {
    "width": 1280,
    "height": 800,
    "container": "container",
    "fitCenter": True,
    "linkCenter": True,
    "layout": {
      "type": "random",
      "width": 1280,
      "height": 800,
    },
    "defaultNode": {
      "type": "circle",
      "size": [40],
      "color": "#5B8FF9",
      "style": { "fill": "#9EC9FF", "lineWidth": 3 },
      "labelCfg": { "style": { "fill": "#000", "fontSize": 14 } }
    },
    "defaultEdge": {
      "type": "quadratic",
      "labelCfg": { "autoRotate": True, },
      "style": {
        "endArrow": True
      }
    },
    "modes": {
      "default": ["drag-canvas", "drag-node"],
    },
    "nodeStateStyles": {
      "hover": { "fillOpacity": 0.8 },
      "selected": { "lineWidth": 5 }
    }
  }

  st.subheader("Component Test")
  rv = my_component(name="NameViteVanilla", key="K1", config=config, nodes=nodes, edges=edges)
  my_component(name="NameViteVanilla", key="K2", config=config, nodes=nodes, edges=edges)
  my_component(name="NameViteVanilla", key="K3", config=config, nodes=nodes, edges=edges)
  st.write(rv)
  # st.markdown("You've clicked %s times!" % int(rv['numClicks']))
  # st.markdown(f'Selected Node Is: {rv['selectedNode']}')
