workshop_a = ["Aryan", "Meera", "Rohan", "Fatima", "Karan"]
workshop_b = ["Meera", "Karan", "Priya", "Sneha", "Aryan"]

set_1 = set(workshop_a)
set_2 = set(workshop_b)

print(type(set_1))
print(type(set_2))

both_workshop = set_1.intersection(set_2)
print(both_workshop)

a_only = set_1.difference(set_2)
print(a_only)
atl_one = set_1.union(set_2)
print(atl_one)
only_one = set_1.symmetric_difference(set_2)
print(only_one)