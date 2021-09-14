import streamlit as st
from app1 import app1
from app2 import app2

st.set_page_config(page_title="Streamlit Demo", page_icon="🖖")

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

page = st.sidebar.radio("Go to",['Home', 'Page One', 'Page Two'])

optionals = st.expander("Search And Filter", False)
optionals.checkbox("Active")
optionals.radio("Pick Your Favourite", ["Apples", "Banaans", "Oranges"])

name_cols = optionals.columns(3)
first_name = name_cols[0].text_input("First Name")
last_name = name_cols[1].text_input("Last Name")
middle_name = name_cols[2].text_input("Middle Name")

print(page)
if page == "Page One":
    app1()
elif page == "Page Two":
    app2()