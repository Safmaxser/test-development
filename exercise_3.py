def find_longest_and_shortest_course(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor,
                       "duration": duration}
        courses_list.append(course_dict)
    min_durations = min(durations)
    max_durations = max(durations)
    maxes = []
    minis = []
    for index, duration in enumerate(durations):
        if duration == max_durations:
            maxes.append(index)
        elif duration == min_durations:
            minis.append(index)
    courses_min = []
    courses_max = []
    for index in minis:
        courses_min.append(courses_list[index]["title"])
    for index in maxes:
        courses_max.append(courses_list[index]["title"])
    return {
        'courses_min': {
            'durations': min_durations,
            'courses': set(courses_min)
        },
        'courses_max': {
            'durations': max_durations,
            'courses': set(courses_max)
        }
    }


if __name__ == '__main__':
    courses_m = ["Java-разработчик с нуля", "Fullstack-разработчик на Python",
                 "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
    mentors_m = [
        ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков",
         "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков",
         "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
         "Никита Шумский",
         "Алексей Степанов", "Денис Коротков", "Антон Глушков",
         "Сергей Индюков",
         "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен",
         "Сергей Сердюк", "Павел Дерендяев"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин",
         "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев",
         "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко",
         "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин",
         "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов",
         "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин",
         "Александр Иванов", "Антон Солонилин", "Максим Филипенко",
         "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер",
         "Татьяна Тен", "Александр Фитискин", "Александр Шлейко",
         "Алена Батицкая",
         "Александр Беспоясов", "Денис Ежков", "Николай Лопин",
         "Михаил Ларченко"]
    ]
    durations_m = [14, 20, 12, 20]

    result = find_longest_and_shortest_course(courses_m, mentors_m,
                                              durations_m)
    print(f'Самый короткий курс(ы): '
          f'{", ".join(result["courses_min"]["courses"])} '
          f'- {result["courses_min"]["durations"]} месяца(ев)')
    print(f'Самый длинный курс(ы): '
          f'{", ".join(result["courses_max"]["courses"])} '
          f'- {result["courses_max"]["durations"]} месяца(ев)')
