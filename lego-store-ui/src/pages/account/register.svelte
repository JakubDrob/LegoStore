<script lang="ts">
  import { Button, Card, Input, Label } from "flowbite-svelte";
</script>

<main>
  <div class="login-form">
    <Card class="mx-auto">
      <h4 class="text-2xl font-bold mb-6 text-center">Rejestracja</h4>
      <div class="flex flex-col ">
        <div class="mb-6">
          <Label for="default-input" class="block mb-2">Email</Label>
          <Input id="default-input" placeholder="email" />
        </div>
        <div class="mb-6">
          <Label for="default-input" class="block mb-2">Hasło</Label>
          <Input id="default-input" placeholder="password" type="password" />
        </div>
        <div class="mb-6">
          <Label for="default-input" class="block mb-2">Powtórz hasło</Label>
          <Input id="default-input" placeholder="password" type="password" />
        </div>
        <Button class="text-center w-2/3 self-center" color="dark">Zarejestruj</Button>
      </div>
    </Card>
  </div>
</main>

<style>
  .login-form {
    min-width: 400px;
  }
</style>
