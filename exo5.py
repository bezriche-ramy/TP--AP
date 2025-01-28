print("Runner1: ")
name1=str(input("Name1: "))
time1=int(input("Time (in seconds): "))

print("Runner2: ")
name2=str(input("Name2: "))
time2=int(input("Time (in seconds): "))

if time2<time1:
    print("The faster runner is ",name2)
elif time2>time1:
    print("The faster runner is ",name1)
else:
    print(name1," and ",name2," have the same time !")
