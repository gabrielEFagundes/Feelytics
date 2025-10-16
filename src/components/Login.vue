<script setup>
  import { ref } from 'vue'
  import firebase from 'firebase/compat/app';
  import { useRouter } from 'vue-router';
  import Warning from '../widgets/Warning.vue';

  const email = ref('');
  const passcode = ref('');

  const err = ref();
  const router = useRouter();

  const login = () => {
    firebase.auth().signInWithEmailAndPassword(email.value, passcode.value)
      .then((data) => {
        router.push('/home');
      })
      .catch((error) => {
        switch(error){
          case 'auth/invalid-email':
            err.value = "Your email is invalid!";
            break;
          case 'auth/user-disabled':
            err.value = "This user has been disabled.";
            break;
          case 'auth/user-not-found':
            err.value = "We couldn't find your account...";
            break;
          case 'auth/wrong-password':
            err.value = "Your password is incorrect!";
            break;
          default:
            err.value = "Check out for your infos and try again.";
            break;
        }
      })
  }
</script>

<template>
    <div class="flex flex-col items-center tab">
        <div class="boxShadow px-[10rem] py-[2.5rem] rounded-2xl text-center">
            <h3 class="text-xl">Log into your account</h3>
            <div class="mt-[2rem]">
              <div>
                <input type="email" v-model="email" placeholder="Email..." class="field mb-[2rem]" required />
              </div>
              <div>
                <input type="password" v-model="passcode" placeholder="Password..." class="field mb-[2rem]" required />
              </div>
              <div>
                <button @click="login" class="submit">Log in!</button>
              </div>
              <a href="/home" class="text-xs">↩ Back to Home</a>
            </div>
        </div>
    </div>
    <Warning v-if="err != null" :err="err" />
</template>

<style scoped>
a{
  color: #535353;
  transition: color 0.3s ease-in-out;
}

a:hover{
  color: #5B94FF;
}

.boxShadow{
    box-shadow: rgba(255, 255, 255, 0.25) 0px 1px 70px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;
}

.field{
    background: #000;
    border: 2px solid #181818;
    padding: 10px;
    width: 100%;
    color: white;
    font-size: 0.8rem;
    border-radius: 2rem;
}

.field:focus{
  background: 
    linear-gradient(#000 0 0) padding-box,
    linear-gradient(to right, #8fb6ff, #3179ff) border-box;
  color: #313149;
  padding: 10px;
  border: 2px solid transparent;
  border-radius: 2rem;
  outline: none;
  color: white;
  transition: all 0.3s ease-in-out;
}

.field:valid{
  background: 
    linear-gradient(#000 0 0) padding-box,
    linear-gradient(to right, #8fffb4, #31ff87) border-box;
  color: #313149;
  padding: 10px;
  border: 2px solid transparent;
  border-radius: 2rem;
  outline: none;
  color: white;
  transition: all 0.3s ease-in-out;
}

.submit{
  cursor: pointer;
  padding: 0.6rem 2rem;
  border-radius: 2rem;
  border: 2px solid #181818;
}

.submit:hover{
  background: 
    linear-gradient(#000 0 0) padding-box,
    linear-gradient(to right, #8fb6ff, #3179ff) border-box;
  color: #313149;
  border: 2px solid transparent;
  border-radius: 2rem;
  outline: none;
  color: white;
  transition: all 0.3s ease-in-out;
}
</style>