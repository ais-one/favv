<template>
  <a-result title="Callback...">
    <template #extra>
      <p>HASH = {{ hash }}</p>
      <a-button v-if="hash" @click="proceed">Proceed</a-button>
    </template>
  </a-result>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { INITIAL_SECURE_PATH } from '/config.js'

export default {
  setup(props, context) {
    const route = useRoute()
    const router = useRouter()
    const store = useStore()

    const hash = ref('')

    // onUnmounted(() => console.log('signIn unmounted'))
    onMounted(async () => {
      console.log('calback mounted!', route.hash) // deal with hashes here if necessary
      hash.value = route.hash
      // 1. verify and add user
      // 2. set token
      // 3. push to dashboard or show error message
    })

    const proceed = async () => {
      await store.dispatch('doLogin', 'Demo User')
      // router.push(INITIAL_SECURE_PATH) // will be done in router auth guard
    }

    return {
      hash,
      proceed
    }
  }
}
</script>
