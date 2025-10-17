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
    .boxShadow{
        box-shadow: rgba(255, 255, 255, 0.25) 0px 1px 70px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;
    }

    .whiteSpace{
        white-space: pre-line;
    }
</style>