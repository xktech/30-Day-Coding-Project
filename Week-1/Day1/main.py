from todolistCLI import add_item, remove_item, view_list, save_list, load_list

while True:
    print("1. ADD")
    print("2. REMOVE")
    print("3. VIEW")
    print("4. SAVE")
    print("5. EXIT")


    choice = input("> ").lower()

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_list()
    elif choice == "4":
        save_list()
    elif choice == "5":
        break

