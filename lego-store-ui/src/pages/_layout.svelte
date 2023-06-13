<script lang="ts">
    import { isActive } from "@roxi/routify";
    import { Navbar, NavBrand, NavHamburger, NavLi, NavUl, Button } from "flowbite-svelte";
    import { setCookie, getCookie, deleteCookie } from 'svelte-cookie';
    import { onMount } from 'svelte';

    let loggedIn: boolean = false;
    let isAdmin: boolean = false;

    loggedIn = getCookie('isLoggedIn');
    isAdmin = getCookie('isAdmin');

    export const load = async ({ request, locals, cookies }) => {
      loggedIn = getCookie('isLoggedIn');
      isAdmin = getCookie('isAdmin');
};

    function logOut() {

      setCookie('isLoggedIn', false, {
          path: '/',
          httpOnly: true
        });

        loggedIn = false;
        isAdmin = false;

        deleteCookie('jwt');
        deleteCookie('email');
        deleteCookie('isAdmin');

    }

</script>
<div class="wrapper">
    <Navbar let:hidden let:toggle>
        <NavBrand href="/">
          <img
            src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/LEGO_logo.svg/2048px-LEGO_logo.svg.png"
            class="mr-3 h-6 sm:h-9"
            alt="Lego Logo"
          />
          <span class="self-center whitespace-nowrap text-3xl font-semibold text-yellow-300 dark:text-white">
            Lego Store
          </span>
        </NavBrand>
        <NavHamburger on:click={toggle} />
        <NavUl {hidden}>
          <NavLi href="/" active={$isActive("/index")}>Strona główna</NavLi>
          {#if loggedIn && isAdmin}
            <NavLi href="/products/addProduct" active={$isActive("/products/addProduct")}>Dodaj Produkty</NavLi>
          {/if}
          <NavLi href="/products" active={$isActive("/products")}>Produkty</NavLi>
          {#if !loggedIn}
            <NavLi href="/account/login" active={$isActive("/account/login")}>Zaloguj</NavLi>
            <NavLi href="/account/register" active={$isActive("/account/register")}>Zarejestruj</NavLi>
          {/if}
          <NavLi href="/account/cart" active={$isActive("/account/cart")}>
            <svg xmlns="http://www.w3.org/2000/svg" height="24" viewBox="0 96 960 960" width="24"><path d="M240 976q-33 0-56.5-23.5T160 896V416q0-33 23.5-56.5T240 336h80q0-66 47-113t113-47q66 0 113 47t47 113h80q33 0 56.5 23.5T800 416v480q0 33-23.5 56.5T720 976H240Zm0-80h480V416h-80v80q0 17-11.5 28.5T600 536q-17 0-28.5-11.5T560 496v-80H400v80q0 17-11.5 28.5T360 536q-17 0-28.5-11.5T320 496v-80h-80v480Zm160-560h160q0-33-23.5-56.5T480 256q-33 0-56.5 23.5T400 336ZM240 896V416v480Z"/></svg>
          </NavLi>
          {#if loggedIn}
            <Button on:click={logOut}>Wyloguj się</Button>
          {/if}
        </NavUl>
      </Navbar>
    <slot/>
</div>

<style>
  .wrapper {
    height: 100vh;
    display: grid;
    grid-template-columns: minmax(10px, 1fr);
    grid-template-rows: min-content 1fr;
    gap: 1px;
  }
</style>