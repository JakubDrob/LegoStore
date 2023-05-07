<script lang="ts">
    import {
    Avatar,
        Button,
        Card,
        Listgroup,
    } from "flowbite-svelte";
    import CartItemQuantity from "../../lib/CartItemQuantity.svelte";
    import { goto } from "@roxi/routify";

    let cart = {
        items: [
            {
                productId: 1,
                title: "Lego Nintendo",
                quantity: 3,
                image:"1.webp",
                price: 55.55
            },
            {
                productId: 2,
                title: "Lego restauracja Ramen",
                quantity: 1,
                image:"restaurant.webp",
                price: 89.99
            },
            {
                productId: 3,
                title: "Lego sklep surferski",
                quantity: 1,
                image:"surfStore.webp",
                price: 39.99
            },
        ],
    };

    function onItemQuantityIncreased(productId: number, quantity: number){
        console.log({productId, quantity})
    }

    function onItemQuantityDescreased(productId: number, quantity: number){
        console.log({productId, quantity})
    }
</script>

<main class="w-full justify-items-center">
    <div class="grid gap-8 lg:grid-cols-3 p-4 max-w-7xl m-auto">
        <div class="col-span-2 w-full">
            <Card size="xl">
                <h5 class="text-xl font-bold">Twój Koszyk:</h5>
                <Listgroup items={cart.items} let:item class="border-0 dark:!bg-transparent">
                    <div class="w-full flex">
                        <Avatar src="/{item.image}" alt="" size="lg" rounded class="flex-shrink-0"/>
                        <div class="flex w-full justify-between items-center">
                            <div class="flex flex-col justify-center mx-5 gap-2">
                                <h5>{item.title}</h5>
                                <p>{item.price} zł</p>
                            </div>
                            <CartItemQuantity value={item.quantity} on:increment={q => onItemQuantityIncreased(item.productId, q.detail.value)} on:decrement={q => onItemQuantityDescreased(item.productId, q.detail.value)}/>
                        </div>
                    </div>
                </Listgroup>
            </Card>
        </div>
        <div>
            <Card class="summary-panel" size="xl">
                <h5 class="font-bold text-2xl my-2">Podsumowanie zamówienia</h5>
                <p class="my-2">Kwota zamówienia: 55.99 zł</p>
                <Button class="my-2" on:click={()=>{$goto('./shippingAddress');}}>
                    <svg
                        aria-hidden="true"
                        class="mr-2 -ml-1 w-5 h-5"
                        fill="currentColor"
                        viewBox="0 0 20 20"
                        xmlns="http://www.w3.org/2000/svg"
                        ><path
                            d="M3 1a1 1 0 000 2h1.22l.305 1.222a.997.997 0 00.01.042l1.358 5.43-.893.892C3.74 11.846 4.632 14 6.414 14H15a1 1 0 000-2H6.414l1-1H14a1 1 0 00.894-.553l3-6A1 1 0 0017 3H6.28l-.31-1.243A1 1 0 005 1H3zM16 16.5a1.5 1.5 0 11-3 0 1.5 1.5 0 013 0zM6.5 18a1.5 1.5 0 100-3 1.5 1.5 0 000 3z"
                        /></svg
                    >
                    Przejdź do płatności
                </Button>
            </Card>
        </div>
    </div>
</main>

<style scoped>
    main {
        background-image: url("../../assets/background.jpg");
        background-repeat: no-repeat;
        background-size: cover;
    }
</style>
