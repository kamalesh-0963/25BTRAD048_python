from member import register_member, view_members, search_member
from book import view_books
from issue import issue_book, view_issued_books
from fine import create_fine_bill

def show_menu():
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Register Member")
    print("2. View Members")
    print("3. Search Member")
    print("4. View Books")
    print("5. Issue Book")
    print("6. View Issued Books")
    print("7. Calculate Fine")
    print("8. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            register_member()
        elif choice == "2":
            view_members()
        elif choice == "3":
            search_member()
        elif choice == "4":
            view_books()
        elif choice == "5":
            issue_book()
        elif choice == "6":
            view_issued_books()
        elif choice == "7":
            create_fine_bill()
        elif choice == "8":
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()
