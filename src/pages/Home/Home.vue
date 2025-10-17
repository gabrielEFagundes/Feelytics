<script setup>
    import Navbar from '../../components/Navbar.vue';
    import TextWrapper from '../../widgets/TextWrapper.vue';
    import Grid from '../../components/Grid.vue';
    import Footer from '../../components/Footer.vue';
</script>

<template>
    <Navbar />
    <main class="p-5">
        <section>
            <div class="flex items-center flex-col mt-[10rem] gap-2">
                <h1 class="text-6xl">Feely<span class="logoColor">tics</span></h1>
                <p>How you <span class="mainColor">feeling</span>?</p>
            </div>
            <TextWrapper msg="The best of data, all in one place" />
        </section>
        <section>
            <div class="flex items-center flex-col mt-[10rem] gap-2">
                <h3 class="text-6xl">Why <span class="mainColor">us</span>?</h3>
            </div>
            <TextWrapper msg="  
            We believe that data shouldn’t be paid, data should be free, especially when talking about researches and statistics.

            On our platform, you can find data from social media, without having to do additional researches or even building a API for yourself.

            We also offer our own API, with data already formatted and usable, powered by AI for you to use.

            " />
        </section>
        <section>
            <div class="flex items-center flex-col mt-[10rem] gap-2">
                <h3 class="text-6xl text-center">Who we <span class="mainColor">are</span>:</h3>
            </div>
            <div class="flex justify-center">
                <Grid />
            </div>
        </section>
    </main>
    <section class="mt-[20rem]">
        <Footer />
    </section>
</template>