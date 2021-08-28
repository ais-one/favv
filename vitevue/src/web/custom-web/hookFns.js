import { useStore } from 'vuex'
import { useMainStore } from './store.js'
import { ws } from '~/services.js'
const { VITE_WS_URL } = import.meta.env

const wsMsgHandler = (e) => {
  const mainStore = useMainStore()
  console.log('ws onmessage', e.data)
  mainStore.message = e.data
}

export const openWs = () => {
  if (VITE_WS_URL) {
    // TBD get initial data
    const store = useStore()
    ws.setOptions({ endpoint: `${VITE_WS_URL}/${store.state.user}` })
    ws.connect()
    ws.setMessage(wsMsgHandler)
  }
}

export const closeWs = () => {
  // TBD clear data
  if (VITE_WS_URL) ws.close()
}
