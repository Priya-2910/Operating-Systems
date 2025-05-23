import os
import yara
from email_alert import send_email_alert
from utils.integrity_checker import check_file_integrity
from utils.report_generator import generate_pdf_report

# List of files to scan
FILES_TO_SCAN = [
    "samples/fake_malware1.txt",
    "samples/fake_virus.exe",
    "samples/clean_file.txt"
]

# YARA rule file
YARA_RULE_PATH = "rules/fake_rules.yar"

# Report path
REPORT_PATH = "/Users/lakshmipriya/Desktop/malware_report.pdf"

# Email to send alerts
TO_EMAIL = "lakshmipriya292004@gmail.com"  # Replace with your actual email

infected_files = []

def scan_file_with_yara(file_path, yara_rule_path):
    """
    Scans a file using YARA rules and returns a list of matched rules.
    """
    try:
        rules = yara.compile(filepath=yara_rule_path)  # Compile YARA rules
        matches = rules.match(file_path)  # Run YARA scan on the file
        
        matched_rules = [match.rule for match in matches]  # Extract the names of matched rules
        return matched_rules
    except Exception as e:
        print(f"Error scanning {file_path} with YARA: {e}")
        return []

print("\n🔎 Starting Malware Scan...\n")

for file_path in FILES_TO_SCAN:
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        continue

    # Run YARA scan
    matches = scan_file_with_yara(file_path, YARA_RULE_PATH)

    # Check integrity
    file_hash = check_file_integrity(file_path)
    print(f"🔗 SHA-256 for {file_path}: {file_hash}")

    if matches:
        print(f"🚨 MALWARE DETECTED in {file_path}! Matched Rules: {matches}\n")
        
        # Append infected file with the matched rules
        infected_files.append({
            "file": file_path,
            "matched_rules": matches  # Use 'matches' here
        })

        # Send alert email
        send_email_alert(
            subject="🚨 Malware Detected!",
            body=f"A malware was found in {file_path}.\nMatched Rules: {matches}",
            to_email=TO_EMAIL
        )
    else:
        print(f"✅ {file_path} is clean.\n")

# Generate report
generate_pdf_report(REPORT_PATH, infected_files)

print(f"\n✅ Scan Complete. PDF Report saved to: {REPORT_PATH}")
