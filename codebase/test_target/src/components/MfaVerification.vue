<template>
  <div class="mfa-verify">
    <input v-model="code" />
    <button @click="verify">Verify</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      code: ''
    };
  },
  methods: {
    async verify() {
      // Direct axios call instead of central API client
      const res = await axios.post('/api/v1/mfa/verify', { code: this.code });
      return res.data;
    }
  }
};
</script>
