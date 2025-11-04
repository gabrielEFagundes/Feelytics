import { createApp } from 'vue';
import { VueFire } from 'vuefire';
import firebase from 'firebase/compat/app';
import 'firebase/compat/auth';
import { getFirestore, collection } from 'firebase/firestore';
import './static/tailwind.css';
import App from './pages/App.vue';
import { router } from './routes/router.js';
import { createPinia } from 'pinia';

const pinia = createPinia();

const firebaseConfig = {
  apiKey: import.meta.env.FEEL_FIREBASE_API_KEY,
  authDomain: import.meta.env.FEEL_FIREBASE_AUTH_DOMAIN,
  projectId: import.meta.env.FEEL_FIREBASE_PROJECT_ID,
  storageBucket: import.meta.env.FEEL_FIREBASE_STORAGE_BUCKET,
  messagingSenderId: import.meta.env.FEEL_FIREBASE_MESSAGING_SENDER,
  appId: import.meta.env.FEEL_FIREBASE_APP_ID
};

const app = firebase.initializeApp(firebaseConfig);

export const db = getFirestore(app);
export const todosRef = collection(db, 'todos');

createApp(App).use(router).use(VueFire, { app }).use(pinia).mount('#app')