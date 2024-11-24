<script setup>
import { RouterLink } from 'vue-router'
import { CalendarDaysIcon, NumberedListIcon } from '@heroicons/vue/24/outline/index.js'
import { computed } from 'vue'
import { useUserSettingsStore } from '@/stores/UserSettingsStore.js'

const userSettingsStore = useUserSettingsStore()

const subject = computed(() => userSettingsStore.getSubject())

const group = computed(() =>
  userSettingsStore.getGroup() ? `Grupa ${userSettingsStore.getGroup()}` : '',
)

const semester = computed(() =>
  userSettingsStore.getSemester() ? `Semestr ${userSettingsStore.getSemester()}` : '',
)
</script>

<template>
  <nav class="bg-gray-100">
    <div class="flex flex-wrap-reverse gap-4 items-center justify-between px-4 py-2 sm:py-3">
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
        <p class="text-[11px] sm:text-xs font-medium text-nowrap text-gray-800">
          {{ subject }}&nbsp;
        </p>
        <p class="text-[11px] sm:text-xs text-gray-600 text-nowrap">{{ semester }}&nbsp;</p>
        <p class="text-[11px] sm:text-xs text-gray-600 text-nowrap">{{ group }}&nbsp;</p>
      </div>
    </div>
  </nav>
</template>
