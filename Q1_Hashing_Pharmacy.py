import time

DELETED = "DELETED"


class Medicine:
    def __init__(self, product_id, name, category, quantity, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.product_id} | {self.name} | {self.category} | {self.quantity} | RM{self.price:.2f}"


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, medicine):
        index = self.hash_function(medicine.product_id)
        start_index = index

        while self.table[index] is not None and self.table[index] != DELETED:
            if self.table[index].product_id == medicine.product_id:
                print("Product ID already exists.")
                return False

            index = (index + 1) % self.size

            if index == start_index:
                print("Hash table is full.")
                return False

        self.table[index] = medicine
        return True

    def search(self, product_id):
        index = self.hash_function(product_id)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] != DELETED and self.table[index].product_id == product_id:
                return self.table[index]

            index = (index + 1) % self.size

            if index == start_index:
                break

        return None

    def edit(self, product_id):
        product = self.search(product_id)

        if product is None:
            print("Product not found.")
            return

        print("\nCurrent Product Details:")
        print(product)

        new_name = input("Enter new product name: ")
        new_category = input("Enter new category: ")

        try:
            new_quantity = int(input("Enter new quantity: "))
            new_price = float(input("Enter new price: RM"))

            product.name = new_name
            product.category = new_category
            product.quantity = new_quantity
            product.price = new_price

            print("Product updated successfully.")

        except ValueError:
            print("Invalid input. Quantity must be number and price must be decimal.")

    def delete(self, product_id):
        index = self.hash_function(product_id)
        start_index = index

        while self.table[index] is not None:
            if self.table[index] != DELETED and self.table[index].product_id == product_id:
                self.table[index] = DELETED
                return True

            index = (index + 1) % self.size

            if index == start_index:
                break

        return False

    def display(self):
        print("\n+------------+----------------------+-----------------+----------+----------+")
        print("| Product ID | Product Name         | Category        | Quantity | Price    |")
        print("+------------+----------------------+-----------------+----------+----------+")

        empty = True

        for item in self.table:
            if item is not None and item != DELETED:
                empty = False
                print(
                    f"| {item.product_id:<10} "
                    f"| {item.name:<20} "
                    f"| {item.category:<15} "
                    f"| {item.quantity:<8} "
                    f"| RM{item.price:<6.2f} |"
                )

        if empty:
            print("| No products available.                                               |")

        print("+------------+----------------------+-----------------+----------+----------+")


def linear_array_search(array, product_id):
    for item in array:
        if item.product_id == product_id:
            return item
    return None


def performance_comparison(hash_table, medicine_array):
    search_keys = [101, 105, 110, 999, 888]

    print("\n+-------------+----------------------+----------------------+")
    print("| Product ID  | Hash Table Time (ns) | Array Time (ns)      |")
    print("+-------------+----------------------+----------------------+")

    for key in search_keys:
        start = time.perf_counter_ns()
        hash_table.search(key)
        hash_time = time.perf_counter_ns() - start

        start = time.perf_counter_ns()
        linear_array_search(medicine_array, key)
        array_time = time.perf_counter_ns() - start

        print(f"| {key:<11} | {hash_time:<20} | {array_time:<20} |")

    print("+-------------+----------------------+----------------------+")


def insert_sample_data(hash_table, medicine_array):
    sample_medicines = [
        Medicine(101, "Paracetamol", "Tablet", 50, 5.50),
        Medicine(102, "Vitamin C", "Supplement", 30, 12.90),
        Medicine(103, "Cough Syrup", "Syrup", 20, 9.80),
        Medicine(104, "Ibuprofen", "Tablet", 45, 7.50),
        Medicine(105, "Calcium", "Supplement", 25, 15.90),
        Medicine(106, "Antacid", "Tablet", 35, 6.20),
        Medicine(107, "Eye Drops", "Liquid", 18, 8.70),
        Medicine(108, "Flu Tablets", "Tablet", 40, 10.50),
        Medicine(109, "Omega 3", "Supplement", 22, 25.00),
        Medicine(110, "Skin Cream", "Cream", 15, 18.90),
    ]

    for medicine in sample_medicines:
        hash_table.insert(medicine)
        medicine_array.append(medicine)


def add_new_product(hash_table, medicine_array):
    try:
        product_id = int(input("Enter Product ID: "))

        if hash_table.search(product_id):
            print("Product ID already exists.")
            return

        name = input("Enter Product Name: ")
        category = input("Enter Category: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price: RM"))

        medicine = Medicine(product_id, name, category, quantity, price)

        if hash_table.insert(medicine):
            medicine_array.append(medicine)
            print("Product inserted successfully.")

    except ValueError:
        print("Invalid input. Please enter correct number format.")


def display_menu():
    print("\n======================================")
    print("      PHARMACY INVENTORY SYSTEM")
    print("======================================")
    print("1. Display Inventory")
    print("2. Search Product")
    print("3. Insert Product")
    print("4. Edit Product")
    print("5. Delete Product")
    print("6. Performance Comparison")
    print("7. Exit")
    print("======================================")


def main():
    hash_table = HashTable(23)
    medicine_array = []

    insert_sample_data(hash_table, medicine_array)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            hash_table.display()

        elif choice == "2":
            try:
                product_id = int(input("Enter Product ID to search: "))
                result = hash_table.search(product_id)

                if result:
                    print("\nProduct Found:")
                    print("+------------+----------------------+-----------------+----------+----------+")
                    print("| Product ID | Product Name         | Category        | Quantity | Price    |")
                    print("+------------+----------------------+-----------------+----------+----------+")
                    print(
                        f"| {result.product_id:<10} "
                        f"| {result.name:<20} "
                        f"| {result.category:<15} "
                        f"| {result.quantity:<8} "
                        f"| RM{result.price:<6.2f} |"
                    )
                    print("+------------+----------------------+-----------------+----------+----------+")
                else:
                    print("Product not found.")

            except ValueError:
                print("Invalid Product ID.")

        elif choice == "3":
            add_new_product(hash_table, medicine_array)

        elif choice == "4":
            try:
                product_id = int(input("Enter Product ID to edit: "))
                hash_table.edit(product_id)
            except ValueError:
                print("Invalid Product ID.")

        elif choice == "5":
            try:
                product_id = int(input("Enter Product ID to delete: "))

                if hash_table.delete(product_id):
                    medicine_array[:] = [
                        item for item in medicine_array
                        if item.product_id != product_id
                    ]
                    print("Product deleted successfully.")
                else:
                    print("Product not found.")

            except ValueError:
                print("Invalid Product ID.")

        elif choice == "6":
            performance_comparison(hash_table, medicine_array)

        elif choice == "7":
            print("Thank you for using Pharmacy Inventory System.")
            break

        else:
            print("Invalid choice. Please enter 1 to 7.")


main()