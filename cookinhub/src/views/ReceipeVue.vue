<script>
import CookinHubNav from '/src/components/BaseNav.vue'

export default {
    name: 'CookinHubReceip',
    components: {
      CookinHubNav
    },
    
}
</script>

<template>
    <CookinHubNav title="Cook'inHub"/> 
    <div class="container p-4">
        <div class="row gx-5">
            <h5 class="card-title">Nom de la recette : </h5>
        </div>
        <div class="row gx-5">
            <div class="col pt-4">
                <div class="card-body">
                    <h5 class="card-title">Ingrédients :</h5>
                    <ol class="list-group list-group-numbered pt-2">
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Cras justo odio</li>
                    </ol>
                </div>
            </div>
            <div class="col pt-4">
                <div class="card-body">
                    <h5 class="card-title">Ustensiles</h5>
                    <ol class="list-group list-group-numbered pt-2">
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Cras justo odio</li>
                        <li class="list-group-item">Cras justo odio</li>
                    </ol>               
                </div>    
            </div>
        </div>
        <div class="row gx-5 p-4">
            <div class="card-body">
                <h5 class="card-title">Etapes :</h5>
                <ol class="list-group list-group-numbered pt-2">
                    <li class="list-group-item">Cras justo odio</li>
                    <li class="list-group-item">Cras justo odio</li>
                    <li class="list-group-item">Cras justo odio</li>
                </ol>
         </div>  
        </div>
    </div>
</template>
