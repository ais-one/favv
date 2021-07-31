import { createRouter, createWebHistory } from 'vue-router'
import store from './store.js'
import { BASE_URL, ROUTES, INITIAL_SECURE_PATH, INITIAL_PUBLIC_PATH } from '../config.js'

// const permissions = {
//   // g1 = route groups, g2 = user groups
//   // go through each route group... check if group matches [list of groups in user]
//   allowed: (g1, g2) => g1.find(x => g2.includes(x))
// }

// const routeGroups = {
//   // '/authors', '/categories', '/books', '/pages', '/books/:id/pages'
//   '/test': ['TestGroup'] //
// }

const authGuard = (to, from, next) => {
  // console.log('authGuard', store.state.user ? 'user' : 'anon', from.path, to.path)

  // TBD find users from localStorage? // potential security leak
  // const item = localStorage.getItem('session') // survive a refresh - POTENTIAL SECURITY RISK - TO REVIEW AND CHANGE USE HTTPONLY COOKIES
  // if (item) {
  //   const user = JSON.parse(item)
  //   if (user.verified) {
  //     store.commit('setUser', user) // need user.token only
  //   }
  // }

  const loggedIn = !!(store.state.user)
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth)

  // const { groups } = store.state.user
  // if (routeGroups[to.matched[0].path]) {
  //   let found = permissions.allowed(routeGroups[to.matched[0].path], groups.split(','))
  //   if (!found) {
  //     alert('Forbidden... Check Page Permissions')
  //     return next('/')
  //   }
  // }
  if (loggedIn === requiresAuth) {
    // console.log('logged in', loggedIn, requiresAuth)
    next()
  } else if (!loggedIn && requiresAuth) {
    next(INITIAL_PUBLIC_PATH)
  } else if (loggedIn && !requiresAuth) {
    next(INITIAL_SECURE_PATH)
  } else {
    // should not get here
    console.log('router should not get here', loggedIn, requiresAuth)
  }
}

for (let route of ROUTES) {
  route.beforeEnter = authGuard
  route.meta = { requiresAuth: true, layout: 'layout-secure' }
}

const routerHistory = createWebHistory(BASE_URL)
const router = createRouter({
  history: routerHistory,
  routes: [
    // public
    { path: '/', name: 'Home', component: () => import('./views/SignIn.vue') },
    { path: '/signin', name: 'SignIn', component: () => import('./views/SignIn.vue'), beforeEnter: authGuard, meta: { requiresAuth: false, layout: 'layout-public' } },
    { path: '/callback', name: 'Callback', component: () => import('./views/Callback.vue'), beforeEnter: authGuard, meta: { requiresAuth: false, layout: 'layout-public' } },

    ...ROUTES,

    // catchall
    { path: '/forbidden', name: 'Forbidden', component: () => import('./views/Forbidden.vue') },
    { path: '/:catchAll(.*)', name: 'catchAll', redirect: { name: 'SignIn' }, meta: { requiresAuth: false, layout: 'layout-public' } }
  ]
})

export default router
