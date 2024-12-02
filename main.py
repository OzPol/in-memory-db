from in_memory_db import InMemoryDB

def main():
    db = InMemoryDB()
    print("\nWelcome to the In-Memory Database CLI!\n")
    print("Remember, you need to start a transaction first,")
    print("before you can choose an option!\n")
    while True:
        print("----------------------------------------------------------")
        print("Choose an option by entering the corresponding number:\n")
        print("1. Begin Transaction")
        print("2. Put (Add/Update Key-Value Pair)")
        print("3. Get (Retrieve Value by Key)")
        print("4. Commit Transaction")
        print("5. Rollback Transaction")
        print("6. Exit")

        try:
            choice = input("\nEnter your choice: ").strip()
            if choice == "1":
                print(db.begin_transaction())
            elif choice == "2":
                key = input("Enter key: ").strip()
                value = input("Enter value (integer): ").strip()
                try:
                    print(db.put(key, int(value)))
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                key = input("Enter key: ").strip()
                print(db.get(key))
            elif choice == "4":
                try:
                    print(db.commit())
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "5":
                try:
                    print(db.rollback())
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "6":
                print("Exiting CLI. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
