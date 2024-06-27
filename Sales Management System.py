# Importing
import sqlite3

# Connect with DB
conn = sqlite3.connect("sales_management_system.db")
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS products(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price INTEGER NOT NULL,
                quantity INTEGER NOT NULL
            )""")
# Calling
conn.commit()
# Closeing
conn.close()

# Functions....

def add_product(name, price, quantity):
    conn = sqlite3.connect("sales_management_system.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO products(name, price, quantity) VALUES(?, ?, ?)",(name, price, quantity))
    conn.commit()
    conn.close()

def update_product(new_name, new_price, new_quantity, name):
    conn = sqlite3.connect("sales_management_system.db")
    cur = conn.cursor()
    cur.execute("UPDATE products SET name = ?, price = ?, quantity = ? WHERE name = ?",(new_name, new_price, new_quantity, name))
    conn.commit()
    conn.close()

def display_product():
    conn = sqlite3.connect("sales_management_system.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM products")
    data_product = cur.fetchall()
    conn.close()
    return data_product

def search_product(search):
    conn = sqlite3.connect("sales_management_system.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE name LIKE ?", ('%' + search + '%',))
    search_products = cur.fetchall()
    conn.commit()
    return search_products

def delete_product(name):
    conn = sqlite3.connect("sales_management_system.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE name = ?", (name,))
    conn.commit()
    conn.close()

def product_exists(name):
    conn = sqlite3.connect("sales_management_system.db")
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM products WHERE name = ?", (name,))
    exists = cur.fetchone() is not None
    conn.close()
    return exists

def main():
    print("-"*15 +"Sales Management System"+ "-"*15)
    while True:
        print("1. Add Product")
        print("2. Update Product")
        print("3. Display Products")
        print("4. Search Product")
        print("5. Delete Product")
        print("6. Exit")
        choice = input("Enter your choice from 1 to 6: ")

        if choice == '1':
            print("# Add Product!")
            product_name = input("Enter a Product Name: ")
            if product_name:
                price = int(input("Enter a Product Price: "))
                if price:
                    quantity = int(input("Enter a Product Quantity: "))
                    add_product(product_name, price, quantity)
                    print("Product Added Successfully!!")
                    print("-" * 15)
                else:
                    print("Error 404, please try again..")
            else:
                print("Error 404, please try again..")

        elif choice == '2':
            print("-" * 15)
            print("# Update Product!")
            name = input("Enter the name of product to update: ")
            if product_exists(name):
                new_name = input("Enter the New Name: ")
                new_price = int(input("Enter the New Price: "))
                new_quantity = int(input("Enter the New Product Quantity: "))
                update_product(new_name, new_price, new_quantity, name)
                print("Product Updated Successfully!!")
                print("-" * 15)
            else:
                print("Product not found!")

        elif choice == '3':
            print("-" * 15)
            print("# Display Product!")
            products = display_product()
            for product in products:
                print(f"[{product[0]}] {product[1]}  |  Price: {product[2]}")
                print(f"Quantity: {product[3]}")
                print()   
            print("-" * 15)

        elif choice == '4':
            print("-" * 15)
            print("# Search Product!")
            while True:
                search = input("Enter the name to search (ex for exit): ")
                if search == 'ex':
                    break
                results = search_product(search)
                if results:
                    for product in results:
                        print(f"[{product[0]}] {product[1]}  |  Price: {product[2]}")
                        print(f"Quantity: {product[3]}")
                        print()
                    print("-"*15)
                    break
                else:
                    print("Product not found!")

        elif choice == '5':
            print("-" * 15)
            print("# Delete Product!")
            while True:
                name = input("Enter the name of product to delete (ex for exit): ")
                if name == 'ex':
                    break
                if product_exists(name):
                    delete_product(name)
                    print("Product Deleted Successfully!!")
                    print("-" * 15)
                    break
                else:
                    print("Product not found!")

        elif choice == '6':
            print("Thanks for trying our app, Have a nice day!")
            break

        else:
            print("Invalid choice, please select a number between 1 and 6!")
# Runing code
if __name__ == '__main__':
    main()