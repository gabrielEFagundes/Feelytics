<script setup>
    import firebase from 'firebase/compat/app';
    import { deleteDoc, doc } from 'firebase/firestore';
    import { db } from '../main.js';

    const user = firebase.auth().currentUser;

    async function deleteAccount() {
        if(confirm("Are you sure you want to delete your account? This action is irreversible. Click again to confirm.")){
        user.delete()
        .then(() => {
            alert("Account deleted successfully.");
        })
        .catch((error) => {
            console.log(error);
        })
        
        await deleteDoc(doc(db, 'users', user.uid));
        }
    }

    function askForLogin(){
    alert("Please, log into your account to delete it. Or relog in if you are already logged in.");
    }
</script>

<template>
    <div class="boxShadow rounded-t-xl flex flex-col gap-[3rem] justify-between items-center py-[5rem] px-[2rem] md:px-[10rem] md:flex-row lg:px-[10rem] lg:flex-row">
        <div class="text-center">
            <h3 class="lg:text-4xl text-xl">🌀Feely<span class="logoColor">tics</span></h3>
            <sub class="hidden lg:inline"><span class="text-red-700">MIT</span> 2025 - Please give us some credit!</sub>
            <sub class="inline lg:hidden"><span class="text-red-700">MIT</span> 2025</sub>
        </div>
        <div>
            <div class="grid grid-rows-2 place-items-center text-center gap-3 lg:grid-cols-4 text-xs lg:text-sm">
                <a href="mailto:gabriel_e_fagundes@estudante.sesisenai.org.br" class="">Contact Us</a>
                <a href="/policy" class="">Privacy Policy</a>
                <a href="/terms" class="">Terms of Use</a>
                <button v-if="user != null" @click="deleteAccount" class="text-red-500 cursor-pointer">Delete Account</button>
                <button v-else @click="askForLogin" class="text-red-500 cursor-pointer">Delete Account</button>
                <div class="lg:col-span-4">
                    <a href="https://github.com/gabrielEFagundes/Feelytics" target="_blank">
                        <img src="/github.svg?url" alt="Github Icon" class="w-[1.5rem] mt-3">
                    </a>
                </div>
            </div>
        </div>
    </div>
</template>