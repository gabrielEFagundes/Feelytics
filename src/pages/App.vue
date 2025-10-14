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
    </nav>
</template>