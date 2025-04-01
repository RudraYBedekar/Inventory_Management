import pandas as pd

# Load your inventory CSV
df = pd.read_csv("robotics_inventory.csv")

# Get item_id input from user
item_id = input("Enter the item_id to search: ").strip().upper()

# Search for the item
item = df[df['item_id'] == item_id]

# Show short report
if not item.empty:
    print("\n Item Report:")
    print(item[['item_id', 'item_name', 'quantity_on_hand', 'quantity_fulfilled', 'last_picked', 'location', 'pick_time_seconds']].to_string(index=False))
else:
    print(" Item not found.")
