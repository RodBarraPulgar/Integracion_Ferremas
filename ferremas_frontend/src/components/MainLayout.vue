<template>
  <div>
    <AppHeader />
    <main>
      <router-view />
    </main>
    <AppFooter />
  </div>
</template>

<script>
import AppHeader from './AppHeader.vue';
import AppFooter from './AppFooter.vue';

export default {
  name: 'MainLayout',
  components: {
    AppHeader,
    AppFooter
  }
}
</script>

<style scoped>
/* Puedes agregar estilos personalizados aquí */
main {
  min-height: 70vh;
}
</style>

