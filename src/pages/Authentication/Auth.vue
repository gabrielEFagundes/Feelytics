<script setup>
  import{ ref } from 'vue'
  import Login from '../../widgets/Login.vue';
  import Signin from '../../widgets/Signin.vue';

  const tabs = {
    Login,
    Signin
  }
  const currTab = ref('Login');
</script>

<template>
    <div class="flex flex-col items-center my-[6rem]">
        <p>Welcome to</p>
        <h1 class="text-6xl">Feely<span class="logoColor">tics</span></h1>
        <div class="mt-[2rem] flex gap-4">
            <button v-for="(_,tab) in tabs" :key="tab" :class="['tab-button', { active: currTab === tab }]" @click="currTab = tab">{{ tab }}</button>
        </div>
        <keep-alive>
          <component :is="tabs[currTab]"></component>
        </keep-alive>
    </div>
</template>

<style scoped>
button{
  cursor: pointer;
  border-top: 2px solid #181818;
  border-top-left-radius: 2rem;
  border-top-right-radius: 2rem;
  padding: 0.5rem 2rem;
  transition: all 0.3s ease-in-out;
}

button:hover{
    transform: translateY(-0.2rem);
}
</style>