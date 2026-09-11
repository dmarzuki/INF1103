inventory = 0
failed_entries = 0

while True:
    user_input = input("Enter stock quantity (or type 'quit' to stop): ")

    if user_input.lower() == "quit":
        break
   
    if user_input.isdigit():
        user_input = int(user_input)
    
    else:
        print ("Error: Invalid input.")
        failed_entries += 1
        continue

    inventory += user_input
    
    if inventory > 500:
        print("ALERT: Inventory has exceeded 500 units.")
        break
    
    

print("Total Units Processed: ", inventory)
print("Number of Failed/Rejected Entries: ", failed_entries)