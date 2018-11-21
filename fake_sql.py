from faker import Faker
fake = Faker('en_US')
# staff = open("/content/drive/My Drive/colab2/staff.txt", "a")
# profile = open("/content/drive/My Drive/colab2/profile.txt", "a")
# DRIVE_URL = "/content/drive/My Drive/colab2/"
import os
PATH = str(os.getcwd()) + '/data/'
NUM = 100000000

while True:
    start = input("----- Start at (id) : ")
    end = input("----- End at (id) : ")
    if start.isdigit() or end.isdigit():
        start = int(start)
        end = int(end)
        break

for i in range(start, end):
    id = str(i)

    staff_file = PATH + "staff_file[" + str(start) + '_' + str(end) + "].txt"
    profile_file = PATH + "profile_file[" + str(start) + '_' + str(end) + "].txt"    
    credit_file = PATH + "credit_file[" + str(start) + '_' + str(end) + "].txt"
    staff = open(staff_file, "a")
    profile = open(profile_file, "a")
    credit = open(credit_file, "a")


    name = str(fake.name())
    staff_record = '('+ id + ',' + name + '),'
    staff.write(staff_record)
    

    address = str(fake.city())
    dob = str(fake.date_this_century(before_today=True, after_today=False))
    phone = str(fake.phone_number())
    profile_record = "(" + id + ',' +  address + ',' + dob + ',' + phone + "),"
    profile.write(profile_record)
    
    card = str(fake.credit_card_number(card_type=None))
    credit_record = '('+ id + ',' + name + '),'
    credit.write(credit_record)
    
    print(i)