<script lang="ts">
    import { Button, Card } from "flowbite-svelte";
    import type { Product } from "./models";
    import { createEventDispatcher } from "svelte";

    export let product: Product
    const dispatchAddedToCart = createEventDispatcher<{addedToCart: {productId: number}}>();
    function addToCart(){
        dispatchAddedToCart('addedToCart', { productId: product.id });

    }
</script>

<Card class="w-full h-fit">
    <div class="img-wrapper">
        <img class="p-8" src={product.image} alt="product 1" />
    </div>
    <div>
        <div>{product.name}</div>
        <div class="py-2">
            <span class="font-bold">{product.price} zł</span>
        </div>
        <div>
            <Button on:click={addToCart} >Dodaj do koszyka</Button>
        </div>
    </div>
</Card>

<style scoped>
    .img-wrapper{
        aspect-ratio: 1;
        height: 100%;
    }

    .img-wrapper > img{
        object-fit: contain;
        float: left;
        width:  450px;
        height: 350px;
        object-fit: cover;
    }
</style>