class Lesson:
    def __init__(self, name: str, start_hour: str, end_hour: str, duration: int):
        self.name = name
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.duration = duration

    def to_dictionary(self):
        return {
            'name': self.name,
            'start_hour': self.start_hour,
            'end_hour': self.end_hour,
            'duration': self.duration           
        }
    