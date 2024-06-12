import re

def check_password_strength(password):
    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    strength = 0
    points_details = []

    if length_criteria:
        strength += 1
        points_details.append("1 point for length (8 or more characters)")
    else:
        points_details.append("0 points for length (less than 8 characters)")

    if uppercase_criteria:
        strength += 1
        points_details.append("1 point for uppercase letter")
    else:
        points_details.append("0 points for uppercase letter")

    if lowercase_criteria:
        strength += 1
        points_details.append("1 point for lowercase letter")
    else:
        points_details.append("0 points for lowercase letter")

    if number_criteria:
        strength += 1
        points_details.append("1 point for number")
    else:
        points_details.append("0 points for number")

    if special_char_criteria:
        strength += 1
        points_details.append("1 point for special character")
    else:
        points_details.append("0 points for special character")
    feedback = []
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character.")

    # Strength messages
    strength_messages = {
        1: "Very Weak",
        2: "Weak",
        3: "Moderate",
        4: "Strong",
        5: "Very Strong"
    }

    strength_message = strength_messages.get(strength, "Undefined")

    return {
        'strength': strength_message,
        'total_points': strength,
        'points_details': points_details,
        'feedback': feedback
    }

password = input("Enter a password to check its strength: ")
result = check_password_strength(password)

print(f"Password Strength: {result['strength']}")
print(f"Total Points: {result['total_points']}/5")
print("Points Awarded:")
for detail in result['points_details']:
    print(detail)
for suggestion in result['feedback']:
    print(f"Suggestion: {suggestion}")
