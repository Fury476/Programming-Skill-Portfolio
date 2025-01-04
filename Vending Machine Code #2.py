# 🥤 Vending Machine Program 🥪

def display_menu():
    menu = {
        "A1": ("🥤 Coke", 1.50, 10),
        "A2": ("🥤 Pepsi", 1.50, 8),
        "B1": ("🍟 Chips", 1.00, 5),
        "B2": ("🍫 Chocolate", 1.20, 7)
    }
    print("\n🤖 Welcome to the Vending Machine 🤖")
    print("📋 Code   🧾 Item       💰 Price    📦 Stock")
    for code, (item, price, stock) in menu.items():
        print(f"{code}    {item}    £{price:.2f}    {stock} left")
    return menu

def select_item(menu):
    while True:
        code = input("\n🔢 Enter the item code: ").upper()
        if code in menu:
            item, price, stock = menu[code]
            if stock > 0:
                return code, item, price
            else:
                print("🚫 Sorry, that item is out of stock.")
        else:
            print("❌ Invalid code. Please try again.")

def process_payment(price):
    while True:
        try:
            amount = float(input("💵 Enter payment amount: £"))
            if amount >= price:
                change = amount - price
                return change
            else:
                print("🚫 Insufficient funds. Please try again.")
        except ValueError:
            print("❌ Invalid input. Please enter a valid amount.")

def dispense_item(menu, code, change):
    item, price, stock = menu[code]
    menu[code] = (item, price, stock - 1)
    print(f"\n✅ Dispensing {item}...")
    if change > 0:
        print(f"💰 Change returned: £{change:.2f}")
    print("🙏 Thank you for your purchase!")

def main():
    menu = display_menu()
    while True:
        code, item, price = select_item(menu)
        change = process_payment(price)
        dispense_item(menu, code, change)
        another = input("\n🛒 Would you like to buy another item? (yes/no): ").lower()
        if another != "yes":
            print("👋 Thank you for using the Vending Machine! Goodbye!")
            break

if __name__ == "__main__":
    main()
