import matplotlib.pyplot as plt
from os_algorithms.fcfs import fcfs
from os_algorithms.sjf import sjf
from os_algorithms.priority_scheduling import priority_scheduling
from os_algorithms.round_robin import round_robin

def get_processes():
    # (PID, Arrival Time, Burst Time, Priority)
    return [
        ("P1", 0, 5, 2),
        ("P2", 1, 3, 1),
        ("P3", 2, 8, 4),
        ("P4", 3, 6, 3)
    ]

def calculate_turnaround_times(results):
    total_time = 0
    for _, arrival, _, _, end in results:
        turnaround = end - arrival
        total_time += turnaround
    return total_time

def run_algorithm(choice):
    processes = get_processes()
    results = []

    if choice == "1":
        print("\n🔸 You selected FCFS")
        results = fcfs(processes)
    elif choice == "2":
        print("\n🔸 You selected SJF")
        results = sjf(processes)
    elif choice == "3":
        print("\n🔸 You selected Priority Scheduling")
        results = priority_scheduling(processes)
    elif choice == "4":
        print("\n🔸 You selected Round Robin (Time Quantum = 3)")
        results = round_robin(processes, time_quantum=3)
    else:
        print("❌ Invalid choice")
        return None

    return calculate_turnaround_times(results)

def plot_graph(efficiency_dict):
    algorithms = ["FCFS", "SJF", "Priority Scheduling", "Round Robin"]
    turnaround_times = [efficiency_dict.get(1), efficiency_dict.get(2), efficiency_dict.get(3), efficiency_dict.get(4)]

    plt.figure(figsize=(10, 6))
    plt.bar(algorithms, turnaround_times, color=['blue', 'green', 'orange', 'red'])
    plt.xlabel('CPU Scheduling Algorithms')
    plt.ylabel('Total Turnaround Time')
    plt.title('Comparison of CPU Scheduling Algorithms')
    plt.show()

if __name__ == "__main__":
    print("\n⚙️ CPU Scheduling Menu:")
    print("1. FCFS")
    print("2. SJF")
    print("3. Priority Scheduling")
    print("4. Round Robin")

    all_efficiency = {}

    for i in range(1, 5):
        total_time = run_algorithm(str(i))
        if total_time:
            all_efficiency[i] = total_time

    best = min(all_efficiency, key=all_efficiency.get)
    best_algo = ["FCFS", "SJF", "Priority", "Round Robin"][best - 1]

    print(f"\n✅ Most Efficient: {best_algo} (based on lowest total turnaround time)")

    # Plot the graph to visualize the efficiency of each algorithm
    plot_graph(all_efficiency)
