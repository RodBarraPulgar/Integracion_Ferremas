<template>
  <div v-if="product">
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <p>Precio: {{ product.price_clp }} CLP</p>
    <p>Stock: {{ product.stock }}</p>
    <img :src="product.image" alt="Imagen del producto" v-if="product.image">

    <h2>Comentarios</h2>
    <div v-if="product.comments.length">
      <div v-for="comment in product.comments" :key="comment.id" class="comment">
        <p><strong>{{ comment.name }}</strong> ({{ comment.rating }}/5)</p>
        <p>{{ comment.comment }}</p>
      </div>
    </div>
    <div v-else>
      <p>No hay comentarios aún.</p>
    </div>

    <h2>Agregar Comentario</h2>
    <form @submit.prevent="submitComment">
      <div>
        <label for="name">Nombre:</label>
        <input type="text" v-model="newComment.name" id="name" required />
      </div>
      <div>
        <label for="comment">Comentario:</label>
        <textarea v-model="newComment.comment" id="comment" required></textarea>
      </div>
      <div>
        <label for="rating">Valoración:</label>
        <select v-model="newComment.rating" id="rating" required>
          <option v-for="n in 5" :key="n" :value="n">{{ n }}</option>
        </select>
      </div>
      <button type="submit">Agregar Comentario</button>
    </form>
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
      product: null,
      newComment: {
        name: '',
        comment: '',
        rating: 1
      }
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
    },
    submitComment() {
      const productId = this.$route.params.id
      axios.post('http://127.0.0.1:8000/api/comments/', {
        product: productId,
        ...this.newComment
      })
        .then(response => {
          this.product.comments.push(response.data)
          this.newComment.name = ''
          this.newComment.comment = ''
          this.newComment.rating = 1
        })
        .catch(error => {
          console.error('Error submitting comment:', error)
        })
    }
  }
}
</script>

<style scoped>
.comment {
  border-bottom: 1px solid #ccc;
  padding-bottom: 10px;
  margin-bottom: 10px;
}
</style>
