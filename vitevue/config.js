// import envjs from './src/.env.js'
// let obj = await import(`./src/.env.localdev.js`)
const { MODE, VITE_APPNAME } = import.meta.env
let obj = await import('./src/' + VITE_APPNAME + '/.env.' + MODE + `.js`)
const envjs = obj.default
console.log('envjs', envjs, import.meta.env)

export const {
  // VITE_HTTPONLY_TOKEN = false, // true, // NOTUSED... replaced by WITH_CREDENTIALS
  // From .env.js
  WITH_CREDENTIALS = envjs.WITH_CREDENTIALS || 'same-origin', // same-origin, include = cors
  CALLBACK_URL = envjs.CALLBACK_URL,
  CONSTANTS = envjs.CONSTANTS,
  API_URL = envjs.API_URL,
  WS_URL = envjs.WS_URL,
  ROUTES = envjs.ROUTES,
  INITIAL_SECURE_PATH = envjs.INITIAL_SECURE_PATH,
  VERSION,

  // from vite.config.js base property
  BASE_URL 
} = import.meta.env

// PAGESIZE: process.env.VUE_APP_PAGESIZE || 4,
// PAGESIZE_OPTS: process.env.VUE_APP_PAGESIZE_OPTS && process.env.VUE_APP_PAGESIZE_OPTS.length ? JSON.parse(process.env.VUE_APP_PAGESIZE_OPTS) : [4, 8, 10],
// APP_VERSION: '0.4.6',
