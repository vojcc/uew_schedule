from backend.models.day import Day
from backend.models.group import Group
from backend.models.lesson import Lesson
from backend.models.schedule import Schedule
from backend.helpers.time_converter import TimeConverter

class ScheduleContentTransformer:
    EIGHT_AM_HOUR = 480
    SEVEN_PM_HOUR = 1140

    GROUP_LIST = [
        "01 IwB",
        "02 IwB",
        "03 IwB",
        "04 IwB",
        "05 IwB",
        "06 IwB",
        "07 IwB",
    ]
    
    @staticmethod
    def transform(rows: list):
        rows_count = 0
        filtered_rows = []
        rows_in_day = len(ScheduleContentTransformer.GROUP_LIST)

        for row in rows:
            if rows_count == rows_in_day + 1:
                rows_count = 0
            if rows_count != 0:
                filtered_rows.append(row)
            rows_count += 1

        schedule = Schedule()

        for group_name in ScheduleContentTransformer.GROUP_LIST:
            group = Group(group_name)
            schedule.add_group(group)

        rows_count = 0
        hour_in_minutes = ScheduleContentTransformer.EIGHT_AM_HOUR
        date = ''

        for row in filtered_rows:
            if hour_in_minutes == ScheduleContentTransformer.SEVEN_PM_HOUR:
                hour_in_minutes = ScheduleContentTransformer.EIGHT_AM_HOUR

            if rows_count == rows_in_day:
                rows_count = 0

            cells = row.find_all('td')

            if rows_count == 0:
                date = cells[0].find('b').text.strip()
                start_iteration_index = 2
            else:
                start_iteration_index = 1

            group = schedule.get_group_by_index(rows_count)
            day = Day(date)

            for cell in cells[start_iteration_index:]:
                if cell.text == '\xa0\xa0\xa0':
                    duration = 15
                    lesson_name = '-'
                else:
                    duration = int(cell.attrs['colspan']) * 15
                    lesson_name = cell.text.strip()

                lesson = Lesson(
                    name = lesson_name,
                    start_hour = TimeConverter.minutes_to_hours(hour_in_minutes),
                    end_hour = TimeConverter.minutes_to_hours(hour_in_minutes + duration),
                    duration = duration,
                )

                day.add_lesson(lesson)
                hour_in_minutes += duration

            group.add_day(day)
            rows_count += 1
        
        return schedule