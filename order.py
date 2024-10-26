class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price

    def __gt__(self,ord2):
        return self.price>ord2.price

ord1=Order("chips",20)
ord2=Order("Popcorn",50)
if(ord1>ord2):
    print("Price of order 1 is greater")
else:
    print("Price of order 2 is greater")