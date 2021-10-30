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

  my_styles = """
  body {
    margin: 0;
  }

  #app {
    margin: 0;
  }

  /* Fixed sidenav, full height */
  .sidenav {
    font-family: Arial;
    height: 100%;
    width: 100%;
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    background-color: #111;
    overflow-x: hidden;
    /* padding-top: 20px; */
  }

  /* Style the sidenav links and the dropdown button */
  .sidenav a, .dropdown-btn {
    padding: 6px 8px 6px 16px;
    text-decoration: none;
    font-size: 20px;
    color: #818181;
    display: block;
    border: none;
    background: none;
    width:100%;
    text-align: left;
    cursor: pointer;
    outline: none;
  }

  /* On mouse-over */
  .sidenav a:hover, .dropdown-btn:hover {
    color: #f1f1f1;
  }

  /* Main content */
  .main {
    margin-left: 200px; /* Same as the width of the sidenav */
    font-size: 20px; /* Increased text to enable scrolling */
    padding: 0px 10px;
  }

  /* Add an active class to the active dropdown button */
  .sidenav a.selected {
    background-color: green;
    color: white;
  }

  /* Dropdown container (hidden by default). Optional: add a lighter background color and some left padding to change the design of the dropdown content */
  .dropdown-container {
    display: none;
    background-color: #262626;
    padding-left: 8px;
  }

  /* Optional: Style the caret down icon */
  .fa-caret-down {
    float: right;
    padding-right: 8px;
  }
  """

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
    print('exception')
    # print(st.session_state)
    pass

  st.subheader("Dropdown Menu Test")
  with st.sidebar:
    rv = st_sidemenu(items=my_items, selected=selected, opened=opened, styles=my_styles, key="menu")
    st.write(rv)
    st.write(st.session_state.menu)