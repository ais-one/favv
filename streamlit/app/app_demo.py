import streamlit as st
import pandas as pd
from file_utils import file_uploads, FileDownloader

from logger import logger

def app_run():
  logger.info('In Demos')
  st.title("Demos")

  with st.expander('File Demos'):
    st.subheader("CSV Files")
    menu = ["Single CSV", "Multiple CSV", "About"]
    choice = st.selectbox("Select CSV File Upload Mode", menu)
    if choice == "Single CSV":
      csv_file = file_uploads(multiple=False, label="Input Single CSV and get data" )
      if csv_file is not None:
        # if csvFile.type == "text/plain"
        #   raw_text = str(csvFile.read(), "utf-8")
        #   st.write(raw_text)
        # "application/pdf"
        st.write(type(csv_file))
        df = pd.read_csv(csv_file)
        st.dataframe(df)
        if st.button("Get CSV for download"):
          FileDownloader(data=df.to_csv(), file_ext='csv').download()
    elif choice == "Multiple CSV":
      csv_files = file_uploads(file_types=['csv'], multiple=True, label="Upload Multiple CSV", folder_path="./" )
      st.write(type(csv_files))
    else:
      st.subheader("About")
    st.subheader("Text Download")
    my_text = st.text_area("Enter Message for download")
    if st.button("Create Download"):
      st.write(my_text)
      FileDownloader(my_text).download()

  with st.expander('Forms Demo'):
    mc1, mc2 = st.columns(2)
    # first form - use with
    with mc1:
      st.subheader("Form 1")
      with st.form(key='form1'):
        firstname = st.text_input("Firstname")
        lastname = st.text_input("Lastname")
        dob = st.date_input("Date of Birth")
        submit_button = st.form_submit_button(label='Sign Up')
      if submit_button:
        st.success("Hello {}. Your account is created".format(firstname))
    # second form
    with mc2:
      st.subheader("Form 2")
      form2 = st.form(key='form2')
      username = form2.text_input("Username")
      jobtype = form2.selectbox("Job", ["Dev", "Data Scientist", "UX Designer"])
      submit_button2 = form2.form_submit_button("Login")
      if submit_button2:
        st.success("{}. Logged In".format(username))

    # 3rd form
    st.subheader("Form 3 - columnar")
    with st.form(key='form3'):
      c1, c2, c3 = st.columns([3, 2, 1])
      with c1:
        amount = st.number_input("Hourly Rate in $")
      with c2:
        hours_per_week = st.number_input("Hours Per Week", 1,120)
      with c3:
        st.text("Salary")
        submit_salary = st.form_submit_button(label="Calculate")
    if submit_salary:
      daily = [amount * 8]
      weekly = [amount * hours_per_week]
      df = pd.DataFrame({ 'hourly': amount, 'daily': daily, 'weekly': weekly })
      st.dataframe(df)
