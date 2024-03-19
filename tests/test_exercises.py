import pytest

from exercise_1 import unique_teacher_names
from exercise_2 import number_of_names
from exercise_3 import find_longest_and_shortest_course


@pytest.mark.parametrize(
    'mentors, expected',
    (
            [[['Олег Сидоров', 'Иван Круглов', 'Олег Крутов'],
              ['Артём Иванов', 'Иван Смирнов', 'Фёдор Антипов'],
              ['Алексей Фадеев', 'Александр Войнов']],
             {'Олег', 'Иван', 'Артём', 'Фёдор', 'Алексей', 'Александр'}],
            [[['Алексей Сидоров', 'Алексей Круглов', 'Олег Крутов'],
              ['Артём Иванов', 'Иван Смирнов', 'Фёдор Антипов'],
              ['Алексей Фадеев', 'Фёдор Войнов']],
             {'Олег', 'Иван', 'Артём', 'Фёдор', 'Алексей'}]
    )
)
def test_unique_teacher_names(mentors, expected):
    result = unique_teacher_names(mentors)
    assert expected == result


@pytest.mark.parametrize(
    'mentors, expected',
    (
            [[['Олег Сидоров', 'Иван Круглов', 'Олег Крутов'],
              ['Артём Иванов', 'Иван Смирнов', 'Фёдор Антипов'],
              ['Алексей Фадеев', 'Александр Войнов']],
             {3: {'Олег'}, 2: {'Иван'}, 6: {'Артём'}, 5: {'Алексей', 'Фёдор'},
              9: {'Александр'}}],
            [[['Адилет Сидоров', 'Владимир Круглов', 'Олег Крутов'],
              ['Антон Иванов', 'Илья Смирнов', 'Вадим Антипов'],
              ['Дмитрий Фадеев', 'Константин Войнов', 'Александр Блинов']],
             {1: {'Адилет'}, 2: {'Владимир'}, 3: {'Олег'}, 4: {'Антон'},
              5: {'Илья'}, 6: {'Вадим'}, 7: {'Дмитрий'}, 8: {'Константин'},
              9: {'Александр'}}]
    )
)
def test_number_of_names(mentors, expected):
    result = number_of_names(mentors)
    assert expected == result


@pytest.mark.parametrize(
    'courses, mentors, durations, expected',
    (
            [['Курс_1', 'Курс_2', 'Курс_3'],
             [['П_1'], ['П_2'], ['П_3']],
             [5, 8, 2],
             {'courses_min': {
                 'durations': 2,
                 'courses': {'Курс_3'}
             },
                 'courses_max': {
                     'durations': 8,
                     'courses': {'Курс_2'}
                 }
             }],
            [['Курс_1', 'Курс_2', 'Курс_3', 'Курс_4'],
             [['П_1'], ['П_2'], ['П_3'], ['П_4']],
             [6, 8, 3, 8],
             {'courses_min': {
                 'durations': 3,
                 'courses': {'Курс_3'}
             },
                 'courses_max': {
                     'durations': 8,
                     'courses': {'Курс_4', 'Курс_2'}
                 }
             }]
    )
)
def test_find_longest_and_shortest_course(courses, mentors, durations,
                                          expected):
    result = find_longest_and_shortest_course(courses, mentors, durations)
    assert expected == result
