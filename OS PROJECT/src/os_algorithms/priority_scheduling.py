def priority_scheduling(processes):
    print("\n🔸 Priority Scheduling")
    processes.sort(key=lambda x: (x[1], x[3]))  # Sort by arrival then priority
    time = 0
    results = []

    while processes:
        ready_queue = [p for p in processes if p[1] <= time]
        if not ready_queue:
            time += 1
            continue

        highest_priority = min(ready_queue, key=lambda x: x[3])
        processes.remove(highest_priority)
        pid, at, bt, prio = highest_priority
        time = max(time, at)
        start_time = time
        end_time = start_time + bt
        results.append((pid, at, start_time, bt, end_time))
        time = end_time
        print(f"Process {pid}: Start={start_time}, End={end_time}, Priority={prio}")

    return results
