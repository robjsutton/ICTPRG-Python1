initials = " "
name_input = str(input("Please enter your full name: "))
split_name = name_input.split()
print(split_name)

for x in split_name:
    x = x + initials 
    print(x[0])