<template>
  <div>
    <h1>Administrar Productos</h1>
    <h2>Agregar Producto</h2>
    <form @submit.prevent="addProduct">
      <div>
        <label for="name">Nombre:</label>
        <input type="text" v-model="newProduct.name" id="name" required />
      </div>
      <div>
        <label for="description">Descripción:</label>
        <input type="text" v-model="newProduct.description" id="description" required />
      </div>
      <div>
        <label for="price">Precio (CLP):</label>
        <input type="number" v-model="newProduct.price_clp" id="price" required />
      </div>
      <div>
        <label for="stock">Stock:</label>
        <input type="number" v-model="newProduct.stock" id="stock" required />
      </div>
      <div>
        <label for="category">Categoría:</label>
        <select v-model="newProduct.category" id="category" required>
          <option v-for="category in categories" :key="category.id" :value="category.id">
            {{ category.name }}
          </option>
        </select>
      </div>
      <div>
        <label for="image">Imagen:</label>
        <input type="file" @change="onFileChange" id="image" />
      </div>
      <button type="submit">Agregar Producto</button>
    </form>

    <h2>Productos Existentes</h2>
    <div v-for="product in products" :key="product.id">
      <p>{{ product.name }} - {{ product.category ? product.category.name : 'Sin Categoría' }}</p>
      <button @click="editProduct(product)">Editar</button>
      <button @click="deleteProduct(product.id)">Eliminar</button>
    </div>

    <div v-if="editingProduct">
      <h2>Editar Producto</h2>
      <form @submit.prevent="updateProduct">
        <div>
          <label for="editName">Nombre:</label>
          <input type="text" v-model="editingProduct.name" id="editName" required />
        </div>
        <div>
          <label for="editDescription">Descripción:</label>
          <input type="text" v-model="editingProduct.description" id="editDescription" required />
        </div>
        <div>
          <label for="editPrice">Precio (CLP):</label>
          <input type="number" v-model="editingProduct.price_clp" id="editPrice" required />
        </div>
        <div>
          <label for="editStock">Stock:</label>
          <input type="number" v-model="editingProduct.stock" id="editStock" required />
        </div>
        <div>
          <label for="editCategory">Categoría:</label>
          <select v-model="editingProduct.category" id="editCategory" required>
            <option v-for="category in categories" :key="category.id" :value="category.id">
              {{ category.name }}
            </option>
        </select>
        </div>
        <div>
          <label for="editImage">Imagen:</label>
          <input type="file" @change="onEditFileChange" id="editImage" />
        </div>
        <button type="submit">Actualizar Producto</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      products: [],
      categories: [],
      newProduct: {
        name: '',
        description: '',
        price_clp: '',
        stock: '',
        category: '',
        image: null
      },
      editingProduct: null
    }
  },
  created() {
    this.fetchProducts()
    this.fetchCategories()
  },
  methods: {
    async fetchProducts() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/products/')
        this.products = response.data
      } catch (error) {
        console.error('Error fetching products:', error)
      }
    },
    async fetchCategories() {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/categories/')
        this.categories = response.data
      } catch (error) {
        console.error('Error fetching categories:', error)
      }
    },
    onFileChange(event) {
      this.newProduct.image = event.target.files[0]
    },
    onEditFileChange(event) {
      this.editingProduct.image = event.target.files[0]
    },
    async addProduct() {
      try {
        const formData = new FormData()
        formData.append('name', this.newProduct.name)
        formData.append('description', this.newProduct.description)
        formData.append('price_clp', this.newProduct.price_clp)
        formData.append('stock', this.newProduct.stock)
        formData.append('category', this.newProduct.category)
        if (this.newProduct.image) {
          formData.append('image', this.newProduct.image)
        }
        await axios.post('http://127.0.0.1:8000/api/products/', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        this.fetchProducts()
        this.newProduct = {
          name: '',
          description: '',
          price_clp: '',
          stock: '',
          category: '',
          image: null
        }
      } catch (error) {
        console.error('Error adding product:', error)
      }
    },
    editProduct(product) {
      this.editingProduct = { ...product }
    },
    async updateProduct() {
      try {
        const formData = new FormData()
        formData.append('name', this.editingProduct.name)
        formData.append('description', this.editingProduct.description)
        formData.append('price_clp', this.editingProduct.price_clp)
        formData.append('stock', this.editingProduct.stock)
        formData.append('category', this.editingProduct.category)
        if (this.editingProduct.image) {
          formData.append('image', this.editingProduct.image)
        }
        await axios.put(`http://127.0.0.1:8000/api/products/${this.editingProduct.id}/`, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
        this.fetchProducts()
        this.editingProduct = null
      } catch (error) {
        console.error('Error updating product:', error)
      }
    },
    async deleteProduct(productId) {
      try {
        await axios.delete(`http://127.0.0.1:8000/api/products/${productId}/`)
        this.fetchProducts()
      } catch (error) {
        console.error('Error deleting product:', error)
      }
    }
  }
}
</script>
