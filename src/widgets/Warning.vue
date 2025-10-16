<script setup>
  defineProps({
    err: String
  })
</script>

<template>
    <div class="border border-red-500 bg-red-950 rounded-md p-3 m-4">
        <p class="text-red-500">{{ err }}</p>
    </div>
</template>