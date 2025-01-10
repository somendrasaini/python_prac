## List operations

new_empty_list = []

names = ['somendra', 'nitish', 'dheeraj', "mayank"]
print(names)



names.append("akhilesh")
names.insert(0, "aman")

print(f"First member of the list is : {names[0].title()} ")

print(f"last member of the list is : {names[-1].title()}")

removed_name = names.pop(0)
names.remove("akhilesh")
names.sort()
print(names)
names.reverse()
print(names)
print(names[-2:])

print(f"First member of the list is : {names[0].title()} ")
print(f"removed name : {removed_name.title()}")


numberList = list(range(0,21,5))
print(numberList)

