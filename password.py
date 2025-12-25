import streamlit as st
import re
import string
def password_strength(password):
    length = len(password)

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    charset = 0
    if has_digit:
        charset += 10
    if has_lower:
        charset += 26
    if has_upper:
        charset += 26
    if has_symbol:
        charset += 32

    combinations = charset ** length

    guesses_per_second = 1_000_000_000  # 1 billion
    seconds = combinations / guesses_per_second

    return length, charset, seconds

def format_time(seconds):
    units = [
        ("years", 60 * 60 * 24 * 365),
        ("days", 60 * 60 * 24),
        ("hours", 60 * 60),
        ("minutes", 60),
        ("seconds", 1),
    ]

    for name, value in units:
        if seconds >= value:
            return f"{seconds / value:.2f} {name}"

    return "instantly"

password = input("Enter your password: ")

length, charset, time_to_crack = password_strength(password)

print("\n🔐 Password Analysis")
print("--------------------")
print(f"Length           : {length}")
print(f"Character set    : {charset}")
print(f"Estimated crack time : {format_time(time_to_crack)}")

if length < 8 or charset < 40:
    print("Strength         : ❌ Weak")
elif length < 12:
    print("Strength         : ⚠️ Medium")
else:
    print("Strength         : ✅ Strong")