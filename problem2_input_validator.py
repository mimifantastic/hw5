# Collect every field before checking the profile.
student_id = input("Enter student ID: ").strip()
name = input("Enter full name: ").strip()
age_text = input("Enter age: ").strip()
major = input("Enter major: ").strip().upper()
errors = []

# Check each ID rule independently; slicing is safe for an empty ID.
if len(student_id) != 8:
    errors.append(
        f"Student ID must be exactly 8 characters (got {len(student_id)})"
    )
if not student_id[:1].isalpha():
    errors.append("Student ID must start with a letter")
if not student_id[1:].isdigit():
    errors.append("Student ID characters after the first must be digits")

if not name:
    errors.append("Name cannot be empty")
elif len(name) < 2:
    errors.append("Name must be at least 2 characters")

# Only check the range if conversion to an integer succeeds.
try:
    age = int(age_text)
    if not 16 <= age <= 99:
        errors.append("Age must be between 16 and 99")
except ValueError:
    errors.append("Age must be a valid integer")

if major not in ["CS", "IT", "CE", "DS"]:
    errors.append(f"Major must be one of: CS, IT, CE, DS (got {major})")

# Report all errors together, or display the accepted profile.
if errors:
    print("Profile has errors:")
    for error in errors:
        print(f"  - {error}")
else:
    print("Profile created successfully!")
    print(f"  Student ID: {student_id}")
    print(f"  Name:       {name}")
    print(f"  Age:        {age}")
    print(f"  Major:      {major}")
