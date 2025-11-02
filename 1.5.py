"""
. Add items (name, price, quantity)
. Remove items
. Update quantity
. Calculate total price
. Apply discount code (10% off if total > $100)
. Display cart summary
"""
cart ={}

def additem(name, price, quantity):
    if name in cart:
        cart[name]+=quantity
    else:
            
        item={
            "price":price,
            "quantity":quantity,
            "total" :price*quantity
        }
        cart[name]=item
def deleteitem(idnamee):
    
    cart.pop(idnamee)
    return cart
def updateq(id , qu):
    for i in id :
        cart[i]['quantity']=qu
        cart[i]['total']=qu * cart[i]['price']
        return True
    return False

def calc():
    tot=0
    for key , i in cart.items():

        tot+=i['quantity']* i['price']

    if tot >100 :
        return tot* .9
    return tot

def show():
    print("{:20s} {:>8s} {:>8s} {:>12s}".format("Item", "Price", "Qty", "Total"))
    print("-" * 52)
    for name, item in cart.items():
        total = item['price'] * item['quantity']
        print("{:20s} {:8.2f} {:8d} {:12.2f}".format(name, item['price'], item['quantity'], total))
    print("-" * 52)
    subtotal=0
    for item in cart.values():
        subtotal += item['price'] * item['quantity']
    print("{:38s} {:12.2f}".format("dicounted:", subtotal- calc()))
    print("{:38s} {:12.2f}".format("Subtotal:", calc()))

    # 
additem("apple", 21, 2)
additem("glass", 29, 1)
additem("banana", 13, 3)
print(cart)
deleteitem("banana")
print(cart)
additem("laptop", 90, 1)

print (calc())
show()