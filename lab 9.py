import csv
from typing import Dict

def load_inventory(filename: str) -> Dict[str, Dict[str, str]]:
    inventory = {}
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            key = f"{row[0]}_{row[1]}_{row[2]}"
            inventory[key] = {'Make': row[0], 'Model': row[1], 'Year': int(row[2]), 'Price': float(row[3])}
    return inventory

def display_inventory(inventory: Dict[str, Dict[str, str]]):
    for key, value in inventory.items():
        print(f"{key}: {value}")

def update_price(inventory: Dict[str, Dict[str, str]], make: str, model: str, year: int, new_price: float) -> str:
    key = f"{make}_{model}_{year}"
    if key in inventory:
        inventory[key]['Price'] = new_price
        return "Price updated successfully!"
    else:
        return "Vehicle Not Found in inventory!"

def sort_by_make(inventory: Dict[str, Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    return dict(sorted(inventory.items(), key=lambda x: x[1]['Make']))

def calculate_price_change(inventory: Dict[str, Dict[str, str]], model: str) -> str:
    vehicles = [vehicle for vehicle in inventory.values() if vehicle['Model'] == model]
    if len(vehicles) < 2:
        return "Not Enough Data to Calculate Price Change!!"
    else:
        vehicle_2022 = vehicles[0]
        vehicle_2024 = vehicles[1]
        price_change = ((vehicle_2024['Price'] - vehicle_2022['Price']) / vehicle_2022['Price']) * 100
        return f"Price change for {model} over two years: {price_change:.2f}%"

def update_file(filename: str, inventory: Dict[str, Dict[str, str]]):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Make', 'Model', 'Year', 'Price'])
        for vehicle in inventory.values():
            writer.writerow([vehicle['Make'], vehicle['Model'], vehicle['Year'], vehicle['Price']])

def menu():
    filename = "vehicle_inventory.csv"
    inventory = load_inventory(filename)

    while True:
        print("\nMenu:")
        print("1. Display Inventory")
        print("2. Update Vehicle Price")
        print("3. Sort Inventory by Make")
        print("4. Calculate Price Change")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            display_inventory(inventory)
        elif choice == '2':
            make = input("Enter make: ")
            model = input("Enter model: ")
            year = int(input("Enter year: "))
            new_price = float(input("Enter new price: "))
            print(update_price(inventory, make, model, year, new_price))
        elif choice == '3':
            sorted_inventory = sort_by_make(inventory)
            display_inventory(sorted_inventory)
        elif choice == '4':
            model = input("Enter model: ")
            print(calculate_price_change(inventory, model))
        elif choice == '5':
            update_file(filename, inventory)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()