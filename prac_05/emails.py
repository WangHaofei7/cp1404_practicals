def main():
    email_name_dict = ()

    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        choice = input(f"Is your name {name}? (Y/n)")
        if choice.upper() == 'Y' or choice =="":
            email_name_dict[email] = name
        else:
            name = input('Name: ').title()
            email_name_dict[email] = name

        email = input("Email: ")

    for email, name in email_name_dict.items():
        print(f"{name} ({email})")

def test():
    name = get_name_from_email("hello@gmail.com")
    print(name)
    name = get_name_from_email("hello.word@gmail.com")
    print(name)
    name = get_name_from_email("hello.my.word@gmail.com")
    print(name)

def get_name_from_email(email):
    name_string = email.split('@')[0]
    name_string = name_string.replace('.', '')
    return name_string.title()

main()
#test()