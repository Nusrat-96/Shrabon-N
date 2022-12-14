#class five 
student = {}
list1=[]



a = int(input("Number of student: "))
for i in range(a):
    name = input("enter student name:")
    student['name']= name
    age = int(input("enter student age: "))
    student["age"]=age
    cgpa = float(input("enter student cgpa: "))
    student["cgpa"]= cgpa
    list1.append(student.copy())
    
print(list1)
# print (list1[0]["name"])
teacher = {}
teacher_info = []
for j in range(a):
    name_t = input("Enter Teacher name: ")
    teacher["name"]=name_t
    subject = input("Insert subject: ").split(' ')
    teacher["subjectes"]=subject
    teacher_info.append(teacher.copy())
print(teacher_info)


