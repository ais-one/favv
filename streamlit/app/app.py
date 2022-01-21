import streamlit as st
from app_demo import app_run as app_run_demo
from app_titanic.app import app_run as app_run_titanic
from app_car_accidents.app import app_run as app_run_car_accidents

from logger import logger

# page config must be the very first activity
# st.set_page_config(
#   page_title="Streamlit Demo",
#   page_icon=":smiley:", # or "🖖"
#   layout="wide",
#   initial_sidebar_state="collapsed" # expanded
# )
PAGE_CONFIG = {
  "page_title": "hello",
  "page_icon": ":smiley:",
  "layout": "wide", # centered, wide
  "initial_sidebar_state": "expanded"
}
st.set_page_config(**PAGE_CONFIG)

# hide menu button
hide_streamlit_menu = False
if hide_streamlit_menu:
  st.markdown(
""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """,
  unsafe_allow_html=True)

# columns
# https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/
# st1, st2, st3 = st.beta_columns(3)

# Use the full page instead of a narrow central column
# st.set_page_config(layout="wide")
# Space out the maps so the first one is 2x the size of the other three
# c1, c2, c3, c4 = st.columns((2, 1, 1, 1))

# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

def init_sessions():
  logger.info('Init Session')
  if 'my_hours_per_week' not in st.session_state:
    st.session_state.my_hours_per_week = 40
  if 'my_amount' not in st.session_state:
    st.session_state.my_amount = 5
  if 'cc1' not in st.session_state:
    st.session_state.cc1 = 0
  if 'cc2' not in st.session_state:
    st.session_state.cc2 = 0
  if 'cc3' not in st.session_state:
    st.session_state.cc3 = 0
  if 'ag1' not in st.session_state:
    st.session_state.ag1 = None
  if 'ag2' not in st.session_state:
    st.session_state.ag2 = None
  if 'ag3' not in st.session_state:
    st.session_state.ag3 = None
  logger.info(st.session_state.cc1)

# from streamlit import caching
# caching.clear_cache()

def main():
  init_sessions()
  st.write(st.session_state)

  # expander
  optionals = st.expander("Search And Filter", False)
  optionals.checkbox("Active")
  optionals.radio("Pick Your Favourite", ["Apples", "Banaans", "Oranges"])

  name_cols = optionals.columns(3)
  first_name = name_cols[0].text_input("First Name")
  last_name = name_cols[1].text_input("Last Name")
  middle_name = name_cols[2].text_input("Middle Name")

  st.sidebar.success("Menu")
  page = st.sidebar.radio(
    "Choose An Item",
    ['Demos', 'Titanic', 'NYC Car Accidents']
  )
  # print(page)
  if page == "Demos":
    app_run_demo()
    logger.info('Demos')
  elif page == "Titanic":
    app_run_titanic()
    logger.info('Titanic')
  elif page == "NYC Car Accidents":
    app_run_car_accidents()
    logger.info('NYC Car Accidents')

if __name__ == '__main__':
  main()