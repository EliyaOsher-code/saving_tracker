import json
import os
if os.path.exists("emails.json"):
    with open ("emails.json" , "r") as file:
        email_list = json.load(file)
else:
    email_list = []

def save_email():
    with open ("emails.json" , "w") as file:
        json.dump(email_list , file)

def create_email(email):
    if email in email_list:
        print ("email already exist")
    else:
        email_list.append(email)
        save_email()



file_name = "email.json"
if os.path.exists(file_name) and os.path.getsize(file_name) >0:
    with open (file_name , "r") as file:
        try: 
            saving = json.load(file)
        except json.JSONDecodeError:
            saving = 0
else:
    saving = 0
def add_money(amount):
    global saving
    saving += amount
    with open (file_name , "w") as file:
        json.dump(saving , file)
        

def remove_money(amount):
    global saving
    saving -= amount
    with open (file_name , "w") as file:
        json.dump(saving ,  file)
    


def only_for_creator():
    password = input ("enter password ")

    if password == '1234567890':
        print("-----------hello and welcome creator----------")
        for us in email_list:
            print(f"user: {email_list}")
        c = input ("what would you want to do ? delete accounts or change accounts ammounts of savings ")
        if 'delete' in c.lower():
            users_change = input(f"what accounts do you want to delete? ")
            if users_change in email_list:
                email_list.remove(users_change)
                save_email()
                print(f"user {users_change} deleted")
            else:
                print("no user was found")

        elif 'erase all' in c.lower() :
            for_safe = input ("are you sure you want to delete all the users ")
            if for_safe.lower() == 'yes' or for_safe.lower() == 'ye':
                email_list.clear()
                save_email()
                print("all users deleted")
 
        elif 'change' in c.lower():
            email= input("what user do you want ")
            if email in email_list:
                remove_or_append = input("would you like to remove or append money? ")
                if 'append' in remove_or_append.lower() or 'add' in remove_or_append.lower():
                    amount = input ("append ")
                    with open (file_name , "w") as file:
                        saving += amount
                        json.dump(saving , file)
                        print(f"{email}")
     
                elif 'remove' in remove_or_append.lower():
                    amount = input ("remove ")
                    with open (file_name , "w") as file:
                        saving -= amount
                        json.dump(saving , file)
                    print(f"{email} ")





def append_or_remove_or_exit_or_delete():
    r = 0
    while r< 7:
        print("")
        choise = input ("would you like to remove or append money or exit or delete")
        print("")
        if 'append' in choise.lower():
            amount_append = float(input("how much "))
            add_money(amount_append)
        
        elif 'remove' in choise.lower():
            amount_remove = float(input("how much"))
            print("")
            remove_money(amount_remove)
        elif 'exit' in choise.lower():
            print(f"your saving is {saving} shekels")
            break

        elif 'delete' in choise.lower():
            the_email = input("enter your email")
            if the_email in email_list:
                email_list.remove(the_email)
                save_email()
                print("account deleted succesfully")
            else:
                print("email not found")
            break
        else :
            print("error")
            print("")
        print(f"your saving is {saving} shekels")


def chek_new_email(email):
    if '@gmail.com' not in email:
        print("something went wrong try again")
    else:
        create_email(email)

only_for_creator()

print("               --------------saving calculator-------------------              ")
h = input("you have a account or do you want to create one ")


if 'have' in h.lower():

    email = input("enter your email ")
    if email not in email_list:
        print("email was not found please try again or create a new acount ")
        attemps = 0
        max_attemps = 7
        succes = False
        while attemps < max_attemps:
            q = input ("would you like to create a new account or try again ")
            if 'create' in q.lower():
                new_account = input("enter your email ")
                chek_new_email(new_account)
                succes = True
                break
        
            elif 'try' in q.lower() or 'again' in q.lower():
                email = input("write your email")
                if email in email_list:
                    succes = True
                    break
                else :
                    attemps += 1
                    print(f"email was not found , {max_attemps - attemps} attemps left")
                

            elif 'exit' in q.lower():
                break
            
            else :
                print("error try again")

        if not succes and attemps > max_attemps:
            no_choise = input("to many failed attemps , create a new account or exit")
            if 'create' in no_choise.lower():
                new_account = input("enter your email ")
                chek_new_email(new_account)
    else:
        append_or_remove_or_exit_or_delete()

elif 'create' in h.lower():
    new_account = input("enter your  email ")
    chek_new_email(new_account)
else:
    print("error try again ")

