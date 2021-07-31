import { openWs, closeWs } from './hookFns.js'

// :key="$route.fullPath" // this is causing problems
import layoutPublic from './layouts/Public.vue'
import layoutSecure from './layouts/Secure.vue'

export default {
  LAYOUTS: {
    layoutPublic,
    layoutSecure
  },
  ROUTES: [
    { path: '/forbidden', name: 'Forbidden', component: () => import('./views/Forbidden.vue') },
    { path: '/:catchAll(.*)', name: 'NotFound', component: () => import('./views/NotFound.vue') },
    // { path: '/:catchAll(.*)', name: 'catchAll', redirect: { name: 'SignIn' }, meta: { requiresAuth: false, layout: 'layout-public' } }
  ],
  PUBLIC_ROUTES: [
    { path: '/', name: 'Home', component: () => import('./views/SignIn.vue') },
    { path: '/signin', name: 'SignIn', component: () => import('./views/SignIn.vue') },
    { path: '/callback', name: 'Callback', component: () => import('./views/Callback.vue') },
  ],
  SECURE_ROUTES: [
    { path: '/dashboard', name: 'Dashboard', component: async () => await import('./Demo/Dashboard.vue') },

    // demo
    { path: '/demo/cnn', name: 'Demo Cnn', component: async () => await import('./Demo/DemoCnn.vue') },
    { path: '/demo/table', name: 'Demo Table', component: async () => await import('./Demo/DemoTable.vue') },
    { path: '/demo/tableapi', name: 'Demo Table API', component: async () => await import('./Demo/DemoTableApi.vue') },
    { path: '/demo/cascade', name: 'Demo Cascade', component: async () => await import('./Demo/Cascade.vue') },
    { path: '/demo/form', name: 'Demo Form', component: async () => await import('./Demo/DemoForm.vue') },
    { path: '/demo/card', name: 'Demo Card', component: async () => await import('./Demo/DemoCard.vue') },
    { path: '/demo/map', name: 'Demo Map', component: async () => await import('./Demo/DemoMap.vue') },
    { path: '/demo-charts/chart1', name: 'Demo Chart1', component: async () => await import('./Demo/DemoChart1.vue') },
    { path: '/demo-charts/chart2', name: 'Demo Chart2', component: async () => await import('./Demo/DemoChart2.vue') },

    // more demo
    { path: '/more-forms', name: 'Demo More Forms', component: async () => await import('./DemoMoreForms.vue') },
    { path: '/api-forms', name: 'Demo Forms (API)', component: async () => await import('./DemoApiForms.vue') },
  ],

  INITIAL_PUBLIC_PATH: '/signin',
  INITIAL_SECURE_PATH: '/dashboard',

  // log-in/logout hook
  ON_LOGIN: () => {
    openWs()
  },
  ON_LOGOUT: () => {
    closeWs()
  },

  VERSION: '0.0.2',
}
