<template>
  <div>
    <h1>Carrito de Compras</h1>
    <div v-if="cart.length === 0">El carrito está vacío</div>
    <div v-else>
      <div v-for="item in cart" :key="item.product.id" class="cart-item">
        <img :src="item.product.image" alt="item.product.name" />
        <h2>{{ item.product.name }}</h2>
        <p>Cantidad: {{ item.quantity }}</p>
        <p>Precio Unitario: ${{ Math.round(item.product.price_clp) }}</p>
        <p>Precio Total: ${{ Math.round(item.quantity * item.product.price_clp) }}</p>
        <button @click="removeFromCart(item.product.id)">Eliminar</button>
      </div>
      <h2>Total de la Compra: ${{ Math.round(totalAmount) }}</h2>
      <button @click="checkout">Finalizar Compra</button>
    </div>
    <div v-if="showConfirm" class="modal">
      <div class="modal-content">
        <h2>¿Está seguro de que desea realizar la compra?</h2>
        <button @click="confirmCheckout">Aceptar</button>
        <button @click="cancelCheckout">Cancelar</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ShoppingCart',
  data() {
    return {
      cart: [],
      showConfirm: false
    }
  },
  computed: {
    totalAmount() {
      return this.cart.reduce((total, item) => total + (item.product.price_clp * item.quantity), 0)
    }
  },
  created() {
    this.loadCart()
  },
  methods: {
    loadCart() {
      this.cart = JSON.parse(localStorage.getItem('cart')) || []
    },
    removeFromCart(productId) {
      this.cart = this.cart.filter(item => item.product.id !== productId)
      localStorage.setItem('cart', JSON.stringify(this.cart))
    },
    checkout() {
      this.showConfirm = true
    },
    async confirmCheckout() {
      try {
        const token = localStorage.getItem('token')
        if (!token) {
          alert('Debe iniciar sesión para finalizar la compra')
          this.$router.push('/login')
          return
        }
        const headers = {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        }
        const items = this.cart.map(item => ({
          product: item.product.id,
          quantity: item.quantity,
          price: item.product.price_clp
        }))
        console.log('Payload:', {
          total_amount: this.totalAmount,
          items
        })
        await axios.post('http://127.0.0.1:8000/api/sales/', {
          total_amount: this.totalAmount,
          items
        }, { headers })
        localStorage.removeItem('cart')
        this.$router.push('/')
        alert('Compra realizada con éxito')
      } catch (error) {
        console.error('Error al realizar la compra:', error.response.data)
        alert('Error al realizar la compra')
      }
    },
    cancelCheckout() {
      this.showConfirm = false
    }
  }
}
</script>

<style scoped>
.cart-item {
  border: 1px solid #ccc;
  padding: 16px;
  margin-bottom: 16px;
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
  background: #fff;
  padding: 20px;
  border-radius: 5px;
  text-align: center;
}
</style>
