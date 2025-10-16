<script setup>
  import Navbar from '../../components/Navbar.vue';
  import Footer from '../../components/Footer.vue';
  import TextWrapper from '../../widgets/TextWrapper.vue';
  import LiquidBtn from '../../widgets/LiquidBtn.vue';
</script>

<template>
    <Navbar />
    <main>
        <div class="flex flex-col items-center my-[5rem]">
            <h1 class="text-6xl">Our <span class="mainColor">Policy</span></h1>
            <TextWrapper msg="
            We believe data privacy is a fundamental human right. Our commitment to protecting your personal information is unwavering, and we strive to be transparent about how we collect, use, and safeguard your data.


            Do not worry, the only data we collect are your posts and comments.

            All data collected and fetched by AI is NOT stored on any of our databases, the ONLY data we store are the topics you search for.
            
            " />
            <TextWrapper msg="
            The only reason we ask for your login is so we can have more precision on the datasets we create for our own application!

            Login is NOT necessary, but it helps us a lot!

            " />
        </div>
        <div class="flex flex-col items-center my-[6rem]">
            <h1 class="text-5xl text-center">Your country<br><span class="mainColor">Your policy</span></h1>
            <TextWrapper msg="
            We follow the privacy rules for every country, no matter where it is.

            If you want to learn more about the policies of your country, please check out the page below and search for your country.
            
            " />

            <LiquidBtn link="https://www.dlapiperdataprotection.com/" msg="Data Protection Laws of the World" class="mt-[2rem]"/>
        </div>
        <div class="flex flex-col items-center my-[5rem]">
            <h1 class="text-6xl">Our <span class="mainColor">License</span></h1>
            <TextWrapper msg="
            This entire project is under the MIT license, and the only thing we ask is to give us some credit if you use any part of this project.

            You can read the full license below.

            ">
            </TextWrapper>

            <LiquidBtn link="https://opensource.org/license/mit/" msg="MIT License" class="mt-[2rem]"/>
        </div>
    </main>
    <Footer />
</template>

<style>

</style>