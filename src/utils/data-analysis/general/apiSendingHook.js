import { ref } from 'vue';
import axios from 'axios';

export function apiSearchRequest(){
    const search = ref('');
    let loading = true;
    
    const sendRequest = async () => {
        await axios.post(`http://127.0.0.1:5000/api/data/reddit?query=${search.value}`,) // change this too when in production!
        .then((res) => {
            console.log(res.data);
            return res.data;
        })
        .catch((e) => {
            console.error(e);
        })
        .finally(() => {
            loading = false;
        })
    }

    return { search, sendRequest };
}