// import envjs from './src/.env.js'
// let obj = await import(`./src/.env.localdev.js`)

//console.log('import.meta.env', import.meta.env)
const { MODE, VITE_APPNAME } = import.meta.env

const setupMod = await import('./src/' + VITE_APPNAME + '/setup.js')
const setup = setupMod.default
// console.log('setup', setup)

const envjsMod = await import('./src/' + VITE_APPNAME + '/.env.' + MODE + `.js`)
const envjs = envjsMod.default
// console.log('envjs', envjs)

export const {
  // VITE_HTTPONLY_TOKEN = false, // true, // NOTUSED... replaced by WITH_CREDENTIALS
  // From setup.js
  CONSTANTS = setup.CONSTANTS,
  ROUTES = setup.ROUTES,
  INITIAL_SECURE_PATH = setup.INITIAL_SECURE_PATH,
  VERSION = setup.VERSION,

  // From .env.[MODE].js
  WITH_CREDENTIALS = envjs.WITH_CREDENTIALS || 'same-origin', // same-origin, include = cors
  CALLBACK_URL = envjs.CALLBACK_URL,
  API_URL = envjs.API_URL,
  WS_URL = envjs.WS_URL,

  // from vite.config.js base property
  BASE_URL 
} = import.meta.env

// PAGESIZE: process.env.VUE_APP_PAGESIZE || 4,
// PAGESIZE_OPTS: process.env.VUE_APP_PAGESIZE_OPTS && process.env.VUE_APP_PAGESIZE_OPTS.length ? JSON.parse(process.env.VUE_APP_PAGESIZE_OPTS) : [4, 8, 10],
// APP_VERSION: '0.4.6',
