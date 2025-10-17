<script>
    export default {
        name: 'App'
    }
</script>

<template>
    <router-view />

    <nav>
        <router-link to="/">Home</router-link>
        <router-link to="/policy">Privacy Policy</router-link>
        <router-link to="/auth">Login</router-link>
    </nav>
</template>

<style>
    nav{
        display: none;
    }
</style>