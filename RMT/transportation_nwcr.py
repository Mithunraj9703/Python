# supply=[20,30,50]
supply_string = input("Enter supply values separated by commas: ")
supply = [int(item.strip()) for item in supply_string.split(',')]

# demand=[30,40,30]
demand_string = input("Enter demand values separated by commas: ")
demand = [int(item.strip()) for item in demand_string.split(',')]
# cost=[[8,6,10],[9,12,3],[4,9,16]]
cost=[]
num_rows = int(input("Enter the number of rows: "))
for i in range(num_rows):
        print(f"Enter row {i + 1} values (space-separated):")
        const = list(map(float, input().split()))
        cost.append(const)
rows=len(supply)
cols=len(demand)

#initialize allocation matrix with zero
allocation=[[0 for _ in range(cols)] for _ in range(rows)]
i=0 # for supply
j=0 # for demand

#NWCR algo
while i<rows and j<cols:
    allocation_amount=min(supply[i],demand[j])
    allocation[i][j]=allocation_amount
    supply[i]-=allocation_amount
    demand[j]-=allocation_amount

    #move to the next rows or cols
    if supply[i]==0:
        i+=1
    if demand[j]==0:
        j+=1

#output the allocation matrix
print("Allocation Matrix")
for row in allocation:
    print(row)

#calculate the transportation cost
total_cost=0
for i in range(rows):
    for j in range(cols):
        total_cost+=allocation[i][j]*cost[i][j]

#output the total cost
print("Total transportation cost is ",total_cost)
