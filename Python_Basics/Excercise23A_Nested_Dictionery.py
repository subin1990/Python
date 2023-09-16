print("Excercise 23A")
Student_data= [
    {'Name': 'Subin',
    'Roll Number': 10,
     'Age': 33,
     'Subject': 'Python'
     },
    {'Name': 'Achu',
     'Roll Number': 11,
     'Age': 30,
     'Subject': 'HTML& CSS'
    }
]


def Add_new_student(Name,Roll_Number,Age,Subject):

    Student_data.append({'Name':Name,
    'Roll Number':Roll_Number,
    'Age': Age,
    'Subject': Subject}
    )





Add_new_student('Rajappan',15,35,'Java')
print(Student_data)