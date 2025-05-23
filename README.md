## 🧩 Features

### 🔍 Malware Detection
- Scans files using YARA rules
- Generates PDF reports for infections
- Sends email alerts if malware is found
- Verifies file integrity using SHA-256 hashing

### 🖥️ OS Simulations
- CPU Scheduling: FCFS, SJF, Priority, Round Robin
- Banker's Algorithm (deadlock avoidance)
- LRU Cache (memory page replacement)

### 📦 All-in-One Runner
- Unified `run-all.py` script with interactive menu
## 📁 Project Structure

project/
├── rules/
│   └── fake_rules.yar
│
├── source/
│   ├── OS_algorithms/
│   │   ├── fcfs.py
│   │   ├── priority-sheridan.py
│   │   ├── round-robin.py
│   │   ├── sjf.py
│   │   └── __init__.py
│   │
│   ├── samples/
│   │   ├── cleanfile.txt
│   │   ├── fake-malware1.txt
│   │   └── fake-virus.exe
│   │
│   ├── utils/
│   │   ├── integrity-checker.py
│   │   ├── report-generated-pdf.py
│   │   └── __init__.py
│   │
│   ├── bankers-algorithm.py
│   ├── email-alert.py
│   ├── file-watcher.py
│   ├── lru-cache.py
│   ├── main-os-runner.py
│   ├── main.py
│   ├── run-all.py
│   ├── yara-scanner.py
│   └── readme.md
