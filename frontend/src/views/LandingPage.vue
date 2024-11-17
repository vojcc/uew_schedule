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


      <div v-if="showUserSettingsForm === true" class="flex flex-col">
        <div class="w-full">
          <form class="flex flex-col gap-6">
            <div class="flex flex-col">
              <label class="text-sm font-medium">Kierunek</label>
              <input readonly disabled class="disabled:bg-white p-2 border border-gray-500 rounded-lg" type="text"
                     v-model="subject">
            </div>

            <div class="flex flex-col">
              <label class="text-sm font-medium">Grupa</label>
              <select v-model="group" class="bg-white p-2 border border-gray-500 rounded-lg" type="text">
                <option v-for="group in groups" :key="group.name">
                  {{ group.name }}
                </option>
              </select>
            </div>

            <div class="flex gap-6 items-center">
              <div @click="chooseSemester('zimowy')"
                   class="flex items-center gap-1 cursor-pointer">
                <input
                  type="radio"
                  class="size-4 accent-uewblue cursor-pointer"
                  value="zimowy"
                  v-model="semester"
                />
                <label class="cursor-pointer">Semestr zimowy</label>
              </div>

              <div @click="chooseSemester('letni')"
                   class="flex items-center gap-1 cursor-pointer">
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

          <!--          <div class="mt-6 w-full" v-if="subject && group && semester">-->
          <!--            <button @click="refreshScheduleForActualSettings()"-->
          <!--                    class="bg-uewblue w-full text-white px-4 py-2 rounded-lg font-medium hover:bg-blue-800">-->
          <!--              Pokaż plan-->
          <!--            </button>-->
          <!--          </div>-->
        </div>
      </div>

      <section>
        <div v-if="selectedGroupDays">
          <hr class="h-[2px] mt-3 mb-2 bg-uewyellow border-0">
          <p v-if="group" class="font-bold text-xl">
            Grupa {{ group }}
          </p>
          <div v-for="day in selectedGroupDays" :key="day.date">
            <br>
            <span class="font-medium">
             {{ day.date }}
          </span>

            <div v-for="(lesson, index) in day.lessons" :key="index">
              <div v-if="lesson.name !== '-'">
                {{ lesson.name }}:
                {{ lesson.start_hour }} - {{ lesson.end_hour }}
              </div>
            </div>
          </div>
        </div>
        <div class="mt-3" v-else>
          <p class="text-sm text-pretty text-gray-600">
            Wybierz kierunek, grupę i semestr, aby przejść do planu.
          </p>
        </div>
      </section>
    </div>
  </main>
</template>
