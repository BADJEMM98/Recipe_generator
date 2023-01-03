
<template>
    <CookinHubNav title="Cook'inHub"/>

    <div class="container p-4">
      <div class="row gx-5">
            <h5 class="card-title">Nom de la recette : {{ titre }}</h5>
        </div>
        <div class="row gx-5">
            <div class="col pt-4">
                <div class="card-body">
                    <h5 class="card-title">Ingrédients :</h5>
                    {{ ingredients }}
                   <!--   <ol class="list-group list-group-numbered pt-2">
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Cras justo odio</li>
                    </ol>-->

                </div>
            </div>
            <div class="col pt-4">
                <div class="card-body">
                    <h5 class="card-title">Ustensiles</h5>
                    {{ ustensiles }}
                    <!--<ol class="list-group list-group-numbered pt-2">
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Cras justo odio</li>
                    </ol>-->
                </div>
            </div>
        </div>
        <div class="row gx-5 p-4">
            <div class="card-body">
                <h5 class="card-title">Etapes :</h5>
                <ol class="list-group pt-2" v-for="item in etapes" :key="item.id">
                    <li class="list-group-item"> {{ item }}</li>
                </ol>
         </div>
        </div>
    </div>
</template>

<script>
import CookinHubNav from '/src/components/BaseNav.vue'
export default{
  name: 'CookinHubReceip',
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
    this.receipe = this.$route.params.receipe;
    const recette = this.receipe.split(",");
    this.titre = recette[0];
    this.ingredients = recette[5];
    this.ustensiles = recette[4];
    this.etapes = recette[6].split("etape")
    this.etapes = this.etapes.slice(1);
  }
}
</script>
