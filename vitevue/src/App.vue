<template>
  <div>
    <component :is="$route.meta.layout || 'layout-public'"></component>
  </div>
</template>

<script>
// :key="$route.fullPath" // this is causing problems
import layoutPublic from './layouts/Public.vue' // store.state.user determines if public or secure
import layoutSecure from './layouts/Secure.vue'

import { computed } from 'vue'
import { useStore } from 'vuex'

export default {
  components: {
    'layout-public': layoutPublic,
    'layout-secure': layoutSecure
  },
  setup(props, context) {
    const store = useStore()
    const storeUser = computed(() => store.state.user)
    const logout = async () => {
      await store.dispatch('doLogin', { forced: true })
    }
    return {
      storeUser // computed
    }
  }
}
</script>
