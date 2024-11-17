import { defineStore } from 'pinia'

export const useUserSettingsStore = defineStore('UserSettingsStore', {
  state: () => ({
    subject: 'Informatyka w Biznesie',
    group: '',
    semester: 'zimowy',
  }),
  actions: {
    // setSubject(subject) {
    //   this.subject = subject
    //   localStorage.setItem('subject', subject.value)
    // },
    getSubject() {
      return this.subject || localStorage.getItem('subject') || ''
    },

    setGroup(group) {
      this.group = group
      localStorage.setItem('group', group.value)
    },
    getGroup() {
      return this.group || localStorage.getItem('group') || ''
    },

    // setSemester(semester) {
    //   this.semester = semester
    //   localStorage.setItem('semester', semester.value)
    // },
    getSemester() {
      return this.semester || localStorage.getItem('semester') || ''
    },
  },
})
