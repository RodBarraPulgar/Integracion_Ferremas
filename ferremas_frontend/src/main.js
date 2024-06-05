import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap';
import 'bootstrap-vue-next/dist/bootstrap-vue-next.css';
import { BCard, BCardText } from 'bootstrap-vue-next';

const app = createApp(App);
app.use(router);

// Registrar componentes individuales
app.component('BCard', BCard);
app.component('BCardText', BCardText);

app.mount('#app');