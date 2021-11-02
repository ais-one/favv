import os
import streamlit.components.v1 as components

_RELEASE = True # set to True for deployment

if not _RELEASE:
  _component_func = components.declare_component("streamlit_xui_placeholder", url="http://localhost:3000")
else:
  parent_dir = os.path.dirname(os.path.abspath(__file__))
  build_dir = os.path.join(parent_dir, "frontend/dist")
  _component_func = components.declare_component("streamlit_xui_placeholder", path=build_dir)

def st_xui_placeholder(size=None):
  """Display a placeholder 
  Parameters
  ----------
  size: Dict | string
    list of menu items.
  """
  component_value = _component_func(size=size, key=key)
  return component_value

if not _RELEASE:
  import streamlit as st

  st_xui_placeholder(size=None)
  st.write('Dibe')
