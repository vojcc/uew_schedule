from .lesson import Lesson

class Day:
    def __init__(self, date: str):
        self.date = date
        self.lessons = []

    def add_lesson(self, lesson: Lesson):
        self.lessons.append(lesson)  

    def to_dictionary(self):
        return {
            'date': self.date,
            'lessons': [lesson.to_dictionary() for lesson in self.lessons],         
        }
    