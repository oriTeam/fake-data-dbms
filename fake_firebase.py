import json
from faker import Faker

fake = Faker('en_US')

import os

PATH = str(os.getcwd()) + '/firebase_data/'

while True:
    start = input("-- Start at (id) : ")
    end = input("-- End at (id) : ")
    if start.isdigit() or end.isdigit():
        start = int(start)
        end = int(end)
        break

staff = {}
profile = {}
# credit = {}

staff_file = PATH + "staff_file[" + str(start) + '_' + str(end) + "].json"
profile_file = PATH + "profile_file[" + str(start) + '_' + str(end) + "].json"
# credit_file = PATH + "credit_file[" + str(start) + '_' + str(end) + "].json"

for i in range(start, end):
    id = str(i)

    staff_w = open(staff_file, "a")
    profile_w = open(profile_file, "a")
    # credit_w = open(credit_file, "a")

    name = str(fake.name())
    staff[i] = {}
    staff[i]['id'] = id
    staff[i]['name'] = name
    with open(staff_file, 'a') as fp:
        json.dump(staff[i], fp)
    staff_w.write(',')

    address = str(fake.city())
    dob = str(fake.date_this_century(before_today=True, after_today=False))
    phone = str(fake.phone_number())
    profile[i] = {}
    profile[i]['id'] = id
    profile[i]['address'] = address
    profile[i]['date_of_birth'] = dob
    profile[i]['phone'] = phone
    with open(profile_file, 'a') as fp:
        json.dump(profile[i], fp)
    profile_w.write(',')

    # card = str(fake.credit_card_number(card_type=None))
    # credit[i] = {}
    # credit[i]['id'] = id
    # credit[i]['credit_card'] = card
    # with open(credit_file, 'a') as fp:
    #     json.dump(credit[i], fp)
    # credit_w.write(',')

    print(i)
