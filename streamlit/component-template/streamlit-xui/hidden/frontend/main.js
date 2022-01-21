import { Streamlit } from "streamlit-component-lib"

function onRender(event) {
  Streamlit.setComponentValue(event.detail.args['value'])
  // Streamlit.setFrameHeight()
}
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
// Streamlit.setFrameHeight()
