#Task1 ask age and return the category from child, adult, Senior citizen

#age = int(input("Enter user age:"))
#print(age)

#def category(age):
 #if age<18:
  #  print("child")
 #elif age>30: 
  #  print("audlt")
 #else: 
  #  print("senior citizen")
#category(age)


#Task 2 ask age name and last four digit of aadharcard and return a unique ID like 
# if name is anmol and age is 12 and aadharcard no is 4567 
# then id will be an124567

age = int(input("Enter your age:"))
print(age)
name = str (input("Enter your name"))
print(name)
aadharcard=int(input("Enter last 4 digit of aadharcard:"))
print(aadharcard)
f2n=(name[0:2])
def category():
    print(f"unique id is:{f2n}{age}{aadharcard}")
category()
    