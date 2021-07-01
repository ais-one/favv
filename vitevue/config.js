//console.log('import.meta.env', import.meta.env)
import setup from './apploader.js'
// const setup = await import('./src/' + VITE_APPNAME + '/setup.js').default // await causes problems

export const {
  MODE,
  // from vite.config.js base property
  BASE_URL,

  // From .env.[MODE]
  VITE_WITH_CREDENTIALS = import.meta.env.VITE_WITH_CREDENTIALS || 'same-origin', // same-origin, include = cors
  VITE_CALLBACK_URL,
  VITE_API_URL, // make an alias
  VITE_WS_URL,
  // HTTPONLY_TOKEN = false, // true, // NOTUSED... replaced by VITE_WITH_CREDENTIALS
  VITE_SSO_URL,
  VITE_VERIFY_URL,

  // From setup.js
  CONSTANTS = setup.CONSTANTS,
  ROUTES = setup.ROUTES,
  INITIAL_SECURE_PATH = setup.INITIAL_SECURE_PATH,
  VERSION = setup.VERSION,
  ON_LOGIN = setup.ON_LOGIN,
  ON_LOGOUT = setup.ON_LOGOUT,
} = import.meta.env
