   
<script>
import CookinHubNav from '/src/components/BaseNav.vue'
// import Papa from 'papaparse'

export default {
    name: 'CookinHubCustomize',
    components: {
      CookinHubNav
    },
    
    data() {
      return {
        items: [
          { id: 1, name: 'Plat principal' },
          { id: 2, name: 'Entrées' },
          { id: 3, name: 'Dessert' },
          { id: 2, name: 'Sauce' },
          { id: 3, name: 'Accompagnement' },
          { id: 2, name: 'Boisson' }
        ]
      //   ,
      //   csvFruits: []
      }
    }
    // ,
    // created(){
    //   Papa.parse('./assets/fruits.csv', {
    //     download: true,
    //     header: true,
    //     complete: results => {
    //       this.csvFruits = results.data
    //     }
    //   })
    // }
  }

</script>

<template>
    <CookinHubNav title="Cook'inHub"/>
    <div class="border border-1 border-warning rounded-bottom mx-2">
      <h5 class="card-title mx-2 mt-3">Type recette :</h5>
      <div class="d-flex flex-wrap">
        <div class="form-check mx-4 mt-1" v-for="item in items" :key="item.id" >
          <input class="form-check-input" type="radio" name="receipeType" id="receipeType1" value="option1" checked>
          <label class="form-check-label" for="'receipeType' + item.id">
            {{ item.name }}
          </label>
        </div>
      </div>

      <h5 class="card-title mx-2 mt-3">Ingrédients :</h5>
      <h6 class="mx-3 mt-3">Viandes :</h6> 
      <div class="form-check mx-4 mt-1">
        <input class="form-check-input" type="checkbox" value="" id="flexCheckIndeterminate">
        <label class="form-check-label" for="flexCheckIndeterminate">
          Indeterminate checkbox
        </label>
      </div>

      <h6 class="mx-3 mt-3">Legumes :</h6>
      <div class="form-check mx-4 mt-1">
        <input class="form-check-input" type="checkbox" value="" id="flexCheckIndeterminate">
        <label class="form-check-label" for="flexCheckIndeterminate">
          Indeterminate checkbox
        </label>
      </div>

      <!-- <h6 class="mx-3 mt-3" v-for="row in csvFruits" :key="row.id">Fruits :</h6>
      <div class="form-check mx-4 mt-1">
        <input class="form-check-input" type="checkbox" value="" id="flexCheckIndeterminate">
        <label class="form-check-label" for="flexCheckIndeterminate" v-for="cell in row" :key="cell">
          {{ cell }}
        </label>
      </div> -->
      <h6 class="mx-3 mt-3">Féculents :</h6>
      <div class="form-check mx-4 mt-1">
        <input class="form-check-input" type="checkbox" value="" id="flexCheckIndeterminate">
        <label class="form-check-label" for="flexCheckIndeterminate">
          Indeterminate checkbox
        </label>
      </div>
      
      <h6 class="mx-3 mt-3">Légumineuses :</h6>
      <div class="form-check mx-4 mt-1">
        <input class="form-check-input" type="checkbox" value="" id="flexCheckIndeterminate">
        <label class="form-check-label" for="flexCheckIndeterminate">
          Indeterminate checkbox
        </label>
      </div>
      
      <h6 class="mx-3 mt-3">Épices :</h6>
      <div class="form-check mx-4 mt-1">
        <input class="form-check-input" type="checkbox" value="" id="flexCheckIndeterminate">
        <label class="form-check-label" for="flexCheckIndeterminate">
          Indeterminate checkbox
        </label>
      </div>
      
      <h6 class="mx-3 mt-3">Herbes :</h6>
      <div class="form-check mx-4 mt-1">
        <input class="form-check-input" type="checkbox" value="" id="flexCheckIndeterminate">
        <label class="form-check-label" for="flexCheckIndeterminate">
          Indeterminate checkbox
        </label>
      </div>
      
      <h5 class="card-title mx-2 mt-3">Ustensiles :</h5>
  </div>
</template>
