<script setup>
    import Navbar from '../../components/Navbar.vue';
    import Footer from '../../components/Footer.vue';

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
</script>

<template>
    <Navbar />

    <main class="p-5 mb-[15rem]">
        <!-- it's supposed to be 10rem, BUT IT DOESN'T WORK??? -->
        <div class="flex flex-col items-center mt-[9rem]">
            <h1 class="text-[#FFA64D] text-6xl">Reddit</h1>
        </div>
        <div class="mx-[20rem]">
            <div class="mt-[5rem] flex flex-col">
                <input type="text" :placeholder="chosenValue" class="bg-neutral-900 px-10 py-3 rounded-4xl focusOutline">
            </div>
        </div>
    </main>

    <Footer />
</template>

<style>
    .focusOutline{
        outline: transparent;
    }

    .focusOutline:focus{
        outline: 1px solid #FFA64D;
        transition: 0.2s ease-in-out;
    }
</style>