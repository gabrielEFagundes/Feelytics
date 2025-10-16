<script setup>
  import firebase from 'firebase/compat/app';
  import { onBeforeUnmount } from 'vue';
  import { ref } from 'vue';

  const isLoggedIn = ref(false);
  const loggedUser = ref();
  const authListener = firebase.auth().onAuthStateChanged(function(user) {
    if(user){
        loggedUser.value = user;
        isLoggedIn.value = true;
    }
  })

  onBeforeUnmount(() => {
    authListener();
  })

  function signOut(){
    firebase.auth().signOut()
        .then(() => {
            isLoggedIn.value = false;
        })
        .catch((error) => {
            console.log(error.message);
        })
  }
</script>

<template>
    <section class="flex justify-evenly items-center mt-10 mb-2">
        <div class="logo">
            <a href="/home" class="font-size-md">🌀</a>
        </div>
        <div>
            <ul class="flex gap-[1.5rem]">
                <a href="#" class="reddit">Reddit</a>
                <a href="#" class="instagram">Instagram</a>
                <a href="#" class="x">X</a>
                <a href="#" class="facebook">Facebook</a>
                <a href="#" class="snapchat">Snapchat</a>
                <a href="#" class="tiktok">Tiktok</a>
                <a href="#" class="discord">Discord</a>
                <a href="#" class="selection">+</a>
            </ul>
        </div>
        <div>
            <span v-if="isLoggedIn"><button @click="signOut" class="selection text-red-500 cursor-pointer">Logout</button></span>
            <span v-else><a href="/auth" class="selection">Register</a></span>
        </div>
    </section>
    <div class="flex justify-center">
        <hr class="w-2/3 border-neutral-600">
    </div>
</template>

<style scoped>
.logo{
    transition: all 0.3s ease-in-out;
}
.logo:hover{
    transform: scale(1.2);
}
.font-size-md{
    font-size: 1.5rem;
}

.selection{
    transition: 0.4s ease-in-out;
}

.selection:hover{
    filter: drop-shadow(0 0 1rem #fff);
}

.reddit:hover{
    color: #FFA64D;
    transition: color ease-in-out;
}

.instagram:hover{
    -webkit-background-clip: text;
    background: linear-gradient(to right, #FB00FF, #FFCC00);
    background-clip: text;
    color: transparent;
    transition: color ease-in-out;
}

.x:hover{
    color: #999;
    transition: color ease-in-out;
}

.facebook:hover{
    color: #0084FF;
    transition: color ease-in-out;
}

.snapchat:hover{
    color: #FFDA0A;
    transition: color ease-in-out;
}

.tiktok:hover{
    -webkit-background-clip: text;
    background: linear-gradient(to right, #00D9FF, #FF00EE);
    background-clip: text;
    color: transparent;
    transition: color ease-in-out;
}

.discord:hover{
    color: #316BFF;
    transition: color ease-in-out;
}
</style>