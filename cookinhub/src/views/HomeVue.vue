<script>

import CookinHubNav from '/src/components/BaseNav.vue'

export default {
  name: 'CookinHubHome',
  components: {
    CookinHubNav
  }
}
</script>
<style>
#homeBody {
  background: url("../../public/Front.png");
  background-size: cover;
  height: 547px;
}
</style>

<template>
  <CookinHubNav title="Cook'inHub"/>
    <div class="row align-items-center w-100 m-0" id="homeBody">
      <div class="d-flex justify-content-center">
        <div class="card border-warning">
          <div class="card-body ">
              <p>A well-known quote, contained in a blockquote element.</p>
            <div class="d-flex justify-content-center">
               <router-link type="button" class="btn btn-warning" to="/customize">Personnaliser</router-link>
            </div>

          </div>
        </div>
      </div>
    </div>
</template>
