from faker import Faker
import json


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
credit = {}


staff_file = PATH + "staff_file[" + str(start) + '_' + str(end) + "].json"
profile_file = PATH + "profile_file[" + str(start) + '_' + str(end) + "].json"
credit_file = PATH + "credit_file[" + str(start) + '_' + str(end) + "].json"

for i in range(start, end):
    id = str(i)

    name = str(fake.name())
    staff[i] = {}
    staff[i]['id'] = id
    staff[i]['name'] = name

    address = str(fake.city())
    dob = str(fake.date_this_century(before_today=True, after_today=False))
    phone = str(fake.phone_number())
    profile[i] = {}
    profile[i]['id'] = id
    profile[i]['address'] = address
    profile[i]['date_of_birth'] = dob
    profile[i]['phone'] = phone

    card = str(fake.credit_card_number(card_type=None))
    credit[i] = {}
    credit[i]['id'] = id
    credit[i]['credit_card'] = card

    print(i)

staff_table = {"staff": staff}
profile_table = {"profile": profile}
credit_table = {"credit": credit}


with open(staff_file, 'w') as fp:
    json.dump(staff_table, fp)

with open(profile_file, 'w') as fp:
    json.dump(profile_table, fp)

with open(credit_file, 'w') as fp:
    json.dump(credit_table, fp)
