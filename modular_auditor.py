def get_valid_input():
        user_input = input("Enter stock quantity (or type 'quit' to stop): ")

        if user_input.lower() == "quit":
            return "quit"
       
        if user_input.isdigit():
            return int(user_input)

        else:
            print("Error: Invalid input.")
            return None

def process_delivery(current_total, new_value):
    return current_total + new_value

def calculate_tax(amount):
    return amount * 0.10

def generate_report(total_units, failed_attempts):
    print("Total Units Processed: ", total_units)
    print("Number of Failed/Rejected Entries: ", failed_attempts)

def main():
    inventory = 0
    failed_entries = 0
    deliveries_processed = 0

    while True:
         result = get_valid_input()

         if result == "quit":
              break

         if result is None:
              failed_entries += 1
              continue

         inventory = process_delivery(inventory, result)
         tax = calculate_tax(result)
         deliveries_processed += 1

         print(f"Delivery of {result} units accepted.Tax owed: {tax}")

    generate_report(deliveries_processed, failed_entries)

if __name__ == "__main__":
     main()