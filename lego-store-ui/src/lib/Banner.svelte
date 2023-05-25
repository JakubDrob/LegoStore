<script lang="ts">
    import { Card, Button } from "flowbite-svelte";


    type BannerType = {
        src: string
    }

    export let banner:BannerType

</script>
<div class="w-full justify-center flex">
    <div class = "card max-w-full">
        <h1 class="text-4xl text-left py-4 text-black-300">Poznaj świat Indiana Jones</h1>
            <div class="relative">
                <img class="rounded-xl" src={banner.src} alt=""/>
                <div class="h-100">
                    <Button class="backdrop-blur-md bg-yellow-200 text-black text-xl absolute right-10 top-1/2 w-46 h-20">
                        Zobacz produkty !
                    </Button>
                </div>
            </div>
    </div>
</div>

<style>

    .card {
        /* Add shadows to create the "card" effect */
        border-radius: 20px;
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
        transition: 0.3s;
        margin-bottom: 2rem;
        background-color: white;
        /* padding: 20px; */
    }
</style>
