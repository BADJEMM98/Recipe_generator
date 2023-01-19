<script>
export default {
	name: 'CookinHubNav',
    props:{
        title : String
    }
}
</script>
<style>
.h1:hover {
  transform:scale(1.08);
}
</style>
<template>
    <div>
        <div class="h1 bg-warning p-4 m-0"><router-link to="/" class="link-dark text-decoration-none m-2 p-4">{{  title  }}</router-link></div>
    </div>
</template>
