import { openWs, closeWs } from './hookFns.js'

export default {
  CONSTANTS: {
    TITLE: 'Dashboard App',
    SUBTITLE: 'Your one-stop web portal',
    LOGO_HEIGHT: 150,
    LOGO_URL: 'https://via.placeholder.com/150x150.png?text=A+Logo',
    LOGO_RECT_URL: 'https://via.placeholder.com/168x32.png?text=A+Logo',
    LOGIN_TEXT: 'Login',
    BUTTON_TYPE: 'default',
    LOGOUT_TEXT: 'Logout',
  },
  ROUTES: [
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
