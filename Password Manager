import pyperclip as pc

web = {
    'Website_1': 'Password_1',
    'Website_2': 'Password_2',
    'Website_3': 'Password_3',
    'Website_4': 'Password_4',
    'Website_5': 'Password_5',
    'Website_6': 'Password_6'
}

def copy_password_to_clipboard(password):
    pc.copy(password)
    print(f"{password}\nCopied To Clipboard\n")

user = input("Enter Your Name: ")

if user.lower() == 'user':
    password = input("Enter The Password: ")

    if password.lower() == 'password@123':
        while True:
            print("Websites:\n")

            for idx, website in enumerate(web.keys(), start=1):
                print(idx, "-", website)

            ask = input("Enter 'q' to quit or Enter the Number for Password: ")

            if ask.lower() == 'q':
                break 

            try:
                ask = int(ask)
                selected_password = list(web.values())[ask - 1]
                copy_password_to_clipboard(selected_password)
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid number.")
    else:
        quit()
else:
    quit()
