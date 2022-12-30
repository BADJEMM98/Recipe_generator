<script>
export default {
    name: 'CookinHubTypeReceipe',

    data() {
      return {
        items: [
          { id: 1, name: 'Plat principal' },
          { id: 2, name: 'Entrées' },
          { id: 3, name: 'Dessert' },
          { id: 4, name: 'Sauce' },
          { id: 5, name: 'Accompagnement' },
          { id: 6, name: 'Boisson' }
        ],
      }
    }
  }

</script>

<template>
 <div class="d-flex justify-content-around flex-wrap">
    <div class="form-check mt-1" v-for="item in items" :key="item.id" >
    <input class="form-check-input" type="radio" :name="selectedType" :id="'receipeType' + item.id" v-bind:value="item.name" v-model="selectedType">
        <label class="form-check-label" for="'receipeType' + item.id">
        {{ item.name }}
        </label>
    </div>
 </div>
</template>
