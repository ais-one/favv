// import.meta is undefined, process.env is not populated with custom values
import vue from '@vitejs/plugin-vue'
import envVite from './src/.env.vite.js'
const path = require('path')

// module.exports = {
export default {
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
    port: 8080,
  }
}
