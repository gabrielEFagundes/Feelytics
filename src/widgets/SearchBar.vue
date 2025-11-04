<script setup>
    import { apiSearchRequest } from '../utils/data-analysis/general/apiSendingHook';
    import { useRedditStore } from '../../stores/redditStore';

    const placeholders = [
        "What topic today?",
        "What you're thinking today?",
        "What would you like to know?",
        "Get ready for some data!",
        "Let's rock those ideas!",
        "Share your ideas!"
    ];
    const placeholderValue = Math.floor(Math.random() * placeholders.length);

    const chosenValue = placeholders[placeholderValue];
    const redditStore = useRedditStore();

    const { search, sendRequest, loading } = apiSearchRequest();

    const handleSearch = async () => {
        const data = await sendRequest()

        if(data != null && data.length > 0){
            const cleanData = JSON.parse(data);

            redditStore.setRedditData(cleanData);
        }
    }
</script>

<template>
    <div class="flex flex-col items-center mt-[10rem]">
            <h1 class="text-[#FFA64D] text-6xl">Reddit</h1>
        </div>
        <div class="lg:mx-[20rem]">
            <div class="mt-[5rem] flex flex-col">
                <input type="text" :placeholder="chosenValue" class="bg-neutral-900 px-10 py-3 rounded-4xl focusOutline text-sm lg:text-base" v-model="search">
                <div class="flex flex-row-reverse">
                    <button @click="handleSearch" class="relative bottom-8.5 lg:bottom-9 right-4 text-neutral-500 btnFocus">-></button>
                </div>
            </div>
            <div v-if="loading" class="text-center">Now Loading...</div>
        </div>
</template>

<style scoped>
    .focusOutline{
        outline: transparent;
    }

    .focusOutline:focus{
        outline: 1px solid #FFA64D;
        transition: 0.2s ease-in-out;
    }

    .btnFocus:hover{
        color: #FFA64D;
        transition: 0.3s ease-in-out;
        cursor: pointer;
    }
</style>