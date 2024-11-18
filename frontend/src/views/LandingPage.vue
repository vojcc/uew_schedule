<script setup>
import {onMounted, ref} from 'vue'
import {useUserSettingsStore} from '@/stores/UserSettingsStore.js'
import {groups} from '../../../backend/schedule.json'
import {
  AdjustmentsHorizontalIcon,
  FireIcon,
  CalendarDaysIcon,
} from '@heroicons/vue/24/outline/index.js'
import { onClickOutside } from '@vueuse/core'
const groupList = ref(null)

onClickOutside(groupList, () => {
  toggleShowGroupList()
})

const subject = ref('')
const group = ref('')
const semester = ref('')

const showUserSettingsForm = ref(true)

function toggleSettingsForm() {
  showUserSettingsForm.value = !showUserSettingsForm.value
}

const userSettingsStore = useUserSettingsStore()

onMounted(() => {
  if (userSettingsStore.getSubject()) {
    subject.value = userSettingsStore.getSubject()
  }

  if (userSettingsStore.getGroup()) {
    group.value = userSettingsStore.getGroup()
  }

  if (userSettingsStore.getSemester()) {
    chooseSemester(userSettingsStore.getSemester())
  }

  refreshScheduleForActualSettings()
})

function selectGroup(groupName) {
  group.value = groupName
  userSettingsStore.setGroup(groupName)
  refreshScheduleForActualSettings()

  selectedDay.value = ''
  toggleShowGroupList()
}

function chooseSemester(semesterName) {
  semester.value = semesterName
}

const selectedGroupDays = ref([])

function refreshScheduleForActualSettings() {
  const selectedGroup = groups.find((item) => item.name === group.value)
  selectedGroupDays.value = selectedGroup?.days
}

const selectedDay = ref()

function selectDay(day) {
  selectedDay.value = day
}

const showGroupList = ref(false)

function toggleShowGroupList() {
  showGroupList.value = !showGroupList.value
}
</script>
<template>
  <main>
    <div class="p-4 sm:p-5">
      <div class="flex flex-col item-center justify-center gap-1">
        <h1 class="w-fit text-3xl sm:text-4xl font-bold text-gray-800">Plan zajęć</h1>
        <h2 class="sm:text-lg font-medium text-balance text-gray-800">Uniwersytetu Ekonomicznego we Wrocławiu</h2>
      </div>

      <div class="w-full flex justify-end">
        <button @click="toggleSettingsForm" class="flex mt-4 items-center gap-1 hover:drop-shadow">
          <AdjustmentsHorizontalIcon class="size-5"/>
          <span class="text-xs text-gray-800">
            {{ showUserSettingsForm === true ? 'Schowaj filtry' : 'Zmień filtry' }}
          </span>
        </button>
      </div>

      <transition name="slide-horizontal" mode="out-in">
        <div v-if="showUserSettingsForm" class="flex flex-col">
          <div class="w-full">
            <form class="flex flex-col gap-6">
              <div class="flex flex-col">
                <label class="text-sm font-medium text-gray-800">Kierunek</label>
                <input
                  readonly
                  class="disabled:bg-white p-2 text-sm text-gray-800 rounded-lg border border-gray-800 ring-inset focus:outline-none focus:ring-uewblue focus:ring-1"
                  type="text"
                  v-model="subject"
                />
              </div>

              <div>
                <label class="block text-sm font-bold text-gray-900">Grupa</label>
                <div class="relative">
                  <button
                    @click="toggleShowGroupList()"
                    type="button"
                    class="relative w-full cursor-default rounded-lg p-2 text-left text-gray-800 border border-gray-800 ring-inset focus:outline-none focus:ring-uewblue focus:ring-1"
                  >
                    <span class="text-sm">{{ group }}</span>
                    <span
                      class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2"
                    >v</span
                    >
                  </button>

                  <ul
                    ref="groupList"
                    v-if="showGroupList"
                    class="absolute z-10 mt-1 max-h-60 w-full overflow-auto rounded-lg bg-white py-1 shadow-lg ring-1 ring-black/5 focus:outline-none text-sm"
                  >
                    <li
                      @click="selectGroup(group.name)"
                      v-for="group in groups"
                      :key="group.name"
                      class="relative select-none py-2 pl-3 pr-9 text-gray-900 hover:bg-gray-50 cursor-pointer"
                    >
                      {{ group.name }}
                    </li>
                  </ul>
                </div>
              </div>

              <div class="flex gap-6 items-center">
                <div
                  @click="chooseSemester('zimowy')"
                  class="flex items-center gap-1 cursor-pointer hover:drop-shadow"
                >
                  <input
                    type="radio"
                    class="size-4 accent-uewblue cursor-pointer"
                    value="zimowy"
                    v-model="semester"
                  />
                  <label class="cursor-pointer text-gray-800">Semestr zimowy</label>
                </div>

                <div @click="chooseSemester('letni')" class="flex items-center gap-1">
                  <input
                    type="radio"
                    readonly
                    disabled
                    class="size-4 accent-uewblue"
                    value="letni"
                    v-model="semester"
                  />
                  <label class="text-gray-400">Semestr letni</label>
                </div>
              </div>
            </form>
          </div>
        </div>
      </transition>

      <section>
        <div v-if="selectedGroupDays">
          <hr class="h-[2px] my-4 bg-uewyellow border-0"/>
          <p v-if="group" class="font-bold text-lg text-gray-800">Grupa {{ group }}</p>

          <div class="flex flex-row overflow-x-scroll gap-2 my-2">
            <button
              @click="selectDay(day)"
              class="px-4 py-2 mb-2 text-sm border rounded-2xl"
              v-for="day in selectedGroupDays"
              :key="day.date"
              :class="
                selectedDay && selectedDay.date === day.date
                  ? 'bg-uewblue text-white '
                  : 'text-gray-800 hover:bg-gray-50'
              "
            >
              <span class="font-medium">
                {{ day.date }}
              </span>
            </button>
          </div>

          <div v-if="selectedDay?.lessons?.length">
            <div class="flex" v-for="(lesson, index) in selectedDay.lessons" :key="index">
              <div class="flex flex-col my-3 gap-1 w-full" v-if="lesson.name !== '-'">
                <div class="w-full flex gap-3 items-center">
                  <span class="text-xs font-medium text-gray-800">{{ lesson.start_hour }}</span>
                  <hr class="flex-grow border-t border-gray-200"/>
                </div>

                <div class="flex justify-end">
                  <div
                    class="flex flex-col border-l-[5px] border-dotted border-blue-800 ml-10 w-full px-4"
                  >
                    <span class="font-bold text-gray-800">{{ lesson.name }}</span>
                    <span class="text-xs text-gray-600">{{ lesson.name_abbr }}</span>
                    <span class="text-gray-600 text-xs">{{ lesson.teacher_name }}</span>
                  </div>
                </div>

                <div class="w-full flex gap-3 items-center">
                  <span class="text-xs font-medium text-gray-800">{{ lesson.end_hour }}</span>
                  <hr class="flex-grow border-t border-gray-200"/>
                </div>
              </div>
            </div>
          </div>
          <div class="mt-12 flex flex-col gap-2 justify-center items-center p-6" v-else>
            <FireIcon class="size-16"/>
            <p class="text-center text-sm font-bold text-gray-800">Brak zajęć tego dnia.</p>
          </div>
        </div>
        <div class="mt-12 flex flex-col gap-2 justify-center items-center p-6" v-else>
          <CalendarDaysIcon class="size-16"/>
          <p class="text-center text-sm font-bold text-gray-800">
            Wybierz kierunek, grupę i semestr,
            <br class="block sm:hidden"/>
            aby przejść do planu.
          </p>
        </div>
      </section>
    </div>
  </main>
</template>

<style scoped>
.slide-horizontal-enter-active,
.slide-horizontal-leave-active {
  transition: all 0.2s ease;
}

.slide-horizontal-enter-from {
  transform: translateX(100%);
  opacity: 0;
}

.slide-horizontal-leave-to {
  transform: translateX(100%);
  opacity: 0;
}
</style>
