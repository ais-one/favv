import os
import streamlit.components.v1 as components

_RELEASE = False

if not _RELEASE:
  _component_func = components.declare_component(
    "vite_vue_component",
    url="http://localhost:3000", # vite dev server port
  )
else:
  parent_dir = os.path.dirname(os.path.abspath(__file__))
  build_dir = os.path.join(parent_dir, "frontend/dist")
  _component_func = components.declare_component("vite_vue_component", path=build_dir)

def my_component(name, key=None):
  component_value = _component_func(name=name, key=key, default=0)
  return component_value

if not _RELEASE:
  import streamlit as st
  st.subheader("Component Test")
  num_clicks = my_component(name = "NameViteVue")
  st.markdown("You've clicked %s times!" % int(num_clicks))
