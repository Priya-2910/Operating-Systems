import time
import os
from yara_scanner import scan_file
from utils.integrity_checker import calculate_sha256

WATCHED_DIR = "samples"

def monitor_directory():
    seen_files = set(os.listdir(WATCHED_DIR))
    print("👀 Monitoring for new files in 'samples/'...\n")

    while True:
        time.sleep(3)
        current_files = set(os.listdir(WATCHED_DIR))
        new_files = current_files - seen_files

        for file in new_files:
            filepath = os.path.join(WATCHED_DIR, file)
            print(f"\n📂 New file detected: {file}")
            scan_file(filepath)  # YARA scan
            print(f"🧪 File hash: {calculate_sha256(filepath)}")
        
        seen_files = current_files

if __name__ == "__main__":
    monitor_directory()
