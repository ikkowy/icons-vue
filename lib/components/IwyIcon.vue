<script setup>
  import { IconIndex } from "../index.js";

  import { computed } from "vue";

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

  const _is = computed(() => {
    const name = (props.name in IconIndex) ? props.name : "unknown";
    const look = IconIndex[name].look.includes(props.look) ? props.look : IconIndex[name].look[0];
    return `iwy-icon-${name}-${look}-svg`;
  });
</script>

<template>
  <component :fill="props.fill" :height="size" :is="_is" />
</template>

<style scoped>
</style>
