# Password Generator

A simple Python application that generates random passwords based on user input.

## Features

- Generate multiple passwords at once
- Specify minimum and maximum password lengths
- Passwords include a mix of lowercase letters, uppercase letters, numbers, and special characters
- Each password is guaranteed to have at least one character from each category

## Requirements

- Python 3.6 or higher

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Follow the prompts to:
   - Enter the number of passwords you want to generate
   - Specify the minimum password length
   - Specify the maximum password length

3. The program will display the generated passwords with their lengths.

## Example

```
Welcome to the Password Generator!
--------------------------------
How many passwords would you like to generate? 3
What is the minimum password length? 8
What is the maximum password length? 12

Generated Passwords:
-------------------
1. Kj#9mP$n (10 characters)
2. P@5vL8xQ (9 characters)
3. R$7tN#mKpL (11 characters)
```

## How It Works

The password generator uses Python's `random` and `string` modules to create random passwords. Each password is guaranteed to contain at least:
- One lowercase letter
- One uppercase letter
- One digit
- One special character

The remaining characters are randomly selected from all available character types. 