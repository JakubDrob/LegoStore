<script lang="ts">
    // import Carousel from '../components/Carousel.svelte';
    import Carousel from '../lib/Carousel.svelte'
    import Banner from '../lib/Banner.svelte'
    import { Card } from "flowbite-svelte";

    let showThumbs = false;
    let showCaptions = false;
    let border = true;

    const images = [
        {title: 'Nintendo',
        src: "1.webp"
        },
        {title: 'Pasta store',
        src: "pastaStore.webp"
        },
        {title: 'Mario world',
        src: "2.webp"
        },
        {title: 'Restaurant',
        src: "foodTruck.webp"
        },
    ];

    const banner = {src:"indianaJonesAdd.webp"}

  </script>

<section class ="flex flex-col item-center px-8 pt-10 page-body">

    <Carousel {images}/>
    <Banner {banner}/>
</section>
  
<style>
    .page-body {
      background-image:  url('../assets/background.jpg');
      background-repeat: no-repeat;
      background-size: cover;
    }
  </style>