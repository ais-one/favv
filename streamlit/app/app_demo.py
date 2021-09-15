import streamlit as st
import pandas as pd
from file_utils import file_uploads

def app_run():
  st.title("app1 File Upload Tutorial")
  menu = ["Home", "Single CSV", "Multiple CSV", "About"]
  choice = st.selectbox("Menu", menu)
  # st.markdown("## app1")
  if choice == "Home":
    st.subheader("Home")
  elif choice == "Single CSV":
    st.subheader("Single CSV")
    csv_file = file_uploads(multiple=False, label="Input Single CSV and get data" )
    if csv_file is not None:
      # if csvFile.type == "text/plain"
      #   raw_text = str(csvFile.read(), "utf-8")
      #   st.write(raw_text)
      # "application/pdf"
      st.write(type(csv_file))
      df=pd.read_csv(csv_file)
      st.dataframe(df)
  elif choice == "Multiple CSV":
    st.subheader("Multiple CSV")
    csv_files = file_uploads(file_types=['csv'], multiple=True, label="Upload Multiple CSV", folder_path="./" )
    st.write(type(csv_files))
  else:
    st.subheader("About")
