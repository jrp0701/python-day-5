bank_dict = {
    "Priya" : {"balance" : 100, "pin" : "4821"},
    "Carlos" : {"balance": 300, "pin" : "1092"},
    "Amira" : {"balance" : 0, "pin": "0000"},
    "Jordan" : {"balance" : 7788, "pin": "9999"}
}

'''
Name: print_welcome
Task: Prints the welcome message to the terminal
Input: None
Side Effects (printing/display): the welcome message
Return: None
'''
def print_welcome():
    print("Welcome to Berklee Bank!")

'''
Name: get_username
Task: Prompt the user for their name
Input: None
Side Effects (printing/display): Prompt "What is your name?"
Return: return the username
'''
def get_username():
    name = input("What is your name? ")
    return name

'''
Name: get_pin
Task: Prompt the user for their pin
Input: None
Side Effects (printing/display): Prompt "What is your pin"
Return: return the pin
'''
def get_pin():
    pin = input("What is your PIN? ")
    return pin

'''
Name: verify_identity
Task: Take the name and pin and see if there's a valid user in the system. If so, get their data. IF not, fail.
Input: username, pin
Side Effects (printing/display): If they don't exist, it says "Access Denied"
Return: True if user exists, False if not
'''
def verify_identity(username, pin):
    if bank_dict.get(username): 
        users_values = bank_dict.get(username)
        if pin == users_values.get("pin"):
            return True
    print("Access denied for ", username, "with pin ", pin)
    return False

'''
Name: get_menu_choice
Task: Print the functionality of the bank (the commands they can do) to the terminal, and ask what they want
Input: None
Side Effects (printing/display):  do you wanna deposit, withdraw, get balance, quit (they type their answer)
Return: the string the user typed in
'''
def get_menu_chioce():
    choice = input("Do you want to... deposit withdraw balance quit ")
    return choice
'''
Name: get_balance
Task:  gets the balance and prints it
Input: username
Side Effects (printing/display):  the balance
Return: None
'''
def get_balance(username):
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        
'''
Name: deposit_money
Task: Ask the user how much they want to deposit then add that to the balance
Input: username
Side Effects (printing/display): prompting the user for the amount to deposit
Return: None
'''
def deposit_money(username):
    deposit_amount = int(input("How much would you like to deposit"))
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        previous_bal = users_values.get("balance")
        new_bal = previous_bal + deposit_amount
        users_values.update({"balance": new_bal})
        print(new_bal)
    else:
        return None
'''
Name: withdraw_money
Task:  Ask the user how much they want to withdraw. If they have enough, reduce balance. If not, tell them.
Input: username
Side Effects (printing/display): Asking the user the amount, telling them if successful
Return: None
'''
def withdraw_money(username):
    withdraw_amount = int(input("How much would you like to withdraw? "))
    if bank_dict.get(username):
        users_values = bank_dict.get(username)
        previous_bal = users_values.get("balance")
        new_bal = previous_bal - withdraw_amount
        if new_bal < 0: 
            print("insufficient funds")
        else:
            users_values.update({"balance": new_bal})


def run_tests():
    deposit_money("Priya")





def main():
    print_welcome()
    name = get_username()
    pin = get_pin()
    valid = verify_identity(name,pin)
    if not valid:
        return None

    while True:
        users_choice = get_menu_chioce()
        if users_choice == "balance":
            get_balance(name)
        elif users_choice == "withdraw":
            withdraw_money(name)
        elif users_choice == "deposit":
            deposit_money(name)
        elif users_choice == "quit":
            break
        else:
            print("You can't choose that.")

main()