password=input("Enter the password : ")
check=set()
if len(password) >= 8:
    for i in password:
        if i.islower():
            check.add('l')
        elif i.isupper():
            check.add('u')
        elif i.isdigit():
            check.add('n')
        else:
            check.add('s')

    if len(check) == 4:
        print(" Strong Password ")
    else:
        print(" Weak Password ")
else:
    print("Password Length Should be 8 characters ")
