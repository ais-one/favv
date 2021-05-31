<template>
  <a-layout>
    <a-back-top />
    <a-layout-sider v-model:collapsed="collapsed" :trigger="null" collapsible :collapsedWidth="0">
      <div class="logo" :style="`background-image: url(${constants.LOGO_RECT_URL});`" />
      <a-menu theme="dark" mode="inline" v-model:selectedKeys="selectedKeys">
        <template v-for="route in mappedRoutes">
          <a-sub-menu v-if="route.submenu" :key="route.submenu" :title="toPascalCase(route.submenu)">
            <a-menu-item v-for="menu in subMenus[route.submenu]" :key="menu.path" @click="$router.push(menu.path)">{{ menu.name }}</a-menu-item>
          </a-sub-menu>
          <a-menu-item v-else :key="route.path" @click="$router.push(route.path)">{{ route.name }}</a-menu-item>
        </template>
        <a-menu-item key="6" @click="logout">{{ constants.LOGOUT_TEXT}}</a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="background: #fff; padding: 0">
        <menu-unfold-outlined v-if="collapsed" class="trigger" @click="() => (collapsed = !collapsed)" />
        <menu-fold-outlined v-else class="trigger" @click="() => (collapsed = !collapsed)" />
        <span>{{ constants.TITLE }}</span>
      </a-layout-header>
      <a-layout-content :style="{ margin: '16px 12px', padding: '16px', background: '#fff', minHeight: 'calc(100vh - 96px)' }">
        <!--
        <a-breadcrumb style="margin: 8px 0">
          <a-breadcrumb-item>Home</a-breadcrumb-item><a-breadcrumb-item>Dashboard</a-breadcrumb-item>
        </a-breadcrumb>
        -->
        <router-view :key="$route.fullPath"></router-view>
      </a-layout-content>
      <!-- <a-layout-footer style="text-align: center">Ant Design ©2021</a-layout-footer> -->
    </a-layout>
  </a-layout>
</template>
<script>

import { onMounted, onUnmounted, onBeforeUnmount, ref, reactive } from 'vue'
import { useStore } from 'vuex'
// import { useRouter } from 'vue-router'
import { MenuUnfoldOutlined, MenuFoldOutlined } from '@ant-design/icons-vue'
import { CONSTANTS, ROUTES, ON_LOGIN, ON_LOGOUT } from '/config.js'

export default {
  components: { MenuUnfoldOutlined, MenuFoldOutlined },
  setup(props, context) {
    const constants = ref(CONSTANTS)
    const store = useStore()
    // const router = useRouter()
    const mappedRoutes = reactive([])
    const subMenus = reactive({})

    const toPascalCase = (str) => {
      str = str.replace(/-\w/g,(x) => ` ${x[1].toUpperCase()}`)
      return str[0].toUpperCase() + str.substring(1,str.length)
    }

    onMounted(async () => {
      console.log('SECURE mounted!')
      ROUTES.filter(route => route.meta.layout === 'layout-secure').forEach(route => {
        const submenu = route.path.split('/').length === 3 ? route.path.split('/', 2)[1] : '' // 2 or 3 only
        if (submenu) {
          if (!subMenus[submenu]) { // first time
            subMenus[submenu] = []
            mappedRoutes.push({
              name: route.name, path: route.path, submenu: submenu
            })
          }
          subMenus[submenu].push({ // add
            name: route.name, path: route.path
          })
        } else {
          mappedRoutes.push({
            name: route.name, path: route.path, submenu: ''
          })
        }
      })
      if (ON_LOGIN) ON_LOGIN()
    })
    onUnmounted(() => {
      console.log('SECURE unmounted')
    })
    onBeforeUnmount(() => {
      if (ON_LOGOUT) ON_LOGOUT()
    })

    const logout = async () => await store.dispatch('doLogin', null)

    return {
      constants,
      logout,
      selectedKeys: ref([]),
      collapsed: ref(false),
      mappedRoutes,
      subMenus,
      toPascalCase
    }
  }
}
</script>

<style>
.trigger {
  font-size: 18px;
  line-height: 64px;
  padding: 0 24px;
  cursor: pointer;
  transition: color 0.3s;
}

.trigger:hover {
  color: #1890ff;
}

.logo {
  height: 32px;
  background: rgba(255, 255, 255, 0.3);
  margin: 16px;
}

.site-layout .site-layout-background {
  background: #fff;
}
</style>