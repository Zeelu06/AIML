students = [
    ("Aryan", 21, "Computer Science"),
    ("Meera", 22, "Mathematics"),
    ("Rohan", 20, "Physics"),
    ("Sneha", 23, "Computer Science"),
]

for name, age, department in students:
    print(f"{name} ({age}) - {department}")

totalcs = 0

for student in students:
    if student[2] == "Computer Science":
        totalcs = totalcs + 1

print("Total CS student:", totalcs) 

def oldest_student():
    
    oldest = students[0]

    for student in students:
        if student[1] > oldest[1]:
            oldest = student

    print(oldest)
    return oldest 
oldest_student()
names = ()
for name, age, department in students:
    names = names + (name,)
print(names)