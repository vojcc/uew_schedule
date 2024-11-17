<script setup>
import {RouterLink} from 'vue-router'
import {CalendarDaysIcon, NumberedListIcon} from "@heroicons/vue/24/outline/index.js";
import {computed} from "vue";
import {useUserSettingsStore} from "@/stores/UserSettingsStore.js";
const userSettingsStore = useUserSettingsStore()

const subject = computed(() => userSettingsStore.getSubject() || '');

const group = computed(() => userSettingsStore.getGroup() ? `Grupa ${userSettingsStore.getGroup()}` : '');

const semester = computed(() => userSettingsStore.getSemester() ? `Semestr ${userSettingsStore.getSemester()}` : '');

</script>

<template>
  <nav class="bg-gray-100">
    <div class="flex items-center justify-between px-4 sm:px-5 py-2 sm:py-3">

      <div class="flex items-center">
        <div class="flex items-center gap-5 font-medium">
          <RouterLink to="/" class="flex items-center gap-1 border-b-2 border-transparent hover:border-uewyellow">
            <NumberedListIcon class="size-5 shrink-0"/>
            <span class="text-xs sm:text-sm">Plan zajęć</span>
          </RouterLink>

          <RouterLink to="/kalendarz" class="flex items-center gap-1 border-b-2 border-transparent hover:border-uewyellow">
            <CalendarDaysIcon class="size-5 shrink-0"/>
            <span class="text-xs sm:text-sm">Kalendarz</span>
          </RouterLink>
        </div>
      </div>

      <div class="flex flex-col items-end">
        <p class="text-[11px] sm:text-xs font-medium text-nowrap">{{ subject }}&nbsp;</p>
        <p class="text-[11px] sm:text-xs text-gray-600 text-nowrap">{{ semester }}&nbsp;</p>
        <p class="text-[11px] sm:text-xs text-gray-600 text-nowrap">{{ group }}&nbsp;</p>
      </div>
    </div>
  </nav>
</template>
