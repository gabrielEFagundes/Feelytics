import { defineStore } from "pinia";

export const useRedditStore = defineStore('reddit', {
    state: () => ({
        redditData: null,
    }),
    
    actions: {
        setRedditData(data){
            this.redditData = data;
        }
    },

    getters: {
        getRedditData: (data) => data.redditData,
    }
})