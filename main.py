from datetime import datetime,timedelta
import os

class DuplicateVisitorError(Exception):
    def __init__(self, visitor):
        self.visitor = visitor
        super().__init__(f"Visitor '{visitor}' has already visited.")
    

class EarlyEntryError(Exception):
    def __init__(self):
        super().__init__("A 5-minuites wait is required between visitors.")
    

FILENAME = "visitors.txt"

def ensure_file():
    """ To create visitors file if it doesn't exist"""
    try:
         with open(FILENAME,'r') as f:
            pass
    except FileNotFoundError:
        print(f"File '{FILENAME}' not found, creting one.")
        with open(FILENAME,'w') as f:
            pass
       
def get_last_visitor():
     with open(FILENAME,'r') as f:
        lines = f.readlines()
        if lines:
            return lines[-1].strip().split(" | ")[0]
def get_last_timestamp():
        with open(FILENAME, 'r') as f:
            lines = f.readlines()
            if lines:
                return lines[-1].strip().split(" | ")[1]

def add_visitor(visitor_name):
    last_visitor = get_last_visitor()
    last_timestamp = get_last_timestamp()
    if visitor_name == last_visitor:
        raise DuplicateVisitorError(visitor_name)
    if last_timestamp:
        last_time = datetime.fromisoformat(last_timestamp)
        current_time = datetime.now()
        time_diff = current_time - last_time
        if time_diff < timedelta(minutes=5):
            raise EarlyEntryError()
    timestamp = datetime.now().isoformat()
    entry = f"{visitor_name} | {timestamp}\n"

    with open(FILENAME, 'a') as f:
        f.write(entry)

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
