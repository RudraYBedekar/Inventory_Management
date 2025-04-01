import pandas as pd

# Load CSV
df = pd.read_csv("robotics_inventory.csv")

# Calculate KPIs
df['turnover_rate'] = df['quantity_fulfilled'] / (df['quantity_on_hand'] + 1)
df['fulfillment_rate'] = df['quantity_fulfilled'] / df['quantity_fulfilled'].sum()

# Save updated inventory with KPIs
df.to_csv("processed_inventory_with_kpis.csv", index=False)

# Identify slow zones
location_pick_stats = df.groupby("location")["pick_time_seconds"].mean().reset_index()
location_pick_stats.columns = ["location", "avg_pick_time"]

# Save all location stats
location_pick_stats.to_csv("location_pick_stats.csv", index=False)

# Save only slow zones
slow_zones = location_pick_stats[location_pick_stats["avg_pick_time"] > location_pick_stats["avg_pick_time"].mean()]
slow_zones.to_csv("slow_zones.csv", index=False)

print("Files saved: processed_inventory_with_kpis.csv, location_pick_stats.csv, slow_zones.csv")
