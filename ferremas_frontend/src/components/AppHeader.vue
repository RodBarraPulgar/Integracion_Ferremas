<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <router-link class="navbar-brand" to="/">Ferremas</router-link>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0 d-flex flex-row">
            <li class="nav-item">
              <router-link class="nav-link" to="/">Inicio</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/productos">Productos</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/nosotros">Nosotros</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" to="/contacto">Contacto</router-link>
            </li>
            <li v-if="isLoggedIn" class="nav-item">
              <router-link class="nav-link" to="/carrito">Carrito de Compras</router-link>
            </li>
          </ul>
          <ul class="navbar-nav ms-auto d-flex flex-row">
            <li v-if="isLoggedIn" class="nav-item">
              <span class="nav-link">Bienvenido, {{ username }}</span>
            </li>
            <li v-if="!isLoggedIn" class="nav-item">
              <router-link class="nav-link" to="/login">Iniciar Sesión</router-link>
            </li>
            <li v-if="!isLoggedIn" class="nav-item">
              <router-link class="nav-link" to="/register">Registrarse</router-link>
            </li>
            <li v-if="isLoggedIn" class="nav-item">
              <button class="nav-link btn btn-link" @click="logout">Cerrar Sesión</button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <div v-if="showLogoutConfirm" class="modal">
      <div class="modal-content">
        <h2>¿Está seguro que quiere cerrar sesión?</h2>
        <button @click="confirmLogout">Aceptar</button>
        <button @click="cancelLogout">Cancelar</button>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: 'AppHeader',
  data() {
    return {
      isLoggedIn: false,
      username: '',
      showLogoutConfirm: false
    }
  },
  created() {
    this.checkLoginStatus()
  },
  methods: {
    checkLoginStatus() {
      const token = localStorage.getItem('token')
      if (token) {
        this.isLoggedIn = true
        this.username = localStorage.getItem('username')
      }
    },
    logout() {
      this.showLogoutConfirm = true
    },
    confirmLogout() {
      localStorage.removeItem('token')
      localStorage.removeItem('username')
      this.isLoggedIn = false
      this.username = ''
      this.showLogoutConfirm = false
      this.$router.push('/')
    },
    cancelLogout() {
      this.showLogoutConfirm = false
    }
  }
}
</script>

<style scoped>
.navbar {
  background-color: #e0f7fa; /* Pastel aqua */
}

.nav-link {
  color: #00796b !important; /* Dark greenish-blue */
}

.navbar-toggler {
  border-color: #00796b;
}

.navbar-brand {
  font-weight: bold;
  color: #004d40 !important; /* Dark teal */
}

.nav-link:hover {
  color: #004d40 !important;
}

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
  background: #ffffff;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}

button {
  background-color: #00796b;
  color: white; /* Asegurar que el texto es blanco */
  border: none;
  padding: 10px 20px;
  margin: 5px;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #004d40;
  color: white; /* Asegurar que el texto sigue siendo blanco al hacer hover */
}
</style>
