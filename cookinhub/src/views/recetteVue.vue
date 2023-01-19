<template>
    <CookinHubNav title="Cook'inHub"/>

    <div class="container p-4">
      <div class="row gx-5">
            <h4>Recette générée :</h4>
        </div>
        <div class="row gx-5">
            <div class="col pt-4">
                <div class="card-body border border-warning rounded-top p-2">
                    <h5 class="card-title">Ingrédients :</h5>
                    <p class="card-text p-2">{{ ingredients }}</p>
                </div>
            </div>
            <div class="col pt-4">
                <div class="card-body border border-warning rounded-top p-2">
                    <h5 class="card-title">Ustensiles</h5>
                    <p class="card-text p-2">{{ ustensiles }}</p>
                </div>
            </div>
        </div>
        <div class="row gx-5 p-4">
            <div class="card-body border border-warning rounded-bottom p-2">
                <h5 class="card-title">Etapes :</h5>
                <p class="card-text p-2">{{ etapes }}</p>
            </div>
        </div>
    </div>
</template>
<script>
import CookinHubNav from '/src/components/BaseNav.vue'
export default{
  name: 'CookinHubRecette',
  components: {
    CookinHubNav
  },
  data() {
    return {
      receipe: '',
      titre : '',
      ingredients : '',
      ustensiles : '',
      etapes : ''
    }
  },
  created() {
    // this.receipe = this.$route.params.receipe;
    this.receipe ="Ingregients:\n" +
        "1 Pate Feuilletee \n" +
        "12 Olives Vertes Denoyaute \n" +
        "2 Tranches Jambon Cru Potiron Legumes 1 Branche Celeri 2 Pommes Terre 2 Tomates 1 Courgette 1 Oignon 10 Cl Creme Fraiche 1 Navet 1 Bouillon " +
        "Ustensiles Louche Mixeur Plongeant Blender Chauffant Couteau Set 3 Poeles Marmite Marmiton Couvercle Cocotte Minute Mixeur Cuillere Bois Mijoteuse Electrique Balance Cuisine " +
        "Instructions Peler Laver Couper Legumes Petits Morceaux Faire Revenir Poireau Beurre 10 Minutes Marmite Mettre Legumes Recouvrir Eau Ajouter Moitie Bouillon Cube Faire Cuire 30 Minutes 10 Minutes Autocuiseur Recouvrir Poireau Eau Ajouter Bouillon Cube Faire Cuire 20 Minutes Legumes Carottes Navet Tomates Poireau Cuits Mixer Assaisonner Gout Ajouter Creme Fraiche Poireau Non Mixe Melanger Deguster"
    this.titre = "Recette générée";
    this.ingredients = this.receipe.split("Ingregients:")[1].split("Ustensiles")[0];
    this.ustensiles = this.receipe.split("Ustensiles")[1].split("Instructions")[0]
    this.etapes = this.receipe.split("Instructions")[1]
  }
}
</script>
