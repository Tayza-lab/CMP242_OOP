# try:
#     mona = int(input("number: "))
#     mon = int(input("denominator: "))
#     print(mona/mon)
#
# except Exception:
#     print("Error")

def withdraw(balances, amounts):
    if amounts > balances:
        raise ValueError("Insufficient Balance")
    else:
        balances -= amounts
        print("Withdraw successful, Remaining balance:", balances)
    return balances

try:
    amounts = float(input("Enter the amount to withdraw: "))
    withdraw(1000, amounts)
except ValueError as e:
    if "could not convert string to float" in str(e):
        print("Transaction Error: Please enter a valid amount")
    else:
        print("Transaction Error:", e)

# try:
#     balance = 1000
#     print("Your current balance is: ", balance)
#
#     amount = float(input("Enter the amount to withdraw: "))
#     balance = withdraw(balance, amount)
#
# except ValueError as e:
#     print("Transaction Error:", e)