import os
import streamlit.components.v1 as components

_RELEASE = True # set to True for deployment

if not _RELEASE:
  _component_func = components.declare_component("streamlit_sidemenu", url="http://localhost:3000")
else:
  parent_dir = os.path.dirname(os.path.abspath(__file__))
  build_dir = os.path.join(parent_dir, "frontend/dist")
  _component_func = components.declare_component("streamlit_sidemenu", path=build_dir)

def st_sidemenu(items, selected, opened, styles=None, key=None):
  """Display a menu on the sidebar. Nesting is to child only, no grand-child or lower descendents 
  Parameters
  ----------
  options: Dict
    list of menu items.
  selected: str
    selected menu item.
  opened: List
    list of menu groups that are open/expanded
  styles: str
    CSS styling
  key: str
    An optional string to use as the unique key for the widget. 
    Assign a key so the component is not remount every time the script is rerun.
  """
  component_value = _component_func(items=items, selected=selected, opened=opened, key=key)
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
      'label': 'Dropdown 1',
      'children': [
        { 'label': 'Link 1' },
        { 'label': 'Link 2' },
        { 'label': 'Link 3' },
      ]
    },
    {
      'label': 'Dropdown 2',
      'children': [
        { 'label': 'Link A' },
        { 'label': 'Link B' },
      ]
    },
    { 'label': 'Search' },
  ]

  my_styles = {
    'expand-char': '+',
    'collapse-char': '+',
    'font-family': 'Arial',
  }

  selected = 'Link A'
  opened = ['Dropdown 2']
  try:
    print('before1')
    # print('st.session_state.menu', st.session_state.menu['selected'])
    selected = st.session_state.menu['selected']
    opened = st.session_state.menu['opened']
    print('selected', selected)
    print('opened', opened)
  except:
    print('hellooooo')
    # print(st.session_state)
    pass

  st.subheader("Dropdown Menu Test")
  with st.sidebar:
    rv = st_sidemenu(items=my_items, selected=selected, opened=opened, styles=my_styles, key="menu")
    st.write(rv)
    st.write(st.session_state.menu)
