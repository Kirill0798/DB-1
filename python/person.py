from faker import Faker
import random
from constants import *
import pandas as pd

EMPLOYEES_COUNT = 10000
EMPLOYEES_FIRED_COUNT = 2500
DATE_PATTERN = "%d.%m.%Y"
GRADE_COUNT = 8
JOINT_COUNT = 10

fake = Faker('ru_RU')
Faker.seed(0)

text_file_employee = open("output/employee_insert.sql", "w")
text_file_employee_fired = open("output/employee_fired_insert.sql", "w")
text_file_joint_business_trip = open("output/business_trip_insert.sql", "w")

# Пришлось ввести для информации о поездках:
columns = ['personnel_id', 'dept_id', 'grade_id', 'first_name', 'middle_name', 'last_name', 'salary', 'hire_date',
           'fire_date', 'hire_date_origin', 'fire_date_origin']
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
hire_date_origin_list = []
fire_date_origin_list = []


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
    hire_date_origin_list.append(date_origin)

    return department_id, grade_id, first_name, middle_name, last_name, salary, date, date_origin


def fill_with_employees():
    for i in range(EMPLOYEES_COUNT):
        department_id, grade_id, first_name, middle_name, last_name, salary, date, date_origin = form_common_information()
        fire_date_list.append('')
        fire_date_origin_list.append('')

        # Формирование инсерта:
        s = EMPLOYEE_INSERT_TEMPLATE.format(i, department_id, grade_id, first_name, middle_name, last_name, salary, date)


def fill_with_resigned_employees():
    for i in range(EMPLOYEES_FIRED_COUNT):
        department_id, grade_id, first_name, middle_name, last_name, salary, date, date_origin = form_common_information()

        # Дата увольнения:
        date_of_resigned_origin = fake.date_between(start_date=date_origin)
        date_of_resigned = date_of_resigned_origin.strftime(DATE_PATTERN)
        fire_date_list.append(date_of_resigned)
        fire_date_origin_list.append(date_of_resigned_origin)

        s = EMPLOYEE_INSERT_TEMPLATE_PLUS_FIRE_DATE.format(i + EMPLOYEES_COUNT, department_id, grade_id, first_name,
                                                           middle_name, last_name, salary, date, date_of_resigned)


def set_values_to_dataframe():
    df['personnel_id'] = personnel_id_list
    df['dept_id'] = dept_id_list
    df['grade_id'] = grade_id_list
    df['first_name'] = first_name_list
    df['middle_name'] = middle_name_list
    df['last_name'] = last_name_list
    df['salary'] = salary_list
    df['hire_date'] = hire_date_list
    df['hire_date_origin'] = hire_date_origin_list
    df['fire_date'] = fire_date_list
    df['fire_date_origin'] = fire_date_origin_list


def write_empl_rows_to_files():
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


def write_business_rows_to_files(dataframe, trip_id, last_hire_date, first_fire_date):
    city = fake.city()

    start_date = fake.date_between(last_hire_date, first_fire_date)
    end_date = fake.date_between(start_date, first_fire_date)

    for index_w, row in dataframe.iterrows():
        s = BUSINESS_TRIP_INSERT_TEMPLATE.format(index_w, trip_id, row["personnel_id"], city, start_date, end_date,
                                                 row["salary"] / 20 * 2)
        text_file_joint_business_trip.write(s)


def joint_business_trip(travelers_count=10):
    business_df = df.loc[:travelers_count, ['personnel_id', 'salary', 'hire_date_origin', 'fire_date_origin']]

    # index - trip-id
    trip_id = 0
    for index in range(len(business_df)):
        # Количество людей в одной поездке:
        rand = random.randrange(1, JOINT_COUNT)

        if (trip_id + rand) >= len(business_df):
            break
        # Выделяем dataframe:
        indexes_for_taken = list(range(trip_id, trip_id + rand))
        trip_id += rand
        index += rand
        current_df = business_df.take(indexes_for_taken)

        # Сортируем по дате увольнения и выкидываем чуваков, кто был устроен после:
        # Список дат устройства на работу для людей из одной поездки:
        fire_date_one_trip = []
        for _, row in current_df.iterrows():
            if row["fire_date_origin"] != '':
                fire_date_one_trip.append(row["fire_date_origin"])

        fire_date_one_trip.sort()

        if fire_date_one_trip:
            current_df = current_df[current_df["hire_date_origin"] < fire_date_one_trip[0]]

        hire_date_one_trip = current_df["hire_date_origin"].tolist()
        hire_date_one_trip.sort()

        first_fire_date = fire_date_one_trip[0] if (fire_date_one_trip and fire_date_one_trip[0] != '') else 'today'
        write_business_rows_to_files(current_df, trip_id, hire_date_one_trip[-1], first_fire_date)


if __name__ == '__main__':
    # Инсерты для сотрудников:
    fill_with_resigned_employees()
    fill_with_employees()
    set_values_to_dataframe()
    write_empl_rows_to_files()


    # Перемешаем данные:
    df = df.sample(frac=1)
    joint_business_trip()

