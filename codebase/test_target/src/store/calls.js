import { defineStore } from 'pinia';

export const useCallsStore = defineStore('calls', {
  state: () => ({
    activeCalls: [],
    isMuted: false
  }),
  actions: {
    setMuted(val) {
      this.isMuted = val;
    }
  }
});
