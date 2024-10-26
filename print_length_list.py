cities=["banka","amarpur","bhagalpur","purniya"]
book=["Ramayana","Geeta","Mahabharat"]
def print_len(list):
    for item in list:
        print(item,end=" ")
    print("\nLength of the list ",len(list))

print_len(cities)
print_len(book)