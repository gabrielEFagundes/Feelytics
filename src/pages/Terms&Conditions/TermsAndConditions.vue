<script setup>
    import Navbar from '../../components/Navbar.vue';
    import Footer from '../../components/Footer.vue';
    import TextWrapper from '../../widgets/TextWrapper.vue';
</script>

<template>
    <Navbar />
    <section class="flex flex-col items-center my-[10rem] p-5">
        <div>
            <h1 class="text-6xl text-center">Terms & <span class="mainColor">Conditions</span></h1>
        </div>
        <TextWrapper msg="
        The usage of our program is completely free, we never ask for payments. The only money you can send to us is through the 'Buy me a Coffee' option.

        If anyone asks for money using our money, please contact us through the button on the page's footer. Again, we'll NEVER ask for money.

        "/>

        <div>
            <h3 class="text-4xl mt-[10rem] text-center">Frequently asked <span class="mainColor">Questions</span></h3>
            <div class="grid grid-cols-1 gap-[1rem] lg:grid-cols-2">
                <TextWrapper msg="- How should I use your platform?
                
                You choose! There is no 'right way' to use this platform. Search for any topic and have a look on what people think about it!" />
                <TextWrapper msg="- Is this platform open-sourced?
                
                Yep! Our platform was initially made for a school project, but soon it will be open-sourced for anyone to contribute to it!" />
                <TextWrapper msg="- Is your API free?
                
                Yes! You don't have to pay anything to use our API, but consider donating!" />
                <TextWrapper msg="- How can I use your API?
                
                For now, our API is only disponible only for Java (in development). To use it, read our docs!" />
            </div>
        </div>
    </section>
    <Footer />
</template>