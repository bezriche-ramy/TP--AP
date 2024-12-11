nbr_ppl=int(input("Ask the user how many people need a ride ? : "))
ppl_taxi=int(input("Ask the user how many people can fit in a taxi ? : "))

nbr_taxi=nbr_ppl//ppl_taxi

if nbr_ppl%ppl_taxi!=0:
    nbr_taxi+=1

print("The number of taxi needed is : ",nbr_taxi)