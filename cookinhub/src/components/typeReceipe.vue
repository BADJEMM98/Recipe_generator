   
<script>


export default {
    name: 'CookinHubTypeReceipe',
    
    data() {
      return {
        items: [
          { id: 1, name: 'Plat principal' },
          { id: 2, name: 'Entrées' },
          { id: 3, name: 'Dessert' },
          { id: 2, name: 'Sauce' },
          { id: 3, name: 'Accompagnement' },
          { id: 2, name: 'Boisson' }
        ]
      }
    }

  }

</script>

<template>
    <div class="d-flex justify-content-around">
        <div class="form-check mt-1" v-for="item in items" :key="item.id" >
            <input class="form-check-input" type="radio" name="receipeType" id="'receipeType' + item.id" value="'receipeType' + item.id" checked>
            <label class="form-check-label" for="'receipeType' + item.id">
            {{ item.name }}
            </label>
        </div>
    </div>
</template>
