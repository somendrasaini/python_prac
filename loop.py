

## for loop
## while loop
cus_name = []

while True :
    first_name = input("Enter your first name : ")
    if first_name == "quit":
        break
    last_name = input("Enter your last name : ")
    fullname = []
    fullname.append(first_name)
    fullname.append(last_name)
    cus_name.append(fullname)



for i in cus_name:
    for j in i:
        print(j.title())


my_name = ("somendra", "saini")


