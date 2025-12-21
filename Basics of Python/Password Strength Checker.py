def check_password_strength():
    Password=input("Enter you Password: ")
    islngthok= len(Password)>=8
    has_upper=False
    has_lower = False
    has_special = False
    has_number = False


    for i in Password:
        if i.isupper():
            has_upper=True
        elif i.islower():
            has_lower=True
        elif i.isnumeric():
            has_number=True
        elif i in "!@#$%&*%<>?/-_₹":
            has_special=True
    requirement_list=[islngthok,has_special,has_upper,has_lower]
    total=(islngthok+has_number+has_lower+has_upper+has_special)
    if total>=4:
        print("Password Strength: STRONG\n")
    elif total==3:
        print("Password Strength: MEDIUM ")
        print("Can be stronger👍\n")
    else:
        print("Password Strength: WEAK")
        print("Make it stronger\n")

    if islngthok:
        print("Length Requirement Met ✔")
    else:
        print("Must have more than or at least 8 Characters")
    if has_upper:
        print("Contains Uppercase Letters ✔")
    else:
        print("Must contain at least 1 upper case letter.")
    if has_lower:
        print("Contains Lower case letters ✔")
    else:
        print("Must have at least 1 lower case letter")
    if has_number:
        print("Contains Numbers ✔")
    else:
        print("Must at least contain 1 number")
    if has_special:
        print("Contains Special Letters ✔")
    else:
        print("Must contain at least one special character.")
    print("\n")
check_password_strength()