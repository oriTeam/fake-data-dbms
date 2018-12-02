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
#Tao 2 bien dan den 2 file staff_file va profile_file
staff_w = open(staff_file, "a")
profile_w = open(profile_file, "a")

#ghi vao trong file staff_file doan text: {
staff_record = '{'
staff_w.write(staff_record)
#ghi vao trong fil profile_file doan text: {
profile_record = '{'
profile_w.write(profile_record)

 
for i in range(start, end - 1) :
    id = str(i)

    staff_w = open(staff_file, "a")
    profile_w = open(profile_file, "a")
    # credit_w = open(credit_file, "a")

    name = str(fake.name())
    staff_record = '"'+ id + '" : { "id" : ' + '"' + id + '", "name" : ' + '"' + name + '"}, '

    staff_w.write(staff_record)

    address = str(fake.city())
    dob = str(fake.date_this_century(before_today=True, after_today=False))
    phone = str(fake.phone_number())
    profile_record = '"' + id + '": {"id" : ' + '"' + id + '", "address" : ' + '"' + address + '", "date_of_birth" : ' + '"' + dob +'", "phone" : ' + '"' + phone + '"}, '
    profile_w.write(profile_record)

    # card = str(fake.credit_card_number(card_type=None))
    # credit[i] = {}
    # credit[i]['id'] = id
    # credit[i]['credit_card'] = card
    # with open(credit_file, 'a') as fp:
    #     json.dump(credit[i], fp)
    # credit_w.write(',')

    print(i)

print(end - 1)
id = str(end - 1)
staff_w = open(staff_file, "a")
profile_w = open(profile_file, "a")
# credit_w = open(credit_file, "a")

name = str(fake.name())
staff_record = '"'+ id + '" : { "id" : ' + '"' + id + '", "name" : ' + '"' + name + '"}}'

staff_w.write(staff_record)
address = str(fake.city())
dob = str(fake.date_this_century(before_today=True, after_today=False))
phone = str(fake.phone_number())
profile_record = '"' + id + '": {"id" : ' + '"' + id + '", "address" : ' + '"' + address + '", "date_of_birth" : ' + '"' + dob +'", "phone" : ' + '"' + phone + '"}}'
profile_w.write(profile_record)



