name=str(input("please enter your name ? : "))
cost=15.5

if name=="VIP":
    print("Enjoy the show for free!")
else:
    nbr_tickets=int(input("How many tickets do you want ? : "))
    print("The total cost is : ",nbr_tickets*cost)
