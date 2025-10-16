<script setup>
  import { ref } from 'vue';
  import firebase from 'firebase/compat/app';
  import { useRouter } from 'vue-router';

  const username = ref('');
  const email = ref('');
  const passcode = ref('');

  const err = ref();
  const router = useRouter();

  const signin = () => {
    firebase.auth().createUserWithEmailAndPassword(email.value, passcode.value)
      .then(() => {
        firebase.auth().onAuthStateChanged((user) => {
          if(user){
            user.updateProfile({
              displayName: username.value
            })
            .catch((error) => {
              err.value = "Something went wrong!";
            })
          }
        })
      })
      .then((data) => {
        router.push('/home');
      })
      .catch((error) => {
        switch(error){
          case 'auth/invalid-email':
            err.value = "Your email is invalid!";
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
            <h3 class="text-xl">Sign a new account</h3>
            <div class="mt-[2rem]">
              <div>
                <input type="text" v-model="username" placeholder="Your Name..." class="field mb-[2rem]" required>
              </div>
              <div>
                <input type="email" v-model="email" placeholder="Email..." class="field mb-[2rem]" required />
              </div>
              <div>
                <input type="password" v-model="passcode" placeholder="Password..." class="field mb-[2rem]" required />
              </div>
              <div>
                <button @click="signin" class="submit">Sign in!</button>
              </div>
              <a href="/home" class="text-xs">↩ Back to Home</a>
            </div>
        </div>
        <p class="mt-3 text-red-400" v-if="err">{{ err }}</p>
    </div>
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