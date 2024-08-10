#1
dict1={"num1":1,"num2":2}
print(dict1["num1"])
#2
a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
print(a_dict.items())
for key, value in a_dict.items():
    print(key, '->', value)
#3
sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}
print(sample_dict["class"]["student"]["marks"]["history"])
#4
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}
keys_to_remove = ["name", "salary"]
for key in keys_to_remove:
    del sample_dict[key]
print(sample_dict)
#5
student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}
student_averages={}
student_letter_grades={}
for key in student_grades:
    student_averages[key]=(student_grades[key][0]+student_grades[key][1]+student_grades[key][2])/3
for key in student_averages:
    if student_averages[key]>=90:
        student_letter_grades[key]="A"
    elif student_averages[key]>=80 and student_averages[key]<90:
        student_letter_grades[key]="8"
    elif student_averages[key]>=70 and student_averages[key]<80:
        student_letter_grades[key]="C"
    elif student_averages[key]>=60 and student_averages[key]<70:
        student_letter_grades[key]="D"
    else: student_letter_grades[key]="D"
print(student_letter_grades)
print(student_averages)