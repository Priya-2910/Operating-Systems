def is_safe_state(alloc, max_need, avail):
    n = len(alloc)
    m = len(avail)
    need = [[max_need[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]

    finish = [False] * n
    safe_seq = []
    work = avail[:]

    while len(safe_seq) < n:
        allocated_this_round = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += alloc[i][j]
                safe_seq.append(f"P{i}")
                finish[i] = True
                allocated_this_round = True
                break
        if not allocated_this_round:
            return False, []

    return True, safe_seq

# 🔹 Sample test
if __name__ == "__main__":
    alloc = [
        [0, 1, 0],
        [2, 0, 0],
        [3, 0, 2],
        [2, 1, 1],
        [0, 0, 2]
    ]

    max_need = [
        [7, 5, 3],
        [3, 2, 2],
        [9, 0, 2],
        [2, 2, 2],
        [4, 3, 3]
    ]

    avail = [3, 3, 2]

    is_safe, seq = is_safe_state(alloc, max_need, avail)
    if is_safe:
        print("✅ System is in a SAFE STATE.")
        print("🟢 Safe Sequence:", " → ".join(seq))
    else:
        print("❌ System is in an UNSAFE STATE. Deadlock possible!")
