amount_of_homework_done: int = 12
number_of_hours_spent: float = 1.5
course_name: str = 'Python'
time_for_one_task = number_of_hours_spent / amount_of_homework_done

print(f"Курс {course_name}, всего задач: {amount_of_homework_done}, среднее время выполнения {time_for_one_task} часа.")
