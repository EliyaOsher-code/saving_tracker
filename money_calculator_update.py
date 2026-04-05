
import json
import os

if os.path.exists("emails.json"):
    with open("emails.json", "r") as file:
        try:
            email_dict = json.load(file)
        except json.JSONDecodeError:
            email_dict = {}
else:
    email_dict = {}

email_list = list(email_dict.keys())
current_email = None

def save_all():
    with open("emails.json", "w") as file:
        json.dump(email_dict, file)

def get_saving():
    return email_dict.get(current_email, 0)

def create_email(email):
    if email in email_dict:
        print("email already exist")
    else:
        email_dict[email] = 0
        email_list.append(email)
        save_all()

def add_money(amount):
    email_dict[current_email] += amount
    save_all()

def remove_money(amount):
    email_dict[current_email] -= amount
    save_all()

def chek_new_email(email):
    if '@gmail.com' not in email:
        print("something went wrong try again")
    else:
        create_email(email)

def only_for_creator():
    password = input("enter password ")
    if password == '1234567890':
        print("-----------hello and welcome creator----------")
        for us in email_list:
            print(f"user: {us} | saving: {email_dict[us]}")
        c = input("what would you want to do? delete / erase all / change ")

        if 'delete' in c.lower():
            users_change = input("what account do you want to delete? ")
            if users_change in email_dict:
                del email_dict[users_change]
                email_list.remove(users_change)
                save_all()
                print(f"user {users_change} deleted")
            else:
                print("no user was found")

        elif 'erase all' in c.lower():
            for_safe = input("are you sure you want to delete all users? ")
            if for_safe.lower() in ['yes', 'ye']:
                email_dict.clear()
                email_list.clear()
                save_all()
                print("all users deleted")

        elif 'change' in c.lower():
            email = input("what user do you want? ")
            if email in email_dict:
                remove_or_append = input("would you like to remove or append money? ")
                if 'append' in remove_or_append.lower() or 'add' in remove_or_append.lower():
                    amount = float(input("how much? "))
                    email_dict[email] += amount
                    save_all()
                    print(f"{email} now has {email_dict[email]} shekels")
                elif 'remove' in remove_or_append.lower():
                    amount = float(input("how much? "))
                    email_dict[email] -= amount
                    save_all()
                    print(f"{email} now has {email_dict[email]} shekels")

def append_or_remove_or_exit_or_delete():
    r = 0
    while r < 7:
        print("")
        choise = input("would you like to append / remove / exit / delete? ")
        print("")

        if 'append' in choise.lower():
            amount_append = float(input("how much? "))
            add_money(amount_append)

        elif 'remove' in choise.lower():
            amount_remove = float(input("how much? "))
            remove_money(amount_remove)

        elif 'exit' in choise.lower():
            print(f"your saving is {get_saving()} shekels")
            break

        elif 'delete' in choise.lower():
            the_email = input("enter your email: ")
            if the_email in email_dict:
                del email_dict[the_email]
                email_list.remove(the_email)
                save_all()
                print("account deleted successfully")
            else:
                print("email not found")
            break

        elif 'creator' in choise.lower():
            only_for_creator()

        else:
            print("error")
            r += 1

        print(f"your saving is {get_saving()} shekels")


print("          --------------saving calculator-------------------          ")
h = input("you have an account or do you want to create one? ")

if 'have' in h.lower():
    email = input("enter your email: ")
    if email not in email_dict:
        print("email was not found, please try again or create a new account")
        attempts = 0
        max_attempts = 7
        succes = False

        while attempts < max_attempts:
            q = input("would you like to create a new account or try again? ")

            if 'create' in q.lower():
                new_account = input("enter your email: ")
                chek_new_email(new_account)
                current_email = new_account
                succes = True
                break

            elif 'try' in q.lower() or 'again' in q.lower():
                email = input("write your email: ")
                if email in email_dict:
                    current_email = email
                    succes = True
                    break
                else:
                    attempts += 1
                    print(f"email was not found, {max_attempts - attempts} attempts left")

            elif 'exit' in q.lower():
                break
            else:
                print("error try again")

        if succes:
            append_or_remove_or_exit_or_delete()

    else:
        current_email = email
        append_or_remove_or_exit_or_delete()

elif 'create' in h.lower():
    new_account = input("enter your email: ")
    chek_new_email(new_account)
    current_email = new_account
    append_or_remove_or_exit_or_delete()

else:
    print("error try again")
