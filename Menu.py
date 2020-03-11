from Queues import Queues as Q
instance_amount = Q()
instance_price = Q()
profit = 0
inventory = 0
while True:
    print("""Welcome! Choose below to proceed!
    MENU:
    1. Add to the inventory.
    2. Sell items in inventory.
    3. Check profit to date.
    4. Display inventory.
    5. Enter 5 to exit.""")
    select = int(input("\n>>>"))
    if select == 1:
        amount = int(input("Please specify how many:\n>>>"))
        instance_amount.enqueue(int(amount))
        inventory += amount
        price = int(input("Please specify hom much it cost:\n>>>"))
        instance_price.enqueue(int(price))
    if select == 2:
        amount_to_sell = int(input("Specify how many will be deleted:\n>>>"))
        if amount_to_sell > inventory:
            print("You specified too large amount.")
            break
        else:
            inventory -= amount_to_sell
            last_price = None
            x = instance_amount.display()[0]

            if x < amount_to_sell:
                storage = 0
                while storage != amount_to_sell and storage < amount_to_sell:
                    selling_item = instance_amount.dequeue()
                    storage += selling_item
                    last_price = instance_price.dequeue()
                if storage > amount_to_sell:
                    difference = storage - amount_to_sell
                    instance_amount.enqueue(difference)
                    instance_price.enqueue(last_price)
                    profit += (last_price * 0.1) * amount_to_sell

            if amount_to_sell < x and amount_to_sell > 0:
                selling_item = instance_amount.dequeue()
                last_price = instance_price.dequeue()
                difference = selling_item - amount_to_sell
                instance_amount.enqueue(difference)
                instance_price.enqueue(last_price)
                profit += (last_price * 0.1) * amount_to_sell

            if x == amount_to_sell:
                selling_item = instance_amount.dequeue()
                last_price = instance_price.dequeue()
                profit += (last_price * 0.1) * selling_item

    if select == 3:
        print("So far you have made:")
        print(profit)
    if select == 4:
        print(instance_amount.display())
    if select == 5:
        break
