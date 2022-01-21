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
      const data = event.detail
      count.value = data.args['default']

      msg.value = `Hello, ` + data.args['name']
      Streamlit.setFrameHeight()
    }

    onMounted(() => {
      Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
      Streamlit.setComponentReady()
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