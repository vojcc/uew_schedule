<script setup>
import { RouterLink } from 'vue-router'
import {CalendarIcon, NumberedListIcon} from "@heroicons/vue/24/outline/index.js";
</script>

<template>
  <nav class="bg-gray-100">
    <div class="flex items-center justify-between">

      <div class="flex items-center pl-3 pr-5 gap-4">
        <RouterLink to="/">
          <img src="../assets/uew-logo.png" alt="" class="size-16 hover:drop-shadow"/>
        </RouterLink>
        <div class="flex items-center gap-4 font-medium">
          <RouterLink to="/kalendarz" class="flex items-center gap-1 border-b-2 border-transparent hover:border-uewyellow">
            <CalendarIcon class="size-5"/>
            Kalendarz
          </RouterLink>

          <RouterLink to="/plan" class="flex items-center gap-1 border-b-2 border-transparent hover:border-uewyellow">
            <NumberedListIcon class="size-5"/>
            Plan
          </RouterLink>
        </div>
      </div>

      <div class="flex flex-col items-end px-5">
        <p class="font-medium text-xs">Informatyka w biznesie</p>
        <p class="text-xs text-gray-600">Grupa IwB 06</p>
        <p class="text-xs text-gray-600">Semestr letni</p>
      </div>
    </div>

  </nav>

</template>
