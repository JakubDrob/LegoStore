<script lang="ts">
    import type { Product } from "../../lib/models";
    import ProductItem from "../../lib/ProductItem.svelte";
    import { getProducts } from "../../lib/services";
    import { Button, Card, Input, Label } from "flowbite-svelte";

    let products: Product[] = [];
    let searchText = {"searchPhrase" : ""};
    let searchBar;

    getProducts()
    .then(x => {
        // temporary until image will be available from backend
        // x.forEach(item => item.imgUrl = "2.webp"); 
        console.log(x)
        products = x;
        console.log(products)
        // console.log(products[0].image)
    })

    function getSearchFromBackend(){
        console.log("Sending search phrase:")
        console.log(searchText["searchPhrase"])
        
        fetch("http://127.0.0.1:5000/products/search/", {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(searchText)
        })
        .then(response => {
            if (response.ok) {
            response.json().then(data => {
                console.log(data)
                products = data;
                console.log("kength: ", Object.keys(products).length)
                console.log("Products[0]: ", products["products"][0])
            });
            }
        })
        .then(data => {
        console.log('Message:', data);

        })
        .catch(error => {
        console.error('Error:', error);
        });
    }

</script>

<main class="page-body">
    <div class=" py-3 flex justify-center bg-transparent">
        <form class="w-3/5">   
            <label for="default-search" class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-white">Search</label>
            <div class="relative">
                <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
                    <svg aria-hidden="true" class="w-5 h-5 text-gray-500 dark:text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path></svg>
                </div>
                <input 
                    bind:value={searchText["searchPhrase"]}
                    bind:this = {searchBar}
                    type="search" 
                    id="default-search" 
                    class="block w-full p-4 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Szukaj..." required>
                <Button on:click={()=>{getSearchFromBackend()}} class="text-white absolute right-2.5 bottom-2.5 bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-2 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Search</Button>
            </div>
        </form>
    </div>
    <div class="grid gap-8 lg:grid-cols-3 w-full py-5 justify-items-center">
        {#if Object.keys(products).length == 1}
            <ProductItem product={products["products"][0]} />
        {:else}
            {#each products as item}
                <ProductItem product={item} />
            {/each}
        {/if}
    </div>
</main>


<style>
    .page-body {
      background-image:  url('../../assets/background.jpg');
      background-repeat: no-repeat;
      background-size: cover;
    }
  </style>
  