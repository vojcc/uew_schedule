<script setup>
import { RouterLink } from 'vue-router'
import { CalendarDaysIcon, NumberedListIcon } from '@heroicons/vue/24/outline/index.js'
import { computed } from 'vue'
import { useUserSettingsStore } from '@/stores/UserSettingsStore.js'

const userSettingsStore = useUserSettingsStore()

const group = computed(() =>
  userSettingsStore.getGroup() ? `Grupa ${userSettingsStore.getGroup()}` : '',
)
</script>

<template>
  <nav class="bg-gray-100">
    <div class="flex flex-wrap-reverse gap-4 items-center justify-between px-4 py-3 sm:py-4">
      <div class="flex items-center">
        <div class="flex items-center gap-5 font-medium">
          <RouterLink to="/" class="flex items-center gap-1 hover:drop-shadow">
            <NumberedListIcon class="size-5 shrink-0" />
            <span class="text-sm text-gray-800">Plan zajęć</span>
          </RouterLink>

          <span class="flex items-center gap-1">
            <CalendarDaysIcon class="size-5 shrink-0 text-gray-300" />
            <span class="text-sm text-gray-300">Kalendarz</span>
          </span>
        </div>
      </div>

      <div class="flex flex-col items-end">
        <p class="text-[10px] sm:text-xs font-medium text-nowrap text-gray-800">Informatyka w biznesie</p>
        <p class="text-[10px] sm:text-xs text-gray-600 text-nowrap">{{ group }}&nbsp;</p>
      </div>
    </div>
  </nav>
</template>
