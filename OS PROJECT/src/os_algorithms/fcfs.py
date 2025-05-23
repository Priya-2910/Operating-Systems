
def fcfs(processes):
    print("\n🔸 FCFS Scheduling")
    processes.sort(key=lambda x: x[1])  # Sort by arrival time
    time = 0
    results = []

    for pid, at, bt, prio in processes:
        time = max(time, at)
        start_time = time
        end_time = start_time + bt
        results.append((pid, at, start_time, bt, end_time))
        time = end_time
        print(f"Process {pid}: Start={start_time}, End={end_time}")

    return results
