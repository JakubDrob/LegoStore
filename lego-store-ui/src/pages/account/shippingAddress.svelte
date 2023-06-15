<script lang="ts">
import { Button, Card, Input, Label } from "flowbite-svelte";
import { onMount } from 'svelte'
import { redirect, goto } from "@roxi/routify";
import { validate_component } from "svelte/internal";
import { setCookie, getCookie } from 'svelte-cookie';

let stripe = null


let inputFields = []
let saveAddressCheckBox = false;
// let email = "getCookie('email')"
//TEST
let email = "blabla@gmail.com"

let inputClass = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500";

let info = {
"FirstName":"",
"LastName":"",
"StreetName":"",
"StreetNo":"",
"AppartmentNo":"",
"PostCode":"",
"City":"",
"Country":"",
"Email":""
}


onMount(async () => {
    getAddressData();
});

function getAddressData(){
    fetch("http://legostorebackend.azurewebsites.net/api/cart/getAddress/", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(email)
        })
        .then(response => {
            if (response.ok) {
              response.json().then(data => {
                console.log(data);
                info["FirstName"] = data.data.FirstName
                info["LastName"] = data.data.LastName
                info["StreetName"] = data.data.StreetName
                info["StreetNo"] = data.data.StreetNo
                info["AppartmentNo"] = data.data.AppartmentNo
                info["PostCode"] = data.data.PostCode
                info["City"] = data.data.City
                info["Country"] = data.data.Country
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

function finalizePayment(){
    if(isAnyBoxEmpty()){
        return;
    }
    else if(saveAddressCheckBox)
    {
        console.log("SAVING....")
        info['Email'] = email;
        fetch("http://legostorebackend.azurewebsites.net/api/cart/saveAddress/", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(info)
        })
        .then(response => {
            if (!response.ok) {
              response.json().then(data => {
                console.log(data);
              });
            }
        })
        .then(data => {
          console.log('Success:', data);

        })
        .catch(error => {
          console.error('Error:', error);
        });
    }
}

function isAnyBoxEmpty(){
    let grid = document.getElementById("grid");
    let i=0;
    let isEmpty = false;

    for(var infoField in info){
        if(infoField == "Email" || infoField == "AppartmentNo" ) continue;

        if(info[infoField] == "")
        {
            inputFields[i].style.borderColor = "red";
            inputFields[i].style.borderWidth = "2px";
             isEmpty = true;
        }
        else{
            inputFields[i].style.borderColor = "";
            inputFields[i].style.borderWidth = "";
        }
        i++;
    }

    return isEmpty
}

</script>

<main class="flex p-10 page-body justify-center items-center w-full">
    <Card class="w-9/12 min-h-fit min-w-fit">
        <h4 class="text-2xl font-bold mb-6 text-center">Dane do wysyłki</h4>
        <form>
            <div id="grid" class="grid gap-6 mb-1 md:grid-cols-2">
                <div>
                    <label for="first_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Imię</label>
                    <input 
                        bind:value={info["FirstName"]}
                        bind:this = {inputFields[0]}
                        type="text" 
                        id="first_name" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="John" required>
                </div>
                <div>
                    <label for="last_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Nazwisko</label>
                    <input 
                        bind:value={info["LastName"]}
                        bind:this = {inputFields[1]}
                        type="text" 
                        id="last_name" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Doe" required>
                </div>
                <div>
                    <label for="street" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Ulica</label>
                    <input 
                        bind:value={info["StreetName"]}
                        bind:this = {inputFields[2]}
                        type="text" 
                        id="company" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Piotrkowska" required>
                </div> 
                <div>
                    <label for="strNumber" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Numer ulicy</label>
                    <input 
                        bind:value={info["StreetNo"]}
                        bind:this = {inputFields[3]}
                        type="text" id="strNumber" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="50" required>
                </div>
                <div>
                    <label for="strNumber" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Numer mieszkania</label>
                    <input 
                        bind:value={info["AppartmentNo"]}
                        bind:this = {inputFields[4]}
                        type="text" id="strNumber" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="5A">
                </div>
                <div>
                    <label for="postal" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Kod pocztowy</label>
                    <input 
                        bind:value={info["PostCode"]}
                        bind:this = {inputFields[5]}
                        type="text" 
                        id="appNo" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="50-903" required>
                </div>
                <div>
                    <label for="city" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Miasto</label>
                    <input 
                        bind:value={info["City"]}
                        bind:this = {inputFields[6]}
                        type="text" 
                        id="first_name" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Lodz" required>
                </div>
                <div>
                    <label for="last_name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Państwo</label>
                    <input 
                        bind:value={info["Country"]}
                        bind:this = {inputFields[7]}
                        type="text" 
                        id="last_name"
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        placeholder="Poland" 
                        required>
                </div>
                <div class="flex items-center mb-4">
                    <input bind:value={saveAddressCheckBox} type="checkbox" class="w-4 h-4 border border-gray-300 rounded bg-gray-50 focus:ring-3 focus:ring-blue-300 dark:bg-gray-700 dark:border-gray-600 dark:focus:ring-blue-600 dark:ring-offset-gray-800">
                    <!-- svelte-ignore a11y-label-has-associated-control -->
                    <label id="saveAddress" class="ml-2 text-sm font-medium text-gray-900 dark:text-gray-300">Zapisz mój adres </label>
                </div>
            </div>

            <hr class="w-120 h-2 t-20 ">
            <h4 class="text-2xl font-bold mb-6 text-center">Dane do płatności</h4>

            <form>
              <input class={inputClass} type="text" name="card" id="card" placeholder="1234 5678 9012 3456">
              <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white" 
                for="text">Numer karty
              </label>
              <div id="grid" class="grid gap-6 mb-1 md:grid-cols-2">
                <div>
                  <input class = {inputClass} type="text" placeholder="MM/RR">
                  <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    for="text">Data waźności
                  </label>
                </div>
                <div>
                  <input class = {inputClass} type="number" placeholder="123">
                  <label class="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    for="text">CCV
                  </label>
                </div>
              </div>
            </form>

            {#if info["FirstName"] != "" && info["LastName"]!="" && info["StreetName"]!="" && info["AppartmentNo"] != "" && info["City"] != "" && info["PostCode"] != "" }
              <hr class="w-52 h-1 t-20 ">
              <h3 class="py-3 text-gray-900"> Adres rozliczeniowy</h3>
              <p class="text-gray-600 text-sm ">{info["FirstName"]} {info["LastName"]},</p>
              <p class="text-gray-600 text-sm">{info["StreetName"]} {info["StreetNo"]} m.{info["AppartmentNo"]},</p>
              <p class="text-gray-600 text-sm pb-8">{info["City"]}, {info["PostCode"]}</p>
            {/if}

            <Button on:click={()=>{finalizePayment()}} class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Kontynuuj</Button>
        </form>
    </Card>
</main>
   

<style>
.page-body {
    background-image:  url('../../assets/background.jpg');
    background-repeat: no-repeat;
    background-size: cover;
  }
</style>