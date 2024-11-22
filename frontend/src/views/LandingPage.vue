<script setup>
import {onMounted, onUpdated, ref, watch} from 'vue'
import {useUserSettingsStore} from '@/stores/UserSettingsStore.js'
import {groups} from '../../../backend/schedule.json'
import {
  AdjustmentsHorizontalIcon,
  CalendarDaysIcon,
  ChevronDownIcon,
  ChevronUpIcon,
  FireIcon
} from '@heroicons/vue/24/outline/index.js'
import {onClickOutside} from '@vueuse/core'


const subject = ref('')
const group = ref('')
const semester = ref('')
const selectedDay = ref('')
const showUserSettingsForm = ref(true)
const showGroupList = ref(false)
const userSettingsStore = useUserSettingsStore()
const groupList = ref(null)
const buttonRefs = ref({})
const scrollContainer = ref(null)

onMounted(() => {
  if (userSettingsStore.getSubject()) {
    subject.value = userSettingsStore.getSubject()
  }

  if (userSettingsStore.getGroup()) {
    group.value = userSettingsStore.getGroup()
  }

  if (userSettingsStore.getSemester()) {
    selectSemester(userSettingsStore.getSemester())
  }

  if (userSettingsStore.getSelectedDay()) {
    selectedDay.value = userSettingsStore.getSelectedDay()
  }

  if (group.value) {
    setSelectedGroupDays()
  }
})

onUpdated(() => {
  if (selectedDay.value && buttonRefs.value[selectedDay.value.date]) {
    buttonRefs.value[selectedDay.value.date].scrollIntoView({
      behavior: 'smooth',
      inline: 'center',
      block: 'nearest',
    });
  }
})

function selectGroup(groupName) {
  toggleShowGroupList()

  group.value = groupName
  userSettingsStore.setGroup(groupName)
  if (group.value) {
    setSelectedGroupDays()
  }
}

function selectSemester(semesterName) {
  semester.value = semesterName
}

function selectDay(day) {
  selectedDay.value = day
  userSettingsStore.setSelectedDay(day)
}

const selectedGroupDays = ref([])

function setSelectedGroupDays() {
  //Prepare list of dates of selected group
  const selectedGroup = groups.find((item) => item.name === group.value)
  selectedGroupDays.value = selectedGroup?.days

  //If user didn't select any day then assign the closest day to today
  if (!selectedDay.value) {
    const closest = selectedGroupDays.value
      .map(entry => ({
        ...entry,
        parsedDate: new Date(entry.date.replace(/\./g, '-'))
      }))
      .filter(entry => entry.parsedDate >= new Date())
      .sort((a, b) => a.parsedDate - b.parsedDate)

    selectedDay.value = closest.length > 0 ? closest[0] : null
  }
}

function setButtonRef(date, element) {
  if (element) {
    buttonRefs.value[date] = element
  }
}

function toggleSettingsForm() {
  showUserSettingsForm.value = !showUserSettingsForm.value
}

function toggleShowGroupList() {
  showGroupList.value = !showGroupList.value
}

onClickOutside(groupList, () => {
  showGroupList.value = false
})
</script>

<template>
  <main>
    <div class="p-4 sm:p-5">
      <div class="flex items-center gap-2">
        <img src="../assets/uew-logo.png" alt="" class="size-7">
        <h1 class="w-fit text-2xl sm:text-3xl font-bold text-gray-800">Plan zajęć</h1>
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
                <label class="text-sm font-bold text-gray-800">Kierunek</label>
                <input
                  readonly
                  class="disabled:bg-white shadow-md min-h-12 p-3 text-sm text-gray-800 rounded-lg ring-1 ring-gray-200 ring-inset focus:outline-none focus:ring-uewblue"
                  type="text"
                  v-model="subject"
                />
              </div>

              <div>
                <label class="block text-sm font-bold text-gray-900">Grupa</label>
                <div ref="groupList" class="relative">
                  <button
                    @click="toggleShowGroupList()"
                    type="button"
                    class="flex items-center shadow-md relative min-h-12 w-full cursor-default rounded-lg p-3 text-left text-gray-800 ring-1 ring-gray-200 ring-inset active:outline-none active:ring-uewblue focus:outline-none focus:ring-uewblue"
                  >
                    <span class="text-sm">{{ group }}</span>
                    <span class="pointer-events-none absolute inset-y-0 right-0 flex items-center pr-2">
                      <ChevronUpIcon v-if="showGroupList" class="size-4 text-gray-800"/>
                      <ChevronDownIcon v-else class="size-4 text-gray-800"/>
                    </span>
                  </button>

                  <ul
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
                  @click="selectSemester('zimowy')"
                  class="flex items-center gap-1 cursor-pointer hover:drop-shadow"
                >
                  <input
                    type="radio"
                    class="size-4 accent-uewblue cursor-pointer"
                    value="zimowy"
                    v-model="semester"
                  />
                  <label class="cursor-pointer text-sm text-gray-800">Semestr zimowy</label>
                </div>

                <div @click="selectSemester('letni')" class="flex items-center gap-1">
                  <input
                    type="radio"
                    readonly
                    disabled
                    class="size-4 accent-uewblue"
                    value="letni"
                    v-model="semester"
                  />
                  <label class="text-gray-400 text-sm">Semestr letni</label>
                </div>
              </div>
            </form>
          </div>
        </div>
      </transition>

      <section>
        <div v-if="selectedGroupDays.length">
          <hr class="h-[2px] my-4 bg-uewyellow border-0"/>
          <p v-if="group" class="font-bold text-lg text-gray-800">Grupa {{ group }}</p>

          <div class="flex flex-row overflow-x-scroll gap-2 my-2" ref="scrollContainer">
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
              :ref="element => setButtonRef(day.date, element)"
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
