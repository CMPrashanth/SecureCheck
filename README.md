# Secure Check

This Password Complexity Checker is a Python tool designed to assess the strength of a password based on various criteria such as length, presence of uppercase and lowercase letters, numbers, and special characters. The tool provides feedback on the password's strength and suggestions for improvement.

## Features

- Checks if the password meets the following criteria:
  - **Length**: At least 8 characters long.
  - **Uppercase Letter**: Contains at least one uppercase letter (A-Z).
  - **Lowercase Letter**: Contains at least one lowercase letter (a-z).
  - **Number**: Contains at least one number (0-9).
  - **Special Character**: Contains at least one special character (e.g., !@#$%^&*(),.?":{}|<>).
- Provides a strength assessment based on the criteria:
  - Very Weak
  - Weak
  - Moderate
  - Strong
  - Very Strong
- Offers specific feedback on how to improve the password's strength.
- Displays detailed points awarded for each criterion.

## Points System

The password strength is evaluated based on the following points system, with a maximum of 5 points:

1. **Length**:
   - **1 point**: Password is at least 8 characters long.
   - **0 points**: Password is less than 8 characters long.

2. **Uppercase Letter**:
   - **1 point**: Password contains at least one uppercase letter (A-Z).
   - **0 points**: Password does not contain any uppercase letters.

3. **Lowercase Letter**:
   - **1 point**: Password contains at least one lowercase letter (a-z).
   - **0 points**: Password does not contain any lowercase letters.

4. **Number**:
   - **1 point**: Password contains at least one number (0-9).
   - **0 points**: Password does not contain any numbers.

5. **Special Character**:
   - **1 point**: Password contains at least one special character (e.g., !@#$%^&*(),.?":{}|<>).
   - **0 points**: Password does not contain any special characters.

The total points determine the overall strength of the password:

- **1 point**: Very Weak
- **2 points**: Weak
- **3 points**: Moderate
- **4 points**: Strong
- **5 points**: Very Strong
