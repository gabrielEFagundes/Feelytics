<script setup>
    import { ref } from 'vue';
    import axios from 'axios';

    const placeholders = [
        "What topic today?",
        "What you're thinking today?",
        "What would you like to know?",
        "What do you say about 'Cute Puppies'?",
        "Let's rock those ideas!",
        "Share your ideas!"
    ];
    const placeholderValue = Math.floor(Math.random() * placeholders.length);

    const chosenValue = placeholders[placeholderValue];

    const search = ref('');
    const sendRequest = () => {
        axios.post('http://127.0.0.1:5000/api/search', {
            request: search.value,
        }) // TODO: cors not allowing to send the request, solve that
        .catch((e) => {
            console.error(e);
        });
    }
</script>

<template>
    <div class="flex flex-col items-center mt-[10rem]">
            <h1 class="text-[#FFA64D] text-6xl">Reddit</h1>
        </div>
        <div class="mx-[20rem]">
            <div class="mt-[5rem] flex flex-col">
                <input type="text" :placeholder="chosenValue" class="bg-neutral-900 px-10 py-3 rounded-4xl focusOutline" v-model="search">
                <div class="flex flex-row-reverse">
                    <button @click="sendRequest" class="relative bottom-9 right-4 text-neutral-500 btnFocus">-></button>
                </div>
            </div>
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