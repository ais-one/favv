<template>
  <div class="super-center-parent" >
    <a-result :title="constants.TITLE" :sub-title="constants.SUBTITLE">
      <template #icon>
        <a-image :height="constants.LOGO_HEIGHT" :src="constants.LOGO_URL" />
      </template>
      <template #extra>
        <a-button :type="constants.LOGIN_TYPE" size="large" html-type="button" @click="login">{{ constants.LOGIN_TEXT }}</a-button>
      </template>
    </a-result>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import { VITE_CALLBACK_URL, CONSTANTS, INITIAL_SECURE_PATH } from '/config.js'

export default {
  setup(props, context) {
    const constants = ref(CONSTANTS)
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
    })
    // onBeforeUnmount(() => { })

    const _setUser = async () => {
      await store.dispatch('doLogin', 'Demo User') // store user
    }

    const login = async () => {
      _setUser()
      loading.value = false
      router.push(INITIAL_SECURE_PATH)
    }

    return {
      // samlLogin,
      login,
      errorMessage,
      loading,
      callbackUrl,
      constants,
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
