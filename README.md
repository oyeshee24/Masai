# Masai
#A banking application having the basic function including:
1.Creating an account
2.Logging in to the account
3.Performing different Transactions
4.Exit

#Starting to explain in detail we can say,i have imported different libraries,to make it safer for the user.Keeping in mind of the user's safety i have imported 'hashlib' library to obfuscate passwords.

Next I have used tkiner library mainly to enhance the security. by replacing the password entry with asterisks '*'.For both while creating passwords as well during log-in.

#Next i have used the os module ,mainly to prevent the same text file to created again,in process loosing previous data,as the previous data gets erased,when file is opened in write mode.

#After taking required inputs from the user such as(Account No.,Name,Intial Deposit and Password),it is stored in th file.

#Next in log-in function we verify if the acc no. provided by the user matches any account no. from our records and then we check the password matches the stored password.

#I have raised custom exceptions to hold in case the user enters a wrong password,or the user enters an account no. that doesnt exist in our records

#The 3rd choice is performing tranactions ,that includes 
1.Deposit
2.Withdrawal
First we ask the user for type of transaction he wants to conduct,on the basis of that we ask for the amount,and then the transaction is done. And the final balance is shown to the user and new balance is updated in the "accounts.txt" file ,as well the transaction record is recorded in the "transactions.txt".

#In case of withdrawal,if the user enters a value more than the balance, an error exception is generated ,informing the user that there is insufficient balance.

#At last i have taken a while loop for it to run till the user wants it too by a simple question,which is intialized as yes at first.Inside the loop the console menu is shown to the user.Where as the user enters his certain choice,that particular method is called.
As the user enter "Nn" the loop exits and ends with a thankyou note. 
