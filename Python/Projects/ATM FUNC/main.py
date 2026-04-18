
pin='1234'
balance=50000
number=1122334455

print('Welcome to XYZ atm')
print('''1. Show account balance.
2. Cash withdrawal
3. Cash deposit
4. Pin Change''')

while True:
    ch=int(input('enter your choice:'))
    if ch == 1:
        pinnn =  input("Enter pin : ")
        if pinnn == pin:
            if balance == 0:
                print("You are out of balance !")
            else:
                print(f"You account balance is {balance}")
        else:
            print("Incorrect Pin !")
    elif ch == 2:
        pinn = input("Enter pin : ")
        if pinn == pin:
            print(f"You account balance is {balance}")
            amt = int(input("Enter the amount to withdraw :"))
            if balance <= 0 or amt > balance :
                print("Not enough amount !")
            else:
                balance-=amt
                print(f"Cash withdrawl successful , remaining balance is {balance}")
        else:
            print("Incorrect Pin !")
    elif ch == 3:
        amtt = int(input("Enter amount to deposit :"))
        balance+=amtt
        print(f"Balance updated , Available balance : {balance}")
    elif ch == 4:
        while True:
            old = str(input("Enter old pin :"))
            if old == pin:
                new = input("Enter new pin :")
                pin = new
                print("Pin updated !")
                break
            else:
                print("Incorrect Pin !Try Again !")


