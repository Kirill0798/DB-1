from faker import Faker
import random
from constants import *
import pandas as pd

EMPLOYEES_COUNT = 10000
EMPLOYEES_FIRED_COUNT = 2500
DATE_PATTERN = "%d.%m.%Y"
GRADE_COUNT = 8

fake = Faker('ru_RU')
Faker.seed(0)

text_file_employee = open("output/employee_insert.sql", "w")
text_file_employee_fired = open("output/employee_fired_insert.sql", "w")

# Пришлось ввести для информации о поездках:
columns = ['personnel_id', 'dept_id', 'grade_id', 'first_name', 'middle_name', 'last_name', 'salary', 'hire_date', 'fire_date']
df = pd.DataFrame(columns=columns)

personnel_id_list = list(range(EMPLOYEES_COUNT + EMPLOYEES_FIRED_COUNT))
dept_id_list = []
grade_id_list = []
first_name_list = []
middle_name_list = []
last_name_list = []
salary_list = []
hire_date_list = []
fire_date_list = []


def form_common_information():
    rand = random.randrange(GRADE_COUNT)

    # Получение id департамента:
    department_id = DEPARTMENT_GRADE[rand].get("department")
    dept_id_list.append(department_id)

    # Генерация грейда в этом департаменте:
    grade_id = random.choice(DEPARTMENT_GRADE[rand].get("grades"))
    grade_id_list.append(grade_id)

    # Генерация ФИО:
    if rand % 2 == 0:
        first_name, middle_name, last_name = fake.first_name_male(), fake.middle_name_male(), fake.last_name_male()
    else:
        first_name, middle_name, last_name = fake.first_name_female(), fake.middle_name_female(), fake.last_name_female()

    first_name_list.append(first_name)
    middle_name_list.append(middle_name)
    last_name_list.append(last_name)

    # Получаем нижнюю, верхнюю границы по зп для грейда:
    low_salary, high_salary = SALARY_GRADE_LIST[grade_id - 1].get("low_salary"), SALARY_GRADE_LIST[
        grade_id - 1].get("high_salary")

    # Генерация зп:
    salary = random.randrange(low_salary, high_salary)
    salary_list.append(salary)

    # Генерация даты зачисления на работу:
    date_origin = fake.date_between(start_date='-10y')

    date = date_origin.strftime(DATE_PATTERN)
    hire_date_list.append(date)

    return department_id, grade_id, first_name, middle_name, last_name, salary, date, date_origin


def fill_with_employees():
    for i in range(EMPLOYEES_COUNT):
        department_id, grade_id, first_name, middle_name, last_name, salary, date, date_origin = form_common_information()
        fire_date_list.append('')

        # Формирование инсерта:
        s = EMPLOYEE_INSERT_TEMPLATE.format(i, department_id, grade_id, first_name, middle_name, last_name, salary, date)

        # Запись в файл:
        #text_file_employee.write(s)

    #text_file_employee.close()


def fill_with_resigned_employees():
    for i in range(EMPLOYEES_FIRED_COUNT):
        department_id, grade_id, first_name, middle_name, last_name, salary, date, date_origin = form_common_information()

        # Дата увольнения:
        date_of_resigned_origin = fake.date_between(start_date=date_origin)
        date_of_resigned = date_of_resigned_origin.strftime(DATE_PATTERN)
        fire_date_list.append(date_of_resigned)

        s = EMPLOYEE_INSERT_TEMPLATE_PLUS_FIRE_DATE.format(i + EMPLOYEES_COUNT, department_id, grade_id, first_name, middle_name,
                                                           last_name, salary, date, date_of_resigned)
        #text_file_employee_fired.write(s)

    #text_file_employee_fired.close()


def set_values_to_dataframe():
    df['personnel_id'] = personnel_id_list
    df['dept_id'] = dept_id_list
    df['grade_id'] = grade_id_list
    df['first_name'] = first_name_list
    df['middle_name'] = middle_name_list
    df['last_name'] = last_name_list
    df['salary'] = salary_list
    df['hire_date'] = hire_date_list
    df['fire_date'] = fire_date_list


def write_rows_to_files():
    for index, row in df.iterrows():
        if row['fire_date'] == '':
            # Формирование инсерта:
            s = EMPLOYEE_INSERT_TEMPLATE.format(index, row['dept_id'], row['grade_id'], row['first_name'],
                                                row['middle_name'], row['last_name'], row['salary'], row['hire_date'])
            # Запись в файл:
            text_file_employee.write(s)
        else:
            s = EMPLOYEE_INSERT_TEMPLATE_PLUS_FIRE_DATE.format(index, row['dept_id'], row['grade_id'],
                                                               row['first_name'], row['middle_name'], row['last_name'],
                                                               row['salary'], row['hire_date'], row['fire_date'])
            text_file_employee_fired.write(s)


fill_with_resigned_employees()
fill_with_employees()
set_values_to_dataframe()
write_rows_to_files()
