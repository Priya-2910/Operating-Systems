def round_robin(processes, time_quantum):
    print("\n🔸 Round Robin Scheduling")
    from collections import deque

    queue = deque()
    time = 0
    remaining = {pid: bt for pid, at, bt, prio in processes}
    start_times = {}
    results = []
    arrived = []

    while processes or queue or arrived:
        # Add newly arrived processes
        arrived += [p for p in processes if p[1] <= time]
        processes = [p for p in processes if p[1] > time]
        for p in arrived:
            if p not in queue:
                queue.append(p)
        arrived.clear()

        if not queue:
            time += 1
            continue

        pid, at, bt, prio = queue.popleft()
        if pid not in start_times:
            start_times[pid] = time

        run_time = min(time_quantum, remaining[pid])
        time += run_time
        remaining[pid] -= run_time

        if remaining[pid] > 0:
            queue.append((pid, at, bt, prio))
        else:
            end_time = time
            results.append((pid, at, start_times[pid], bt, end_time))
            print(f"Process {pid}: Start={start_times[pid]}, End={end_time}")

    return results
