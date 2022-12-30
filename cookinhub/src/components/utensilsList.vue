<script>
export default {
    name: 'CookinHubUtensils',
    data() {
      return {
        utensils: [
            { id: 1, name :'Couteau de cuisine'},
            { id: 2, name :'Fourchette'},
            { id: 3, name :'Cuillère à soupe'},
            { id: 4, name :'Cuillère à dessert'},
            { id: 5, name :'Louche'},
            { id: 6, name :'Spatule'},
            { id: 7, name :'Pince à épiler'},
            { id: 8, name :'Économe'},
            { id: 9, name :'Couteau à désosser'},
            { id: 10, name :'Couteau à pain'},
            { id: 11, name :'Couteau à éplucher'},
            { id: 12, name :'Couteau à beurre'},
            { id: 13, name :'Couteau à découper'},
            { id: 14, name :'Couteau à légumes'},
            { id: 15, name :'Couteau à filet'},
            { id: 16, name :'Couteau à viande'},
            { id: 17, name :'Couteau à fromage'},
            { id: 18, name :'Couteau à huîtres'},
            { id: 19, name :'Couteau à tarte'},
            { id: 20, name :'Couteau à gâteau'},
            { id: 21, name :'Couteau à jambon'},
            { id: 22, name :'Couteau à sushi'},
            { id: 23, name :'Couteau à châtaignes'},
            { id: 24, name :'Couteau à poisson'},
            { id: 25, name :'Couteau à découper les volailles'},
            { id: 26, name :'Couteau à découper les viandes'},
            { id: 27, name :'Couteau à découper les légumes'},
            { id: 28, name :'Couteau à découper les fruits'},
            { id: 29, name :'Plat à gratin'},
            { id: 30, name :'Plat à tarte'},
            { id: 31, name :'Plat à cake'},
            { id: 32, name :'Plat à quiche'},
            { id: 33, name :'Plat à lasagne'},
            { id: 34, name :'Plat à roast-beef'},
            { id: 35, name :'Plat à pie'},
            { id: 36, name :'Plat à gratin dauphinois'},
            { id: 37, name :'Plat à gratin savoyard'},
            { id: 38, name :'Casserole'},
            { id: 39, name :'Sauteuse'},
            { id: 40, name :'Faitout'},
            { id: 41, name :'Poêle'},
            { id: 42, name :'Wok'},
            { id: 43, name :'Grillade'},
            { id: 44, name :'Plancha'},
            { id: 45, name :'Poêle à crêpes'},
            { id: 46, name :'Poêle à omelette'},
            { id: 47, name :'Poêle à crèpes'},
            { id: 48, name :'Poêle à frire'},
            { id: 49, name :'Mouli-légumes'},
            { id: 50, name :'Presse-purée'},
            { id: 51, name :'Épluche-légumes'},
            { id: 52, name :'Épluche-pommes de terre'},
            { id: 53, name :'Épluche-carottes'},
            { id: 54, name :'Râpe'},
            { id: 55, name :'Grattoir'},
            { id: 56, name :'Coupe-légumes'},
            { id: 57, name :'Coupe-fruits'},
            { id: 58, name :'Écumoire'},
            { id: 59, name :'Passoire'},
            { id: 60, name :'Chinois'},
            { id: 61, name :'Passoire à légumes'},
            { id: 62, name :'Passoire à fruits'},
            { id: 63, name :'Spatule en silicone'},
            { id: 64, name :'Spatule en bois'},
            { id: 65, name :'Spatule en métal'},
            { id: 66, name :'Spatule à cake'},
            { id: 67, name :'Spatule à gâteau'},
            { id: 68, name :'Spatule à crème'},
            { id: 69, name :'Spatule à mayonnaise'},
            { id: 70, name :'Spatule à glace'},
            { id: 71, name :'Cuillère en bois'},
            { id: 72, name :'Cuillère en métal'},
            { id: 73, name :'Cuillère à crème'},
            { id: 74, name :'Cuillère à mayonnaise'},
            { id: 75, name :'Cuillère à glace'},
            { id: 76, name :'Fouet'},
            { id: 77, name :'Batteur'},
            { id: 78, name :'Mixeur'},
            { id: 79, name :'Blender'},
            { id: 80, name :'Robot culinaire'},
            { id: 81, name :'Hachoir'},
            { id: 82, name :'Mijoteuse'},
            { id: 83, name :'Machine à pain'},
            { id: 84, name :'Machine à pâtes'},
            { id: 85, name :'Machine à glace'},
            { id: 86, name :'Tasse à mesurer'},
            { id: 87, name :'Verre à mesurer'},
            { id: 88, name :'Balance'},
            { id: 89, name :'Thermomètre'},
            { id: 90, name :'Minuteur'},
            { id: 91, name :'Grille-pain'},
            { id: 92, name :'Cafetière'},
            { id: 93, name :'Théière'},
            { id: 94, name :'Bouilloire'},
            { id: 95, name :'Planche à découper'},
            { id: 96, name :'Planche à hacher'},
            { id: 97, name :'Planche à sushi'},
            { id: 98, name :'Planche à fromage'},
            { id: 99, name :'Planche à pain'}
            ]
        }
    }

}
</script>

<template>
    <div class="container m-3">
        <div class="row row-cols-2 row-cols-lg-5 g-2 g-lg-3">
            <div class="form-check mx-4 mt-1" v-for="item in utensils" :key="item.id">
                <div class="col">
                    <input class="form-check-input" type="checkbox" name="utensils" id="'utensil' + item.id" value="item.name" v-model="item.selected">
                    <label class="form-check-label" for="'utensil' + item.id">
                    {{ item.name }}
                    </label>
                </div>
            </div>
        </div> 
    </div>
</template>