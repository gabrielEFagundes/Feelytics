<script setup>
    defineProps({
        title: String,
        data: String,
    })
</script>

<template>
    <div class="border border-2 border-[#FFA64D] rounded-2xl py-10 px-5">
        <p class="mb-4">{{ title }}</p>
        <p class="text-4xl text-[#FFA64D] text-center">{{ data }}</p>
        <slot />
    </div> 
</template>