import { createApp } from 'vue'
import { VueFire } from 'vuefire'
import firebase from 'firebase/compat/app'
import 'firebase/compat/auth'
import { getFirestore, collection } from 'firebase/firestore'
import './static/tailwind.css'
import App from './pages/App.vue'
import { router } from './routes/router.js'

const firebaseConfig = {
  apiKey: "AIzaSyAneRA2MWXMkST5yOCnNsFvKBP-UpZKZzU",
  authDomain: "feelytics-dev.firebaseapp.com",
  projectId: "feelytics-dev",
  storageBucket: "feelytics-dev.firebasestorage.app",
  messagingSenderId: "892519628455",
  appId: "1:892519628455:web:4820056d26b814b18a6582"
};

const app = firebase.initializeApp(firebaseConfig);

export const db = getFirestore(app);
export const todosRef = collection(db, 'todos');

createApp(App).use(router).use(VueFire, { app }).mount('#app')