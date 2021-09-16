import streamlit as st
import base64
import time
import os
TIME_FORMAT = time.strftime("%Y%m%d-%H%M%S")

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

class FileDownloader(object):
  def __init__(self, data, filename='myfile', file_ext='txt'):
    self.data = data
    self.filename = filename
    self.file_ext = file_ext
  def download(self):
    b64 = base64.b64encode(self.data.encode()).decode()
    fname = "{}_{}.{}".format(self.filename, TIME_FORMAT, self.file_ext)
    st.markdown("### Download File")
    href = f'<a href="data:file/{self.file_ext};base64,{b64}" download="{fname}">Download File</a>'
    st.markdown(href, unsafe_allow_html=True)
