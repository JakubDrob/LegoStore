<script lang="ts">
  import { Router } from "@roxi/routify"
  import { routes } from "../.routify/routes";
</script>

<svelte:head>
	<title>Lego Store</title>
</svelte:head>

<main class="w-full h-full">
  <Router {routes}/>
</main>

<style>
</style>