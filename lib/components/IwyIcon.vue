<script setup>
  const props = defineProps({
    name: String,
    look: {
      type: String,
      default: "regular",
      validator(value) {
        return ["regular", "solid"].includes(value);
      }
    },
    size: {
      type: String,
      default: "24px"
    },
    fill: {
      type: String,
      default: "black"
    }
  });
</script>

<template>
  <component :fill="props.fill" :height="size" :is="`iwy-icon-${props.name}-${props.look}-svg`" />
</template>

<style scoped>
</style>
