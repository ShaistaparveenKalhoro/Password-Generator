import random
import string

def generate_password(length):
    """
    Generate a random password of specified length
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Combine all character sets
    all_chars = lowercase + uppercase + digits + special_chars
    
    # Ensure password contains at least one of each character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffle the password to make it more random
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    print("--------------------------------")
    
    # Get user input
    try:
        num_passwords = int(input("How many passwords would you like to generate? "))
        min_length = int(input("What is the minimum password length? "))
        max_length = int(input("What is the maximum password length? "))
        
        # Validate input
        if num_passwords <= 0:
            print("Number of passwords must be greater than 0.")
            return
        
        if min_length < 4:
            print("Minimum password length must be at least 4 characters.")
            return
        
        if max_length < min_length:
            print("Maximum password length must be greater than or equal to minimum length.")
            return
        
        # Generate passwords
        print("\nGenerated Passwords:")
        print("-------------------")
        for i in range(num_passwords):
            # Randomly select a length between min_length and max_length
            length = random.randint(min_length, max_length)
            password = generate_password(length)
            print(f"{i+1}. {password} ({length} characters)")
            
    except ValueError:
        print("Please enter valid numbers for all inputs.")

if __name__ == "__main__":
    main()
