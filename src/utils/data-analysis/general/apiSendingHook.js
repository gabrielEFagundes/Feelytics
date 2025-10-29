import { ref } from 'vue';
import axios from 'axios';

export function apiSearchRequest(){
    const search = ref('');
    
    const sendRequest = () => {
        axios.post(`http://127.0.0.1:5000/api/data/reddit?query=${search.value}`,) // change this too when in production!
        .then((res) => {
            console.log(res.data);
        })
        .catch((e) => {
            console.error(e);
        });
    }
}