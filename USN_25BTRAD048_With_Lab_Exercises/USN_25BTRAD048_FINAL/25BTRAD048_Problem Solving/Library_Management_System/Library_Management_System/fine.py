FINE_PER_DAY = 5

def create_fine_bill():
    print("\n--- Library Fine Calculation ---")
    member_name = input("Member name: ").strip()
    if not member_name:
        print("Member name is required.")
        return

    try:
        late_days = int(input("Number of days late: "))
        damage = float(input("Damage charges (Rs.): "))
        lost = float(input("Lost book charges (Rs.): "))
        if min(late_days, damage, lost) < 0:
            raise ValueError
    except ValueError:
        print("Enter valid non-negative values.")
        return

    late_fee = late_days * FINE_PER_DAY
    total = late_fee + damage + lost
    print("\n========== FINE RECEIPT ==========")
    print(f"Member: {member_name}")
    print(f"Late fee ({late_days} days x Rs. {FINE_PER_DAY}): Rs. {late_fee:.2f}")
    print(f"Damage charges:   Rs. {damage:.2f}")
    print(f"Lost book charge: Rs. {lost:.2f}")
    print("----------------------------------")
    print(f"Total amount: Rs. {total:.2f}")
    print("==================================")
