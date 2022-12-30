<script>
export default {
    name: 'CookinHubIngredients',   
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
        ],
        vegetables : [
            { id: 112, name :'Tomates'},
            { id: 113, name :'Carottes'},
            { id: 114, name :'Poivrons'},
            { id: 115, name :'Épinards'},
            { id: 116, name :'Champignons'},
            { id: 117, name :'Aubergines'},
            { id: 118, name :'Brocolis'},
            { id: 119, name :'Panais'},
            { id: 120, name :'Courgettes'},
            { id: 121, name :'Oignons'},
            { id: 122, name :'Pommes de terre'},
            { id: 123, name :'Chou-fleur'},
            { id: 124, name :'Haricots verts'},
            { id: 125, name :'Petits pois'},
            { id: 126, name :'Artichauts'},
            { id: 127, name :'Asperges'},
            { id: 128, name :'Betteraves'},
            { id: 129, name :'Céleri'},
            { id: 130, name :'Concombres'},
            { id: 131, name :'Courges'},
            { id: 132, name :'Epinards'},
            { id: 133, name :'Fenouil'},
            { id: 134, name :'Laitues'},
            { id: 135, name :'Navets'},
            { id: 136, name :'Oignons verts'},
            { id: 137, name :'Poireaux'},
            { id: 138, name :'Radis'},
            { id: 139, name :'Salades'},
            { id: 140, name :'Cresson'},
            { id: 141, name :'Endives'}
        ],
        starchyFoods : [
            { id: 142, name :'Riz'},
            { id: 143, name :'Pâtes'},
            { id: 144, name :'Pommes de terre'},
            { id: 145, name :'Quinoa'},
            { id: 146, name :'Couscous'},
            { id: 147, name :'Polenta'},
            { id: 148, name :'Maïs'},
            { id: 149, name :'Millet'},
            { id: 150, name :'Sarrasin'},
            { id: 151, name :'Orge'},
            { id: 152, name :'Avoine'},
            { id: 153, name :'Seigle'},
            { id: 154, name :'Blé'},
            { id: 155, name :'Épeautre'},
            { id: 156, name :'Kamut'},
            { id: 157, name :'Pois chiches'},
            { id: 158, name :'Haricots rouges'},
            { id: 159, name :'Haricots blancs'},
            { id: 160, name :'Haricots mungo'},
            { id: 161, name :'Haricots noirs'},
            { id: 162, name :'Lentilles'},
            { id: 163, name :'Fèves'},
            { id: 164, name :'Pois cassés'},
            { id: 165, name :'Pois chiches'},
            { id: 166, name :'Pois verts'}
        ],
        meats :[
            { id: 167, name :'Bœuf'},
            { id: 168, name :'Porc'},
            { id: 169, name :'Poulet'},
            { id: 170, name :'Agneau'},
            { id: 171, name :'Dinde'},
            { id: 172, name :'Veau'},
            { id: 173, name :'Chevreau'},
            { id: 174, name :'Mouton'},
            { id: 175, name :'Agneau'},
            { id: 176, name :'Venaison'},
            { id: 177, name :'Gibier'},
            { id: 178, name :'Lapin'},
            { id: 179, name :'Canard'},
            { id: 180, name :'Oie'},
            { id: 181, name :'Pigeon'},
            { id: 182, name :'Pintade'},
            { id: 183, name :'Faisan'},
            { id: 184, name :'Perdrix'},
            { id: 185, name :'Gésier'},
            { id: 186, name :'Foie'},
            { id: 187, name :'Ris de veau'},
            { id: 188, name :'Langue'},
            { id: 189, name :'Oreilles'},
            { id: 190, name :'Tendons'},
            { id: 191, name :'Queue'},
            { id: 192, name :'Cervelles'},
            { id: 193, name :'Cervelle de veau'},
            { id: 194, name :'Jambon'},
            { id: 195, name :'Lard'},
            { id: 196, name :'Poitrine'},
            { id: 197, name :'Jambon cru'},
            { id: 198, name :'Jambon cuit'},
            { id: 199, name :'Jambon fumé'},
            { id: 200, name :'Jambon blanc'},
            { id: 201, name :'Jambon noir'}
        ],
        spices : [
            { id: 202, name :'Curry'},
            { id: 203, name :'Cumin'},
            { id: 204, name :'Coriandre'},
            { id: 205, name :'Paprika'},
            { id: 206, name :'Poivre'},
            { id: 207, name :'Gingembre'},
            { id: 208, name :'Cannelle'},
            { id: 209, name :'Curcuma'},
            { id: 210, name :'Fenouil'},
            { id: 211, name :'Cardamome'}
        ],
        herbs : [
            { id: 212, name :'Persil'},
            { id: 213, name :'Basilic'},
            { id: 214, name :'Coriandre'},
            { id: 215, name :'Ciboulette'},
            { id: 216, name :'Menthe'},
            { id: 217, name :'Origan'},
            { id: 218, name :'Persil'},
            { id: 219, name :'Romarin'},
            { id: 220, name :'Thym'}
        ],
        legumes : [
            { id: 221, name :'Haricots'},
            { id: 222, name :'Pois chiches'},
            { id: 223, name :'Lentilles'},
            { id: 224, name :'Fèves'},
            { id: 225, name :'Pois cassés'},
            { id: 226, name :'Pois chiches'},
            { id: 227, name :'Pois verts'},
            { id: 228, name :'Lentilles vertes'},
            { id: 229, name :'Lentilles rouges'},
            { id: 230, name :'Lentilles jaunes'},
            { id: 231, name :'Haricots blancs'},
            { id: 232, name :'Haricots rouges'},
            { id: 233, name :'Haricots noirs'},
            { id: 234, name :'Haricots mungo'},
            { id: 235, name :'Haricots de soja'},
            { id: 236, name :'Haricots azuki'},
            { id: 237, name :'Haricots adzuki'},
            { id: 238, name :'Haricots de Lima'},
            { id: 239, name :'Haricots de navy'},
            { id: 240, name :'Haricots de pinto'},
            { id: 241, name :'Haricots de cranberry'},
            { id: 242, name :'Haricots blancs coco'},
            { id: 243, name :'Haricots roses'},
            { id: 244, name :'Haricots verts'},
            { id: 245, name :'Haricots jaunes'}
        ]
      }
    }

  }
</script>

<template>
    <h6 class="m-3">Viandes :</h6>
    <div class="container">
        <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
            <div class="form-check mx-4 mt-1" v-for="item in meats" :key="item.id">
                <div class="col">
                    <input class="form-check-input" type="checkbox" name="ingredients" id="'ingredient' + item.id" value="item\.name"  v-model="item.selectedIngredients" >
                    <label class="form-check-label" for="'ingredient' + item.id">
                    {{ item.name }}
                    </label>
                </div>
            </div>
        </div> 
    </div>

    <h6 class="m-3">Legumes :</h6>
    <div class="container">
        <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
            <div class="form-check mx-4 mt-1" v-for="item in fruits" :key="item.id">
                <div class="col">
                    <input class="form-check-input" type="checkbox" name="ingredients" id="'ingredient' + item.id" value="item\.name" v-model="item.selectedIngredients">
                    <label class="form-check-label" for="'ingredient' + item.id">
                    {{ item.name }}
                    </label>
                </div>
            </div>
        </div> 
    </div>

    <h6 class="m-3">Fruits :</h6>
    <div class="container">
        <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
            <div class="form-check mx-4 mt-1" v-for="item in fruits" :key="item.id">
                <div class="col">
                    <input class="form-check-input" type="checkbox" name="ingredients" id="'ingredient' + item.id" value="item\.name" v-model="item.selectedIngredients">
                    <label class="form-check-label" for="'ingredient' + item.id">
                    {{ item.name }}
                    </label>
                </div>
            </div>
        </div> 
    </div>

    <h6 class="m-3">Féculents :</h6>
    <div class="container">
        <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
            <div class="form-check mx-4 mt-1" v-for="item in starchyFoods " :key="item.id">
                <div class="col">
                    <input class="form-check-input" type="checkbox" name="ingredients" id="'ingredient' + item.id" value="item\.name" v-model="item.selectedIngredients">
                    <label class="form-check-label" for="'ingredient' + item.id">
                    {{ item.name }}
                    </label>
                </div>
            </div>
        </div> 
    </div>
    
    <h6 class="m-3">Légumineuses :</h6>
    <div class="container">
        <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
            <div class="form-check mx-4 mt-1" v-for="item in legumes" :key="item.id">
                <div class="col">
                    <input class="form-check-input" type="checkbox" name="ingredients" id="'ingredient' + item.id" value="item\.name" v-model="item.selectedIngredients">
                    <label class="form-check-label" id="'ingredient' + item.id" >
                    {{ item.name }}
                    </label>
                </div>
            </div>
        </div> 
    </div>
       
    <h6 class="m-3">Epices :</h6>
    <div class="container">
        <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
            <div class="form-check mx-4 mt-1" v-for="item in spices" :key="item.id">
                <div class="col">
                    <input class="form-check-input" type="checkbox" name="ingredients" id="'ingredient' + item.id" value="item\.name" v-model="item.selectedIngredients">
                    <label class="form-check-label" id="'ingredient' + item.id" >
                    {{ item.name }}
                    </label>
                </div>
            </div>
        </div> 
    </div>

    <h6 class="m-3">Herbes :</h6>
    <div class="container">
        <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
            <div class="form-check mx-4 mt-1" v-for="item in herbs" :key="item.id">
                <div class="col">
                    <input class="form-check-input" type="checkbox" name="ingredients" id="'ingredient' + item.id" value="item\.name" v-model="item.selectedIngredients">
                    <label class="form-check-label" id="'ingredient' + item.id" >
                    {{ item.name }}
                    </label>
                </div>
            </div>
        </div> 
    </div>
</template>