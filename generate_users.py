import random

from faker import Faker
from models import *


def generate_random_users_profiles():
    faker = Faker()
    i = 0
    while i < 1000000:
        profile = faker.simple_profile()
        user_profile = User(name=profile['name'], username=profile['username'], sex='F', email='Bob@email.com',
                            active=faker.pybool(), admin=faker.pybool())
        user_profile.save()
        print(i)
        print(user_profile)
        i = i+1


if __name__ == '__main__':
    db.connect()
    db.create_tables([User])
    print(generate_random_users_profiles())

