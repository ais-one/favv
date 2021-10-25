import streamlit as st
from streamlit_sidemenu import st_sidemenu 

print("START COMPONENT")

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
