from faker import Faker

import constants

fake = Faker('ru_RU')
Faker.seed(0)

for _ in range(5):
    print(fake.city_name())

print(constants.SALARY_GRADE_LIST)