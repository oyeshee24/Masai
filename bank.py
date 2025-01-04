import hashlib
from datetime import date
import os # Check if files exist before writing headers 
import tkinter as tk 
from tkinter import simpledialog

if not os.path.exists("accounts.txt"):
    f=open("accounts.txt",'w')
    f.write("Account Number,Name,Password,Balance\n")
    #f.write([123456,"John Doe","password123","1500"])
    f.close()

if not os.path.exists("transactions.txt"):
    f1=open("transactions.txt",'w')
    f1.write("Account Number, Transaction Type (Deposit/Withdrawal), Amount, Date\n")
    #f1.write("123456","Deposit",500,"2024-12-23"])
    f1.close()

def hash_password(password): 
    return hashlib.sha256(password.encode()).hexdigest()

def get_password(prompt): 
    root = tk.Tk() 
    root.withdraw() 
    # Hide the main window 
    password = simpledialog.askstring("Password", prompt, show='*') 
    root.destroy() 
    return password

def is_account_number_taken(acc_no): 
    with open("accounts.txt", 'r') as f: 
        lines = f.readlines()[1:] # Skip the header line 
        for line in lines: 
            existing_acc_no = line.strip().split(",")[0] 
            if int(existing_acc_no) == acc_no: 
                return True 
    return False

def creating_acc():
    f=open("accounts.txt",'a')
    
    nam=input("Enter your name:")
    initial_deposit=int(input("Enter your initial deposit:"))
    while True: 
        acc_no = int(input("Your account number: ")) 
        if is_account_number_taken(acc_no): 
            print("Account number already exists. Please enter a different account number.") 
        else: 
            break
    
    
    passw=get_password("Enter a password")
    hashed_pass = hash_password(passw)
    print("Account created successfully!")
    f.write(f"{acc_no},{nam},{hashed_pass},{initial_deposit}\n")
    #print(c)
    f.close()

    #with open("accounts.txt", 'r') as f: 
        #print("Contents of accounts.txt after creating account:") 
        #print(f.read()) # Debug print to check the file contents


ctr=0
take_acc_no = None # Declare global variable

class Invalid_passwd(Exception):
    pass

class Incorrect_cred(Exception):
    pass

class Insuff_bal(Exception):
    pass

def log_in():
    global take_acc_no
    f2=open("accounts.txt",'r')

    take_acc_no=int(input("Enter your account number:"))
    take_passwd=get_password("Enter your password:")
    hashed_take_passwd = hash_password(take_passwd)
    c1=f2.readlines()[1:]
    #print(c1)
    ctr=0
    for k in c1:
        t=k.strip().split(",")
        #print(f"Checking account: {t[0]} with password: {t[2]}") # Debug print
        if int(t[0])==take_acc_no:
            
            if t[2]==hashed_take_passwd:
                print("Login succesfull!")
                ctr=1
                return take_acc_no
            else:
                raise Invalid_passwd("Invalid password")
    if ctr==0:
        print("Account number not found.") # Debug print
        raise Incorrect_cred("Incorrect credentials")
    f2.close()

amt=0
def performing_transactions():
    global take_acc_no
    f3=open("transactions.txt",'a')
    f4=open("accounts.txt",'r+')
    
    c4=f4.readlines()
    
    print("1.Deposit\n2.Withdrawal")
    choice=int(input("Enter your desired choice in nos.\t"))
    
    if choice==1:
        dep=int(input("Enter amount to deposit:\t"))
        
        #f3.write(f"{take_acc_no},Deposit,{dep},{date.today()}\n")
        
        for idx, k in enumerate(c4[1:], start=1):
            t1=k.strip().split(",")
            f3.write(f"{t1[0]},Deposit,{dep},{date.today()}\n")
            if int(t1[0])==take_acc_no:
                amt=int(t1[3])+dep 
                print(f"Deposit successful! Current balance:{amt}")
                c4[idx] = f"{t1[0]},{t1[1]},{t1[2]},{amt}\n"
                break
    
    elif choice==2:
        withd=int(input("Enter amount to withdraw\t"))

        


        for idx,k in enumerate(c4[1:], start=1):
            t2 = k.strip().split(",") 
            f3.write(f"{t2[0]},Withdrawal,{withd},{date.today()}\n")
            if int(t2[0]) == take_acc_no: 
                if int(t2[3]) < withd:
                    raise Insuff_bal("Insufficient Balance") 
                else: 
                    amt = int(t2[3]) - withd
                    print(f"Withdrawal successful! Current balance:{amt}")
                    c4[idx] = f"{t2[0]},{t2[1]},{t2[2]},{amt}\n"
                    break 
    else:
        raise ValueError("Invalid input ")

    f4.seek(0) 
    f4.writelines(c4)
    
    amt=0
    f3.close()
    f4.close()

def Log_out():
    global take_acc_no 
    take_acc_no = None # Clear the logged-in account number
    print("Logged out of the account successfully\nExit\n")
    

ans='y'   
while ans in "yY":
    print("Welcome to the Mahalaxshmi Banking System!\n1. Create Account\n2. Login\n3.Performing transactions\n4.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        creating_acc()
    elif ch==2:
        log_in()
    elif ch==3:
        if take_acc_no is not None: 
            print("Proceeding to transactions") 
            performing_transactions() 
        else: 
            print("Please log in first.")
        
        '''acc_no=log_in()
        print(acc_no)'''
        
    elif ch==4:
        Log_out()
    else:
        raise ValueError("Invalid choice")
    ans=input("enter [y/n] if you want to make another choice")

if ans in "Nn":
    print("\tThankyou for using Mahalaxshmi Bank\n\tVisit us again")