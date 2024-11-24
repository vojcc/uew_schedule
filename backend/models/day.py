from backend.models.lesson import Lesson

class Day:
    def __init__(self, date: str):
        self.date = date
        self.name = ''
        self.lessons = []

    def set_name(self, name: str):
        self.name = name

    def add_lesson(self, lesson: Lesson):
        self.lessons.append(lesson)

    def to_dictionary(self):
        return {
            'date': self.date,
            'name': self.name,
            'lessons': [lesson.to_dictionary() for lesson in self.lessons],         
        }
    