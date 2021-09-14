import streamlit as st
# import pandas as pd
import os

def save_uploadedfile(uploadedfile):
  with open(os.path.join("tempDir",uploadedfile.name),"wb") as f:
    f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to tempDir".format(uploadedfile.name))

def page_uploadfile_csv():
  datafile = st.file_uploader("Upload CSV",type=['csv'])
  if datafile is not None:
    file_details = {"FileName":datafile.name,"FileType":datafile.type}
    # df  = pd.read_csv(datafile)
    # st.dataframe(df)
    save_uploadedfile(datafile)

def page_uploadfile_image():
  image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
  if image_file is not None:
    file_details = {"FileName": image_file.name,"FileType": image_file.type}
    # st.write(file_details)
    # img = load_image(image_file)
    # st.image(img,height=250,width=250)
    save_uploadedfile(datafile)


# uploadedfiles = st.file_uploader(“Upload PDF”, type=[‘pdf’], accept_multiple_files=True)
# for file in uploadedfiles:
# if uploadedfiles is not None:
# save_uploadedfile(file)