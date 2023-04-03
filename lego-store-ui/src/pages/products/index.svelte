<script lang="ts">
    import type { Product } from "../../lib/models";
    import ProductItem from "../../lib/ProductItem.svelte";

    const items: Product[] = [
        {
            title: "Lego product 1 ale to jest dłuższe niż normalnie",
            imgUrl: "1.webp",
            price: 5.50,
            id: "nfwjfw"
        },
        {
            title: "Lego product 2",
            imgUrl: "2.webp",
            price: 7.30,
            id: "ada"
        },
        {
            title: "Lego product 3",
            imgUrl: "3.webp",
            price: 9.10,
            id: "gffff"
        },
        {
            title: "Lego product 3",
            imgUrl: "3.webp",
            price: 3.30,
            id: "adadafff"
        },
        {
            title: "Lego product 3",
            imgUrl: "3.webp",
            price: 2.10,
            id: "fwhfwnf"
        }
    ]

</script>

<main class="grid gap-8 lg:grid-cols-3 w-full justify-items-center p-4">
    {#each items as item}
        <ProductItem product={item} />
    {/each}
</main>
