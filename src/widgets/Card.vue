<script setup>
  defineProps({
      img: String,
      name: String,
      role: String,
      biografy: String,
      github: String
  })
</script>

<template>
    <div class="bg-neutral-900 rounded-xl">
            <div>
                <img :src="img" :alt="name" class="max-w-xs rounded-t-xl">
            </div>
            <div class="p-3">
                <p>{{ name }}</p>
                <sub class="text-gray-500">{{role}}</sub>
                <p class="mt-7 text-xs text-gray-300 max-w-[17rem] leading-3.9">{{biografy}}</p>
            </div>
            <div class="p-3">
                <a :href="github" class="font-black mt-7">GitHub</a>
            </div>
        </div>
</template>

<style>
.boxShadow{
    box-shadow: rgba(255, 255, 255, 0.25) 0px 1px 70px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset;
}
</style>