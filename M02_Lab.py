# Jorden Wolf
# GPA tester
# Will test gpas and tell user if a person has made Dean's list or Honor roll.
while True:
    last_name = input("What's your last name?: ").strip().capitalize()
    if last_name.lower() == "zzz":
        break # Not sure why we do this
    first_name = input("What's your first name?: ").strip().capitalize()
    gpa = None
    while not gpa:
        try:
            gpa = float(input("What's your GPA?: ").strip())
        except ValueError:
            print("Value entered must be a number.")
    if gpa > 3.5:
        print(f"{first_name} {last_name} has made the Dean's list.")
    elif gpa > 3.25:
        print(f"{first_name} {last_name} has made the Honor roll.")
