import { Streamlit } from 'streamlit-component-lib'
import { traverseJson } from '@es-labs/esm/util'
import G6 from '@antv/g6'

let key = ""
let selectedNodes = []
let selectedEdges = []
let graph = null

window.stProps = {
  key: () => key,
  Streamlit: () => Streamlit,
  G6: () => G6,
  graph: () => graph,
}

function onRender(event) {
  console.log('RENDER EVENT', Date.now())
  const data = event.detail
  const options = data.args["options"] || {
    selectNodes: 3, // 0, 1, n
    selectEdges: 3, //0, 1, n
    clickClearAll: false, // clear all nodes if clicking on canvas
  }
  key = data.args["key"]
  const gdata = { }
  gdata.nodes = data.args["nodes"] || []
  gdata.edges = data.args["edges"] || []
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
  G6.Util.processParallelEdges(gdata.edges)

  if (!graph) {
    let config = data.args["config"]

    traverseJson(config, (val) => {
      try {
        const json = JSON.parse(val)
        if (json && json.length && json[0] === '__#fn#__') {
          json.shift()
          val = new Function( ...json )
        }
      } catch(e) {
      }
      return val
    })

    // console.log('config', config)

    const container = document.body.appendChild(document.createElement("div"))
    container.setAttribute('id', 'container')
  
    if (!config.plugins) config.plugins = []

    const toolbar = new G6.ToolBar({
      // https://github.com/antvis/G6/blob/master/packages/plugin/src/toolBar/index.ts
      getContent: () => {
        return `
          <ul class='g6-component-toolbar'>
            <li code='realZoom'>
              <svg class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" width="20" height="24">
                <path d="M384 320v384H320V320h64z m256 0v384H576V320h64zM512 576v64H448V576h64z m0-192v64H448V384h64z m355.968 576H92.032A28.16 28.16 0 0 1 64 931.968V28.032C64 12.608 76.608 0 95.168 0h610.368L896 192v739.968a28.16 28.16 0 0 1-28.032 28.032zM704 64v128h128l-128-128z m128 192h-190.464V64H128v832h704V256z"></path>
              </svg>
            </li>
            <li code='autoZoom'>
              <svg class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" width="20" height="24">
                <path d="M684.288 305.28l0.128-0.64-0.128-0.64V99.712c0-19.84 15.552-35.904 34.496-35.712a35.072 35.072 0 0 1 34.56 35.776v171.008h170.944c19.648 0 35.84 15.488 35.712 34.432a35.072 35.072 0 0 1-35.84 34.496h-204.16l-0.64-0.128a32.768 32.768 0 0 1-20.864-7.552c-1.344-1.024-2.816-1.664-3.968-2.816-0.384-0.32-0.512-0.768-0.832-1.088a33.472 33.472 0 0 1-9.408-22.848zM305.28 64a35.072 35.072 0 0 0-34.56 35.776v171.008H99.776A35.072 35.072 0 0 0 64 305.216c0 18.944 15.872 34.496 35.84 34.496h204.16l0.64-0.128a32.896 32.896 0 0 0 20.864-7.552c1.344-1.024 2.816-1.664 3.904-2.816 0.384-0.32 0.512-0.768 0.768-1.088a33.024 33.024 0 0 0 9.536-22.848l-0.128-0.64 0.128-0.704V99.712A35.008 35.008 0 0 0 305.216 64z m618.944 620.288h-204.16l-0.64 0.128-0.512-0.128c-7.808 0-14.72 3.2-20.48 7.68-1.28 1.024-2.752 1.664-3.84 2.752-0.384 0.32-0.512 0.768-0.832 1.088a33.664 33.664 0 0 0-9.408 22.912l0.128 0.64-0.128 0.704v204.288c0 19.712 15.552 35.904 34.496 35.712a35.072 35.072 0 0 0 34.56-35.776V753.28h170.944c19.648 0 35.84-15.488 35.712-34.432a35.072 35.072 0 0 0-35.84-34.496z m-593.92 11.52c-0.256-0.32-0.384-0.768-0.768-1.088-1.088-1.088-2.56-1.728-3.84-2.688a33.088 33.088 0 0 0-20.48-7.68l-0.512 0.064-0.64-0.128H99.84a35.072 35.072 0 0 0-35.84 34.496 35.072 35.072 0 0 0 35.712 34.432H270.72v171.008c0 19.84 15.552 35.84 34.56 35.776a35.008 35.008 0 0 0 34.432-35.712V720l-0.128-0.64 0.128-0.704a33.344 33.344 0 0 0-9.472-22.848zM512 374.144a137.92 137.92 0 1 0 0.128 275.84A137.92 137.92 0 0 0 512 374.08z"></path>
              </svg>
            </li>
            <li code='sendData' style="width: 56px;border: 1px;">
              <svg class="svg-icon" viewBox="0 0 20 20" width="20" height="24" style="vertical-align: middle;">
                <path d="M17.218,2.268L2.477,8.388C2.13,8.535,2.164,9.05,2.542,9.134L9.33,10.67l1.535,6.787c0.083,0.377,0.602,0.415,0.745,0.065l6.123-14.74C17.866,2.46,17.539,2.134,17.218,2.268 M3.92,8.641l11.772-4.89L9.535,9.909L3.92,8.641z M11.358,16.078l-1.268-5.613l6.157-6.157L11.358,16.078z"></path>
              </svg> Send
            </li>
          </ul>
        `;
      },
      handleClick: (code, _graph) => {
        switch (code) {
          case 'realZoom':
            _graph.zoomTo(1);
            break
          case 'autoZoom':
            _graph.fitView([20, 20]);
            break
          case 'sendData':
            console.log(key, selectedNodes, selectedEdges)
            Streamlit.setComponentValue({ key, selectedNodes, selectedEdges })
            break
          default:
        }
      }
    })
    config.plugins = [toolbar]
    config.enabledStack = false

    // NOSONAR
    // window.outerHeight
    // window.outerWidth
    // if (config?.defaultEdge?.style?.endArrow) {
    //   config.defaultEdge.style.endArrow = {
    //     path: G6.Arrow.triangle(10, 15, 20),
    //     d: 20,
    //     fill: '#f00',
    //   }
    // }

    console.log(window.innerWidth, window.innerHeight, window.outerHeight, document.getElementById('container').scrollHeight)
    config.width = window.innerWidth // NOSONAR config.width || window.innerWidth || document.getElementById('container').scrollWidth;
    config.height = config.height || document.getElementById('container').scrollHeight || 500
    config.layout.width = config.width 
    config.layout.height = config.height
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


    graph.on('canvas:contextmenu', (evt) => {
      console.log('ssss', evt)
      // Streamlit.setComponentValue({ selectedNodes, selectedEdges })
    })

    graph.on('canvas:click', (evt) => {
      if (options.clickClearAll) {
        selectedNodes = []
        selectedEdges = []
        graph.getEdges().forEach((edge) => graph.clearItemStates(edge))
        graph.getNodes().forEach((node) => graph.clearItemStates(node))  
      }
    })
    
    if (options['canvas:dblclick']) {
      const fn = new Function(...options['canvas:dblclick'])
      graph.on('canvas:dblclick', fn)
    }

  } else {
    // TBD set new width and height
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
