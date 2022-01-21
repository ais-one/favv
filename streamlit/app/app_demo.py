import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
from file_utils import file_uploads, FileDownloader
import streamlit.components.v1 as components

import textwrap # SVG testing
import base64

from logger import logger
import os

## CUSTOM COMPONENTS

# https://docs.streamlit.io/en/stable/publish_streamlit_components.html
# base_dir = os.path.dirname(os.path.abspath(__file__))
# _vanilla_component = components.declare_component("vanilla_component", os.path.join(base_dir, "..", "component-template", "streamlit-vite", "vanilla_component" , "frontend" ,"dist"))
# _vue_component = components.declare_component("vue_component", path=os.path.join(base_dir, "..", "component-template", "streamlit-vite", "vue_component" , "frontend" ,"dist"))

## METHODS
def form3_callback():
  if 'my_amount' in st.session_state:
    st.write(st.session_state.my_amount)
  if 'my_hours_per_week' in st.session_state:
    st.write(st.session_state.my_hours_per_week)

## APP RUN
def app_run():
  logger.info('In Demos')
  st.title("Demos")

  config = {
    "container": "container",
    "fitCenter": True,
    "linkCenter": True,
    "defaultNode": {
      "type": "circle",
      "size": [40],
      "color": "#5B8FF9",
      "style": { "fill": "#9EC9FF", "lineWidth": 3 },
      "labelCfg": { "style": { "fill": "#000", "fontSize": 14 } }
    },
    "defaultEdge": {
      "type": "quadratic",
      "labelCfg": { "autoRotate": True, },
    },
    "modes": {
      "default": ["drag-canvas", "drag-node"],
    },
    "nodeStateStyles": {
      "hover": { "fillOpacity": 0.8 },
      "selected": { "lineWidth": 5 }
    }
  }

  nodes = [
    { "id": "node1", "x": 50, "y": 350, "label": "A", },
    { "id": "node2", "x": 250, "y": 150, "label": "B", },
    { "id": "node3", "x": 450, "y": 350, "label": "C", },
  ]
  edges = []

  for x in range(8):
    edges.append({ "source": "node1", "target": "node2", "label": f'{x}th edge of A-B', })
  for x in range(5):
    edges.append({ "source": "node2", "target": "node3", "label": f'{x}th edge of B-C', })

  # rv0 = g6(name="NameViteVanilla", config=config, nodes=nodes, edges=edges, key="c0")
  # st.write(rv0)

  # rv1 = _vue_component(key="cc1", name="ViteVue1", default=st.session_state.cc1) # create your component
  # st.write(rv1)
  # rv2 = _vanilla_component(key="cc2", name="ViteVanilla", default=st.session_state.cc2)
  # st.write(rv2)
  # rv3 = _vue_component(key="cc3", name="ViteVue2", default=st.session_state.cc3)
  # st.write(rv3)

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

  with st.expander('Forms Demo', expanded=False):
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
        amount = st.number_input("Hourly Rate in $", 0, 50000, key='my_amount', value=st.session_state.my_amount)
      with c2:
        hours_per_week = st.number_input("Hours Per Week", 1, 120, key='my_hours_per_week', value=st.session_state.my_hours_per_week)
      with c3:
        st.text("Salary")
        submit_salary = st.form_submit_button(label="Calculate", on_click=form3_callback)
    if submit_salary:
      daily = [amount * 8]
      weekly = [amount * hours_per_week]
      df = pd.DataFrame({ 'hourly': amount, 'daily': daily, 'weekly': weekly })
      st.dataframe(df)

  with st.expander('Cascading/Dependent Dropdown'):
    st.subheader("The Americas")

    list_americas = ["North America", "South America"]
    list_na = ["United States", "Canada"]
    list_sa = ["Brazil", "Argentina", "Chile"]

    map_americas = {
      "North America": list_na,
      "South America": list_sa
    }

    america = st.selectbox("Select Americas Region", list_americas)
    country_list = map_americas[america]

    country = st.selectbox("Select Country In Americas Region", country_list)

    if st.button("Selected Options"):
      st.write(america)
      st.write(country)

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

  # SVG Testing
  def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<div style="width:100%%;overflow:scroll;"><img src="data:image/svg+xml;base64,%s"/></div>' % b64
    st.write(html, unsafe_allow_html=True)

  def render_svg_example():
    # text_file = open("ud.svg", "r")
    # svg = text_file.read()
    # text_file.close()
    svg = """
        <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
            <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
        </svg>
    """
    st.write('## Rendering an SVG in Streamlit')
    # st.write('### SVG Input')
    # st.code(textwrap.dedent(svg), 'svg')
    st.write('### SVG Output')
    render_svg(svg)
  render_svg_example()
