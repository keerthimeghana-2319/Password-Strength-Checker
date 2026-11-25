
import tkinter as tk
from tkinter import messagebox
import re

common_passwords = [
    "password",
    "password123",
    "admin123",
    "qwerty123",
    "welcome123"
]

def toggle_password():
    if password_entry.cget("show") == "*":
        password_entry.config(show="")
        show_button.config(text="Hide")
    else:
        password_entry.config(show="*")
        show_button.config(text="Show")


def check_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning("Warning", "Please enter a password!")
        return

    checks = {
        "At least 8 characters": len(password) >= 8,
        "Uppercase letters": bool(re.search(r"[A-Z]", password)),
        "Lowercase letters": bool(re.search(r"[a-z]", password)),
        "Numbers": bool(re.search(r"[0-9]", password)),
        "Special characters": bool(re.search(r"[^A-Za-z0-9]", password))
    }

    score = sum(checks.values())
    is_common = password.lower() in common_passwords

    if is_common or score <= 2:
        strength = "WEAK"
        color = "red"
    elif score <= 4:
        strength = "MEDIUM"
        color = "orange"
    else:
        strength = "STRONG"
        color = "green"

    result_label.config(
        text=f"Password Strength: {strength}",
        fg=color
    )

    # Update strength meter
    meter_canvas.delete("all")
    meter_width = score * 60

    if is_common:
        meter_width = 0

    meter_canvas.create_rectangle(
        0, 0, meter_width, 20,
        fill=color,
        outline=""
    )

    # Security report
    report = f"Security Score: {score}/5\n\n"

    for condition, passed in checks.items():
        status = "PASS" if passed else "FAIL"
        report += f"{status}: {condition}\n"

    if is_common:
        report += "\nWARNING: Common password detected!"

    report_label.config(text=report)

    # Suggestions
    if is_common:
        suggestion = "Avoid commonly used passwords."
    elif score < 5:
        suggestion = "Improve the failed security checks."
    else:
        suggestion = "All basic checks passed!"

    suggestion_label.config(text=suggestion)


# Main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("470x570")
root.configure(bg="#202b38")
root.resizable(False, False)

# Heading
title = tk.Label(
    root,
    text="PASSWORD STRENGTH CHECKER",
    font=("Arial", 16, "bold"),
    bg="#202b38",
    fg="white"
)
title.pack(pady=25)

# Password input
password_entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 13),
    show="*"
)
password_entry.pack(pady=10)

# Show/Hide button
show_button = tk.Button(
    root,
    text="Show",
    command=toggle_password
)
show_button.pack(pady=5)

# Check button
check_button = tk.Button(
    root,
    text="CHECK PASSWORD",
    command=check_password,
    bg="#168aad",
    fg="white",
    font=("Arial", 11, "bold"),
    width=20
)
check_button.pack(pady=15)

# Result
result_label = tk.Label(
    root,
    text="Password Strength: Not Checked",
    font=("Arial", 13, "bold"),
    bg="#202b38",
    fg="white"
)
result_label.pack(pady=10)

# Strength meter
meter_canvas = tk.Canvas(
    root,
    width=300,
    height=20,
    bg="#465362",
    highlightthickness=0
)
meter_canvas.pack(pady=10)

# Security report
report_label = tk.Label(
    root,
    text="Your security report will appear here.",
    font=("Arial", 10),
    bg="#202b38",
    fg="white",
    justify="left"
)
report_label.pack(pady=15)

# Suggestions
suggestion_label = tk.Label(
    root,
    text="",
    font=("Arial", 10, "italic"),
    bg="#202b38",
    fg="#ffd166",
    wraplength=400
)
suggestion_label.pack(pady=10)

root.mainloop()
