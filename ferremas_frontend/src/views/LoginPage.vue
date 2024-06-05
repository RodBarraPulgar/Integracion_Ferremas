<template>
  <div>
    <h1>Iniciar Sesión</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">Nombre de usuario:</label>
        <input type="text" v-model="username" id="username" required />
      </div>
      <div>
        <label for="password">Contraseña:</label>
        <input type="password" v-model="password" id="password" required />
      </div>
      <button type="submit">Iniciar Sesión</button>
    </form>
    <p>No tienes una cuenta? <router-link to="/register">Regístrate aquí</router-link></p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'LoginPage',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/api/token/', {
          username: this.username,
          password: this.password
        })
        localStorage.setItem('token', response.data.access)
        localStorage.setItem('username', this.username)
        this.$router.push('/')
        this.$emit('login', this.username)
        window.location.href = 'http://localhost:8080/'
      } catch (error) {
        console.error('Error al iniciar sesión:', error)
        alert('Error al iniciar sesión')
      }
    }
  }
}
</script>
