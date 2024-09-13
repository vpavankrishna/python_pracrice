# Supermarket Bill Generator

class SupermarketBill:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        """Add an item to the bill."""
        total_price = quantity * price
        self.items.append({
            'name': name,
            'quantity': quantity,
            'price': price,
            'total': total_price
        })

    def generate_bill(self):
        """Generate and print the final bill."""
        if not self.items:
            print("No items added to the bill.")
            return

        print("\n===== Supermarket Bill =====")
        total_amount = 0
        for item in self.items:
            print(f"{item['name']} (x{item['quantity']}): Rs.{item['price']} each, Total: Rs.{item['total']:.2f}")
            total_amount += item['total']

        print("\n============================")
        print(f"Total Amount: Rs.{total_amount:.2f}")
        print("============================")

# Main function
def main():
    bill = SupermarketBill()

    while True:
        name = input("Enter the item name (or type 'done' to finish): ")
        if name.lower() == 'done':
            break

        try:
            quantity = int(input(f"Enter the quantity for {name}: "))
            price = float(input(f"Enter the price for one {name}: Rs."))
        except ValueError:
            print("Invalid input! Please enter numbers for quantity and price.")
            continue

        bill.add_item(name, quantity, price)

    bill.generate_bill()

if __name__ == "__main__":
    main()