<script setup>
    defineProps({
        postTitle: String,
        postAuthor: String,
        postBody: String,
        postScore: Number,
    })
</script>

<template>
    <div class="border border-2 border-[#FFA64D] rounded-2xl py-10 px-5">
        <p class="text-xl">{{ postTitle }}</p>
        <p class="text-sm mb-2">{{ postAuthor }}</p>
        <p class="text-neutral-400 mb-3">{{ postBody }}</p>
        <div class="flex items-center gap-1">
            <p class="text-[#FFA64D] text-3xl">&#x21e7;</p>
            <p class="text-neutral-500 text-sm">{{ postScore }}</p>
        </div>
    </div>
</template>