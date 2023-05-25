<script lang="ts">
    import { Card } from "flowbite-svelte";
    import type { Product } from "./models";
    import ProductItem from "./ProductItem.svelte";
    import { getProducts } from "./services";

    let products: Product[] = [];

    getProducts()
    .then(x => {
        // temporary until image will be available from backend
        // x.forEach(item => item.imgUrl = "2.webp"); 
        console.log(x)
        products = x;
        console.log(products)
        console.log(products[0].image_path)
    })


    type ImageType = {
        title: string
        src: string
    }
    export let images: ImageType[]
    export const getItemId = (index: number) => `carousel-item-${index}`
</script>
<div class = "card">
    <h1 class="text-4xl text-left py-4 text-black-300">Polecane dla ciebie</h1>
    <ul class="flex overflow-x-auto gap-6 snap-x snap-mandatory py-4">
        {#each  products as item, index}
            <li id={getItemId(index)} class="relative shrink-0 snap-center shadow-lg">
                    <ProductItem product = {item}/>
            </li>
        {/each}
    </ul>
</div>

<style>
    img {
        float: left;
        width:  450px;
        height: 350px;
        object-fit: cover;
    }

    .page-body {
      background-image:  url('../assets/background.jpg');
      background-repeat: no-repeat;
      background-size: cover;
    }

    .card {
    /* Add shadows to create the "card" effect */
    border-radius: 20px;
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    transition: 0.3s;
    margin-bottom: 2rem;
    background-color: white;
    /* padding: 20px; */
    }

    /* On mouse-over, add a deeper shadow */
    .card:hover {
    box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
    }

    /* Add some padding inside the card container */
    .container {
    /* padding: 2px 16px; */
    }

</style>