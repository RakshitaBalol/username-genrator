

print("== USERNAME GENERATOR ==")

first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
fav_word = input("Enter your favourite word: ").strip()

username1 = first_name[:3].lower() + last_name[:3].lower()

username2 = "-".join([first_name.title(), last_name.title()])

username3 = first_name[::-1] + last_name[0].upper()

username4 = f"{first_name.lower()}_{fav_word.upper()}_{len(first_name)+len(last_name)}"

print("\nHere are some username suggestions for you:")
print(f"1️⃣ {username1}")
print(f"2️⃣ {username2}")
print(f"3️⃣ {username3}")
print(f"4️⃣ {username4}")

choice = input("\nEnter the number of your favourite username (1-4): ").strip()

if choice == "1":
    final = username1
elif choice == "2":
    final = username2
elif choice == "3":
    final = username3
elif choice == "4":
    final = username4
else:
    final = "Invalid choice"

print(f"\n✅ Your final username is: {final}")