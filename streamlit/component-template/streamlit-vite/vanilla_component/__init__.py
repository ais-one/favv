import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
  _component_func = components.declare_component("vanilla_component", url="http://localhost:3000") # vite dev server port
else:
  _component_func = components.declare_component("vanilla_component", path=os.path.join(os.path.dirname(os.path.abspath(__file__)), "frontend/dist"))

def vanilla_component(name, key=None, default=0):
  component_value = _component_func(name=name, key=key, default=default)
  return component_value

if not _RELEASE:
  import streamlit as st
  st.subheader("Component Test")
  num_clicks = vanilla_component(name = "Vanilla")
  st.markdown("You've clicked %s times!" % int(num_clicks))
