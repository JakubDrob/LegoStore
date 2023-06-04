<script lang="ts">
    import { Card } from "flowbite-svelte";
    import type { Product } from "../../lib/models";
    import ProductItem from "../../lib/ProductItem.svelte";
    import { getProducts } from "../../lib/services";

    let products: Product[] = [];

    getProducts()
    .then(x => {
        // temporary until image will be available from backend
        // x.forEach(item => item.imgUrl = "2.webp"); 
        console.log(x)
        products = x;
        console.log(products)
        // console.log(products[0].image)
    })

</script>

<main class="grid gap-8 lg:grid-cols-3 w-full pt-5 justify-items-center page-body">
    {#each products as item}
        <ProductItem product={item} />
    {/each}
</main>


<style>
    .page-body {
      background-image:  url('../../assets/background.jpg');
      background-repeat: no-repeat;
      background-size: cover;
    }
  </style>
  