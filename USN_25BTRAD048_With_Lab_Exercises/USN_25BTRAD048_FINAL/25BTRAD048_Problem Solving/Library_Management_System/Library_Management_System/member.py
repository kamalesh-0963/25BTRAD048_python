from storage import load_data, save_data

FILE = "members.json"

def register_member():
    members = load_data(FILE)
    member_id = max([m["id"] for m in members], default=1000) + 1

    print("\n--- Member Registration ---")
    name = input("Member name: ").strip()
    age_text = input("Age: ").strip()
    gender = input("Gender: ").strip()
    phone = input("Phone number: ").strip()
    interest = input("Favourite genre: ").strip()

    if not name or not age_text.isdigit() or int(age_text) <= 0:
        print("Please enter a valid name and age.")
        return

    member = {
        "id": member_id,
        "name": name,
        "age": int(age_text),
        "gender": gender,
        "phone": phone,
        "interest": interest
    }
    members.append(member)
    save_data(FILE, members)
    print(f"Member registered successfully. Member ID: {member_id}")

def view_members():
    members = load_data(FILE)
    print("\n--- Member List ---")
    if not members:
        print("No member records found.")
        return
    for m in members:
        print(f'ID: {m["id"]} | Name: {m["name"]} | Age: {m["age"]} | '
              f'Gender: {m["gender"]} | Phone: {m["phone"]} | Genre: {m["interest"]}')

def search_member():
    members = load_data(FILE)
    search_id = input("Enter member ID: ").strip()
    if not search_id.isdigit():
        print("Member ID must be a number.")
        return
    for m in members:
        if m["id"] == int(search_id):
            print("\nMember found:")
            for key, value in m.items():
                print(f"{key.title()}: {value}")
            return
    print("Member not found.")
