## print
## .title()
## .lower()
## .upper()
## f" {variable}"
## \t tab
## \n new line
## rstrip lstrip strip
## .removeprefix

print("hello World")

name = "  somendra saini  "
name = name.title()
print(name)

print(name.lower())

print(name.upper())

print(f"my name is : {name.title()}")

print(f"my name is : {(name.lstrip()).title()}")
print(f"my name is : {(name.rstrip()).title()}")
print(f"my name is : {(name.strip()).title()}")
print(f"\tmy name is {(name.strip()).title()} \n\tI study in Amity University")
linkedin_link = "https://linkedin.com/somendra"
print(f"\tmy name is {(name.strip()).title()} \n\tI study in Amity University \n\tMy linkedin is = {linkedin_link.removeprefix("https://")}")
