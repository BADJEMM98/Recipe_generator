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
     background-image:
      linear-gradient(
        rgba(181, 112, 112, 0.6),
        rgba(112, 122, 181, 0.6)
      ),
      url("../../public/Front.png");
        background-size: cover;
        height: 660px;
   }

button:hover {
  transform:scale(1.08);
}

.card:hover {
  transform:scale(1.08);
}
</style>

<template>
  <CookinHubNav title="Cook'inHub"/>
    <div class="row align-items-center w-100 m-0" id="homeBody">
      <div class="d-flex justify-content-center">
        <div class="card border-warning m-4">
          <div class="card-body">
              <h3 class="p-4">Vous voudriez une recette propre à vous ? Cook'inHub est là pour vous !</h3>
              <div class="d-flex justify-content-center">
                <button class="btn btn-warning"><router-link  class="link-dark text-decoration-none" to="/customize">Personnaliser</router-link></button>
              </div>
          </div>
        </div>
      </div>
    </div>
</template>
