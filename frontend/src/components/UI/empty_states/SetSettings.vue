<script setup>
import { CalendarDaysIcon } from '@heroicons/vue/24/outline/index.js'
</script>

<template>
  <div class="flex flex-col gap-2 justify-center items-center">
    <CalendarDaysIcon class="size-16" />
    <p class="text-center text-sm font-bold text-gray-800">
      Wybierz kierunek, grupę i semestr,
      <br class="block sm:hidden" />
      aby przejść do planu
    </p>
  </div>
</template>
