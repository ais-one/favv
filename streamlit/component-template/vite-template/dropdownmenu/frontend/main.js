import { Streamlit } from "streamlit-component-lib"

// button.onclick = function() {
//   Streamlit.setComponentValue({ numClicks, selectedNodes, selectedEdges })
// }

const span = document.body.appendChild(document.createElement("span"))
const textNode = span.appendChild(document.createTextNode(""))
const button = span.appendChild(document.createElement("button"))
button.textContent = "Click Me!"

function onRender(event) {
  // NOSONAR
  // const data = event.detail
  // let name = data.args["name"]
  console.log('XXXXXXXXXXXXXXXXXXXXXXXXXX')

  const div = document.createElement('span')
  div.innerHTML = `
    <div class="sidenav">
    <a href="#about">About</a>
    <a href="#services">Services</a>
    <a href="#clients">Clients</a>
    <a href="#contact">Contact</a>
    <button class="dropdown-btn">Dropdown V</button>
    <div class="dropdown-container">
      <a href="#">Link 1</a>
      <a href="#">Link 2</a>
      <a href="#">Link 3</a>
    </div>
    <a href="#contact">Search</a>
    </div>
  `
  document.getElementById('app').appendChild(div)
  
  //* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
  var dropdown = document.getElementsByClassName("dropdown-btn");
  var i;

  for (i = 0; i < dropdown.length; i++) {
    dropdown[i].addEventListener("click", function () {
      this.classList.toggle("active");
      var dropdownContent = this.nextElementSibling;
      if (dropdownContent.style.display === "block") {
        dropdownContent.style.display = "none";
      } else {
        dropdownContent.style.display = "block";
      }
    });
  }

  Streamlit.setFrameHeight()
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight()
