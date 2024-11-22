import { defineStore } from 'pinia'

export const useUserSettingsStore = defineStore('UserSettingsStore', {
  state: () => ({
    subject: 'Informatyka w Biznesie',
    group: '',
    semester: 'zimowy',
  }),
  actions: {
    getSubject() {
      return this.subject || localStorage.getItem('subject') || ''
    },

    setGroup(group) {
      this.group = group
      localStorage.setItem('group', group)
    },
    getGroup() {
      return this.group || localStorage.getItem('group') || ''
    },

    getSemester() {
      return this.semester || localStorage.getItem('semester') || ''
    },
  },
})
