SALARY_GRADE_LIST = [
    {"grade": 1, "low_salary": 15000, "high_salary": 20000},
    {"grade": 2, "low_salary": 21000, "high_salary": 25000},
    {"grade": 3, "low_salary": 26000, "high_salary": 38000},
    {"grade": 4, "low_salary": 40000, "high_salary": 56000},
    {"grade": 5, "low_salary": 58000, "high_salary": 78000},
    {"grade": 6, "low_salary": 83000, "high_salary": 126000},
    {"grade": 7, "low_salary": 135000, "high_salary": 296000},
    {"grade": 8, "low_salary": 300000, "high_salary": 450000},
]

COURSES_LIST = [
    {"course_id": 0, "course_name": "Поиск цели и смысла жизни"},
    {"course_id": 1, "course_name": "Японский язык для начинающих"},
    {"course_id": 2, "course_name": "Введение в облачные вычисления"},
    {"course_id": 3, "course_name": "Основы самоосознанности"},
    {"course_id": 4, "course_name": "Основы финансов"},
    {"course_id": 5, "course_name": "Машинное обучение"},
    {"course_id": 6, "course_name": "Искусственный интеллект для каждого"},
    {"course_id": 7, "course_name": "Финансовые рынки"},
    {"course_id": 8, "course_name": "Начало работы с AWS"},
    {"course_id": 9, "course_name": "Прогнозная аналитика и интеллектуальный анализ данных"},
    {"course_id": 10, "course_name": "Получение навыков обучения от Калифорнийского университета в Сан-Диего"},
    {"course_id": 11, "course_name": "Основы бизнеса"},
    {"course_id": 12, "course_name": "Управление карьерным ростом"},
    {"course_id": 13, "course_name": "Охрана труда"},
    {"course_id": 14, "course_name": "Электробезопасность"},
    {"course_id": 15, "course_name": "Управление стрессом"},
    {"course_id": 16, "course_name": "Управление конфликтами и их регулировка (Compliance)"},
]

EMPLOYEE_INSERT_TEMPLATE = "INSERT INTO public.employee (personnel_id, dept_id, grade_id, first_name, middle_name, " \
                           "last_name, salary, hire_date) VALUES ({}, {}, {}, \'{}\', \'{}\', \'{}\', {}, \'{}\'); \n"

EMPLOYEE_INSERT_TEMPLATE_PLUS_FIRE_DATE = "INSERT INTO public.employee (personnel_id, dept_id, grade_id, first_name, " \
                                          "middle_name, last_name, salary, hire_date, fire_date) " \
                                          "VALUES ({}, {}, {}, \'{}\', \'{}\', \'{}\', {}, \'{}\', \'{}\'); \n"

BUSINESS_TRIP_INSERT_TEMPLATE = "INSERT INTO public.business_trip (id, trip_id, personnel_id, city, start_date, " \
                                "end_date, day_salary) VALUES ({}, {}, {}, \'{}\', \'{}\', \'{}\', {}); \n"

DEPARTMENT_GRADE = [
    {"department": 1, "grades": [1, 2, 3, 4, 5, 8]},
    {"department": 2, "grades": [6, 7]},
    {"department": 3, "grades": [1, 2, 3, 4, 5, 8]},
    {"department": 4, "grades": [1, 2, 3, 4, 5, 8]},
    {"department": 5, "grades": [1, 2, 3, 4, 5, 8]},
    {"department": 6, "grades": [1, 2, 3, 4, 5, 8]},
    {"department": 7, "grades": [1, 2, 3, 4, 5, 8]},
    {"department": 8, "grades": [8]}
]