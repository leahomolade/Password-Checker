# Helper functions
def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_char(password):
    special_characters = "!@#$%^&*"
    return any(char in special_characters for char in password)

def get_password_strength(password):
    checks_passed = 0
    feedback = []

    if len(password) >= 8:
        checks_passed += 1
    else:
        feedback.append("at least 8 characters")

    if has_lowercase(password):
        checks_passed += 1
    else:
        feedback.append("lowercase letters")

    if has_uppercase(password):
        checks_passed += 1
    else:
        feedback.append("uppercase letters")

    if has_digit(password):
        checks_passed += 1
    else:
        feedback.append("digits")

    if has_special_char(password):
        checks_passed += 1
    else:
        feedback.append("special characters (!@#$%^&*)")

    # Determine strength
    if checks_passed <= 2:
        strength = "Weak"
    elif checks_passed == 3 or checks_passed == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, feedback

# Main function
def main():
    print("Welcome to the Password Strength Checker!")
    password = input("Enter your password: ")

    strength, feedback = get_password_strength(password)
    print(f"\nPassword Strength: {strength}")

    if strength != "Strong":
        print("Try including:", ", ".join(feedback))

# Run the program
if __name__ == "__main__":
    main()
