<script lang="ts">
    import { Button, Card, Input, Label } from "flowbite-svelte";
    import { onMount } from 'svelte'
    import { redirect, goto } from "@roxi/routify";
    import { validate_component } from "svelte/internal";
    import { setCookie, getCookie } from 'svelte-cookie';
    import { Toast } from 'flowbite-svelte';
    
    let stripe = null
    
    
    let inputFields = []
    let saveAddressCheckBox = false;
    let email = "blabla@gmail.com"
    let avatar;
    let fileinput;
    let isEmptyAvatar = false;
    let notification = false;

    // console.log("Avatar: ", avatar);
    
    let info = {
        "Name": "",
        "SetNo": "",
        "Price": "",
        "Description": "",
        "Image": "",
        "Availability": 0,
        "ReleaseDate": "",
        "PieceCount": 0,
        "ProductTypeID": 0
    }

    function saveProduct() {
        if (isAnyBoxEmpty()) {
            return;
        }
        else{
            info["Image"] = avatar;
            console.log("SAVING....")
            fetch("http://legostorebackend.azurewebsites.net/addProduct", {
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
                for (var i in info) {
                    info[i] = "";
                }
                avatar = undefined;
                showSuccessNotification();
                
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    }


    
    function isAnyBoxEmpty() {
        let grid = document.getElementById("grid");
        let i = 0;
        let isEmpty = false;
    
        for (var infoField in info) {
            if (infoField == "Image" || infoField == "Availability" || infoField == "Description") 
            {
                i++;
                continue;
            }
    
            if (info[infoField] == "") {
                console.log(infoField, info[infoField])
                inputFields[i].style.borderColor = "red";
                inputFields[i].style.borderWidth = "2px";
                isEmpty = true;
            }
            else {
                inputFields[i].style.borderColor = "";
                inputFields[i].style.borderWidth = "";
            }
            i++;
        }

        if( avatar == undefined)
        {
            isEmpty = true;
            isEmptyAvatar = true;
        }
        else
        {
            isEmptyAvatar = false;
        }
    
        console.log("isEmpty: ",isEmpty)
        return isEmpty;
    }

	const onFileSelected =(e)=>{
            let image = e.target.files[0];
            let reader = new FileReader();
            reader.readAsDataURL(image);
            reader.onload = e => {
                avatar = e.target.result
                // console.log(avatar);
            };
    }

    async function showSuccessNotification()
    {
        console.log(notification);
        notification = true;
        await delay(2000);
        console.log(notification);
        notification = false;
    }

    function delay(ms: number) {
    return new Promise( resolve => setTimeout(resolve, ms) );
    }
</script>

<main class="flex p-10 page-body justify-center items-center w-full">
    <Card class="w-9/12 min-h-fit min-w-fit">
        <!-- <Button on:click={bla}> Test</Button> -->
        <h4 class="text-2xl font-bold mb-6 text-center">Dane produktu</h4>
        <form>
            <div id="grid" class="grid gap-6 mb-1 md:grid-cols-2">
                <div>
                    <label for="name" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Nazwa</label>
                    <input 
                        bind:value={info["Name"]}
                        bind:this={inputFields[0]}
                        type="text" 
                        id="name" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                        placeholder="Product Name" 
                        required
                    >
                </div>
                <div>
                    <label for="set_no" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Numer zestawu</label>
                    <input 
                        bind:value={info["SetNo"]}
                        bind:this={inputFields[1]}
                        type="text" 
                        id="set_no" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                        placeholder="Set Number" 
                        required
                    >
                </div>
                <div>
                    <label for="price" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Cena</label>
                    <input 
                        bind:value={info["Price"]}
                        bind:this={inputFields[2]}
                        type="text" 
                        id="price" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                        placeholder="Price" 
                        required
                    >
                </div>
                <div>
                    <label for="availability" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Liczba sztuk</label>
                    <input 
                        bind:value={info["Availability"]}
                        bind:this={inputFields[4]}
                        type="number" 
                        id="availability" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                        placeholder="Availability" 
                        required
                    >
                </div>
                <div>
                    <label for="release_date" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Data wydania</label>
                    <input 
                        bind:value={info["ReleaseDate"]}
                        bind:this={inputFields[6]}
                        type="date" 
                        id="release_date" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                        placeholder="Release Date" 
                        required
                    >
                </div>
                <div>
                    <label for="piece_count" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Liczba elementów</label>
                    <input 
                        bind:value={info["PieceCount"]}
                        bind:this={inputFields[7]}
                        type="number" 
                        id="piece_count" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                        placeholder="Piece Count" 
                        required
                    >
                </div>
                <div>
                    <label for="product_type_id" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Typ produktu</label>
                    <select 
                        bind:value={info["ProductTypeID"]}
                        bind:this={inputFields[8]}
                        id="product_type_id" 
                        class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        required
                    >
                        <option value="1">Figurka</option>
                        <option value="2">Zestaw</option>
                        <option value="3">Klocki</option>
                        <option value="4">Gra planszowa</option>
                    </select>
                </div>
                <div id="app">
                        <!-- <label  class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Dodaj zdjecie</label> -->
                        {#if avatar != undefined}
                            <Button class="" on:click={()=>{fileinput.click();}} >Zmień zdjecie</Button>
                        {:else}
                            <Button class="" on:click={()=>{fileinput.click();}} >Dodaj zdjecie</Button>
                        {/if}
                        <input style="display:none" type="file" accept=".webp, .jpg, .jpeg, .png" on:change={(e)=>onFileSelected(e)} bind:this={fileinput} >
                        {#if isEmptyAvatar}
                            <p class = "text-xs font-semibold text-red-700"> Zdjęcie jest wymagane !</p>
                        {/if}
                
                </div>
        </form>
        <div class="w-full felx  justify-center">
            <label for="description" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Opis</label>
            <textarea 
                bind:value={info["Description"]}
                bind:this={inputFields[3]}
                id="description" 
                rows="3" 
                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                placeholder="Description" 
                required
            ></textarea>
        </div>

        <div class="flex justify-center">
            {#if avatar != undefined}
            <img class="avatar" src="{avatar}" alt="d" />
            {/if}
        </div>
        {#if notification}
        <div class = "flex justify-center">
            <Toast color="green">
                <svelte:fragment slot="icon">
                <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path></svg>
                <span class="sr-only">Check icon</span>
                </svelte:fragment>
                Przedmiot dodany do bazy
            </Toast>
        </div>
        {/if}

        <div class="mt-6">
            <Button 
                type="button" 
                on:click={saveProduct}
                class="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            >
                Zapisz
            </Button>
        </div>
    </Card>
</main>

<style>
    .page-body {
        background-image:  url('../../assets/background.jpg');
        background-repeat: no-repeat;
        background-size: cover;
    }

    #app{
	display:flex;
		align-items:center;
		justify-content:center;
		flex-flow:column;
}

	.upload{
		display:flex;
	height:50px;
		width:50px;
		cursor:pointer;
	}
	.avatar{
		display:flex;
		height:200px;
		width:200px;
	}
    </style>