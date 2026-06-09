# num=int(input("Enter a number:"))
# print(num)
# import random
# user = random.randint(1,5)
# print(user)
# if num==user:
#     print("win")
# else:
#         print("loss")

tasklist = {
    "tasks":[]
}

while True:
    choice = input("press 1 to add, \npress 2 to delete, \npress 3 to update \npress 4 to see tasks \nEnter Choice:")

    if choice == "1":
        name = input("enter name of task:")    
        desc = input("enter description:")
        email = input("enter email:")
        data = {"name":name, "description":desc,"email":email }
        tasklist["tasks"].append(data)
        
        print("Task Addedd Successfully")
     
     elif choice =="3":
        update = input("Enter task name to update:")
        for task ["name"] == update:

            task["name"] = input["Enter new name:"]
            task["description"] = input["Enter new description:"]
            task["email"] = input["Enter new email:"]
            
            print ("Task update successfully")

    else:
        print("task not found")
                
