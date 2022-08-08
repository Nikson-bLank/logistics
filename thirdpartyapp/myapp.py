import requests
import json

########create##############

# URL =  "http://localhost:8000/driver_create/"

# data = {
#     'first_name':'veer',
#     'last_name':'yadav',
#     'email':'amit@gmail.com',
#     'password':"amin@123",
#     'phone_number':8689876769,
#     'address':'rau',
#     'vehicle_registration_number':'KG%&*R^%BV',
#     'driving_licence_number':'2432HHGHGJH3',
#     'registration_card_photo':'./Screenshot_from_2022-01-17_11-49-41.png',
#     'driving_licence_photo':'./Screenshot_from_2022-02-03_12-39-17.png',

# }

# json_data = json.dumps(data)
# r = requests.post(url = URL, data = json_data)

# data = r.json()
# print(data)

# ######update##########

# URL =  "http://localhost:8000/driver_update/"

# data = {
#     'id':4, 
#     'first_name':'vinay',
#     'last_name':'tiwari',
#     'email':'amit@gmail.com',
#     'password':"amin@123",
#     'phone_number':8689876769,
#     'address':'indore',
#     'vehicle_registration_number':'KG%&*R^%BV',
#     'driving_licence_number':'2432HHGHGJH3',
#     # 'registration_card_photo':'./Screenshot_from_2022-01-17_11-49-41.png',
#     # 'driving_licence_photo':'./Screenshot_from_2022-02-03_12-39-17.png',

# }

# json_data = json.dumps(data)
# r = requests.put(url = URL, data = json_data)

# data = r.json()
# print(data)

########delete##############

URL =  "http://localhost:8000/driver_delete/"

data = {'id':1,}

json_data = json.dumps(data)
r = requests.delete(url = URL, data = json_data)

data = r.json()
print(data)
