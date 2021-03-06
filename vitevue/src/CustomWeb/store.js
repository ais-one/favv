import { defineStore } from 'pinia'

export const useMainStore = defineStore({
  // name of the store
  // it is used in devtools and allows restoring state
  id: 'main',
  // a function that returns a fresh state
  state: () => ({
    counter: 5,
    form: {
      delivery: true,
      date1: '2021-04-01'
    }
  }),
  // optional getters
  getters: {
    doubleCount() {
      return this.counter * 2
    },
    doubleCountPlusOne() {
      return this.doubleCount * 2 + 1 // use getters in other getters
    },
  },
  // optional actions
  actions: {
    reset() {
      this.counter = 0 // `this` is the store instance
    },
  },
})
