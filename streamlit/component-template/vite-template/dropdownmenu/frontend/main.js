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

// button.onclick = function() {
//   Streamlit.setComponentValue({ numClicks, selectedNodes, selectedEdges })
// }
let rendered = false
function onRender(event) {
  // console.log(document.body.scrollHeight, document.body.clientHeight)
  // console.log('zzzzzzzzzzz', parent.document.body.scrollHeight)
  // document.body.height = 1000
  // document.getElementById('app').height = '500px'

  if (rendered) return
  else rendered = true

  console.log('Render')

  // TBD create based on table NOSONAR
  const data = event.detail
  const items = data.args["items"]

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
        childATag.onclick = console.log('child', child.label)
        childATag.innerHTML = child.label
        divContainerDd.appendChild(childATag)
      })
      root.appendChild(divContainerDd)
    } else {
      const aTag = document.createElement('a')
      aTag.onclick = console.log('parent', item.label)
      aTag.innerHTML = item.label
      root.appendChild(aTag)
    }
  })

  document.getElementById('app').appendChild(root)

  document.getElementById('app').style.height = '240px' // TBD set the height here
  document.getElementById('app').style.overflow = 'auto'
  // document.getElementById('app').style.height = '500px'

  // const div = document.createElement('span')
  // div.innerHTML = `
  //   <div class="sidenav">
  //   <a href="#about">About</a>
  //   <a href="#services">Services</a>
  //   <a href="#clients">Clients</a>
  //   <a href="#contact">Contact</a>
  //   <button class="dropdown-btn">Dropdown V</button>
  //   <div class="dropdown-container">
  //     <a href="#">Link 1</a>
  //     <a href="#">Link 2</a>
  //     <a href="#">Link 3</a>
  //   </div>
  //   <a href="#contact">Search</a>
  //   </div>
  // `
  // document.getElementById('app').appendChild(div)
  
  //* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content - This allows the user to have multiple dropdowns without any conflict */
  // var dropdown = document.getElementsByClassName("dropdown-btn");
  // console.log('dropdown', dropdown)
  // var i;

  // for (i = 0; i < dropdown.length; i++) {
  //   dropdown[i].addEventListener("click", function () {
  //     console.log('click click')
  //     this.classList.toggle("active");
  //     var dropdownContent = this.nextElementSibling;
  //     if (dropdownContent.style.display === "block") {
  //       dropdownContent.style.display = "none";
  //     } else {
  //       dropdownContent.style.display = "block";
  //     }
  //   });
  // }

  Streamlit.setFrameHeight()
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight()
