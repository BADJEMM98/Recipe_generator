<script>
export default {
    name: 'CookinHubIngredients',
    components: {
    },
    
    data() {
      return {
        fruits: [
            { id: 1, name :'Pommes'},
            { id: 2, name :'Bananes'},
            { id: 3, name :'Avocats'},
            { id: 4, name :'Fraises'},
            { id: 5, name :'Cerises'},
            { id: 6, name :'Oranges'},
            { id: 7, name :'Mandarines'},
            { id: 8, name :'Pêches'},
            { id: 9, name :'Poires'},
            { id: 10, name :'Ananas'},
            { id: 11, name :'Kiwis'},
            { id: 12, name :'Mangues'},
            { id: 13, name :'Melons'},
            { id: 14, name :'Grenades'},
            { id: 15, name :'Noix de cajou'},
            { id: 16, name :'Noix de pécan'},
            { id: 17, name :'Noix de coco'},
            { id: 18, name :'Raisins'},
            { id: 19, name :'Fraises des bois'},
            { id: 20, name :'Mûres'},
            { id: 21, name :'Framboises'},
            { id: 22, name :'Groseilles'},
            { id: 23, name :'Cassis'},
            { id: 24, name :'Myrtilles'},
            { id: 25, name :'Bleuets'},
            { id: 26, name :'Pamplemousses'},
            { id: 27, name :'Citrons'},
            { id: 28, name :'Limes'},
            { id: 29, name :'Oranges sanguines'},
            { id: 30, name :'Pomelos'},
            { id: 31, name :'Mandarines'},
            { id: 32, name :'Clementines'},
            { id: 33, name :'Tangerines'},
            { id: 34, name :'Satsumas'},
            { id: 35, name :'Oranges douces'},
            { id: 36, name :'Pomelos roses'},
            { id: 37, name :'Grapefruits jaunes'},
            { id: 38, name :'Grapefruits roses'},
            { id: 39, name :'Abricots'},
            { id: 40, name :'Pêches jaunes'},
            { id: 41, name :'Pêches roses'},
            { id: 42, name :'Pêches blanches'},
            { id: 43, name :'Nectarines'},
            { id: 44, name :'Prunes'},
            { id: 45, name :'Reines-claudes'},
            { id: 46, name :'Mirabelles'},
            { id: 47, name :'Abricots secs'},
            { id: 48, name :'Pruneaux'},
            { id: 49, name :'Amandes'},
            { id: 50, name :'Noix'},
            { id: 51, name :'Noisettes'},
            { id: 52, name :'Marrons'},
            { id: 53, name :'Noix de macadamia'},
            { id: 54, name :'Noix de cajou'},
            { id: 55, name :'Noix de pécan'},
            { id: 56, name :'Noix de coco'},
            { id: 57, name :'Noix de Grenoble'},
            { id: 58, name :'Noix de Brésil'},
            { id: 59, name :'Noix de velours'},
            { id: 60, name :'Noix de St-Jacques'},
            { id: 61, name :'Noix de pinyon'},
            { id: 62, name :'Ananas'},
            { id: 63, name :'Mangues'},
            { id: 64, name :'Papayes'},
            { id: 65, name :'Litchis'},
            { id: 66, name :'Longans'},
            { id: 67, name :'Durians'},
            { id: 68, name :'Ramboutans'},
            { id: 69, name :'Feijoas'},
            { id: 70, name :'Carambolas'},
            { id: 71, name :'Melons'},
            { id: 72, name :'Melons cantaloup'},
            { id: 73, name :'Melons honeydew'},
            { id: 74, name :'Pastèques'},
            { id: 75, name :'Coco'},
            { id: 76, name :'Anones'},
            { id: 77, name :'Cactus'},
            { id: 78, name :'Cédrats'},
            { id: 79, name :'Citrons verts'},
            { id: 80, name :'Citrons jaunes'},
            { id: 81, name :'Limes vertes'},
            { id: 82, name :'Limes jaunes'},
            { id: 83, name :'Mandarines'},
            { id: 84, name :'Oranges'},
            { id: 85, name :'Oranges sanguines'},
            { id: 86, name :'Pomelos'},
            { id: 87, name :'Tangerines'},
            { id: 88, name :'Satsumas'},
            { id: 89, name :'Abricots'},
            { id: 90, name :'Pêches jaunes'},
            { id: 91, name :'Pêches roses'},
            { id: 92, name :'Pêches blanches'},
            { id: 93, name :'Nectarines'},
            { id: 94, name :'Prunes'},
            { id: 95, name :'Reines-claudes'},
            { id: 96, name :'Mirabelles'},
            { id: 97, name :'Abricots secs'},
            { id: 98, name :'Pruneaux'},
            { id: 99, name :'Amandes'},
            { id: 100, name :'Noix'},
            { id: 101, name :'Noisettes'},
            { id: 102, name :'Marrons'},
            { id: 103, name :'Noix de macadamia'},
            { id: 104, name :'Noix de cajou'},
            { id: 105, name :'Noix de pécan'},
            { id: 106, name :'Noix de coco'},
            { id: 107, name :'Noix de Grenoble'},
            { id: 108, name :'Noix de Brésil'},
            { id: 109, name :'Noix de velours'},
            { id: 110, name :'Noix de St-Jacques'},
            { id: 111, name :'Noix de pinyon'}
        ]
      }
    }

  }
</script>

<template>
    <h6 class="m-3">Fruits :</h6>
    <div class="container">
        <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
            <div class="form-check mx-4 mt-1" v-for="item in fruits" :key="item.id">
                <div class="col">
                    <input class="form-check-input" type="checkbox" value="" id="flexCheckIndeterminate">
                    <label class="form-check-label" for="'receipeType' + item.id">
                    {{ item.name }}
                    </label>
                </div>
            </div>
        </div> 
    </div>
</template>