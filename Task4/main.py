#imports libraries
import os
import random
from builtins import open, str, print, int, input


def operation():
    print('1. To create new bank account')
    print('2. To check account details ')
    print('3. To log out')
    request = int(input('Enter your choice: '))
    return request


def get_account_details():
    detail = []
    AccountName = input("Enter customers account name: ")
    detail.append(AccountName)
    Opening_Bal = int(input("What's the opening balance: "))
    detail.append(Opening_Bal)
    Account_Type = input("Enter the account type: ")
    detail.append(Account_Type)
    Account_email = input("Enter account email: ")
    detail.append(Account_email)

    return detail


def get_account_no():
    file = open("customer.txt", "r")
    accountDetails = file.readline()
    accountNumber = file.readline()
    file.close()
    return accountNumber


def get_account_info():
    file = open("customer.txt", "r")
    accountDetails = file.readline()
    accountNumber = file.readline()
    file.close()
    return accountDetails


def staff_login():
    print("Welcome, please make a choice: ")
    print("1:Staff Login")
    print("2:Close App")
    choice = int(input())
    return choice


def session_file():
    file_handler = open('session.txt', 'w+')
    file_handler.write(username)
    file_handler.write(password)
    file_handler.close()

#main program
status = True
while status:
    choice = staff_login()




    if choice == 1:
        print("Please log in")
        username = str(input('Enter your username: '))
        password = input('Enter your password: ')
        session_file()

        with open('staff.txt', 'r') as f:
            for line in f:
                info = line.split(",")
                username1 = str(info[0])
                password1 = str(info[1])
                username2 = str(info[4])
                password2 = str(info[5])

            if username == username1 and password == password1:
                get_request = operation()
                if get_request == 1:
                    x = get_account_details()
                    account_number = random.randint(1000000000, 9999999999)
                    print(account_number)
                    details = open('customer.txt', 'w')
                    details.write('%s\n' % x)
                    details.write('%d\n' % account_number)
                    details.close()

                get_request = operation()
                if get_request == 2:
                    accountNumber = get_account_no()
                    account_number = int(input('Enter account number: '))
                    if account_number == int(accountNumber):
                        account_info = get_account_info()
                        print(account_info)

                get_request = operation()
                if get_request == 3:
                    file = open('session.txt', 'r+')
                    file.truncate(0)
                    file.close()



                status = True

            elif username == username2 and password == password2:
                get_request = operation()
                if get_request == 1:
                    x = get_account_details()
                    account_number = random.randint(1000000000, 9999999999)
                    print(account_number)
                    details = open('customer.txt', 'w')
                    details.write('%s\n' % x)
                    details.write('%d\n' % account_number)
                    details.close()

                get_request = operation()
                if get_request == 2:
                    accountNumber = get_account_no()
                    account_number = int(input('Enter account number: '))
                    if account_number == int(accountNumber):
                        account_info = get_account_info()
                        print(account_info)

                get_request = operation()
                if get_request == 3:
                    file = open('session.txt', 'r+')
                    file.truncate(0)
                    file.close()



                status = True

            else:
                print('Your username or password is incorrect, pls try again. ')



    else:
        break
        status = False
