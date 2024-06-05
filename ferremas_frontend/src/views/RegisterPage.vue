<template>
  <div>
    <h1>Registro</h1>
    <form @submit.prevent="register">
      <div>
        <label for="username">Nombre de usuario:</label>
        <input type="text" v-model="username" id="username" required />
      </div>
      <div>
        <label for="password">Contraseña:</label>
        <input type="password" v-model="password" id="password" required />
      </div>
      <div>
        <label for="email">Correo Electrónico:</label>
        <input type="email" v-model="email" id="email" required />
      </div>
      <div>
        <label for="phone">Teléfono:</label>
        <input type="text" v-model="phone" id="phone" />
      </div>
      <div>
        <label for="address">Dirección:</label>
        <input type="text" v-model="address" id="address" />
      </div>
      <div>
        <label for="rut">RUT:</label>
        <input type="text" v-model="rut" id="rut" required />
      </div>
      <button type="submit">Registrarse</button>
    </form>
    <p>Ya tienes una cuenta? <router-link to="/login">Inicia sesión aquí</router-link></p>
    
    <!-- Modal de Éxito -->
    <div v-if="successMessage" class="modal">
      <div class="modal-content">
        <h2>Usuario registrado con éxito</h2>
        <button @click="goToLogin">Aceptar</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'RegisterPage',
  data() {
    return {
      username: '',
      password: '',
      email: '',
      phone: '',
      address: '',
      rut: '',
      successMessage: false
    }
  },
  methods: {
    async register() {
      try {
        await axios.post('http://127.0.0.1:8000/api/users/', {
          username: this.username,
          password: this.password,
          email: this.email,
          phone: this.phone,
          address: this.address,
          rut: this.rut
        })
        this.successMessage = true
      } catch (error) {
        console.error('Error al registrarse:', error)
      }
    },
    goToLogin() {
      this.successMessage = false
      this.$router.push('/login')
    }
  }
}
</script>

<style scoped>
/* Estilos para el modal */
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(0, 0, 0, 0.5);
}
.modal-content {
  background: #fff;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}
</style>
