<template>
  <div v-if="visible" class="banner">
    Warning!
  </div>
</template>

<script>
export default {
  data() {
    return {
      visible: true
    };
  },
  mounted() {
    setTimeout(() => {
      this.visible = false;
    }, 1500);
  }
};
</script>
