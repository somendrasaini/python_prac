
user_0 = {"username":"ssaini","firstname":"somendra","lastname":"saini","id":"0"}

print(user_0['firstname'])

for k,v in user_0.items():
    print(f"Key : {k.title()}")
    print(f"Value : {v.title()}")