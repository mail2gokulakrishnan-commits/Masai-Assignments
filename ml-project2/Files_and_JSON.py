import json

# --- SETUP: Creating the initial file for you to work with ---
initial_data = [
    {"title": "The Alchemist", "author": "Paulo Coelho", "price": 12.99, "in_stock": True},
    {"title": "1984", "author": "George Orwell", "price": 9.99, "in_stock": True}
]

with open('inventory.json', 'w') as f:
    json.dump(initial_data, f)

# --- TASK 1: Read the inventory ---
# We use 'r' for "read" mode. The 'with' block ensures the file closes automatically.
with open('inventory.json', 'r') as file:
    inventory = json.load(file)

print(f"Total number of books: {len(inventory)}")
print("-" * 30)

# --- TASK 2: Update and save ---
new_book = {
    "title": "Atomic Habits", 
    "author": "James Clear", 
    "price": 14.99, 
    "in_stock": True
}

# Add the new dictionary to our list
inventory.append(new_book)

# Write back to the file. 'w' stands for "write" (this overwrites the old file).
# indent=4 makes the file human-readable instead of one long line.
with open('inventory.json', 'w') as file:
    json.dump(inventory, file, indent=4)

# --- TASK 3: Display the inventory ---
# Read it one last time to confirm the save worked
with open('inventory.json', 'r') as file:
    updated_inventory = json.load(file)

for book in updated_inventory:
    print(f"Title: {book['title']} | Author: {book['author']} | Price: ${book['price']}")
