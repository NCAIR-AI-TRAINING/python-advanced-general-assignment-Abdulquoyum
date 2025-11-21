from datetime import datetime
import os

class DuplicateVisitorError(Exception):
    pass

class EarlyEntryError(Exception):
    pass

FILENAME = "visitors.txt"

def ensure_file():
    """ To create visitors file if it doesn't exist"""
    if not os.path.exists(FILENAME):
        with open(FILENAME,'w') as f:
            pass

def get_last_visitor():
    try:
        with open(FILENAME, 'r') as f:
            lines = f.readlines()
        if not lines:
            return None, None
        
        last_line = None
        for line in reversed(lines):
            if line.strip():
                last_line = line.strip()
                break
        if not last_line:
            return None, None
        
        parts = last_line.split('-', 1)
        if len(parts) == 2:
            timestamp_str = parts[0]
            name = parts[1]
            timestamp = datetime. strftime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            return name, timestamp
        return None, None
    except Exception as e:
        return None, None
    

def add_visitor(visitor_name):
    if not visitor_name:
        raise ValueError("Visitor name cannot be empty")
    last_name, last_timestamp = get_last_visitor()
    current_time = datetime.now()

    if last_name is not None and last_name == visitor_name:
        raise DuplicateVisitorError(f"{visitor_name} is the last visitor logged")
    with open(FILENAME, 'a') as f:
        timestamp_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"{timestamp_str} - {visitor_name}\n")
    
    pass

def main():
    ensure_file()
    name = input("Enter visitor's name: ")
    try:
        add_visitor(name)
        print("Visitor added successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
