<script setup>
import {onMounted, ref, watch} from "vue";
import {useUserSettingsStore} from "@/stores/UserSettingsStore.js";
import {groups} from "../../../backend/schedule.json"
import {AdjustmentsHorizontalIcon} from "@heroicons/vue/24/outline/index.js";

const userSettingsStore = useUserSettingsStore()

const subject = ref('')
const group = ref('')
const semester = ref('')

const showUserSettingsForm = ref(true)

function toggleSettingsForm() {
  showUserSettingsForm.value = !showUserSettingsForm.value
}

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

// watch(subject, () => {
//   userSettingsStore.setSubject(subject)
// })

watch(group, () => {
  userSettingsStore.setGroup(group)
  refreshScheduleForActualSettings()

  selectedDay.value = ''
})

function chooseSemester(semesterName) {
  semester.value = semesterName
  // userSettingsStore.setSemester(semester)
}

const selectedGroupDays = ref([])

function refreshScheduleForActualSettings() {
  const selectedGroup = groups.find(item => item.name === group.value)
  selectedGroupDays.value = selectedGroup?.days
}

const selectedDay = ref()

function selectDay(day) {
  selectedDay.value = day
}

// watch(selectedDay, () => {
//   refreshScheduleForActualSettings()
// })

</script>
<template>
  <main>
    <div class="p-4 sm:p-5">
      <div class="flex flex-col item-center justify-center gap-1">
        <h1 class="w-fit text-3xl sm:text-4xl font-bold">
          Plan zajęć
        </h1>
        <h2 class="sm:text-lg font-medium text-balance">
          Uniwersytetu Ekonomicznego we Wrocławiu
        </h2>
      </div>

      <div class="w-full flex justify-end">
        <button @click="toggleSettingsForm"
                class="flex mt-4 items-center gap-1 border-b-2 border-transparent hover:border-uewyellow">
          <AdjustmentsHorizontalIcon class="size-5"/>
          <span class="text-xs">
            {{ showUserSettingsForm === true ? 'Schowaj filtry' : 'Zmień filtry' }}
          </span>
        </button>
      </div>

      <transition
        name="slide-horizontal"
        mode="out-in"
      >
        <div
          v-if="showUserSettingsForm"
          class="flex flex-col"
          key="settings-form"
        >
          <div class="w-full">
            <form class="flex flex-col gap-6">
              <div class="flex flex-col">
                <label class="text-sm font-medium">Kierunek</label>
                <input
                  readonly
                  disabled
                  class="disabled:bg-white p-2 border border-gray-500 rounded-lg"
                  type="text"
                  v-model="subject"
                />
              </div>

              <div class="flex flex-col">
                <label class="text-sm font-medium">Grupa</label>
                <select
                  v-model="group"
                  class="bg-white p-2 border border-gray-500 rounded-lg"
                >
                  <option v-for="group in groups" :key="group.name">
                    {{ group.name }}
                  </option>
                </select>
              </div>

              <div class="flex gap-6 items-center">
                <div @click="chooseSemester('zimowy')" class="flex items-center gap-1 cursor-pointer">
                  <input
                    type="radio"
                    class="size-4 accent-uewblue cursor-pointer"
                    value="zimowy"
                    v-model="semester"
                  />
                  <label class="cursor-pointer">Semestr zimowy</label>
                </div>

                <div @click="chooseSemester('letni')" class="flex items-center gap-1 cursor-pointer">
                  <input
                    type="radio"
                    readonly
                    disabled
                    class="size-4 accent-uewblue cursor-pointer"
                    value="letni"
                    v-model="semester"
                  />
                  <label class="cursor-pointer text-gray-400">Semestr letni</label>
                </div>
              </div>
            </form>
          </div>
        </div>
      </transition>

      <section>
        <div v-if="selectedGroupDays">
          <hr class="h-[2px] mt-3 mb-2 bg-uewyellow border-0">
          <p v-if="group" class="font-bold text-xl">
            Grupa {{ group }}
          </p>

          <div class="flex flex-row overflow-x-scroll gap-2 my-2">
            <button @click="selectDay(day)" class="px-4 py-2 mb-2 border rounded-2xl"
                    v-for="day in selectedGroupDays" :key="day.date"
                    :class="selectedDay && selectedDay.date === day.date ? 'bg-uewblue text-white ' : ''"
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
                  <span class="text-xs font-medium">{{ lesson.start_hour }}</span>
                  <hr class="flex-grow border-t border-gray-200"/>
                </div>

                <div class="flex justify-end">
                  <div class="flex flex-col border-l-[5px] border-dotted border-blue-800 ml-10 w-full px-4">
                    <span class="font-bold">{{ lesson.name }}</span>
                    <span class="text-xs">{{ lesson.name_abbr }}</span>

                    <span class="text-gray-600 text-xs">{{ lesson.teacher_name }}</span>
                  </div>
                </div>

                <div class="w-full flex gap-3 items-center">
                  <span class="text-xs font-medium">{{ lesson.end_hour }}</span>
                  <hr class="flex-grow border-t border-gray-200"/>
                </div>
              </div>
            </div>
          </div>
          <div class="mt-12 flex gap-1 justify-center items-center" v-else>
            <img src="../assets/beer.png" alt="">
            <p class="text-sm font-medium">
              Brak zajęć, idź na piwo.
            </p>
          </div>
        </div>
        <div class="mt-12 flex gap-4 justify-center items-center" v-else>
          <img class="size-12" src="../assets/calendar.png" alt="">
          <p class="text-sm font-medium">
            Wybierz kierunek, grupę i semestr, aby przejść do planu.
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
