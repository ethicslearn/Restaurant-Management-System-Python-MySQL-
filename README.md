# 🍽️ Restaurant Management System  
_A CBSE Class 12 Computer Science Project using Python, SQLite3, and Tabulate_

---

## 📌 Project Overview  
The **Restaurant Management System** is a Python + SQL-based project designed to manage:  
- ✅ Menu Items (Add / View)  
- ✅ Customers (Add / View)  
- ✅ Orders (Place / View)  
- ✅ Daily Sales Report  

It uses **SQLite3** for database management and **Tabulate** for displaying data in a well-formatted table view.

---

## ⚙️ Requirements  

Install required Python modules:  

```bash
# pip install tabulate

 ## 📂 Project Structure


restaurant_management/
│── restaurant.py        # Main Python program
│── restaurant.db        # SQLite database (auto-created on first run)
│── README.md            # Documentation

##🛠️ Features & Working
1. Database Connection & Tables

Uses sqlite3.connect() to create restaurant.db.

Creates Menu, Customer, and Orders tables if not present.

db = sqlite3.connect("restaurant.db")
cursor = db.cursor()

2. Menu Management

Add Menu Item → Insert new dish with name, price, and category.

View Menu → Display menu items in a formatted table using tabulate.

📸 Example Output:

╒═════════╤═══════════╤════════╤════════════╕
│ ItemID  │ Name      │ Price  │ Category   │
╞═════════╪═══════════╪════════╪════════════╡
│ 1       │ Pizza     │ 250.0  │ Fast Food  │
│ 2       │ Pasta     │ 180.0  │ Italian    │
╘═════════╧═══════════╧════════╧════════════╛

3. Customer Management

Add Customer → Store customer details (Name, Phone, Email).

View Customers → Display customers in a table.

📸 Example Output:

╒════════════╤═══════════╤════════════╤══════════════════╕
│ CustomerID │ Name      │ Phone      │ Email            │
╞════════════╪═══════════╪════════════╪══════════════════╡
│ 1          │ Rahul     │ 9876543210 │ rahul@gmail.com  │
│ 2          │ Priya     │ 8765432109 │ priya@yahoo.com  │
╘════════════╧═══════════╧════════════╧══════════════════╛

4. Order Management

Place Order → Links a customer + menu item + quantity.

View Orders → Displays all orders with customer & item details.

📸 Example Output:

╒══════════╤═══════════╤══════════╤══════════╤════════════════════╕
│ OrderID  │ Customer  │ Item     │ Quantity │ OrderDate          │
╞══════════╪═══════════╪══════════╪══════════╪════════════════════╡
│ 1        │ Rahul     │ Pizza    │ 2        │ 2025-08-29 12:30   │
│ 2        │ Priya     │ Pasta    │ 1        │ 2025-08-29 13:10   │
╘══════════╧═══════════╧══════════╧══════════╧════════════════════╛

5. Daily Sales Report

Calculates total items sold & revenue for the current date.

📸 Example Output:

╒══════════╤═════════════╤═══════════════╕
│ Item     │ Total Sold  │ Revenue (₹)   │
╞══════════╪═════════════╪═══════════════╡
│ Pizza    │ 2           │ 500.0         │
│ Pasta    │ 1           │ 180.0         │
╘══════════╧═════════════╧═══════════════╛

🐍 Python Modules Used
1. sqlite3 (Built-in)

Provides SQLite database connectivity.

import sqlite3

2. tabulate (External)

Displays results in tabular format for better readability.

from tabulate import tabulate


📌 Install with:

pip install tabulate

3. datetime (Built-in)

Used to handle order timestamps and daily sales reports.

import datetime

4. os (Built-in, optional)

Used for clearing the console to improve user interface.

import os

🚀 How to Run

Save all project files.

Run the program:

python restaurant.py


Choose from options in the menu:

Add/View Menu

Add/View Customers

Place/View Orders

Daily Sales Report

📊 Future Enhancements

GUI interface using Tkinter / PyQt

Export reports to Excel/CSV

Add Admin login system

📚 Author

👨‍💻 Developed by SHREYANSH JAISWAL 
📌 Language: Python 3.x
📌 Database: SQLite3
