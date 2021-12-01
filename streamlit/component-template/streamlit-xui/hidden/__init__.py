import os
import streamlit.components.v1 as components

_RELEASE = True # set to True for deployment

if not _RELEASE:
  _component_func = components.declare_component("streamlit_xui_hidden", url="http://localhost:3000")
else:
  parent_dir = os.path.dirname(os.path.abspath(__file__))
  build_dir = os.path.join(parent_dir, "frontend/dist")
  _component_func = components.declare_component("streamlit_xui_hidden", path=build_dir)

def st_xui_hidden(key, value=None):
  """hidden 
  Parameters
  ----------
  value: your data.
  """
  component_value = _component_func(key=key, value=value)
  return component_value

if not _RELEASE:
  import streamlit as st

  st_xui_hidden(key="test-key", value="test value")
  st.write('Testing')
