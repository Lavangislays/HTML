# Name 10 students as input , add it in list
# sort it first so that names are alphabetwise
# then print it with roll number
# Tell me last 3 students names using indexing

name_list = []
for i in range(10):
    name = input("Enter your name")
    name_list.append(name)

print(name_list)

name_list.sort()

print(name_list)

length = len(name_list)
print(length)
 
for i in range(length):
    print(f"Name {i+1}: {name_list[i]}") 