<template>
  <div class="super-center-parent" >
    <a-result title="Dashboard App" sub-title="Your one-stop web portal">
      <template #icon>
        <a-image :height="150" src="https://via.placeholder.com/150x150.png?text=A+Logo" />
      </template>
      <template #extra>
        <a-button type="default" size="large" html-type="button" @click="login">Login</a-button>
      </template>
    </a-result>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import { VITE_CALLBACK_URL, VITE_SSO_URL } from '/config.js'

export default {
  setup(props, context) {
    const store = useStore()
    const route = useRoute()
    const router = useRouter()

    const loading = ref(false)
    const errorMessage = ref('')

    const callbackUrl = VITE_CALLBACK_URL

    // onUnmounted(() => console.log('signIn unmounted'))
    onMounted(async () => {
      // console.log('signIn mounted!', route.hash) // deal with hashes here if necessary
      errorMessage.value = ''
      loading.value = false

      if (VITE_SSO_URL) {
        window.location.assign(VITE_SSO_URL + '/login')
      }
    })
    // onBeforeUnmount(() => { })

    const _setUser = async () => {
      await store.dispatch('doLogin', 'Demo User') // store user
    }

    const login = async () => {
      _setUser()
      loading.value = false
      // router.push(INITIAL_SECURE_PATH) // will be done in router auth guard
    }

    return {
      // samlLogin,
      login,
      errorMessage,
      loading,
      callbackUrl,
    }
  }
}
</script>

<style>
.super-center-parent {
  display: grid;
  place-items: center;
  width: 100vw;
  height: 100vh;
}
</style>
