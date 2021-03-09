<template>
  <div class="super-center-parent" >
    <a-result title="Verification" sub-title="In progress...">
      <template #icon>
        <a-image :height="constants.LOGO_HEIGHT" :src="constants.LOGO_URL" />
      </template>
      <template #extra>
        <a-button :type="constants.LOGIN_TYPE" size="large" html-type="button" @click="backToLogin">Back To Login</a-button>
      </template>
    </a-result>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useStore } from 'vuex'
import { useRoute, useRouter } from 'vue-router'
import { CONSTANTS } from '/config.js'

export default {
  setup(props, context) {
    const constants = ref(CONSTANTS)
    const store = useStore()
    const route = useRoute()
    const router = useRouter()

    const loading = ref(false)
    const errorMessage = ref('')

    // onUnmounted(() => console.log('signIn unmounted'))
    onMounted(async () => {
      console.log('calback mounted!', route.hash) // deal with hashes here if necessary
      // 1. verify and add user
      // 2. set token
      // 3. push to dashboard or show error message
      errorMessage.value = ''
    })
    // onBeforeUnmount(() => { })

    // const _setUser = async () => {
    //   await store.dispatch('doLogin', 'Demo User') // store user
    // }

    const backToLogin = async () => {
      // _setUser()
      // loading.value = false
      // router.push('/dashboard')
      router.push('/') //  looks like a job for jwtserver...!
    }

    return {
      backToLogin,
      errorMessage,
      loading,
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
