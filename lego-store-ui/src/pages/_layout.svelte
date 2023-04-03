<script>
    import { isActive } from "@roxi/routify";
    import { Navbar, NavBrand, NavHamburger, NavLi, NavUl } from "flowbite-svelte";

</script>
<div class="wrapper">
    <Navbar let:hidden let:toggle>
        <NavBrand href="/">
          <img
            src="https://flowbite.com/docs/images/logo.svg"
            class="mr-3 h-6 sm:h-9"
            alt="Flowbite Logo"
          />
          <span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white">
            Flowbite
          </span>
        </NavBrand>
        <NavHamburger on:click={toggle} />
        <NavUl {hidden}>
          <NavLi href="/" active={$isActive("/index")}>Strona główna</NavLi>
          <NavLi href="/products" active={$isActive("/products")}>Produkty</NavLi>
          <NavLi href="/account/login" active={$isActive("/account/login")}>Zaloguj</NavLi>
          <NavLi href="/account/register" active={$isActive("/account/register")}>Zarejestruj</NavLi>
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