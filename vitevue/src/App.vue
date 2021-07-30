<template>
  <div>
    <component :is="$route.meta.layout || 'layout-public'"></component>
  </div>
</template>

<script>
import { LAYOUTS } from '../config.js'
// import { computed } from 'vue'
// import { useStore } from 'vuex'

export default {
  components: {
    'layout-public': LAYOUTS.layoutPublic,
    'layout-secure': LAYOUTS.layoutSecure
  },
  setup(props, context) {
    // const store = useStore()
    // const storeUser = computed(() => store.state.user)
    // const logout = async () => {
    //   await store.dispatch('doLogin', { forced: true })
    // }
    return {
      // storeUser // computed
    }
  }
}
</script>
