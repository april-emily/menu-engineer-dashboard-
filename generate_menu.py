import pandas as pd
import random

# Define categories and items
menu_structure = {
    "Coffee": ["Latte", "Cappuccino", "Flat White", "Long Black", "Espresso", "Mocha", "Iced Latte"],
    "Breakfast": ["Smashed Avo", "Big Brekky", "Eggs Benedict", "Bacon & Egg Roll", "Pancakes", "Acai Bowl", "Toastie"],
    "Lunch": ["Chicken Burger", "Beef Burger", "Caesar Salad", "Fish & Chips", "BLT", "Steak Sandwich", "Veggie Wrap"]
}

data = []

for category, items in menu_structure.items():
    for item in items:
        # Simulate realistic pricing based on category
        if category == "Coffee":
            sales_price = round(random.uniform(4.5, 6.5), 2)
            cost_price = round(sales_price * random.uniform(0.15, 0.25), 2) # High margin on coffee
            sold = random.randint(50, 500)
        elif category == "Breakfast":
            sales_price = round(random.uniform(18.0, 26.0), 2)
            cost_price = round(sales_price * random.uniform(0.25, 0.35), 2)
            sold = random.randint(20, 150)
        else: # Lunch
            sales_price = round(random.uniform(20.0, 30.0), 2)
            cost_price = round(sales_price * random.uniform(0.28, 0.38), 2)
            sold = random.randint(20, 120)
            
        data.append([item, category, sales_price, cost_price, sold])

# Create DataFrame
df = pd.DataFrame(data, columns=["Item", "Category", "Sales_Price", "Cost_Price", "Number_Sold"])

# Save to CSV
df.to_csv("menu_data.csv", index=False)

print("✅ 'menu_data.csv' has been generated successfully!")
