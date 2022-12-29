<script>
// import CookinHubHome from "@/views/HomeVue.vue";
// import CookinHubReceip from './components/ReceipeVue.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

export default {
    name: 'App',
    components: {
      // CookinHubHome,
      // CookinHubReceip
    }
}

</script>

<template>
   <div>
      <!-- <div>
        <router-link to="/">Home</router-link> |       
        <router-link to="/receipe">Receipe</router-link> |
        <router-link to="/customize">Customize Receipe</router-link>
      </div> -->
       <router-view />
       <!-- <CookinHubHome /> -->
    </div>
</template>

