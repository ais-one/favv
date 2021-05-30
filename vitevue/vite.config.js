// import.meta is undefined, process.env is not populated with custom values
import vue from '@vitejs/plugin-vue'
// import envVite from './src/.env.vite.js'
const path = require('path')

export default ({ command, mode }) => {
  const envVite = require('dotenv').config({ path: path.join(__dirname, '.env.' + mode) }).parsed
  console.log(envVite)
  return {
    base: envVite.WEB_BASEPATH || '/', // set to '/vite' for dev:build, '/' otherwise
    // build: {
    //   rollupOptions: { // vite 2
    //     external: [
    //       // 'react' // ignore react stuff
    //     ]
    //   }  
    // },
    // optimizeDeps: {
    //   include: [
    //   ]
    // },
    plugins: [
      vue({
        template: {
          compilerOptions: {
            isCustomElement: tag => tag.startsWith('bwc-') || tag.startsWith('vcxwc-')
          }
        }
      })
    ],
    resolve: {
      // alias: [
      //     {find: "@", replacement: path.resolve(__dirname, 'src')}
      // ],
      alias: {
        '~': path.resolve(__dirname, 'src')
      }
    },
    server: {
      port: envVite.DEV_SERVER_PORT || 8080,
    }
  }
}
