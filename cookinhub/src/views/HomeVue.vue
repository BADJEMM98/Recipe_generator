<script>
import CookinHubNav from '/src/components/BaseNav.vue'

export default {
    name: 'CookinHubHome',
    components: {
      CookinHubNav
    },
    
}
</script>

<template>
    <CookinHubNav title="Cook'inHub"/>
    <div class="border border-1 border-warning rounded-bottom mx-2">
        <div class="container px-4">
            <div class="row gx-5">
                <div class="col">
                    <div class="p-3">
                        <input class="form-control" list="datalistOptions" id="recettesDataList" placeholder="Trouver une recette">
                    </div>
                </div>
                <div class="col">
                    <div class="d-grid gap-2 p-3">
                        <router-link type="button" class="btn btn-warning" to="/customize">Personnaliser</router-link>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
