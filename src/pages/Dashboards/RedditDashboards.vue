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
        <div class="mt-[10rem] lg:mx-[10rem]" v-if="redditData">
            <div class="flex flex-col lg:flex-row gap-4 mb-[10rem] lg:mb-10 justify-evenly">
                <BasicBoard title="Amount of relevant posts found:" :data=redditData[0].amount_of_relevant_posts_on_analysis />
                <BasicBoard title="People engagement about the topic:" :data=redditData[0].topic_engajement_level_in_word />
                <BasicBoard title="General feeling about the topic:" :data=redditData[0].one_emoji_popular_opinion_about_topic />
            </div>
            <p>Most <span class="text-[#FFA64D]">engaged</span> posts</p>
            <div class="grid grid-rows-4 lg:grid-cols-2 lg:grid-rows-2 gap-5">
                <PostsBoard :post-title=redditData[0].most_scored_post_title
                            :post-author=redditData[0].most_scored_post_author
                            :post-body=redditData[0].most_scored_post_body
                            :post-score=redditData[0].most_scored_post_score />
                    
                <AiResume :data=redditData[0].resume_about_analysis_and_popular_opinion />

                <PostsBoard :post-title=redditData[0].second_most_scored_post_title
                                :post-author=redditData[0].second_most_scored_post_author
                                :post-body=redditData[0].second_most_scored_post_body
                                :post-score=redditData[0].second_most_scored_post_score />

                <div class="grid grid-cols-2 gap-5">
                    <BasicBoard title="Similar Topics:">
                        <li class="list-none" v-for="topic in redditData[0].three_similar_topics_in_one_word">
                            <ul class="text-neutral-400">{{ topic }}</ul>
                        </li>
                    </BasicBoard>
                    <BasicBoard title="Main Subreddit About the Topic:">
                        <p class="text-lg">{{ redditData[0].main_subreddit_about_topic }}</p>
                        <p class="text-neutral-500">{{ redditData[0].about_main_subreddit }}</p>
                    </BasicBoard>
                </div>
            </div>
        </div>
    </main>

    <Footer />
</template>