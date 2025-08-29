import sqlite3
from datetime import datetime
from tabulate import tabulate   # For pretty tables

# ---------------- DATABASE CONNECTION ---------------- #
db = sqlite3.connect("restaurant.db")
cursor = db.cursor()

# ---------------- CREATE TABLES ---------------- #
cursor.execute('''
CREATE TABLE IF NOT EXISTS Menu (
    ItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Price REAL NOT NULL,
    Category TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Customer (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Phone TEXT,
    Email TEXT
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    CustomerID INTEGER,
    ItemID INTEGER,
    Quantity INTEGER,
    OrderDate TEXT,
    FOREIGN KEY (CustomerID) REFERENCES Customer(CustomerID),
    FOREIGN KEY (ItemID) REFERENCES Menu(ItemID)
)
''')

db.commit()

# ---------------- FUNCTIONS ---------------- #

# Add Menu Item
def add_menu_item():
    name = input("Enter Item Name: ")
    price = float(input("Enter Item Price: "))
    category = input("Enter Category: ")
    cursor.execute("INSERT INTO Menu (Name, Price, Category) VALUES (?, ?, ?)", (name, price, category))
    db.commit()
    print("✅ Item added successfully!")

# View Menu
def view_menu():
    cursor.execute("SELECT * FROM Menu")
    items = cursor.fetchall()
    if items:
        print("\n------ MENU ------")
        print(tabulate(items, headers=["ItemID", "Name", "Price", "Category"], tablefmt="fancy_grid"))
    else:
        print("⚠️ No menu items found.")

# Add Customer
def add_customer():
    name = input("Enter Customer Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    cursor.execute("INSERT INTO Customer (Name, Phone, Email) VALUES (?, ?, ?)", (name, phone, email))
    db.commit()
    print("✅ Customer added successfully!")

# View Customers
def view_customers():
    cursor.execute("SELECT * FROM Customer")
    customers = cursor.fetchall()
    if customers:
        print("\n------ CUSTOMERS ------")
        print(tabulate(customers, headers=["CustomerID", "Name", "Phone", "Email"], tablefmt="fancy_grid"))
    else:
        print("⚠️ No customers found.")

# Place Order
def place_order():
    view_customers()
    cust_id = int(input("Enter Customer ID: "))
    view_menu()
    item_id = int(input("Enter Item ID: "))
    qty = int(input("Enter Quantity: "))
    order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute("INSERT INTO Orders (CustomerID, ItemID, Quantity, OrderDate) VALUES (?, ?, ?, ?)", 
                   (cust_id, item_id, qty, order_date))
    db.commit()
    print("✅ Order placed successfully!")

# View Orders
def view_orders():
    cursor.execute('''
    SELECT Orders.OrderID, Customer.Name, Menu.Name, Orders.Quantity, Orders.OrderDate
    FROM Orders
    JOIN Customer ON Orders.CustomerID = Customer.CustomerID
    JOIN Menu ON Orders.ItemID = Menu.ItemID
    ''')
    orders = cursor.fetchall()
    if orders:
        print("\n------ ORDERS ------")
        print(tabulate(orders, headers=["OrderID", "Customer", "Item", "Quantity", "OrderDate"], tablefmt="fancy_grid"))
    else:
        print("⚠️ No orders found.")

# Daily Sales Report
def daily_sales_report():
    today = datetime.now().strftime("%Y-%m-%d")
    cursor.execute('''
    SELECT Menu.Name, SUM(Orders.Quantity), SUM(Orders.Quantity * Menu.Price)
    FROM Orders
    JOIN Menu ON Orders.ItemID = Menu.ItemID
    WHERE date(OrderDate) = ?
    GROUP BY Menu.Name
    ''', (today,))
    report = cursor.fetchall()
    if report:
        print(f"\n📊 Sales Report for {today}")
        print(tabulate(report, headers=["Item", "Total Sold", "Revenue (₹)"], tablefmt="fancy_grid"))
    else:
        print("⚠️ No sales found for today.")

# ---------------- MAIN MENU ---------------- #
def main():
    while True:
        print("\n===== RESTAURANT MANAGEMENT SYSTEM =====")
        print("1. Add Menu Item")
        print("2. View Menu")
        print("3. Add Customer")
        print("4. View Customers")
        print("5. Place Order")
        print("6. View Orders")
        print("7. Daily Sales Report")
        print("8. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            add_menu_item()
        elif choice == "2":
            view_menu()
        elif choice == "3":
            add_customer()
        elif choice == "4":
            view_customers()
        elif choice == "5":
            place_order()
        elif choice == "6":
            view_orders()
        elif choice == "7":
            daily_sales_report()
        elif choice == "8":
            print("👋 Exiting...")
            db.close()
            break
        else:
            print("❌ Invalid choice! Try again.")

# Run program
if __name__ == "__main__":
    main()
