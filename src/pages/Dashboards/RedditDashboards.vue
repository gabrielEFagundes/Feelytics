<script setup>
    import Navbar from '../../components/Navbar.vue';
    import Footer from '../../components/Footer.vue';
    import SearchBar from '../../widgets/SearchBar.vue';
    import { BasicBoard, PostsBoard, AiResume } from './dashboardComponents';
</script>

<template>
    <Navbar />

    <main class="p-5 mb-[15rem]">
        <SearchBar />
        <div class="mt-[10rem]">
            <div class="flex justify-center gap-4 mb-10">
                <BasicBoard title="Amount of relevant posts found:" data="81 posts" />
                <BasicBoard title="People engagement about the topic:" data="Very High" />
                <BasicBoard title="General feeling about the topic:" data="😊" />
            </div>
            <div class="grid grid-cols-2 justify-center gap-5">
                <div>
                    <p>Most <span class="text-[#FFA64D]">engaged</span> posts</p>
                    <PostsBoard post-title="Post's title" 
                                post-author="Post's author"
                                post-body="Post's body (placeholder, duh)"
                                post-score=150 />
                    <PostsBoard post-title="Placeholder"
                                post-author="Placeholder"
                                post-body="Placeholder"
                                post-score=90 />
                </div>
                <div>
                    <p>&#x2726; Ai Resume:</p>
                    <AiResume data="Data that will come from AI's analysis" />

                    <div>
                        <BasicBoard title="Top Related Topics">
                            <li class="list-none">
                                <ul class="text-[#FFA64D] font-bold">Topic</ul>
                                <ul>Topic</ul>
                                <ul>Topic</ul>
                            </li>
                        </BasicBoard>
                    </div>
                    <div>
                        <BasicBoard title="Main subreddit about the topic:">
                            <div>
                                <p>r/devBr</p>
                                <p class="text-sm text-neutral-500">Put more stuff here please</p>
                            </div>
                        </BasicBoard>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <Footer />
</template>