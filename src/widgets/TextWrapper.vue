<script setup>
    defineProps({
        msg: String,
    })
</script>

<template>
    <div class="flex justify-center mt-[5rem]">
        <div class="flex boxShadow py-4 px-8 rounded-xl">
            <p class="text-sm max-w-[33rem] whiteSpace">{{msg}}</p>
        </div>
    </div>
</template>

<style>
    .whiteSpace{
        white-space: pre-line;
    }
</style>