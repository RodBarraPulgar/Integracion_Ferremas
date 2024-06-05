import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../views/HomePage.vue'
import ProductListPage from '../views/ProductList.vue'
import AboutPage from '../views/AboutPage.vue'
import ContactPage from '../views/ContactPage.vue'
import ProductDetailPage from '../views/ProductDetailPage.vue'
import LoginPage from '../views/LoginPage.vue'
import RegisterPage from '../views/RegisterPage.vue'
import ShoppingCartPage from '../views/ShoppingCart.vue'
import SalesChartPage from '../views/SalesChart.vue'
import ProductAdmin from '../views/ProductAdmin.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/productos',
    name: 'Products',
    component: ProductListPage
  },
  {
    path: '/nosotros',
    name: 'About',
    component: AboutPage
  },
  {
    path: '/contacto',
    name: 'Contact',
    component: ContactPage
  },
  {
    path: '/productos/:id',
    name: 'ProductDetail',
    component: ProductDetailPage,
    props: true
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginPage
  },
  {
    path: '/register',
    name: 'Register',
    component: RegisterPage
  },
  {
    path: '/carrito',
    name: 'Cart',
    component: ShoppingCartPage
  },
  {
    path: '/ventas',
    name: 'SalesChart',
    component: SalesChartPage
  },
  { path: '/admin/products', 
  name: 'ProductAdmin',
   component: ProductAdmin 
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
