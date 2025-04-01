import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed for reproducibility
np.random.seed(42)

# Number of records to generate
num_records = 3000

# Generate data fields
item_ids = [f"ITEM{str(i).zfill(4)}" for i in range(num_records)]
item_names = [f"Product_{i}" for i in range(num_records)]
quantities_on_hand = np.random.randint(10, 500, size=num_records)
quantities_fulfilled = np.random.randint(5, 300, size=num_records)
last_picked_dates = [datetime.today() - timedelta(days=random.randint(0, 30)) for _ in range(num_records)]
locations = [f"Zone-{random.choice(['A', 'B', 'C', 'D'])}{random.randint(1, 5)}" for _ in range(num_records)]
pick_times = np.random.normal(loc=8, scale=2, size=num_records).round(2)  

# Create DataFrame
df = pd.DataFrame({
    "item_id": item_ids,
    "item_name": item_names,
    "quantity_on_hand": quantities_on_hand,
    "quantity_fulfilled": quantities_fulfilled,
    "last_picked": last_picked_dates,
    "location": locations,
    "pick_time_seconds": pick_times
})

# Save to CSV
csv_path = "robotics_inventory.csv"
df.to_csv(csv_path, index=False)

print(f"CSV file saved as '{csv_path}' with {num_records} records.")
print("Sample data generated successfully.")