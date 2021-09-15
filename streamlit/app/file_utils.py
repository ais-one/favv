import streamlit as st
# import pandas as pd
import os

def save_uploaded_file(uploaded_file, folder_path):
  uploaded = None
  try:
    # uploaded_file has name, type, getbuffer()
    with open(os.path.join(folder_path, uploaded_file.name),"wb") as f:
      f.write(uploaded_file.getbuffer())
      # return st.success("Saved File:{} to folder_path".format(uploaded_file.name))
      uploaded = True
  except IOError:
    uploaded = False
  return uploaded

# CSV - pandas
# df = pd.read_csv(result)
# st.dataframe(df)
# IMAGE - PIL, OpenCV
# st.write(file_details)
# img = load_image(image_file)
# st.image(img,height=250,width=250)
# Docx - docx2txt, python-docx
# PDF - PyPDF2, Pdfplumber, textract
# TXT - st.write(file.read())
def file_uploads(label="Upload File", file_types=['csv'], multiple=False, folder_path=""):
  test = None
  result = st.file_uploader(label, type=file_types, accept_multiple_files=multiple) # csv, txt, pdf, docx, png, jpg, jpeg, etc...
  if folder_path and result is not None:
    if multiple==True:
      for file in result:
        test = save_uploaded_file(file, folder_path)
    else:
      test = save_uploaded_file(result, folder_path)
  return result
