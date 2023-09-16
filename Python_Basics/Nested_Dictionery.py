print("Nested Dictionary")

Student_data = {
    'Subin': {'Roll Number': 13, 'Age': 33, 'Subject': 'Python'},
    'Rajappan':{'Roll Number': 12, 'Age': 32, 'Subject': 'HTML'},
    'Achu':{'Roll Number': 10, 'Age': 30, 'Subject': 'CSS'},
    'Kannan':{'Roll Number': 11, 'Age': 4, 'Subject': 'Java'},
}
print(Student_data)
print("Accessing Subin")
print(Student_data['Subin'])
print("Accessing Subin's Subject")
print(Student_data['Subin']['Subject'])
print("Adding mobile number in Kannan")
Student_data['Kannan']['Mobile Number']= 9910247855
Student_data['Achu']['Mobile Number']= 8368315928
print(Student_data['Kannan'])
print(Student_data['Achu'])
print("Delecting Achu's Phone number")
del Student_data['Achu']['Mobile Number']
print(Student_data['Achu'])
print("Delecting Kannan's Mobile Number using pop")
print(Student_data['Kannan'].pop("Mobile Number"))
print(Student_data['Kannan'])

print("Nesting a list in a dictionary")

travel_data= {
    'Kerala': ['Munnar','Vagamon', 'Alappuzha'],
    'Tamil Nadue': ['Ooty', 'Kodaikanal', 'Vellure']
}
print(travel_data)
print(travel_data['Kerala'])

print("Nesing dictionaries in a list")
st_data= [{'Name':'Subin',
           'Age':33,
           'Subject': 'Python'
           },
          {'Name':'Kandan',
           'Age':4,
           'Subject': 'CSS',
           'phonenumber':[9910247855,9633468540]
           }
]

print(st_data)
print(st_data[1])
print(st_data[1]['Subject'])
print(st_data[1]['phonenumber'])