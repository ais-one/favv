import { Streamlit } from "streamlit-component-lib"

const devMode = import.meta.env.MODE === 'development'

const defaultStyle = /*css*/`
body {
  margin: 0;
}

#app {
  margin: 0;
}

/* Fixed sidenav, full height */
.sidenav {
  font-family: Arial;
  height: 100%;
  width: 100%;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #111;
  overflow-x: hidden;
  /* padding-top: 20px; */
}

/* Style the sidenav links and the dropdown button */
.sidenav a, .dropdown-btn {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  font-size: 20px;
  color: #818181;
  display: block;
  border: none;
  background: none;
  width:100%;
  text-align: left;
  cursor: pointer;
  outline: none;
}

/* On mouse-over */
.sidenav a:hover, .dropdown-btn:hover {
  color: #f1f1f1;
}

/* Main content */
.main {
  margin-left: 200px; /* Same as the width of the sidenav */
  font-size: 20px; /* Increased text to enable scrolling */
  padding: 0px 10px;
}

/* Add an active class to the active dropdown button */
.sidenav a.selected {
  background-color: green;
  color: white;
}

/* Dropdown container (hidden by default). Optional: add a lighter background color and some left padding to change the design of the dropdown content */
.dropdown-container {
  display: none;
  background-color: #262626;
  padding-left: 8px;
}

/* Optional: Style the caret down icon */
.fa-caret-down {
  float: right;
  padding-right: 8px;
}
`

let rendered = false
let heightReduce = 280
let heightFactor = 1.0

function setHeight(height) {
  height = height * heightFactor
  let menuVisibleHeight = height - heightReduce
  if (menuVisibleHeight < 0) menuVisibleHeight = heightReduce
  document.getElementById('app').style.height = menuVisibleHeight + 'px'
  Streamlit.setFrameHeight()
}

function returnState(selected, opened) {
  Streamlit.setComponentValue({ selected, opened })
}

function onRender(event) {
  // NOSONAR
  // if (rendered) return // why does render fire twice ? It also happens in example code
  // else rendered = true
  devMode && console.log('Render', event, import.meta.env.MODE)

  const data = event.detail
  const items = data.args["items"]
  let selected = data.args["selected"] || ''
  let opened = data.args["opened"] || []
  const { customStyle = null, OPEN_ICON = '>+', CLOSE_ICON = '>-', HEIGHT_REDUCE = 280, HEIGHT_FACTOR = 1.0 } = data.args["options"]
  heightReduce = HEIGHT_REDUCE
  heightFactor = HEIGHT_FACTOR
  const closeIcon = CLOSE_ICON
  const openIcon = OPEN_ICON 

  const styles = customStyle || defaultStyle
  const styleTag = document.createElement('style') // hopefully this does not keep getting created...
  styleTag.innerText = styles
  document.head.appendChild(styleTag)

  const root = document.createElement('div')
  root.classList.add('sidenav')

  function setupMenuItem(menuItem) {
    const aTag = document.createElement('a') // to refactor duplicate
    if (selected === menuItem.label) aTag.classList.add('selected')
    aTag.onclick = () => {
      selected = menuItem.label // No need to update style
      returnState(selected, opened)
    }
    aTag.innerHTML = menuItem.label
    return aTag
  }

  items.forEach((item) => {
    if (item.children) { // menu group
      const btnTag = document.createElement('button')
      btnTag.classList.add('dropdown-btn')
      // btnTag.innerHTML = item.label

      const divContainerDd = document.createElement('div')
      divContainerDd.classList.add('dropdown-container')

      if (opened.includes(item.label)) {
        divContainerDd.style.display = "block"
        btnTag.innerHTML = closeIcon + item.label
      } else {
        btnTag.innerHTML = openIcon + item.label 
      }

      btnTag.onclick = (e) => {
        const dropdownContent = divContainerDd
        if (dropdownContent.style.display === "block") {
          opened = opened.filter(open => item.label !== open)
          btnTag.innerHTML = openIcon + item.label 
          dropdownContent.style.display = "none"
        } else {
          opened.push(item.label)
          btnTag.innerHTML = closeIcon + item.label
          dropdownContent.style.display = "block"
        }
      }
      root.appendChild(btnTag)
      item.children.forEach((child) => {
        const childATag = setupMenuItem(child)
        divContainerDd.appendChild(childATag)
      })
      root.appendChild(divContainerDd)
    } else { // menu item
      const aTag = setupMenuItem(item)
      root.appendChild(aTag)
    }
  })

  document.getElementById('app').appendChild(root)

  setHeight(window.outerHeight)
  document.getElementById('app').style.overflow = 'auto'
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

// https://github.com/streamlit/streamlit/issues/3889