class VendingMachine:
    def __init__(self):
        # Initialise the Vending Machine with classified items
        self.items = {
            "Drinks": {
                "1": {"name": "🥤 Coke", "price": 1.50, "category": "Drinks", "stock": 10},
                "2": {"name": "🥤 Pepsi", "price": 1.30, "category": "Drinks", "stock": 8},
            },
            "Snacks": {
                "3": {"name": "🍟 Chips", "price": 1.00, "category": "Snacks", "stock": 5},
                "4": {"name": "🍫 Chocolate", "price": 1.20, "category": "Snacks", "stock": 6},
            },
            "Hot Drinks": {
                "5": {"name": "☕ Coffee", "price": 2.00, "category": "Hot Drinks", "stock": 3},
                "6": {"name": "🍵 Tea", "price": 1.80, "category": "Hot Drinks", "stock": 4},
            }
        }
        self.transactions = []  # Log of all transactions

    def display_menu(self):
        # prints out the codes of the menu item, name, prices, and stock.
        print("\n=== 🛒 Vending Machine Menu ===")
        for category, items in self.items.items():
            print(f"\n📂 {category}:")
            for code, item in items.items():
                print(f" {code}. {item['name']} - 💰 ${item['price']:.2f} (📦 Stock: {item['stock']})")
        print("\nEnter '0' to exit.")

    def select_item(self):
        # Allow user to select item by code and quantity
        while True:
            choice = input("\nEnter the item code: ")
            if choice == "0":
                return None  # Exit the machine
            for category in self.items.values():
                if choice in category:
                    item = category[choice]
                    if item["stock"] > 0:
                        quantity = input(f"How many {item['name']} would you like to buy? (Stock available: {item['stock']}): ")
                        try:
                            quantity = int(quantity)
                            if quantity <= item["stock"]:
                                return choice, item, quantity  # Return item and quantity
                            else:
                                print(f"❌ Sorry, we don't have that many in stock. Max available: {item['stock']}.")
                        except ValueError:
                            print("⚠️ Invalid input. Please enter a valid quantity.")
                    else:
                        print("❌ Sorry, this item is out of stock.")
                        return None
            print("⚠️ Invalid selection. Please try again.")

    def process_payment(self, item, quantity):
        # Process the payment-making sure the user inserted enough money, pays the exact change
        total_price = item["price"] * quantity
        while True:
            try:
                money = float(input(f"💵 Insert money for {quantity}x {item['name']} (${total_price:.2f}): $"))
                if money < total_price:
                    print("❌ Insufficient money. Please insert more.")
                else:
                    change = round(money - total_price, 2)
                    item["stock"] -= quantity  # Deduct stock after purchase
                    print(f"\n🚚 Dispensing {quantity}x {item['name']}...")
                    if change > 0:
                        print(f"💰 Returning change: ${change:.2f}")
                    return money, change
            except ValueError:
                print("⚠️ Invalid input. Please enter a valid amount.")

    def suggest_purchase(self, item_name):
        # Suggest complementary purchases based on user's selection
        suggestions = {
            "🥤 Coke": "🍟 Chips",
            "🥤 Pepsi": "🍟 Chips",
            "🍟 Chips": "🥤 Soda",
            "🍫 Chocolate": "☕ Coffee",
            "☕ Coffee": "🍪 Biscuits",
            "🍵 Tea": "🍪 Cookies",
        }
        if item_name in suggestions:
            print(f"\n💡 How about adding {suggestions[item_name]} to complement your {item_name}?")

    def buy_additional_item(self):
        # Allow user to purchase more items
        while True:
            additional = input("\n🔄 Would you like to buy another item? (y/n): ")
            if additional.lower() == 'y':
                return True
            elif additional.lower() == 'n':
                return False
            else:
                print("⚠️ Invalid input. Please enter 'y' or 'n'.")

    def display_payment(self, selected_items):
        total_price = sum(item['price'] * item['quantity'] for item in selected_items)  # Calculate total price
        print("\n--------------- Payment Details ---------------")
        for item in selected_items:  # Loop through the list of selected items
            print(f"{item['name']} - {item['quantity']}x - Price: ${item['price'] * item['quantity']}")
        print(f"Total Price: ${total_price}")
        money_inserted = float(input("\n- Enter the amount of money: "))  # Get the amount of money entered

        if money_inserted >= total_price:
            change = round(money_inserted - total_price, 2)
            print(f"~ Your change will be: ${change} ~")
            generateReceipt(selected_items, money_inserted, change)  # Generate receipt after payment
        else:
            print("\n--------------- Error ---------------\nInsufficient funds. Please try again.")
            self.display_payment(selected_items)  # Restart the function if insufficient funds

    def run(self):
        # Main loop of the program for handling users' interactions with the machine.
        print("Welcome to the 🥤 Vending Machine!")
        selected_items = []
        while True:
            self.display_menu()
            selected = self.select_item()
            if not selected:  # Exit if no item selected
                break
            code, item, quantity = selected
            selected_items.append({
                "name": item["name"],
                "price": item["price"],
                "quantity": quantity
            })
            paid, change = self.process_payment(item, quantity)
            self.transactions.append({"item": item["name"], "quantity": quantity, "paid": paid, "change": change})
            self.suggest_purchase(item["name"])

            # Ask if the user wants to buy more items
            if not self.buy_additional_item():
                break

        # Display payment details and transaction summary
        if selected_items:
            self.display_payment(selected_items)
        print("\nThank you for using the 🥤 Vending Machine. Here's your purchase summary:")
        for t in self.transactions:
            print(f" - ✅ {t['quantity']}x {t['item']} purchased for 💰 ${t['paid']:.2f}. Change returned: 💰 ${t['change']:.2f}")


# Function to show user payment outside the VendingMachine class
def generateReceipt(selectedItems, moneyInserted, change):
    print("\n--------------- Receipt ---------------")
    for item in selectedItems:  # Loops through the items within the list and prints their details
        print(f"{item['name']} - {item['quantity']}x - Price: ${item['price'] * item['quantity']}")
    print(f"Total Price: ${sum(item['price'] * item['quantity'] for item in selectedItems)}")
    print(f"Cash: ${moneyInserted}")
    print(f"Change: ${change}")
    print("\n~ Thank you for your purchase! ~")


# Run the vending_machine program if this script is run directly  
if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()
