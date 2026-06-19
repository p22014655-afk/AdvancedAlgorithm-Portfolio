import time


class Transaction:
    def __init__(self, transaction_id, customer_name, product_name, amount, transaction_date):
        self.transaction_id = transaction_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.amount = amount
        self.transaction_date = transaction_date


recursive_calls = 0


def display_transactions(transactions):
    print("\n+----------------+----------------------+----------------------+------------+------------------+")
    print("| Transaction ID | Customer Name        | Product Name         | Amount     | Date             |")
    print("+----------------+----------------------+----------------------+------------+------------------+")

    if len(transactions) == 0:
        print("| No transactions available.                                                                |")
    else:
        for transaction in transactions:
            print(
                f"| {transaction.transaction_id:<14} "
                f"| {transaction.customer_name:<20} "
                f"| {transaction.product_name:<20} "
                f"| RM{transaction.amount:<8.2f} "
                f"| {transaction.transaction_date:<16} |"
            )

    print("+----------------+----------------------+----------------------+------------+------------------+")


def merge_sort(transactions):
    global recursive_calls
    recursive_calls += 1

    if len(transactions) <= 1:
        return transactions

    # Divide step
    middle = len(transactions) // 2
    left_half = transactions[:middle]
    right_half = transactions[middle:]

    # Conquer step using recursion
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combine step
    return merge(left_sorted, right_sorted)


def merge(left, right):
    sorted_list = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i].transaction_id <= right[j].transaction_id:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list


def binary_search(transactions, target_id):
    low = 0
    high = len(transactions) - 1

    while low <= high:
        middle = (low + high) // 2

        if transactions[middle].transaction_id == target_id:
            return transactions[middle]

        elif transactions[middle].transaction_id < target_id:
            low = middle + 1

        else:
            high = middle - 1

    return None


def linear_search(transactions, target_id):
    for transaction in transactions:
        if transaction.transaction_id == target_id:
            return transaction

    return None


def add_transaction(transactions):
    try:
        transaction_id = int(input("Enter Transaction ID: "))

        for transaction in transactions:
            if transaction.transaction_id == transaction_id:
                print("Transaction ID already exists.")
                return

        customer_name = input("Enter Customer Name: ")
        product_name = input("Enter Product Name: ")
        amount = float(input("Enter Amount: RM"))
        transaction_date = input("Enter Transaction Date (YYYY-MM-DD): ")

        new_transaction = Transaction(
            transaction_id,
            customer_name,
            product_name,
            amount,
            transaction_date
        )

        transactions.append(new_transaction)
        print("Transaction added successfully.")

    except ValueError:
        print("Invalid input. Transaction ID must be number and amount must be decimal.")


def sort_by_amount(transactions):
    sorted_list = sorted(transactions, key=lambda transaction: transaction.amount)
    return sorted_list


def display_search_result(result):
    if result:
        print("\nTransaction Found:")
        print("+----------------+----------------------+----------------------+------------+------------------+")
        print("| Transaction ID | Customer Name        | Product Name         | Amount     | Date             |")
        print("+----------------+----------------------+----------------------+------------+------------------+")
        print(
            f"| {result.transaction_id:<14} "
            f"| {result.customer_name:<20} "
            f"| {result.product_name:<20} "
            f"| RM{result.amount:<8.2f} "
            f"| {result.transaction_date:<16} |"
        )
        print("+----------------+----------------------+----------------------+------------+------------------+")
    else:
        print("Transaction not found.")


def performance_comparison(transactions):
    global recursive_calls

    print("\nPerformance Comparison")
    print("The test searches for existing and non-existing transaction IDs.")

    search_keys = [101, 108, 115, 999]

    recursive_calls = 0

    start = time.perf_counter_ns()
    sorted_transactions = merge_sort(transactions)
    merge_sort_time = time.perf_counter_ns() - start

    print("\nMerge Sort Result:")
    print("Merge Sort Time:", merge_sort_time, "ns")
    print("Total Recursive Calls:", recursive_calls)

    print("\n+----------------+----------------------+----------------------+")
    print("| Transaction ID | Binary Search Time   | Linear Search Time   |")
    print("+----------------+----------------------+----------------------+")

    for key in search_keys:
        start = time.perf_counter_ns()
        binary_search(sorted_transactions, key)
        binary_time = time.perf_counter_ns() - start

        start = time.perf_counter_ns()
        linear_search(transactions, key)
        linear_time = time.perf_counter_ns() - start

        print(f"| {key:<14} | {binary_time:<20} | {linear_time:<20} |")

    print("+----------------+----------------------+----------------------+")
    print("\nNote: Binary Search needs sorted data first, while Linear Search can work on unsorted data.")


def display_complexity_table():
    print("\n+------------------+----------------------+-----------------------------+")
    print("| Algorithm        | Time Complexity      | Explanation                 |")
    print("+------------------+----------------------+-----------------------------+")
    print("| Merge Sort       | O(n log n)           | Divide and merge records    |")
    print("| Binary Search    | O(log n)             | Divide search range by half |")
    print("| Linear Search    | O(n)                 | Check one by one            |")
    print("+------------------+----------------------+-----------------------------+")


def insert_sample_transactions():
    transactions = [
        Transaction(108, "Ali", "Laptop", 2500.00, "2026-01-10"),
        Transaction(103, "John", "Mouse", 55.00, "2026-01-05"),
        Transaction(115, "Sarah", "Keyboard", 150.00, "2026-01-18"),
        Transaction(101, "Ahmad", "Monitor", 600.00, "2026-01-01"),
        Transaction(112, "Lisa", "SSD", 350.00, "2026-01-15"),
        Transaction(106, "Ben", "RAM", 200.00, "2026-01-06"),
        Transaction(110, "David", "GPU", 1800.00, "2026-01-13"),
        Transaction(104, "Mike", "CPU", 1200.00, "2026-01-08"),
        Transaction(109, "Amy", "Headset", 180.00, "2026-01-12"),
        Transaction(102, "Tom", "Webcam", 220.00, "2026-01-11"),
        Transaction(114, "Siti", "Printer", 750.00, "2026-01-20"),
        Transaction(107, "Daniel", "Tablet", 980.00, "2026-01-09"),
        Transaction(111, "Mei Ling", "Router", 300.00, "2026-01-14"),
        Transaction(105, "Kumar", "Speaker", 130.00, "2026-01-07"),
        Transaction(113, "Nina", "Smartwatch", 450.00, "2026-01-17"),
    ]

    return transactions


def display_menu():
    print("\n==============================================")
    print("        TRANSACTION MANAGEMENT SYSTEM")
    print("==============================================")
    print("1. Display All Transactions")
    print("2. Sort Transactions by Transaction ID")
    print("3. Search Transaction using Binary Search")
    print("4. Search Transaction using Linear Search")
    print("5. Add New Transaction")
    print("6. Sort Transactions by Amount")
    print("7. Performance Comparison")
    print("8. Display Time Complexity Table")
    print("9. Exit")
    print("==============================================")


def main():
    global recursive_calls

    transactions = insert_sample_transactions()
    sorted_transactions = None

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            display_transactions(transactions)

        elif choice == "2":
            print("\nBefore Sorting:")
            display_transactions(transactions)

            recursive_calls = 0

            start = time.perf_counter_ns()
            sorted_transactions = merge_sort(transactions)
            sort_time = time.perf_counter_ns() - start

            print("\nAfter Sorting by Transaction ID:")
            display_transactions(sorted_transactions)

            print("Merge Sort Time:", sort_time, "ns")
            print("Total Recursive Calls:", recursive_calls)

        elif choice == "3":
            if sorted_transactions is None:
                sorted_transactions = merge_sort(transactions)

            try:
                target_id = int(input("Enter Transaction ID to search: "))

                start = time.perf_counter_ns()
                result = binary_search(sorted_transactions, target_id)
                search_time = time.perf_counter_ns() - start

                display_search_result(result)
                print("Binary Search Time:", search_time, "ns")

            except ValueError:
                print("Invalid Transaction ID.")

        elif choice == "4":
            try:
                target_id = int(input("Enter Transaction ID to search: "))

                start = time.perf_counter_ns()
                result = linear_search(transactions, target_id)
                search_time = time.perf_counter_ns() - start

                display_search_result(result)
                print("Linear Search Time:", search_time, "ns")

            except ValueError:
                print("Invalid Transaction ID.")

        elif choice == "5":
            add_transaction(transactions)
            sorted_transactions = None

        elif choice == "6":
            sorted_by_amount = sort_by_amount(transactions)

            print("\nTransactions Sorted by Amount:")
            display_transactions(sorted_by_amount)

        elif choice == "7":
            performance_comparison(transactions)

        elif choice == "8":
            display_complexity_table()

        elif choice == "9":
            print("Thank you for using Transaction Management System.")
            break

        else:
            print("Invalid choice. Please enter 1 to 9.")


main()