<script setup>
    defineProps({
      title: String,
    })
</script>

<template>
    <div class="flex flex-col items-center">
        <div class="boxShadow px-[10rem] py-3 rounded-2xl">
            <h3 class="text-xl">{{ title }}</h3>
            <div class="mt-[2rem]">
              <div class="formGroup">
                <input type="text" v-model="email" class="field" />
                <label for="text" class="label">Email</label>
              </div>
            </div>
        </div>
    </div>
</template>

<style>
    .formGroup{
      position: relative;
      padding: 15px 0 0;
      margin-top: 0.7rem;
    }

    .label{
      position: absolute;
      top: 2rem;
      display: block;
      transition: 0.2s;
      font-size: 1rem;
      color: #9e9e9e;
    }

    .field{
      font-family: inherit;
      width: 100%;
      border: 0;
      border-bottom: 2px solid #535353;
      outline: 0;
      font-size: 1.3rem;
      padding: 7px 0;
      background: transparent;
      transition: border-color 0.2s;
    }

    .field:focus{
      ~ .label{
        top: -1rem;
        font-size: 0.8rem;
        color: #5B94FF;
      }
    }
</style>