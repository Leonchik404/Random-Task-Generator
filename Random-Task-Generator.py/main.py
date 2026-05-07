from task_manager import TaskManager

def main():
    manager = TaskManager()
    
    while True:
        print("\n--- RANDOM TASK GENERATOR ---")
        print("1. Generate Task\n2. View History\n3. Filter History\n4. Exit")
        choice = input("Select option: ").strip()

        if choice == "1":
            task = manager.generate_random_task()
            print(f"Generated: {task.get_details()}")
        
        elif choice == "2":
            print("\nHistory (Last 10):")
            for t in manager.history: print(t.get_details())
            
        elif choice == "3":
            crit = input("Enter Type (Work/Sport/Study) or Difficulty (1-5): ").strip()
            results = manager.filter_history(crit)
            print("\nFiltered results:")
            for r in results: print(r.get_details())
            
        elif choice == choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid input. Please enter 1-4.")

if __name__ == "__main__":
    main
