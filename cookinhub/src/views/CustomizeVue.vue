<template>
  <CookinHubNav title="Cook'inHub"/>
  <div class="border border-1 border-warning rounded-bottom mx-2 mb-5">
    <form @submit.prevent="submitForm">
      <h5 class="card-title mx-2 mt-3">Type recette :</h5>
      <CookinHubTypeReceipe v-model="selectedType" />

      <h5 class="card-title mx-2 mt-3">Ingrédients :</h5>
      <CookinHubIngredients v-model="selectedIngredients" />

      <h5 class="card-title mx-2 mt-3">Ustensiles :</h5>
      <CookinHubUtensils v-model="selectedUtensils" />
      <div class="d-flex justify-content-center">
        <button class="btn btn-warning m-2" type="submit" value="Submit">Confirmer ma selection</button>
      </div>
    </form>
  </div>
</template>

<script>
import CookinHubNav from '/src/components/BaseNav.vue'
import CookinHubIngredients from '/src/components/ingredientsList.vue'
import CookinHubUtensils from '/src/components/utensilsList.vue'
import CookinHubTypeReceipe from '/src/components/typeReceipe.vue'
import axios from 'axios'

export default {
  name: 'CookinHubCustomize',
  components: {
    CookinHubNav,
    CookinHubTypeReceipe,
    CookinHubIngredients,
    CookinHubUtensils
  },
  data() {
    return {
    }
  },
  methods: {
    async submitForm() {
      // Récupère les sélections de l'utilisateur
      const data = {
        type: this.selectedType,
        ingredients: this.selectedIngredients,
        utensils: this.selectedUtensils
      }

      try {
        // Envoie les données sélectionnées à l'API
        const response = await axios.post('http://13.38.128.70:9000/receipes', data)

        // Traite la réponse de l'API
        console.log(response.data)
      } catch (error) {
        console.error(error)
      }
    }
  }
}
</script>
