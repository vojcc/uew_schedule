<script setup>
import {ref} from "vue";

const subject = ref('Informatyka w biznesie')
const group = ref('IwB 06')
const semester = ref('')

function chooseSemester(semesterId) {
  semester.value = semesterId
}
</script>

<template>
  <main>
    <div class="p-5">
      <div class="flex flex-col item-center justify-center gap-1">
        <h1 class="text-4xl font-bold">
          Plan zajęć
        </h1>
        <h2 class="text-xl font-medium text-balance">
          Uniwersytetu Ekonomicznego we Wrocławiu
        </h2>
      </div>
      <div class="flex flex-col mt-8">

        <p class="text-sm">Wybierz kierunek, grupę i semestr, aby przejść do planu</p>
        <p class="text-sm">Wybór zostanie zapisany, ale można go zmienić</p>

        <div class="mt-8 w-full">
          <form class="flex flex-col gap-6">
            <div class="flex flex-col">
              <label class="text-sm font-medium">Kierunek</label>
              <input class="p-2 border border-uewblue rounded-lg" type="text" v-model="subject">
            </div>

            <div class="flex flex-col">
              <label class="text-sm font-medium">Grupa</label>
              <input class="p-2 border border-uewblue rounded-lg" type="text" v-model="group">
            </div>

            <div class="flex gap-6 items-center">
              <div @click="chooseSemester(1)"
                   class="flex items-center gap-1 cursor-pointer">
                <input
                  type="radio"
                  class="size-4 accent-uewblue"
                  value="1"
                  v-model="semester"
                />
                <label>Semestr zimowy</label>
              </div>

              <div @click="chooseSemester(2)"
                   class="flex items-center gap-1 cursor-pointer">
                <input
                  type="radio"
                  class="size-4 accent-uewblue"
                  value="2"
                  v-model="semester"
                />
                <label>Semestr letni</label>
              </div>
            </div>
          </form>

          <div class="mt-6 w-full" v-if="subject && group && semester">
            <button class="bg-uewblue w-full text-white px-4 py-3 rounded-lg font-medium hover:bg-blue-800">
              Przejdź do planu
            </button>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>
