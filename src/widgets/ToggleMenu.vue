<script setup>
    function showMenu(){
        document.getElementById('menu')
            .classList.toggle('showing');
    }

    document.addEventListener('click', function(event){
        const menu = document.getElementById('menu');
        const button = event.target;
        if(!menu.contains(event.target) && button.textContent !== '+'){
            menu.classList.remove('showing');
        }
    });
</script>

<template>
    <div class="flex flex-col">
        <button class="text-sm" @click="showMenu">+</button>
        <div class="lg:hidden" id="menu">
            <div class="bg-black boxShadow absolute ml-[-5rem] mt-2 p-4 rounded-xl">
                <ul class="flex flex-col gap-3">
                    <a href="#">Reddit</a>
                    <a href="#">Instagram</a>
                    <a href="#">X</a>
                    <a href="#">Facebook</a>
                    <a href="#">Snapchat</a>
                    <a href="#">Tiktok</a>
                    <a href="#">Discord</a>
                </ul>
            </div>
        </div>
    </div>
</template>

<style scoped>
    #menu{
        opacity: 0;
        transition: opacity 0.4s ease-in-out;
    }

    #menu.showing{
        opacity: 1;
        transition: opacity 0.4s ease-in-out;
    }
</style>