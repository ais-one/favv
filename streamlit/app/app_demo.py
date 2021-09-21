import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
from file_utils import file_uploads, FileDownloader
import streamlit.components.v1 as components

from logger import logger
import os

# https://docs.streamlit.io/en/stable/publish_streamlit_components.html
parent_dir = os.path.dirname(os.path.abspath(__file__))
build_dir = os.path.join(parent_dir, "component-template", "template", "my_component" , "frontend" ,"build")
_my_component = components.declare_component("my_component", path=build_dir)
# _my_component = components.declare_component( "my_component", url="http://localhost:3001") # dev


def app_run():
  logger.info('In Demos')
  st.title("Demos")

  rv1 = _my_component(key="c1", greeting="6Hello", name="Aaron") # create your component
  st.write(rv1)
  rv2 = _my_component(key="c2", greeting="5Ola!", name="Gong")
  st.write(rv2)

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

  with st.expander('Streamlit Components Static'):
    stc.html("<p style='color: red;'>Streamlit is Awesome</p>")
    st.markdown("<p style='color: blue;'>Streamlit is Awesome Markdown</p>", unsafe_allow_html=True)

  stc.html("""
<style>
* {box-sizing: border-box}
body {font-family: Verdana, sans-serif; margin:0}
.mySlides {display: none}
img {vertical-align: middle;}

/* Slideshow container */
.slideshow-container {
  max-width: 1000px;
  position: relative;
  margin: auto;
}

/* Next & previous buttons */
.prev, .next {
  cursor: pointer;
  position: absolute;
  top: 50%;
  width: auto;
  padding: 16px;
  margin-top: -22px;
  color: white;
  font-weight: bold;
  font-size: 18px;
  transition: 0.6s ease;
  border-radius: 0 3px 3px 0;
  user-select: none;
}

/* Position the "next button" to the right */
.next {
  right: 0;
  border-radius: 3px 0 0 3px;
}

/* On hover, add a black background color with a little bit see-through */
.prev:hover, .next:hover {
  background-color: rgba(0,0,0,0.8);
}

/* Caption text */
.text {
  color: #f2f2f2;
  font-size: 15px;
  padding: 8px 12px;
  position: absolute;
  bottom: 8px;
  width: 100%;
  text-align: center;
}

/* Number text (1/3 etc) */
.numbertext {
  color: #f2f2f2;
  font-size: 12px;
  padding: 8px 12px;
  position: absolute;
  top: 0;
}

/* The dots/bullets/indicators */
.dot {
  cursor: pointer;
  height: 15px;
  width: 15px;
  margin: 0 2px;
  background-color: #bbb;
  border-radius: 50%;
  display: inline-block;
  transition: background-color 0.6s ease;
}

.active, .dot:hover {
  background-color: #717171;
}

/* Fading animation */
.fade {
  -webkit-animation-name: fade;
  -webkit-animation-duration: 1.5s;
  animation-name: fade;
  animation-duration: 1.5s;
}

@-webkit-keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

@keyframes fade {
  from {opacity: .4} 
  to {opacity: 1}
}

/* On smaller screens, decrease text size */
@media only screen and (max-width: 300px) {
  .prev, .next,.text {font-size: 11px}
}
</style>


<body>

<div class="slideshow-container">

<div class="mySlides fade">
  <div class="numbertext">1 / 3</div>
  <img src="https://www.w3schools.com/howto/img_nature_wide.jpg" style="width:100%">
  <div class="text">Caption Text</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">2 / 3</div>
  <img src="https://www.w3schools.com/howto/img_snow_wide.jpg" style="width:100%">
  <div class="text">Caption Two</div>
</div>

<div class="mySlides fade">
  <div class="numbertext">3 / 3</div>
  <img src="https://www.w3schools.com/howto/img_mountains_wide.jpg" style="width:100%">
  <div class="text">Caption Three</div>
</div>

<a class="prev" onclick="plusSlides(-1)">&#10094; AAAA</a>
<a class="next" onclick="plusSlides(1)">&#10095; BBBB</a>

</div>
<br>

<div style="text-align:center">
  <span class="dot" onclick="currentSlide(1)"></span> 
  <span class="dot" onclick="currentSlide(2)"></span> 
  <span class="dot" onclick="currentSlide(3)"></span> 
</div>

<script>
var slideIndex = 1;
showSlides(slideIndex);

function plusSlides(n) {
  showSlides(slideIndex += n);
}

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}    
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";  
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active";
}
</script>

</body>
    """)