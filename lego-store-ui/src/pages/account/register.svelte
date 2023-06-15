<script lang="ts">
  import { redirect, goto } from "@roxi/routify";
  import { Button, Card, Checkbox, Input, Label } from "flowbite-svelte";
  import { createForm } from "svelte-forms-lib";

  const errorBorder = "bg-gray-50 border-2 border-rose-600 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500 ";
  const correctBorder = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"

  let formErrors = {};
  let adminCheckbox: boolean = false;

  const { form, handleChange, handleSubmit } = createForm({
    initialValues: {
      email: "",
      password: "",
      confirmPassword: "",
      adminPassword: ""
    },
    validate: (values) => {
    /**************************************
     *    Validate inputs
     **************************************/
      validateInputs(values);
    },
    onSubmit: (values) => {
    /**************************************
     *    Handle submit
     **************************************/
      if(!formErrors.email && (!formErrors.password) && (!formErrors.confirmPassword))
      { 
        console.log(values);
        delete values.confirmPassword;
        if(!adminCheckbox) values.adminPassword = "";
        // alert(JSON.stringify(values));
        fetch("http://legostorebackend.azurewebsites.net/api/auth/register/", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(values)
        })
        .then(response => {
          if (!response.ok) {
            if(response.status === 400){
              response.json().then(data => {
                if(data.message.includes("admin")){
                  formErrors.adminPassword = data.message;
                  console.log("admin error");
                  console.log(data);
                  document.getElementById("adminPassword").className = errorBorder;
                }
                else{
                  console.log("email error");
                  formErrors.email = data.message;
                  console.log(data);
                  document.getElementById("email").className = errorBorder;
                }

              });
            }
            else{
              throw new Error('Network response was not ok');
            }
          }
          return response.json();
        })
        .then(data => {
          console.log('Success:', data);

          $goto('./login');
        })
        .catch(error => {
          console.error('Error:', error);
        });
      }
    },
  });


  function validateInputs(values){
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    let emailInput = document.getElementById("email");
    let passwordInput = document.getElementById("password");
    let passwordConfInput = document.getElementById("confirmPassword");

    if ('email' in values) {
        if(!emailRegex.test(values.email))
        {
          formErrors.email = "Wrong email";
          emailInput.className = errorBorder
        }
        else if(!values.email)
        {
          formErrors.email = "Email is required";
          emailInput.className = errorBorder
        }
        else{
          emailInput.className = correctBorder;
          formErrors.email = "";
        }
      }
     
      if ('confirmPassword' in values) {
        if (passwordInput.value !== values.confirmPassword) {
          passwordInput.className = errorBorder
          passwordConfInput.className = errorBorder

          formErrors.confirmPassword = "Passwords do not match";
          formErrors.password = "Passwords do not match";
          
        }else{
          passwordInput.className = correctBorder;
          passwordConfInput.className = correctBorder;
          formErrors.confirmPassword = "";
          formErrors.password = "";
        }
      }

      if('password' in values){
        if(values.password.length < 8){
          passwordInput.className = errorBorder;
          formErrors.password = "Passwords must be at least 8 characters";
        }
        else if(values.password !== passwordConfInput.value) {
          passwordInput.className = errorBorder;
          passwordConfInput.className = errorBorder;
          
          formErrors.confirmPassword = "Passwords do not match";
          formErrors.password = "Passwords do not match";
        }
        else{
          passwordInput.className = correctBorder;
          passwordConfInput.className = correctBorder;
          formErrors.confirmPassword = "";
          formErrors.password = "";
        }
    }
  }

</script>


<main class="flex justify-center items-center page-body">
  <div class="login-form">
    <Card class="mx-auto">
      <h4 class="text-2xl font-bold mb-6 text-center">Rejestracja</h4>
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
          <Label for="default-input" class="block mb-2">Hasło</Label>
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
        <div class="mb-6">
          <Label  id="confirmedPass-label" for="default-input" class="block mb-2">Powtórz hasło</Label>
          <Input 
            id="confirmPassword" 
            placeholder="confirm password" 
            type="password" 
            on:input={handleChange}
          />
          {#if formErrors.confirmPassword}
          <p class="text-xs font-bold text-red-600">{formErrors.confirmPassword}</p>
          {/if}
        </div>
        {#if adminCheckbox}
          <div class="mb-6">
            <Label  id="confirmedPass-label" for="default-input" class="block mb-2">Hasło administracyjne</Label>
            <Input 
              id="adminPassword" 
              type="password" 
              on:input={handleChange}
            />
            {#if formErrors.adminPassword}
            <p class="text-xs font-bold text-red-600">{formErrors.adminPassword}</p>
            {/if}
          </div>
          {/if}
        <div class="pb-4">
          <Checkbox bind:checked={adminCheckbox}>Zarejestruj konto administratora</Checkbox>
        </div>
        <Button id="registerBtn" class="text-center w-2/3 self-center" color="blue" on:click={()=>{handleSubmit()}}>Zarejestruj się</Button>
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