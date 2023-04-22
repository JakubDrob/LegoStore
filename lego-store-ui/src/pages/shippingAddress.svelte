<script>
import { Button, Card, Input, Label } from "flowbite-svelte";

  let info = {
    "First Name":"",
    "Last Name":"",
    "Phone Number":"",
    "Street Name":"",
    "Street Number":"",
    "Postal Code":"",
    "City":"",
    "Country":""
  }
</script>

<main class="flex p-10 page-body justify-center items-center w-full">
    <Card class="w-9/12 min-h-fit min-w-fit">
    <p>{info["First Name"]} {info["Last Name"]}</p>
        <div class="grid grid-rows-4 grid-flow-col gap-4 p-5">
          {#each Object.keys(info) as field}
          <div class="flex flex-row py-2 px-2">
                <div>
                    <Input bind:value={info[field]} class="" placeholder={field} type={(field==="Phone Number" || field ==="Street Number")?"number":"text"} />
                </div>
          </div>
          {/each}
        </div>
    </Card>
</main>

  
  
   

<style>
.page-body {
    background-image:  url('../assets/background.jpg');
    background-repeat: no-repeat;
    background-size: cover;
  }
</style>
