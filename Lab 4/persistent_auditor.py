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
    print("Total Units: ", total_units)
    print("Number of Failed/Rejected Entries: ", failed_attempts)

def load_inventory():
    inventory = 0
    history = []
    try:
          file = open('inventory.txt', 'r')
          lines = file.readlines()
          file.close()

          if len(lines) > 0:
               inventory = int(lines[0].strip())
          
          if len(lines) > 1:
               pieces = lines[1].strip().split(",")
               i = 0
               while i < len(pieces):
                    history.append(int(pieces[i]))
                    i += 1

          return inventory, history
          
    except FileNotFoundError:
         return 0, []

def save_inventory(total, history):
     file = open('inventory.txt', 'w')
     file.write(str(total) + "\n")

     history_strings = []
     i = 0
     while i < len(history):
          history_strings.append(str(history[i]))
          i += 1

     file.write(",".join(history_strings))
     file.close()

def main():
    inventory, history = load_inventory() 
    failed_entries = 0

    while True:
         result = get_valid_input()

         if result == "quit":
              break

         if result is None:
              failed_entries += 1
              continue

         inventory = process_delivery(inventory, result)
         tax = calculate_tax(result)
         history.append(result)
         print("Tax owed: ", round(tax, 2))
         print(history)

    generate_report(inventory, failed_entries)
    save_inventory(inventory, history)

main()