<template>
  <a-result title="Verification" sub-title="In progress...">
    <template #extra>
      <!-- <p>HASH = {{ hash }}</p> -->
      <!-- <a-button v-if="hash" @click="proceed">Proceed</a-button> -->
      <a-button v-if="!hash" type="default" size="large" html-type="button" @click="backToLogin">Back To Login</a-button>
    </template>
  </a-result>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useStore } from 'vuex'
import { INITIAL_PUBLIC_PATH } from '/config.js'
import { VITE_VERIFY_URL } from '/config.js'
import * as http from '~/http.js'

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
      if (route.hash) {
        try {
          const hash = route.hash.split('#')[1]
          const tokens = hash.split(',')
          http.setToken(tokens[0]) // set the tokens
          http.setRefreshToken(tokens[1])
          if (VITE_VERIFY_URL) {
            // call the verify url
          }
          await store.dispatch('doLogin', hash) // push to dashboard
        } catch (e) {
          alert('Sign In Error') // or show error
        }
      }
    })

    const proceed = async () => await store.dispatch('doLogin', hash.value) // router.push(INITIAL_SECURE_PATH) // will be done in router auth guard
    const backToLogin = async () => router.push(INITIAL_PUBLIC_PATH) //  looks like a job for an auth server...!

    return {
      backToLogin,
      hash,
      proceed,
    }
  }
}
</script>
