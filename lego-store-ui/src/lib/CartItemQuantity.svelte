<script lang="ts">

    import { Button, ButtonGroup, InputAddon } from "flowbite-svelte";
    import { createEventDispatcher } from "svelte";

    export let value: number;

    const dispatchIncrement = createEventDispatcher<{increment: {value: number}}>();
    const dispatchDecrement = createEventDispatcher<{decrement: {value: number}}>();

    function decrement(){
        value -= 1;
        dispatchDecrement('decrement', { value });
    }

    function increment(){
        value += 1;
        dispatchIncrement('increment', { value });
    }

</script>
<ButtonGroup>
    <Button color="blue" on:click={decrement} disabled={value <= 0}>
        <svg class="fill-white" xmlns="http://www.w3.org/2000/svg" height="20" viewBox="0 96 960 960" width="20"><path d="M240 612v-72h480v72H240Z"/></svg>
    </Button>
    <InputAddon class="w-10 justify-center">{value}</InputAddon>
    <Button color="blue" on:click={increment} disbaled={value >= 100}>
        <svg class="fill-white" xmlns="http://www.w3.org/2000/svg" height="20" viewBox="0 96 960 960" width="20"><path d="M444 816V612H240v-72h204V336h72v204h204v72H516v204h-72Z"/></svg>
    </Button>
</ButtonGroup>