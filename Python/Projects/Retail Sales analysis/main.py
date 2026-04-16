class storage:
    def __init__(self,name,category,price,quantity):
        self.name=name
        self.category=category
        self.price=price
        self.quantity=quantity

class items_manager:
    def __init__(self):
        self.items=[]
    
    def additem(self):
        name = input("Enter the name of the item : ")
        category = input("Enter Item category : ")
        price = int(input("Enter the cost price of the item : "))
        quantity = int(input("Enter the quantity of item : "))
        temp = storage(name,category,price,quantity)
        self.items.append(temp)
        print(f"Item added successfully ! {name , category , price , quantity}")

    def updateitem(self):
        name = input("Enter the name of the item you want to update :")
        quan = int(input("Enter the new quantity : "))
        for items in self.items:
            if items.name == name :
                temp = items
        items.quantity = quan
        print(f"Item Updated successfully {items.name , items.quantity}")

    #This function is copied from CHATGPT to create borders so table looks easy to understand . Rest is original
    def list_items(self):
        if not self.items:
            print("No items found.\n")
            return
        headers = ["Name", "Category", "Price", "Quantity", "Total Sales"]
        data = [
            [item.name, item.category, item.price, item.quantity, item.quantity * item.price]
            for item in self.items
        ]
        widths = [len(h) for h in headers]
        for row in data:
            for i, val in enumerate(row):
                widths[i] = max(widths[i], len(str(val)))
        def line():
            print("+" + "+".join("-" * (w + 2) for w in widths) + "+")
        def row_print(row):
            print("| " + " | ".join(f"{str(val):<{widths[i]}}" for i, val in enumerate(row)) + " |")
        print("\n===== Items List =====")
        line()
        row_print(headers)
        line()
        for row in data:
            row_print(row)
        line()
        print()

def main():
    print("Welcome to the cafe inventory and sales tracker! \n\n What would you like to do?")
    manager = items_manager()
    while True:
        print("1. Add new item to menu\n2. Update Item quantity\n3. List Items\n4. Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            manager.additem()
            print()
        elif choice == 2:
            manager.updateitem()
            print()
        elif choice == 3:
            manager.list_items()
        elif choice == 4:
            print("Program Exited !!!")
            break
        else:
            print("Enter a valid choice")


if __name__=="__main__":
    main()
