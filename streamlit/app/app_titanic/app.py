import pandas as pd
import time
import streamlit as st
import plotly.express as px
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder
from st_aggrid.shared import JsCode, GridUpdateMode, DataReturnMode

import os
import streamlit.components.v1 as components
from logger import logger

cellsytle_jscode = JsCode(
"""
function(params) {
  if (params.value.includes('Southampton')) {
    return {
      'color': 'white',
      'backgroundColor': 'darkred'
    }
  } else {
    return {
      'color': 'black',
      'backgroundColor': 'white'
    }
  }
};
"""
)

@st.cache
def load_dataset(data_link):
    dataset = pd.read_csv(data_link)
    return dataset

def app_run():
  titanic_link = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
  titanic_data = load_dataset(titanic_link)

  st.title("Titanic Data Demo")

  selected_class = st.radio("Select Class", titanic_data['class'].unique())
  st.write("Selected Class:", selected_class)
  # st.write("Selected Class Type:", type(selected_class))

  selected_sex = st.selectbox("Select Sex", titanic_data['sex'].unique())
  st.write(f"Selected Option: {selected_sex!r}")

  selected_decks = st.multiselect("Select Decks", titanic_data['deck'].unique())
  st.write("Selected Decks:", selected_decks)

  age_columns = st.columns(2)
  age_min = age_columns[0].number_input("Minimum Age", value=titanic_data['age'].min())
  age_max = age_columns[1].number_input("Maximum Age", value=titanic_data['age'].max())
  if age_max < age_min:
    st.error("The maximum age can't be smaller than the minimum age!")
  else:
    st.success("Congratulations! Correct Parameters!")
    subset_age = titanic_data[(titanic_data['age'] <= age_max) & (age_min <= titanic_data['age'])]
    st.write(f"Number of Records With Age Between {age_min} and {age_max}: {subset_age.shape[0]}")

  optionals = st.expander("Optional Configurations", True)
  fare_min = optionals.slider(
    "Minimum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
  )
  fare_max = optionals.slider(
    "Maximum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
  )
  subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) & (fare_min <= titanic_data['fare'])]
  st.write(f"Number of Records With Fare Between {fare_min} and {fare_max}: {subset_fare.shape[0]}")

  progress_bar = st.progress(0)
  progress_text = st.empty()
  for i in range(101):
    time.sleep(0.01)
    progress_bar.progress(i)
    progress_text.text(f"Progress: {i}%")

  st.dataframe(titanic_data)

  with st.echo("below"):
    balloons = st.text_input("Please enter awesome to see some balloons")
    if balloons == "awesome":
      st.balloons()

  st.write("This is a large text area.")
  st.text_area("A very big area", height=300)

  # test aggrid
  st.subheader("streamlit-aggrid test")
  # https://towardsdatascience.com/7-reasons-why-you-should-use-the-streamlit-aggrid-component-2d9a2b6e32f0

  gb = GridOptionsBuilder.from_dataframe(titanic_data)
  gb.configure_pagination()
  # gb.configure_selection(selection_mode="multiple", use_checkbox=True)
  gb.configure_selection(selection_mode="single", use_checkbox=True)

  # gb.configure_side_bar()

  # gb.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc="sum", editable=True)
  # gb.configure_column("embark_town", cellStyle=cellsytle_jscode)

  gridOptions = gb.build()
  grid_data = AgGrid(
    titanic_data,
    key="ag1",
    gridOptions=gridOptions,
    # enable_enterprise_modules=True,
    # allow_unsafe_jscode=True,
    update_mode=GridUpdateMode.SELECTION_CHANGED, # able to detect more than one type of update? # for multiselect, how to batch updates?
    input_mode=DataReturnMode.FILTERED # only one?
  )

  grid_data2 = AgGrid(titanic_data, key="ag2", gridOptions=gridOptions)
  grid_data3 = AgGrid(titanic_data, key="ag3", gridOptions=gridOptions)

  st.write(DataReturnMode.__members__)
  st.write(GridUpdateMode.__members__)

  st.write(grid_data)
  st.write(grid_data2)
  st.write(grid_data3)

  selected_rows = grid_data["selected_rows"]
  selected_rows = pd.DataFrame(selected_rows)

  if len(selected_rows) != 0:
    fig = px.bar(selected_rows, "embark_town", color="pclass")
    st.plotly_chart(fig)

  # set your session states here...
  if 'cc1' in st.session_state:
    st.session_state.cc1 = st.session_state.cc1 # this is not useless, it sets the session data...
  if 'cc2' in st.session_state:
    st.session_state.cc2 = st.session_state.cc2
  if 'cc3' in st.session_state:
    st.session_state.cc3 = st.session_state.cc3
  if 'my_hours_per_week' in st.session_state:
    st.session_state.my_hours_per_week = st.session_state.my_hours_per_week
  if 'my_amount' in st.session_state:
    st.session_state.my_amount = st.session_state.my_amount
