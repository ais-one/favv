import os
import streamlit.components.v1 as components
import json

_RELEASE = True

if not _RELEASE:
  _component_func = components.declare_component("streamlit-antv_g6", url="http://localhost:3000") # vite dev server port
else:
  _component_func = components.declare_component("streamlit-antv_g6", path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend/dist"))

def st_antv_g6(config, nodes, edges, options=None, key=None):
  component_value = _component_func(config=config, nodes=nodes, edges=edges, options=options, key=key, default=0)
  return component_value

if not _RELEASE:
  import streamlit as st
  import pandas as pd

  print("START COMPONENT")

  @st.cache
  def load_dataset(csv_file_path):
    dataset = pd.read_csv(csv_file_path, index_col=0)
    return dataset

  df = load_dataset("g6/test-data.txt")
  nodes = []
  edges = []
  for col in df.columns:
    # print(col)
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
      # NOSONAR print(f'{i}, {j} = {value}', end="\t")
      # print(edge)
      edges.append(edge)
    # print()
  st.write(df.shape)
  st.dataframe(df)

  # NOSONAR nodes = [
  #   { "id": "node1", "x": 50, "y": 350, "label": "A", },
  #   { "id": "node2", "x": 250, "y": 150, "label": "B", },
  #   { "id": "node3", "x": 450, "y": 350, "label": "C", },
  # ]
  # edges = []
  # for x in range(8):
  #   edges.append({ "source": "node1", "target": "node2", "label": f'{x}th edge of A-B', })
  # for x in range(5):
  #   edges.append({ "source": "node2", "target": "node3", "label": f'{x}th edge of B-C', })

  # Additional options
  options = {
    'selectNodes': 3, # 0 (no selection), 1 (single select), n (multi select)
    'selectEdges': 3, # 0 (no selection), 1 (single select), n (multi select)
    'clickClearAll': False # True = clear all nodes if clicking on canvas
  }

  # G6 configurations
  config = {
    "width": 1280,
    "height": 800,
    "container": "container",
    "fitCenter": True,
    "linkCenter": True,
    "layout": {
      "type": "grid",
      "width": 1280,
      "height": 800,
      "onLayoutEnd": json.dumps(['__#fn#__', 'alert("loaded chart with key=" + window.stProps.key());'])
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
  rv = st_antv_g6(key="K1", config=config, nodes=nodes, edges=edges, options=options)
  st.write(rv)
  rv2 = st_antv_g6(key="K2", config=config, nodes=nodes, edges=edges, options=options)
  st.write(rv2)
  rv3 = st_antv_g6(key="K3", config=config, nodes=nodes, edges=edges, options=options)
  st.write(rv3)
