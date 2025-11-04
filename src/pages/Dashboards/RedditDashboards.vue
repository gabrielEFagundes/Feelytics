<script setup>
    import Navbar from '../../components/Navbar.vue';
    import Footer from '../../components/Footer.vue';
    import { BasicBoard, PostsBoard, AiResume, SearchBar } from './dashboardComponents';
    import { storeToRefs } from 'pinia';
    import { useRedditStore } from '../../../stores/redditStore';

    const redditStore = useRedditStore();

    const { redditData } = storeToRefs(redditStore);
    
    if(redditData){
        console.log(redditData);
    }
</script>

<template>
    <Navbar />

    <main class="p-5 mb-[15rem]">
        <SearchBar />
        <div class="mt-[10rem] lg:mx-[10rem]">
            <p class="mb-10" v-if="redditData && redditData.length > 0">{{ redditData[0].most_scored_post_title }}</p>
            <div class="flex flex-col lg:flex-row gap-4 mb-[10rem] lg:mb-10 justify-evenly">
                <BasicBoard title="Amount of relevant posts found:" data="81 posts" />
                <BasicBoard title="People engagement about the topic:" data="Very High" />
                <BasicBoard title="General feeling about the topic:" data="😊" />
            </div>
            <p>Most <span class="text-[#FFA64D]">engaged</span> posts</p>
            <div class="grid grid-rows-4 lg:grid-cols-2 lg:grid-rows-2 gap-5">
                <PostsBoard post-title="Post's title" 
                            post-author="Post's author"
                            post-body="Post's body (placeholder, duh)"
                            post-score=150 />
                    
                <AiResume data="AI Resume here..." />

                <PostsBoard post-title="Placeholder"
                                post-author="Placeholder"
                                post-body="Placeholder"
                                post-score=90 />

                <div class="grid grid-cols-2 gap-5">
                    <BasicBoard title="Similar Topics:">
                        <li class="list-none">
                            <ul class="text-[#FFA64D]">Title</ul>
                            <ul>Title</ul>
                            <ul>Title</ul>
                        </li>
                    </BasicBoard>
                    <BasicBoard title="Main Subreddit About the Topic:">
                        <p class="text-lg">r/devBr</p>
                        <p class="text-neutral-500">Sub's description, i guess</p>
                    </BasicBoard>
                </div>
            </div>
        </div>
    </main>

    <Footer />
</template>