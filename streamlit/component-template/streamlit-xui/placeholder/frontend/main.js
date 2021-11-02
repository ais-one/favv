import { Streamlit } from "streamlit-component-lib"

const defaultStyle = /*css*/`
body {
  margin: 0;
}

#app {
  margin: 0;
}
`

function onRender(event) {
  const root = document.createElement('div')
  root.innerHTML = 'Placeholder TBD'
  document.getElementById('app').appendChild(root)
  Streamlit.setFrameHeight()
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight()
