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

  @st.cache
  def load_dataset(csv_file_path):
    dataset = pd.read_csv(csv_file_path, index_col=0)
    return dataset

  df = load_dataset("vite_vanilla_component/g6test.txt")
  st.write(df.shape)
  # st.write(df.shape[1])

  print("START START START START START START START START")
  nodes = []
  edges = []
  for col in df.columns:
    print(col)
    nodes.append({ "id": col, "label": col })
  for i in range(df.shape[0]): #iterate over rows
    # nodes.append
    for j in range(df.shape[1]): #iterate over columns
      value = df.iat[i, j] #get cell value
      edge = { "source": df.columns[i], "target": df.columns[j], "label": value }
      if i > j: # , it is return
        edge["return"] = True
      elif i == j: #, it is loop
        edge["type"] = "loop"
      # print(f'{i}, {j} = {value}', end="\t")
      print(edge)
      edges.append(edge)
    print()

  st.dataframe(df)

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

  # nodes = [
  #   { "id": "node0", "label": "Email", },
  #   { "id": "node1", "label": "null", },
  #   { "id": "node2", "label": "conv", },
  #   { "id": "node3", "label": "Digital Media", },
  #   { "id": "node4", "label": "Sales Play", },
  #   { "id": "node5", "label": "3rd Party Lead Gen", },
  #   { "id": "node6", "label": "start", },
  #   { "id": "node7", "label": "Online", },
  #   { "id": "node8", "label": "Events", },
  #   { "id": "node9", "label": "Sales Enablement", },
  # ]

  # edges = []
  # edges.append({ "source": "node0", "target": "node0", "label": "0.105338", "type": "loop" }) # email - email
  # edges.append({ "source": "node0", "target": "node1", "label": "0.023309" }) # email - null
  # edges.append({ "source": "node0", "target": "node2", "label": "0.049587" }) # email - conv
  # edges.append({ "source": "node0", "target": "node3", "label": "0.349889" })
  # edges.append({ "source": "node0", "target": "node4", "label": "0.069114" })
  # edges.append({ "source": "node0", "target": "node5", "label": "0.01031" })
  # edges.append({ "source": "node0", "target": "node6", "label": "0" })
  # edges.append({ "source": "node0", "target": "node7", "label": "0.387885" })
  # edges.append({ "source": "node0", "target": "node8", "label": "0.002743" })
  # edges.append({ "source": "node0", "target": "node9", "label": "0.001824" })

  # edges.append({ "source": "node1", "target": "node0", "label": "0", "return": True }) # null - email 
  # edges.append({ "source": "node1", "target": "node1", "label": "1", "type": "loop" }) # null - null
  # edges.append({ "source": "node1", "target": "node2", "label": "0" }) # null - conv
  # edges.append({ "source": "node1", "target": "node3", "label": "0" })
  # edges.append({ "source": "node1", "target": "node4", "label": "0" })
  # edges.append({ "source": "node1", "target": "node5", "label": "0" })
  # edges.append({ "source": "node1", "target": "node6", "label": "0" })
  # edges.append({ "source": "node1", "target": "node7", "label": "0" })
  # edges.append({ "source": "node1", "target": "node8", "label": "0" })
  # edges.append({ "source": "node1", "target": "node9", "label": "0" })

  # edges.append({ "source": "node2", "target": "node0", "label": "0", "return": True }) # conv - email
  # edges.append({ "source": "node2", "target": "node1", "label": "0", "return": True }) # conv - null
  # edges.append({ "source": "node2", "target": "node2", "label": "1", "type": "loop" }) # conv - conv
  # edges.append({ "source": "node2", "target": "node3", "label": "0" })
  # edges.append({ "source": "node2", "target": "node4", "label": "0" })
  # edges.append({ "source": "node2", "target": "node5", "label": "0" })
  # edges.append({ "source": "node2", "target": "node6", "label": "0" })
  # edges.append({ "source": "node2", "target": "node7", "label": "0" })
  # edges.append({ "source": "node2", "target": "node8", "label": "0" })
  # edges.append({ "source": "node2", "target": "node9", "label": "0" })

  # edges.append({ "source": "node3", "target": "node0", "label": "0.363272", "return": True })
  # edges.append({ "source": "node3", "target": "node1", "label": "0.033978", "return": True })
  # edges.append({ "source": "node3", "target": "node2", "label": "0.027071", "return": True })
  # edges.append({ "source": "node3", "target": "node3", "label": "0.346411", "type": "loop" })
  # edges.append({ "source": "node3", "target": "node4", "label": "0.036137" })
  # edges.append({ "source": "node3", "target": "node5", "label": "0.004757" })
  # edges.append({ "source": "node3", "target": "node6", "label": "0" })
  # edges.append({ "source": "node3", "target": "node7", "label": "0.186499" })
  # edges.append({ "source": "node3", "target": "node8", "label": "0.001273" })
  # edges.append({ "source": "node3", "target": "node9", "label": "0.000603" })

  # edges.append({ "source": "node4", "target": "node0", "label": "0.062031", "return": True })
  # edges.append({ "source": "node4", "target": "node1", "label": "0.011228", "return": True })
  # edges.append({ "source": "node4", "target": "node2", "label": "0.003686", "return": True })
  # edges.append({ "source": "node4", "target": "node3", "label": "0.779703", "return": True })
  # edges.append({ "source": "node4", "target": "node4", "label": "0.062172", "type": "loop" })
  # edges.append({ "source": "node4", "target": "node5", "label": "0.023887" })
  # edges.append({ "source": "node4", "target": "node6", "label": "0" })
  # edges.append({ "source": "node4", "target": "node7", "label": "0.052988" })
  # edges.append({ "source": "node4", "target": "node8", "label": "0.000206" })
  # edges.append({ "source": "node4", "target": "node9", "label": "0.004099" })

  # edges.append({ "source": "node5", "target": "node0", "label": "0.083203", "return": True })
  # edges.append({ "source": "node5", "target": "node1", "label": "0.005357", "return": True })
  # edges.append({ "source": "node5", "target": "node2", "label": "0.002916", "return": True })
  # edges.append({ "source": "node5", "target": "node3", "label": "0.870312", "return": True })
  # edges.append({ "source": "node5", "target": "node4", "label": "0.007289", "return": True })
  # edges.append({ "source": "node5", "target": "node5", "label": "0.023887", "type": "loop" })
  # edges.append({ "source": "node5", "target": "node6", "label": "0" })
  # edges.append({ "source": "node5", "target": "node7", "label": "0.022468" })
  # edges.append({ "source": "node5", "target": "node8", "label": "0.000364" })
  # edges.append({ "source": "node5", "target": "node9", "label": "0.000383" })

  # edges.append({ "source": "node6", "target": "node0", "label": "0.056116", "return": True })
  # edges.append({ "source": "node6", "target": "node1", "label": "0", "return": True })
  # edges.append({ "source": "node6", "target": "node2", "label": "0", "return": True })
  # edges.append({ "source": "node6", "target": "node3", "label": "0.420427", "return": True })
  # edges.append({ "source": "node6", "target": "node4", "label": "0.146831", "return": True })
  # edges.append({ "source": "node6", "target": "node5", "label": "0.008191", "return": True })
  # edges.append({ "source": "node6", "target": "node6", "label": "0", "type": "loop" })
  # edges.append({ "source": "node6", "target": "node7", "label": "0.366649" })
  # edges.append({ "source": "node6", "target": "node8", "label": "0.000253" })
  # edges.append({ "source": "node6", "target": "node9", "label": "0.001535" })

  # edges.append({ "source": "node7", "target": "node0", "label": "0.057593", "return": True })
  # edges.append({ "source": "node7", "target": "node1", "label": "0.003858", "return": True })
  # edges.append({ "source": "node7", "target": "node2", "label": "0.006389", "return": True })
  # edges.append({ "source": "node7", "target": "node3", "label": "0.617353", "return": True })
  # edges.append({ "source": "node7", "target": "node4", "label": "0.223425", "return": True })
  # edges.append({ "source": "node7", "target": "node5", "label": "0.028346", "return": True })
  # edges.append({ "source": "node7", "target": "node6", "label": "0", "return": True })
  # edges.append({ "source": "node7", "target": "node7", "label": "0.060601", "type": "loop" })
  # edges.append({ "source": "node7", "target": "node8", "label": "0.00019" })
  # edges.append({ "source": "node7", "target": "node9", "label": "0.002245" })

  # edges.append({ "source": "node8", "target": "node0", "label": "0.057728", "return": True })
  # edges.append({ "source": "node8", "target": "node1", "label": "0.004325", "return": True })
  # edges.append({ "source": "node8", "target": "node2", "label": "0.086123", "return": True })
  # edges.append({ "source": "node8", "target": "node3", "label": "0.195186", "return": True })
  # edges.append({ "source": "node8", "target": "node4", "label": "0.040053", "return": True })
  # edges.append({ "source": "node8", "target": "node5", "label": "0.01636", "return": True })
  # edges.append({ "source": "node8", "target": "node6", "label": "0", "return": True })
  # edges.append({ "source": "node8", "target": "node7", "label": "0.595525", "return": True })
  # edges.append({ "source": "node8", "target": "node8", "label": "0.002256", "return": True })
  # edges.append({ "source": "node8", "target": "node9", "label": "0.002445", "type": "loop" })

  # edges.append({ "source": "node9", "target": "node0", "label": "0.113616", "return": True })
  # edges.append({ "source": "node9", "target": "node1", "label": "0.00623", "return": True })
  # edges.append({ "source": "node9", "target": "node2", "label": "0.003115", "return": True })
  # edges.append({ "source": "node9", "target": "node3", "label": "0.661525", "return": True })
  # edges.append({ "source": "node9", "target": "node4", "label": "0.121922", "return": True })
  # edges.append({ "source": "node9", "target": "node5", "label": "0.029665", "return": True })
  # edges.append({ "source": "node9", "target": "node6", "label": "0", "return": True })
  # edges.append({ "source": "node9", "target": "node7", "label": "0.058291", "return": True })
  # edges.append({ "source": "node9", "target": "node8", "label": "0.000297", "return": True })
  # edges.append({ "source": "node9", "target": "node9", "label": "0.00534", "type": "loop" })

  st.subheader("Component Test")
  rv = my_component(name="NameViteVanilla", config=config, nodes=nodes, edges=edges)
  st.write(rv)
  # st.markdown("You've clicked %s times!" % int(rv['numClicks']))
  # st.markdown(f'Selected Node Is: {rv['selectedNode']}')
