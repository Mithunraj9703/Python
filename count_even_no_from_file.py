with open("number.txt","r") as f:
    data=f.read()
print(data)
num=data.split(",")
count=0
for val in num:
    if(int(val)%2==0):
        count+=1

print("Total even no ",count)
