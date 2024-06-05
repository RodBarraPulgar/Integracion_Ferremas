<template>
  <div v-if="product">
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Precio: {{ product.price_usd }} CLP</p>
    <p>Stock: {{ product.stock }}</p>
    <img :src="product.image" alt="Imagen del producto" v-if="product.image">
  </div>
  <div v-else>
    <p>Cargando...</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ProductDetailPage',
  data() {
    return {
      product: null
    }
  },
  created() {
    const productId = this.$route.params.id
    this.fetchProduct(productId)
  },
  methods: {
    fetchProduct(id) {
      axios.get(`http://127.0.0.1:8000/api/products/${id}/`)
        .then(response => {
          this.product = response.data
        })
        .catch(error => {
          console.error('Error fetching product:', error)
        })
    }
  }
}
</script>

<style scoped>
/* Puedes agregar estilos personalizados aquí */
</style>
