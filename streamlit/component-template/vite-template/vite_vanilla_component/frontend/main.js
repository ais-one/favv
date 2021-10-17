import { Streamlit } from "streamlit-component-lib"
import G6 from '@antv/g6'

let selectedNodes = []
let selectedEdges = []
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
  Streamlit.setComponentValue({ numClicks, selectedNodes, selectedEdges })
}

function onRender(event) {
  console.log('RENDER EVENT', Date.now())
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

  const options = data.args["options"] || {
    selectNodes: 3, // 0, 1, n
    selectEdges: 3, //0, 1, n
    clickClearAll: false, // clear all nodes if clicking on canvas
  }
  let nodes = data.args["nodes"]
  let edges = data.args["edges"]
  const gdata = {
    edges: [],
    nodes: []
  };
  gdata.nodes = nodes
  gdata.edges = edges
  gdata.edges.forEach((edge) => {
    if (edge.type === 'loop') {
      edge.style = {
        endArrow: {
          path: G6.Arrow.vee(10, 15, 0),
          d: 0,
          stroke: '#0c0',
        }
      }
    } else {
      if (edge.return) {
        edge.style = {
          endArrow: {
            path: G6.Arrow.triangle(10, 15, 20),
            d: 20,
            fill: '#f00',
          }
        }  
      } else {
        edge.style = {
          endArrow: {
            path: G6.Arrow.triangle(10, 15, 20),
            d: 20,
            fill: '#00f',
          }
        }
      }
    }
  })
  G6.Util.processParallelEdges(gdata.edges);

  let config = data.args["config"]
  const container = document.body.appendChild(document.createElement("div"))
  container.setAttribute('id', 'container');

  if (!graph) {
    console.log('w h', config.width, config.height)
    config.width = config.width || document.getElementById('container').scrollWidth;
    config.height = config.height || document.getElementById('container').scrollHeight || 500;

    console.log('w h', config.width, config.height)
    // if (config?.defaultEdge?.style?.endArrow) {
    //   config.defaultEdge.style.endArrow = {
    //     path: G6.Arrow.triangle(10, 15, 20),
    //     d: 20,
    //     fill: '#f00',
    //   }
    // }
    graph = new G6.Graph(config)

    // graph events handling
    graph.on('edge:mouseenter', ({item}) => graph.setItemState(item, 'active', true))
    graph.on('edge:mouseleave', ({item}) => graph.setItemState(item, 'active', false))

    graph.on('edge:click', ({item}) => {
      graph.setItemState(item, 'selected', true)
      if (options.selectEdges) {
        const selected = item._cfg.states.includes('selected')
        if (options.selectEdges > 1) { // multiple
          graph.setItemState(item, 'selected', selected ? false : true)
          if (selected) { // remove
            selectedEdges = selectedEdges.filter((node) => node.id !== item._cfg.model.id)
          } else { // add
            selectedEdges.push(item._cfg.model)
          }
        } else { // single
          graph.getNodes().forEach((node) => graph.clearItemStates(node)) // unselect the rest
          selectedEdges = []
          if (!selected) {
            graph.setItemState(item, 'selected', true) // select this node
            selectedEdges = [item._cfg.model] 
          }
        }
      }
    })

    graph.on('node:click', ({item}) => {
      if (options.selectNodes) {
        const selected = item._cfg.states.includes('selected')
        if (options.selectNodes > 1) { // multiple
          graph.setItemState(item, 'selected', selected ? false : true)
          if (selected) { // remove
            selectedNodes = selectedNodes.filter((node) => node.id !== item._cfg.model.id)
          } else { // add
            selectedNodes.push(item._cfg.model)
          }
        } else { // single
          graph.getNodes().forEach((node) => graph.clearItemStates(node)) // unselect the rest
          selectedNodes = []
          if (!selected) {
            graph.setItemState(item, 'selected', true) // select this node
            selectedNodes = [item._cfg.model] 
          }
        }
      }
    })

    graph.on('canvas:click', (evt) => {
      if (options.clickClearAll) {
        selectedNodes = []
        selectedEdges = []
        graph.getEdges().forEach((edge) => graph.clearItemStates(edge))
        graph.getNodes().forEach((node) => graph.clearItemStates(node))  
      }
    })
  }
  graph.data(gdata);
  graph.render();

  selectedNodes.forEach((selectedNode) => { // highlight nodes
    const foundNode = graph.getNodes().find((_node) => _node._cfg.model.label === selectedNode.label)
    if (foundNode) graph.setItemState(foundNode, 'selected', true)
  })

  selectedEdges.forEach((selectedEdge) => { // highlight edges
    const foundNode = graph.getNodes().find((_node) => _node._cfg.model.label === selectedEdge.label)
    if (foundNode) graph.setItemState(foundNode, 'selected', true)
  })

  Streamlit.setFrameHeight()
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight()

// IN PROGRESS keep state of expanders using session state, keep the result of the calculate after each submission
// TBD Server side caching? limited memory - cache data at server... (check on memory usage and limitations)
// TBD any multiple tabs available on streamlit? able to have expander only show 1 at a time?
