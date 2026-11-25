
import re

print("=" * 45)
print("       PASSWORD STRENGTH CHECKER")
print("=" * 45)

password = input("Enter a sample password: ")

# Common password detection
common_passwords = [
    "password",
    "password123",
    "admin123",
    "qwerty123",
    "welcome123"
]

score = 0

checks = {
    "At least 8 characters": len(password) >= 8,
    "Contains uppercase letters": bool(re.search(r"[A-Z]", password)),
    "Contains lowercase letters": bool(re.search(r"[a-z]", password)),
    "Contains numbers": bool(re.search(r"[0-9]", password)),
    "Contains special characters": bool(re.search(r"[^A-Za-z0-9]", password))
}

print("\n----- SECURITY ANALYSIS -----")

for condition, passed in checks.items():
    if passed:
        print("[PASS] " + condition)
        score += 1
    else:
        print("[FAIL] " + condition)

# Check whether password is common
is_common = password.lower() in common_passwords

if is_common:
    print("\n[WARNING] This is a commonly used password!")
    score = 0

print("\n----- FINAL REPORT -----")

print("Security Score:", score, "/ 5")

if is_common:
    print("Password Strength: WEAK")
elif score <= 2:
    print("Password Strength: WEAK")
elif score <= 4:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: STRONG")

print("\n----- SUGGESTIONS -----")

if is_common:
    print("- Avoid commonly used passwords.")
elif score == 5:
    print("All basic checks passed!")
else:
    for condition, passed in checks.items():
        if not passed:
            print("- Improve: " + condition)

print("\n" + "=" * 45)
print("          ANALYSIS COMPLETED")
print("=" * 45)
