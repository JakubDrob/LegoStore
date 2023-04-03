<script lang="ts">
    import { Card } from "flowbite-svelte";
    import type { Product } from "../../lib/models";
    import ProductItem from "../../lib/ProductItem.svelte";
    import { getProducts } from "../../lib/services";

    let products: Product[] = [];

    getProducts()
    .then(x => {
        // temporary until image will be available from backend
        x.forEach(item => item.imgUrl = "2.webp"); 
        products = x;
    })

</script>

<main class="grid gap-8 lg:grid-cols-3 w-full justify-items-center">
    {#each products as item}
        <ProductItem product={item} />
    {/each}
</main>

<style scoped>
    /* main{
        max-width: 1000px;
    } */
</style>