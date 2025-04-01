import pandas as pd
import mysql.connector

# Load the CSV
df = pd.read_csv("robotics_inventory.csv")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Rudra@2001",
    database="Inventory"
)
cursor = conn.cursor()

# Insert each row from DataFrame into the MySQL table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO warehouse_inventory (
            item_id, item_name, quantity_on_hand, quantity_fulfilled,
            last_picked, location, pick_time_seconds
        ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        row['item_id'],
        row['item_name'],
        int(row['quantity_on_hand']),
        int(row['quantity_fulfilled']),
        str(row['last_picked']).split()[0],
        row['location'],
        float(row['pick_time_seconds'])
    ))

conn.commit()
cursor.close()
conn.close()
print("✅ CSV data inserted into MySQL.")
