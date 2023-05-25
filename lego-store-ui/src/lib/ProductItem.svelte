<script lang="ts">
    import { Button, Card } from "flowbite-svelte";
    import type { Product } from "./models";

    export let product: Product

</script>

<Card class="w-full">
    <div class="img-wrapper">
        <img class="p-8" src={product.image_path} alt="product 1" />
    </div>
    <div>
        <div>{product.name}</div>
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
        float: left;
        width:  450px;
        height: 350px;
        object-fit: cover;
    }
</style>