<template>
  <div>
    <h1>Productos</h1>
    <div class="usd-value-card">
      <b-card title="Valor del dólar" class="mb-2">
        <b-card-text>
          ${{ usdValue !== null ? usdValue.toFixed(2) : 'N/A' }}
        </b-card-text>
      </b-card>
    </div>
    <div class="d-flex flex-wrap justify-content-around">
      <div 
        v-for="product in products" 
        :key="product.id" 
        class="card mb-4" 
        :style="{ width: '20rem', cursor: 'pointer' }"
        @click="goToProductDetail(product.id)"
      >
        <img :src="product.image" class="card-img-top" :alt="product.name">
        <div class="card-body">
          <h5 class="card-title">{{ product.name }}</h5>
          <p class="card-text">{{ product.description }}</p>
          <p class="text-muted">Precio en CLP: ${{ product.price_clp !== null ? Math.round(product.price_clp) : 'N/A' }}</p>
          <div v-if="isLoggedIn">
            <input 
              type="number" 
              v-model.number="productQuantities[product.id]" 
              :max="product.stock" 
              :min="1" 
              class="form-control mb-2" 
              @click.stop
            />
            <button 
              @click.stop="addToCart(product)" 
              class="btn btn-primary"
            >Agregar al Carrito</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import { BCard, BCardText } from 'bootstrap-vue-next';

export default {
  name: 'ProductList',
  components: {
    BCard,
    BCardText
  },
  data() {
    return {
      products: [],
      productQuantities: {},
      isLoggedIn: false,
      usdValue: null
    };
  },
  created() {
    this.fetchProducts();
    this.fetchUsdValue();
    this.checkLoginStatus();
  },
  methods: {
    fetchProducts() {
      axios.get('http://127.0.0.1:8000/api/products/')
        .then(response => {
          this.products = response.data;
        })
        .catch(error => {
          console.error('Error fetching products:', error);
        });
    },
    fetchUsdValue() {
      axios.get('http://127.0.0.1:8000/api/usd-value/')
        .then(response => {
          this.usdValue = response.data.usd_value;
        })
        .catch(error => {
          console.error('Error fetching USD value:', error);
        });
    },
    checkLoginStatus() {
      const token = localStorage.getItem('token');
      if (token) {
        this.isLoggedIn = true;
      }
    },
    addToCart(product) {
      const quantity = this.productQuantities[product.id] || 1;
      if (quantity > product.stock) {
        alert('La cantidad no puede ser mayor al stock disponible');
        return;
      }
      const cart = JSON.parse(localStorage.getItem('cart')) || [];
      const cartItem = cart.find(item => item.product.id === product.id);
      if (cartItem) {
        cartItem.quantity += quantity;
      } else {
        cart.push({ product, quantity });
      }
      localStorage.setItem('cart', JSON.stringify(cart));
      alert('Producto agregado al carrito');
    },
    goToProductDetail(productId) {
      this.$router.push({ name: 'ProductDetail', params: { id: productId } });
    }
  }
};
</script>

<style scoped>
.d-flex {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
}

.mb-4 {
  margin-bottom: 1.5rem;
}

.form-control {
  max-width: 100%;
}

.card {
  cursor: pointer;
}

.usd-value-card {
  margin-bottom: 1.5rem;
  text-align: center;
}
</style>
