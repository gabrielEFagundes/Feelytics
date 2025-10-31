<script setup>
    defineProps({
        data: String,
    })
</script>

<template>
    <div class="bg-neutral-800 border border-[#FFA64D] border-2 rounded-2xl py-3 pb-6 px-4 max-h-full">
        <div class="flex justify-between">
            <p>&#x2726; AI resume</p>
            <div class="flex gap-1">
                <div class="rounded-full bg-green-500 macOsStyledDots"></div>
                <div class="rounded-full bg-yellow-500 macOsStyledDots"></div>
                <div class="rounded-full bg-red-500 macOsStyledDots"></div>
            </div>
        </div>
        <div class="flex">
            <p class="mr-3">>_</p>
            <p>{{ data }}</p>
        </div>
    </div>
</template>

<style scoped>
    .macOsStyledDots{
        content: '';
        width: 10px;
        height: 10px;
    }
</style>