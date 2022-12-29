<script>
export default {
	name: 'CookinHubNav',
    props:{
        title : String
    }
}
</script>

<template>
    <div>
        <div class="h1 bg-warning p-1 m-0"><router-link to="/" class="link-dark text-decoration-none">{{  title  }}</router-link></div>
    </div>
</template>
