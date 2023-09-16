print("Exersice 23 Student Marks")
student_marks ={
  'Subin': 69,
  'Rajappan': 92,
  'Achu': 100,
  'Kannan': 98,
  'Purushu': 38,
  'Srank': 43,
  'Kandan': 57,
  'Rajamma': 75,
  'Kileri': 86
}
print(student_marks)
Student_grade= student_marks.copy()
print(Student_grade)
for i in student_marks:
    if student_marks[i] <40:
        Student_grade[i]='Fail'
    elif student_marks[i]>=40 and student_marks[i]<=50:
        Student_grade[i] = 'D'
    elif student_marks[i]>=51 and student_marks[i]<=60:
        Student_grade[i] = 'C'
    elif student_marks[i]>=61 and student_marks[i]<=70:
        Student_grade[i] = 'B'
    elif student_marks[i]>=71 and student_marks[i]<=80:
        Student_grade[i] = 'B+'
    elif student_marks[i]>=81 and student_marks[i]<=90:
        Student_grade[i] = 'A'
    elif student_marks[i]>=91 and student_marks[i]<=100:
        Student_grade[i] = 'A+'



print(Student_grade)