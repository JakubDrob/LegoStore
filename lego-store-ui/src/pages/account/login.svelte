<script lang="ts">
  import { goto } from "@roxi/routify";
  import { Button, Card, Input, Label } from "flowbite-svelte";
  import { createForm } from "svelte-forms-lib";
  import { setCookie, getCookie } from 'svelte-cookie';

const errorBorder = "bg-gray-50 border-2 border-rose-600 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 ";
const correctBorder = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

let formErrors = {};

const { form, handleChange, handleSubmit } = createForm({
  initialValues: {
    email: "",
    password: "",
  },
  /**************************************
   *    Validate inputs
   **************************************/
  validate: (values) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    let emailInput = document.getElementById("email");
    let passwordInput = document.getElementById("password");

    if(!emailInput.value){
      formErrors.email = "Enter email";
      emailInput.className = errorBorder;
    }
    else if(!emailRegex.test(emailInput.value)){
      formErrors.email = "Wrong email format";
      emailInput.className = errorBorder;
    }
    else{
      emailInput.className = correctBorder;
      formErrors.email = "";
    }

    if(!passwordInput.value){
      formErrors.password = "Enter password";
      passwordInput.className = errorBorder;
    }
    else{
      passwordInput.className = correctBorder;
      formErrors.password = "";
    }
  },
  /**************************************
   *    Handle submit
   **************************************/
  onSubmit: (values) => {
    if((!formErrors.email) && (!formErrors.password))
    { 
      // alert(JSON.stringify(values));
      fetch("http://127.0.0.1:5000/api/auth/login/", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(values)
      })
      .then(response => {
        if (!response.ok) {
          if (response.status === 401) {
            formErrors.password = "Incorrect password";
            document.getElementById("password").className = errorBorder;
          } else if (response.status === 404) {
            formErrors.email = "User with this email does not exists";
            document.getElementById("email").className = errorBorder;
          } 
          else {
            throw new Error('Network response was not ok');
          }
        }
        return response.json();
      })
      .then(data => {
        console.log('Success:', data);
        const jwt = data.data['token'];
        const responseEmail = data.data['email'];

        // Save the token to httpOnly cookie
        setCookie('jwt', jwt, {
          path: '/',
          maxAge: 3600, // set the expiration time for the cookie in seconds
          httpOnly: true
        });

        setCookie('email', responseEmail, {
          path: '/',
          httpOnly: true
        });

        // Use getCookie to retrive the token
        console.log('saved jwt: ',getCookie('jwt'));

        // Go to main page
        $goto('http://localhost:5173');
      })
      .catch(error => {
        console.error('Error:', error);
      });
    }
  },
});
</script>

<!--**************************************
*    HTML code
***************************************-->
<main class="flex justify-center items-center page-body">
  <div class="login-form">
    <Card class="mx-auto">
      <h4 class="text-2xl font-bold mb-6 text-center">Logowanie</h4>
      <div class="flex flex-col ">
        <div class="mb-6">
          <Label for="default-input" class="block mb-2">Email</Label>
          <Input 
            bind:value={$form.email} 
            id="email" 
            placeholder="email"
            on:input={handleChange}
            required
          />
          {#if formErrors.email}
          <p class="text-xs font-bold text-red-600">{formErrors.email}</p>
          {/if}
        </div>
        <div class="mb-6">
          <Label class="block mb-2">Hasło</Label>
          <Input 
            id="password" 
            placeholder="password" 
            type="password" 
            on:input={handleChange}
          />
          {#if formErrors.password}
          <p class="text-xs font-bold text-red-600">{formErrors.password}</p>
          {/if}
        </div>
        <Button class="text-center w-2/3 self-center" color="blue" on:click={()=>{handleSubmit()}}
          >Zaloguj się</Button
        >
      </div>
    </Card>
  </div>
</main>

<style>
  .page-body {
    background-image:  url('../../assets/background.jpg');
    background-repeat: no-repeat;
    background-size: cover;
  }
  .login-form {
    min-width: 500px;
  }
</style>
