<script setup>
  defineProps({
      link: String,
      msg: String,
      event: {
        type: String,
        default: null
      },
  })
</script>

<template>
    <button class="p-[0.5rem] rounded-xl" @click="$emit(event)">
        <a :href="link" target="_blank">{{ msg }}</a>
    </button>
</template>

<style scoped>
button{
    box-shadow: rgba(255, 255, 255, 0.25) 0px 50px 100px -20px, rgba(255, 255, 255, 0.3) 0px 30px 60px -30px, rgba(255, 255, 255, 0.35) 0px -2px 6px 0px inset;
    transition: all 0.3s ease-in-out;
}
button:hover{
    box-shadow: rgba(255, 255, 255, 0.4) 0px 50px 100px -20px, rgba(255, 255, 255, 0.45) 0px 30px 60px -30px, rgba(255, 255, 255, 0.5) 0px -2px 6px 0px inset;
    transform: scale(1.05);
}
</style>