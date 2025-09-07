import os
import random
import string
import time
import sys
from datetime import datetime

def random_string(length=10):
    """Generate a random string of fixed length."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def print_progress(current_size, target_size_bytes, filetype, start_time):
    """Print a progress bar with percentage, size info, and ETA."""
    percent = (current_size / target_size_bytes) * 100
    bar_length = 40  # Length of the progress bar
    filled_length = int(bar_length * current_size // target_size_bytes)
    bar = "█" * filled_length + "-" * (bar_length - filled_length)

    elapsed = time.time() - start_time
    speed = current_size / elapsed if elapsed > 0 else 0  # bytes per second
    remaining = (target_size_bytes - current_size) / speed if speed > 0 else 0

    # Format ETA
    eta = time.strftime("%H:%M:%S", time.gmtime(remaining))

    sys.stdout.write(
        f"\r[{filetype}] |{bar}| {percent:6.2f}% "
        f"({current_size / (1024**2):.2f} MB / {target_size_bytes / (1024**3):.2f} GB) "
        f"ETA: {eta}"
    )
    sys.stdout.flush()

def create_csv_file(target_size_gb):
    """Create a CSV file of approximately target size in GB."""
    target_size_bytes = target_size_gb * (1024 ** 3)
    current_size = 0
    start_time = time.time()
    row_id = 1

    # Build filename later when row count is known
    temp_filename = "temp_output.csv"

    with open(temp_filename, "w", encoding="utf-8") as f:
        # Write header
        header = "id,name,age,email\n"
        f.write(header)
        current_size += len(header)

        while current_size < target_size_bytes:
            name = random_string(8)
            age = random.randint(18, 70)
            email = f"{random_string(5)}@test.com"
            row = f"{row_id},{name},{age},{email}\n"

            f.write(row)
            current_size += len(row)
            row_id += 1

            # Update progress bar every 10k rows
            if row_id % 10000 == 0:
                print_progress(current_size, target_size_bytes, "CSV", start_time)

    print_progress(current_size, target_size_bytes, "CSV", start_time)

    # Final filename with GB, datetime, and row count
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"{int(target_size_gb)}GB_testdata_{timestamp}-{row_id-1}.csv"
    os.rename(temp_filename, filename)

    print(f"\n✅ CSV file '{filename}' created with size ~{current_size / (1024**3):.2f} GB")

def create_sql_file(target_size_gb):
    """Create an SQL insert script file of approximately target size in GB."""
    target_size_bytes = target_size_gb * (1024 ** 3)
    current_size = 0
    start_time = time.time()
    row_id = 1

    # Build filename later when row count is known
    temp_filename = "temp_output.sql"

    with open(temp_filename, "w", encoding="utf-8") as f:
        # Write create table statement
        table_stmt = """CREATE TABLE test_data (
    id INT,
    name VARCHAR(50),
    age INT,
    email VARCHAR(100)
);\n\n"""
        f.write(table_stmt)
        current_size += len(table_stmt)

        while current_size < target_size_bytes:
            name = random_string(8)
            age = random.randint(18, 70)
            email = f"{random_string(5)}@test.com"
            insert_stmt = f"INSERT INTO test_data (id, name, age, email) VALUES ({row_id}, '{name}', {age}, '{email}');\n"

            f.write(insert_stmt)
            current_size += len(insert_stmt)
            row_id += 1

            # Update progress bar every 10k rows
            if row_id % 10000 == 0:
                print_progress(current_size, target_size_bytes, "SQL", start_time)

    print_progress(current_size, target_size_bytes, "SQL", start_time)

    # Final filename with GB, datetime, and row count
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    filename = f"{int(target_size_gb)}GB_testdata_{timestamp}-{row_id-1}.sql"
    os.rename(temp_filename, filename)

    print(f"\n✅ SQL file '{filename}' created with size ~{current_size / (1024**3):.2f} GB")

def main():
    while True:
        print("\nSelect file type to generate:")
        print("1. CSV File")
        print("2. SQL File")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("👋 Exiting program...")
            break
        elif choice not in ["1", "2"]:
            print("❌ Invalid choice. Please try again.")
            continue

        try:
            size_gb = float(input("Enter target file size in GB: ").strip())
            if size_gb <= 0:
                print("❌ Size must be greater than 0.")
                continue
        except ValueError:
            print("❌ Invalid size input.")
            continue

        if choice == "1":
            create_csv_file(size_gb)
        elif choice == "2":
            create_sql_file(size_gb)

if __name__ == "__main__":
    main()
