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
  "layout": "centered",
  "initial_sidebar_state": "expanded"
}
st.set_page_config(**PAGE_CONFIG)

# hide menu button
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

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

# expander
optionals = st.expander("Search And Filter", False)
optionals.checkbox("Active")
optionals.radio("Pick Your Favourite", ["Apples", "Banaans", "Oranges"])

name_cols = optionals.columns(3)
first_name = name_cols[0].text_input("First Name")
last_name = name_cols[1].text_input("Last Name")
middle_name = name_cols[2].text_input("Middle Name")

# from streamlit import caching
# caching.clear_cache()

def main():
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