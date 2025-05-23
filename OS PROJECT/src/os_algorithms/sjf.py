def sjf(processes):
    print("\n🔸 SJF Scheduling")
    processes.sort(key=lambda x: (x[1], x[2]))  # Sort by arrival then burst time
    time = 0
    completed = []
    results = []

    while processes:
        ready_queue = [p for p in processes if p[1] <= time]
        if not ready_queue:
            time += 1
            continue

        shortest = min(ready_queue, key=lambda x: x[2])
        processes.remove(shortest)
        pid, at, bt, prio = shortest
        time = max(time, at)
        start_time = time
        end_time = start_time + bt
        results.append((pid, at, start_time, bt, end_time))
        time = end_time
        print(f"Process {pid}: Start={start_time}, End={end_time}")

    return results
