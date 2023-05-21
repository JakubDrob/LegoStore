<script>
    // import Carousel from '../components/Carousel.svelte';
    import { Carousel } from 'flowbite-svelte'
    import { Card } from "flowbite-svelte";
    import { CarouselTransition } from 'flowbite-svelte'
    import { bounceInOut, backInOut, cubicInOut } from 'svelte/easing';
  
    let showThumbs = false;
    let showCaptions = false;
    let border = true;

    const images = [
        {id: 0,
        name: "Cosmic timetraveler",
        imgurl: "1.webp",
        attribution: "cosmic-timetraveler-pYyOZ8q7AII-unsplash.com",
        },
        {id: 1,
        name: "Cosmic timetraveler",
        imgurl: "3.webp",
        attribution: "cosmic-timetraveler-pYyOZ8q7AII-unsplash.com",
        },
    ];

  </script>
  
  <main class="flex justify-center w-screen page-body">
    <Card size = "xl" vertical class="h-96 w-full mt-10 bg-opacity-60 bg-black">
        <div class="flex justify-center">
            <h2 class="text-2xl text-white font-bold">Nowości !</h2>
        </div>
        <CarouselTransition {images} transitionType="slide" transitionParams="{{duration: 1000, easing: cubicInOut}}" showCaptions={false} showThumbs={false}/>
        <!-- <Carousel {images} {border} loop {showThumbs} {showCaptions} duration="3000"/> -->
      </Card>
  </main>
  

  <style>
    .page-body {
      background-image:  url('../assets/background.jpg');
      background-repeat: no-repeat;
      background-size: cover;
    }
  </style>
