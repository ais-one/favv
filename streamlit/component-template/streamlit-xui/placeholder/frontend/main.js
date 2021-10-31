import { Streamlit } from "streamlit-component-lib"

const defaultStyle = /*css*/`
body {
  margin: 0;
}

#app {
  margin: 0;
}
`

let rendered = false

function onRender(event) {
  // if (rendered) return // why does render fire twice ? It also happens in example code
  // else rendered = true
  console.log('Render', event)

  // const styles = data.args["styles"] || defaultStyle
  // const styleTag = document.createElement('style') // hopefully this does not keep getting created...
  // styleTag.innerText = styles
  // document.head.appendChild(styleTag)

  const root = document.createElement('div')
  root.classList.add('sidenav')
  const h1 = root.createElement('hi')
  h1.innerHTML = 'Hello World'
  document.getElementById('app').appendChild(root)
  
  //* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
  // var dropdown = document.getElementsByClassName("dropdown-btn");
  // console.log('dropdown', dropdown)
  // var i;
  Streamlit.setFrameHeight()
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight()
