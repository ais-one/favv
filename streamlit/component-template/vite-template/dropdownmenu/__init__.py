import os
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
  _component_func = components.declare_component("dropdownmenu", url="http://localhost:3000")
else:
  parent_dir = os.path.dirname(os.path.abspath(__file__))
  build_dir = os.path.join(parent_dir, "frontend/dist")
  _component_func = components.declare_component("dropdownmenu", path=build_dir)

def my_component(name, key=None):
  component_value = _component_func(name=name, key=key, default=0)
  return component_value

if not _RELEASE:
  import streamlit as st

  print("START COMPONENT")

  st.subheader("Dropdown Menu Test")
  with st.sidebar:
    rv = my_component(name="dropdownmenu", key="K1")

  # page = st.sidebar.radio(
  #   "Choose An Item",
  #   ['Demos', 'Titanic', 'NYC Car Accidents']
  # )
  # st.write(rv)
