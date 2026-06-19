import threading
import time


thread_results = {}
thread_execution_times = {}


# ==========================================
# Factorial Function
# ==========================================
def factorial(number):
    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


# ==========================================
# Thread Worker
# ==========================================
def factorial_worker(number):

    start_time = time.perf_counter_ns()

    result = factorial(number)

    end_time = time.perf_counter_ns()

    thread_results[number] = result
    thread_execution_times[number] = end_time - start_time


# ==========================================
# Multithreading Test
# ==========================================
def multithreading_test():

    global thread_results
    global thread_execution_times

    thread_results = {}
    thread_execution_times = {}

    start_time = time.perf_counter_ns()

    thread_1 = threading.Thread(target=factorial_worker, args=(50,))
    thread_2 = threading.Thread(target=factorial_worker, args=(100,))
    thread_3 = threading.Thread(target=factorial_worker, args=(200,))

    thread_1.start()
    thread_2.start()
    thread_3.start()

    thread_1.join()
    thread_2.join()
    thread_3.join()

    end_time = time.perf_counter_ns()

    total_time = end_time - start_time

    return total_time


# ==========================================
# Single Thread Test
# ==========================================
def single_thread_test():

    start_time = time.perf_counter_ns()

    factorial(50)
    factorial(100)
    factorial(200)

    end_time = time.perf_counter_ns()

    total_time = end_time - start_time

    return total_time


# ==========================================
# Display Thread Information
# ==========================================
def display_thread_information():

    print("\nTHREAD EXECUTION DETAILS")

    print("+-----------+----------------------+")
    print("| Factorial | Execution Time (ns)  |")
    print("+-----------+----------------------+")

    for key in sorted(thread_execution_times.keys()):
        print(
            f"| {str(key)+'!':<9} "
            f"| {thread_execution_times[key]:<20} |"
        )

    print("+-----------+----------------------+")


# ==========================================
# Multithreading Experiment
# ==========================================
def run_multithreading_experiment():

    print("\n")
    print("=" * 60)
    print("MULTITHREADING EXPERIMENT")
    print("=" * 60)

    total = 0

    print("+---------+----------------------+")
    print("| Round   | Time (ns)            |")
    print("+---------+----------------------+")

    for round_number in range(1, 11):

        elapsed_time = multithreading_test()

        total += elapsed_time

        print(
            f"| {round_number:<7} "
            f"| {elapsed_time:<20} |"
        )

    print("+---------+----------------------+")

    average = total / 10

    print(f"\nAverage Multithreading Time : {average:.2f} ns")

    display_thread_information()

    return average


# ==========================================
# Single Thread Experiment
# ==========================================
def run_single_thread_experiment():

    print("\n")
    print("=" * 60)
    print("SINGLE THREAD EXPERIMENT")
    print("=" * 60)

    total = 0

    print("+---------+----------------------+")
    print("| Round   | Time (ns)            |")
    print("+---------+----------------------+")

    for round_number in range(1, 11):

        elapsed_time = single_thread_test()

        total += elapsed_time

        print(
            f"| {round_number:<7} "
            f"| {elapsed_time:<20} |"
        )

    print("+---------+----------------------+")

    average = total / 10

    print(f"\nAverage Single Thread Time : {average:.2f} ns")

    return average


# ==========================================
# Complexity Analysis
# ==========================================
def display_complexity_analysis():

    print("\n")
    print("=" * 60)
    print("TIME COMPLEXITY ANALYSIS")
    print("=" * 60)

    print("+----------------------+----------------+")
    print("| Operation            | Complexity     |")
    print("+----------------------+----------------+")
    print("| Factorial Function   | O(n)           |")
    print("| Multithreading       | O(n)           |")
    print("| Single Thread        | O(n)           |")
    print("+----------------------+----------------+")

    print("\nExplanation:")
    print("The factorial function loops from 1 to n.")
    print("Therefore, the number of primitive operations")
    print("increases linearly with the input size.")
    print("Hence the time complexity is O(n).")


# ==========================================
# Comparison
# ==========================================
def compare_results(multithread_average, single_average):

    print("\n")
    print("=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)

    print("+----------------------+----------------------+")
    print("| Method               | Average Time (ns)    |")
    print("+----------------------+----------------------+")

    print(
        f"| {'Multithreading':<20} "
        f"| {multithread_average:<20.2f} |"
    )

    print(
        f"| {'Single Thread':<20} "
        f"| {single_average:<20.2f} |"
    )

    print("+----------------------+----------------------+")

    if multithread_average < single_average:
        print("\nResult:")
        print("Multithreading performed faster.")
    else:
        print("\nResult:")
        print("Single Thread performed faster.")

    print("\nDiscussion:")
    print("Python uses the Global Interpreter Lock (GIL).")
    print("For CPU-intensive tasks such as factorial calculations,")
    print("multithreading may not always provide significant speed improvements.")
    print("However, multithreading is useful when handling")
    print("multiple independent tasks concurrently.")


# ==========================================
# Main Program
# ==========================================
def main():

    print("=" * 60)
    print("FACTORIAL MULTITHREADING PERFORMANCE ANALYSIS")
    print("=" * 60)

    multithread_average = run_multithreading_experiment()

    single_average = run_single_thread_experiment()

    display_complexity_analysis()

    compare_results(
        multithread_average,
        single_average
    )


main()