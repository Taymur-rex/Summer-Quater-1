





student = {}


studentname = input("Enter your student's name: ")
student["Name"] = studentname


StudentAge = input("Enter your student's age: ")
student["Age"] = StudentAge


studentgrade = input("Enter your student's grade: ")
student["Grade"] = studentgrade


hobbies = []
hobby = input("Enter your studetns hobbies; Type 'done' when done").lower()
hobbies.append(hobby)

while hobby != "done":
    hobby = input("Enter your studetns hobbies; Type 'done' when done").lower()
    hobbies.append(hobby)


student["Hobbies"] = hobbies


print(student)
