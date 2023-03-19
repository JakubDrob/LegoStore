<script lang="ts">
    import { Button, Card } from "flowbite-svelte";
    import type { Product } from "./models";

    export let product: Product

</script>

<Card class="w-full">
    <div class="img-wrapper">
        <img class="p-8" src={product.imgUrl} alt="product 1" />
    </div>
    <div>
        <div>{product.title}</div>
        <div class="py-2">
            <span class="font-bold">{product.price} zł</span>
        </div>
        <div>
            <Button>Dodaj do koszyka</Button>
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
    }
</style>