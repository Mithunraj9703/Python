n=int(input("enter the last value of natural no."))
def sum(a):
    if(a==0):
        return 0
    print(a)
    return sum(a-1)+a

print("Total sum = ",sum(n))