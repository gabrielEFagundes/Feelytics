<script setup>
    import Navbar from '../../components/Navbar.vue';
    import Footer from '../../components/Footer.vue';
    import SearchBar from '../../widgets/SearchBar.vue';
</script>

<template>
    <Navbar />

    <main class="p-5 mb-[15rem]">
        <SearchBar />
    </main>

    <Footer />
</template>