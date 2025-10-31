import { ref } from 'vue';
import axios from 'axios';

export function apiSearchRequest(){
    const search = ref('');
    let loading = ref(false);
    
    const sendRequest = async () => {
        
        try{
            loading.value = true
            const res = axios.post(`http://127.0.0.1:5000/api/data/reddit?query=${search.value}`,) // change this too when in production!
            console.log(res);

        } catch(e) {
            console.error('Error sending data -> ', e);

        } finally {
            loading.value = false;
        }
    }

    return { search, sendRequest };
}