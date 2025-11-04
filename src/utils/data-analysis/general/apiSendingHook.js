import { ref } from 'vue';
import axios from 'axios';

export function apiSearchRequest(){
    const search = ref('');
    let loading = ref(false);
    
    const sendRequest = async () => {
        try{
            loading.value = true
            const res = await axios.post(`http://127.0.0.1:5000/api/data/reddit?query=${search.value}`,) // change this too when in production!
            return res.data;
            // return `[{
            //     "most_scored_post_title": "DOGS and CATS test",
            //     "most_scored_post_score": 999999,
            //     "one_emoji_popular_opinion_about_topic": "✅"
            // }]`

        } catch(e) {
            console.error('Error sending data -> ', e);

        } finally {
            loading.value = false;
        }
    }

    return { search, sendRequest, loading };
}