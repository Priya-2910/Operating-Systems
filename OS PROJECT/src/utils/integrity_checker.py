import hashlib
import os
import json

INTEGRITY_DB = "integrity_db.json"

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def initialize_integrity_db(directory):
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file_path] = calculate_sha256(file_path)
    
    with open(INTEGRITY_DB, "w") as db:
        json.dump(file_hashes, db, indent=4)
    print("Integrity DB initialized.")

def check_file_integrity(file_path):
    if not os.path.exists(INTEGRITY_DB):
        print("Integrity DB not found. Run initialization first.")
        return None

    with open(INTEGRITY_DB, "r") as db:
        old_hashes = json.load(db)

    if file_path in old_hashes:
        old_hash = old_hashes[file_path]
        new_hash = calculate_sha256(file_path)
        if new_hash != old_hash:
            print(f"⚠️ WARNING: File has been modified -> {file_path}")
        else:
            print(f"✅ File integrity verified: {file_path}")
        return new_hash
    else:
        print(f"❌ File not found in integrity DB: {file_path}")
        return None
