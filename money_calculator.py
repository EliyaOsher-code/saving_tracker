import os
import json
file_name = "balance.json"
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
    


r = 0
while r< 7:
    print("")
    choise = input ("would you like to remove or append money ")
    print("")
    if 'append' in choise:
        amount_append = float(input("how much "))
        add_money(amount_append)
        
    elif 'remove' in choise:
        amount_remove = float(input("how much"))
        print("")
        remove_money(amount_remove)
        
    else :
        print("error")
        print("")
    print(f"your saving is {saving} shekels")