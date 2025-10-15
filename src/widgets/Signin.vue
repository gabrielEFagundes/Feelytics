<script>
export default{
    name: 'Signin',
}
</script>

<template>
    <div class="flex flex-col items-center tab">
        <div class="boxShadow px-[10rem] py-[2.5rem] rounded-2xl text-center">
            <h3 class="text-xl">Sign a new account</h3>
            <div class="mt-[2rem]">
              <div>
                <input type="text" v-model="name" placeholder="Your name..." class="field mb-[2rem]" />
              </div>
              <div>
                <input type="email" v-model="email" placeholder="Email..." class="field mb-[2rem]" />
              </div>
              <div>
                <input type="password" v-model="passcode" placeholder="Password..." class="field mb-[2rem]" />
              </div>
              <div>
                <button @click="login" class="submit">Sign in!</button>
              </div>
              <a href="/home" class="text-xs">↩ Back to Home</a>
            </div>
        </div>
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
    border-bottom: 2px solid #181818;
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
  border-bottom: 2px solid transparent;
  border-radius: 2rem;
  outline: none;
  color: white;
  transition: all 0.3s ease-in-out;
}

.submit{
  cursor: pointer;
  padding: 0.6rem 2rem;
  border-radius: 2rem;
  border-bottom: 2px solid #181818;
}

.submit:hover{
  background: 
    linear-gradient(#000 0 0) padding-box,
    linear-gradient(to right, #8fb6ff, #3179ff) border-box;
  color: #313149;
  border-bottom: 2px solid transparent;
  border-radius: 2rem;
  outline: none;
  color: white;
  transition: all 0.3s ease-in-out;
}
</style>