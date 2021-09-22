<template>
  <div>
    <h1>{{ msg }}</h1>
    <button @click="doClick">click</button>
    <p>Count {{ count }}</p>
  </div>
</template>

<script>
import { Streamlit } from 'streamlit-component-lib'
import { ref, onMounted } from 'vue'

export default {
  setup(props, context) {
    const msg = ref('No Msg')
    const count = ref(0)

    const doClick = () => {
      count.value += 1

      Streamlit.setComponentValue(count.value)
    }

    const onRender = (event) => {
      // Get the RenderData from the event
      const data = event.detail

      // // Maintain compatibility with older versions of Streamlit that don't send
      // // a theme object.
      // if (data.theme) {
      //   // Use CSS vars to style our button border. Alternatively, the theme style
      //   // is defined in the data.theme object.
      //   const borderStyling = `1px solid var(${
      //     isFocused ? "--primary-color" : "gray"
      //   })`
      //   button.style.border = borderStyling
      //   button.style.outline = borderStyling
      // }

      // // Disable our button if necessary.
      // button.disabled = data.disabled

      // RenderData.args is the JSON dictionary of arguments sent from the
      // Python script.
      msg.value = `Hello, ` + data.args['name']

      // // Show "Hello, name!" with a non-breaking space afterwards.
      // textNode.textContent = `Hello, ${name}! ` + String.fromCharCode(160)

      // We tell Streamlit to update our frameHeight after each render event, in
      // case it has changed. (This isn't strictly necessary for the example
      // because our height stays fixed, but this is a low-cost function, so
      // there's no harm in doing it redundantly.)
      Streamlit.setFrameHeight()
    }

    onMounted(() => {
      // Attach our `onRender` handler to Streamlit's render event.
      Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)

      // Tell Streamlit we're ready to start receiving data. We won't get our
      // first RENDER_EVENT until we call this function.
      Streamlit.setComponentReady()

      // Finally, tell Streamlit to update our initial height. We omit the
      // `height` parameter here to have it default to our scrollHeight.
      Streamlit.setFrameHeight()
    })

    return {
      doClick,
      count,
      msg
    }
  }
}

</script>


<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
</style>
