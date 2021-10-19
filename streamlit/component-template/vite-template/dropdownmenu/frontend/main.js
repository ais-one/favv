import { Streamlit } from "streamlit-component-lib"

/*
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
*/

let rendered = false

function setHeight(height) {
  let menuVisibleHeight = height - 280
  if (menuVisibleHeight < 0) menuVisibleHeight = 240
  document.getElementById('app').style.height = menuVisibleHeight + 'px'
  Streamlit.setFrameHeight()
}

function returnItem(item) {
  Streamlit.setComponentValue({ item })
}

function onRender(event) {
  if (rendered) return
  else rendered = true

  console.log('Render', event)

  // TBD create based on table NOSONAR
  const data = event.detail
  const items = data.args["items"]
  // const styles = data.args["styles"]

  const root = document.createElement('div')
  root.classList.add('sidenav')
  items.forEach((item) => {
    if (item.children) {
      const btnTag = document.createElement('button')
      btnTag.classList.add('dropdown-btn')
      btnTag.innerHTML = item.label

        //   <div class="dropdown-container">
      const divContainerDd = document.createElement('div')
      divContainerDd.classList.add('dropdown-container')

      btnTag.onclick = (e) => {
        // const dropdownContent = btnTag.nextElementSibling
        const dropdownContent = divContainerDd
        if (dropdownContent.style.display === "block") {
          dropdownContent.style.display = "none";
        } else {
          dropdownContent.style.display = "block";
        }
      }
      root.appendChild(btnTag)
        item.children.forEach((child) => {
        const childATag = document.createElement('a')
        childATag.onclick = () => returnItem(child.label)
        childATag.innerHTML = child.label
        divContainerDd.appendChild(childATag)
      })
      root.appendChild(divContainerDd)
    } else {
      const aTag = document.createElement('a')
      aTag.onclick = () => returnItem(item.label)
      aTag.innerHTML = item.label
      root.appendChild(aTag)
    }
  })

  document.getElementById('app').appendChild(root)

  setHeight(window.outerHeight)
  document.getElementById('app').style.overflow = 'auto'
  
  //* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
  // var dropdown = document.getElementsByClassName("dropdown-btn");
  // console.log('dropdown', dropdown)
  // var i;
  Streamlit.setFrameHeight()
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight()

// https://stackoverflow.com/questions/25098021/securityerror-blocked-a-frame-with-origin-from-accessing-a-cross-origin-frame
let timeoutId = null
window.parent.addEventListener('resize', function() {
  clearTimeout(timeoutId)
  timeoutId = setTimeout(() => setHeight(window.outerHeight), 500)
})
// window.parent.addEventListener('resize', () => console.log('aaaaaa'))

// Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
// https://github.com/streamlit/streamlit/issues/3889