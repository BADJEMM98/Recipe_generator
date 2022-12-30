   
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
        items: [
          { id: 1, name: 'Plat principal' },
          { id: 2, name: 'Entrées' },
          { id: 3, name: 'Dessert' },
          { id: 2, name: 'Sauce' },
          { id: 3, name: 'Accompagnement' },
          { id: 2, name: 'Boisson' }
        ],
        selectedItems: []
      }
    },
    methods: {
      async submitForm() {
        // Récupère les éléments sélectionnés
        const selectedItems = this.items.filter(item => item.selected)

        try {
          // Envoie les données sélectionnées à l'API
          const response = await axios.post('https://13.38.128.70:9000/receipes', { items: selectedItems })

          // Traite la réponse de l'API
          console.log(response.data)
        } catch (error) {
          console.error(error)
        }
      }
    }
  }

</script>

<template>

  <CookinHubNav title="Cook'inHub"/>
    <div class="border border-1 border-warning rounded-bottom mx-2 mb-5">
      <form @submit.prevent="submitForm">
        <h5 class="card-title mx-2 mt-3">Type recette :</h5>
        <CookinHubTypeReceipe />

        <h5 class="card-title mx-2 mt-3">Ingrédients :</h5>
        <CookinHubIngredients />

        <h5 class="card-title mx-2 mt-3">Ustensiles :</h5>
        <CookinHubUtensils />
        <div class="d-flex justify-content-center">
          <button class="btn btn-warning m-2" type="submit" value="Submit">Confirmer ma selection</button>
        </div>
      </form>
    
  </div>
</template>
