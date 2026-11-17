from storage import load_data, save_data
from book import BOOKS

FILE = "issued_books.json"

def issue_book():
    members = load_data("members.json")
    if not members:
        print("Register a member before issuing a book.")
        return

    print("\n--- Issue Book ---")
    member_text = input("Enter member ID: ").strip()
    if not member_text.isdigit():
        print("Invalid member ID.")
        return
    member = next((m for m in members if m["id"] == int(member_text)), None)
    if member is None:
        print("Member not found.")
        return

    for book in BOOKS:
        print(f'{book["id"]}. {book["title"]} - {book["author"]}')
    book_text = input("Choose book ID: ").strip()
    if not book_text.isdigit():
        print("Invalid book ID.")
        return
    book = next((b for b in BOOKS if b["id"] == int(book_text)), None)
    if book is None:
        print("Book not found.")
        return

    issue_date = input("Issue date (DD-MM-YYYY): ").strip()
    return_date = input("Due date (DD-MM-YYYY): ").strip()
    if not issue_date or not return_date:
        print("Issue date and due date are required.")
        return

    issued = load_data(FILE)
    issue_id = max([i["id"] for i in issued], default=0) + 1
    issued.append({
        "id": issue_id,
        "member_id": member["id"],
        "member_name": member["name"],
        "book": book["title"],
        "issue_date": issue_date,
        "due_date": return_date
    })
    save_data(FILE, issued)
    print(f"Book issued successfully. Issue ID: {issue_id}")

def view_issued_books():
    issued = load_data(FILE)
    print("\n--- Issued Book List ---")
    if not issued:
        print("No issued books found.")
        return
    for i in issued:
        print(f'ID: {i["id"]} | Member: {i["member_name"]} '
              f'(ID {i["member_id"]}) | Book: {i["book"]} | '
              f'Issued: {i["issue_date"]} | Due: {i["due_date"]}')
