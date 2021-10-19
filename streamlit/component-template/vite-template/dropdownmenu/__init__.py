import os
import streamlit.components.v1 as components

_RELEASE = False

# if not _RELEASE:
#   _component_func = components.declare_component("dropdownmenu", url="http://localhost:3000")
# else:
#   parent_dir = os.path.dirname(os.path.abspath(__file__))
#   build_dir = os.path.join(parent_dir, "frontend/dist")
#   _component_func = components.declare_component("dropdownmenu", path=build_dir)

parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "frontend/dist")
_component_func = components.declare_component("dropdownmenu", path=build_dir)

def my_component(name, items, selected, styles=None, key=None):
  component_value = _component_func(name=name, items=items, selected=selected, key=key, default=0)
  return component_value

if not _RELEASE:
  import streamlit as st

  print("START COMPONENT")

  qp = st.experimental_get_query_params()
  print(qp)

  my_items = [
    { 'label': 'About' },
    { 'label': 'Services' },
    { 'label': 'A very very very very very very very very very long item' },
    { 'label': 'Contact' },
    {
      'label': 'Dropdown V',
      'children': [
        { 'label': 'Link 1' },
        { 'label': 'Link 2' },
        { 'label': 'Link 3' },
      ]
    },
    { 'label': 'Search' },
  ]

  my_styles = {
    'font-family': 'Arial',
  }

  st.subheader("Dropdown Menu Test")
  with st.sidebar:
    rv = my_component(name="dropdownmenu", items=my_items, selected=None, styles=my_styles, key="K1")
    st.write(rv)
