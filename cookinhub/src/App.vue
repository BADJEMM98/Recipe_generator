<!-- <template>
  <img alt="Vue logo" src="./assets/logo.png">
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'

export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style> -->
<script>
import CookinHubHome from "@/views/HomeVue.vue";
// import CookinHubReceip from './components/ReceipeVue.vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

export default {
    name: 'App',
    components: {
      CookinHubHome,
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
       <!-- <router-view /> -->
       <CookinHubHome />
    </div>
</template>

