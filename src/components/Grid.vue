<script setup>
    import Card from '../widgets/Card.vue';
</script>

<template>
    <div class="grid lg:grid-cols-3 justify-items-center mt-[5rem] gap-[5rem]">
        <Card img="https://avatars.githubusercontent.com/u/216910125?v=4" 
        name="Luís Felipe Flores Olegar" 
        role="Developer & Design Analyst"
        biografy="Hi! I am Luís, I'm 18 years old and I chose this field because I want to gain enough knowledge to create a game."
        github="https://github.com/olegar724" />
        
        <Card img="https://avatars.githubusercontent.com/u/185841300?v=4"
        name="Gabriel Ehrat Fagundes"
        role="Lead Developer & Designer"
        biografy="Hey, I'm Gabriel, a passionate and maddend programmer that loves technology and innovation. I'm leading this awesome team!"
        github="https://github.com/gabrielEFagundes" />
        
        <Card img="https://avatars.githubusercontent.com/u/213849483?v=4"
        name="Renan Guilherme Ballock"
        role="Data Analyst & System Analyst"
        biografy="Hello! My name is Renan, I love technologies and am a very curious person. I'm working on keeping the data and system safe!"
        github="https://github.com/renanballock" />
    </div>
</template>