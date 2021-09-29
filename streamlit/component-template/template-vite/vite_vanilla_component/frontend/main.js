import { Streamlit } from "streamlit-component-lib"
import G6 from '@antv/g6'

let selectedNode = null
let graph = null

const span = document.body.appendChild(document.createElement("span"))
const textNode = span.appendChild(document.createTextNode(""))
const button = span.appendChild(document.createElement("button"))
button.textContent = "Click Me!"

let numClicks = 0
let isFocused = false
button.onfocus = function() { isFocused = true }
button.onblur = function() { isFocused = false }
button.onclick = function() {
  numClicks += 1
  Streamlit.setComponentValue({ numClicks, selectedNode })
}

function onRender(event) {
  console.log('RENDER EVENT', Date.now()) //  current status... of numClicks and selectedNode...
  const data = event.detail
  if (data.theme) {
    const borderStyling = `1px solid var(${
      isFocused ? "--primary-color" : "gray"
    })`
    button.style.border = borderStyling
    button.style.outline = borderStyling
  }
  button.disabled = data.disabled
  let name = data.args["name"]
  textNode.textContent = `Hello, ${name}! ` + String.fromCharCode(160)

  let nodes = data.args["nodes"]
  let edges = data.args["edges"]
  const gdata = {
    edges: [],
    nodes: []
  };
  gdata.nodes = nodes
  gdata.edges = edges  
  G6.Util.processParallelEdges(gdata.edges);

  let config = data.args["config"]
  const container = document.body.appendChild(document.createElement("div"))
  container.setAttribute('id', 'container');

  if (!graph) {
    config.width = document.getElementById('container').scrollWidth;
    config.height = document.getElementById('container').scrollHeight || 500;
  
    graph = new G6.Graph(config)

    // graph events handling
    graph.on('edge:mouseenter', ({item}) => graph.setItemState(item, 'active', true))
    graph.on('edge:mouseleave', ({item}) => graph.setItemState(item, 'active', false))
    graph.on('edge:click', ({item}) => graph.setItemState(item, 'selected', true))
    graph.on('node:click', (evt) => {
      const { item } = evt
      graph.getNodes().forEach((node) => graph.clearItemStates(node))
      graph.setItemState(item, 'selected', true)
      const { id, label } =  item._cfg.model
      selectedNode = { id, label } // ${id} ${label}`
    })
    graph.on('canvas:click', (evt) => {
      selectedNode = null
      graph.getEdges().forEach((edge) => graph.clearItemStates(edge))
      graph.getNodes().forEach((node) => graph.clearItemStates(node))
    })
  }
  graph.data(gdata);
  graph.render();
  if (selectedNode) { // highlight node based on label
    const foundNode = graph.getNodes().find((node) => node._cfg.model.label === selectedNode.label)
    if (foundNode) graph.setItemState(foundNode, 'selected', true)
  }

  Streamlit.setFrameHeight()
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight()
