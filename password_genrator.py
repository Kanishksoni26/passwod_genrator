import string
import secrets
import random

# input from the user 
length = int(input("Enter  the length of the password min(8):"))
if length < 8:
    print("Password length must be at least 8.")
    exit()

use_upper = input("Include upper case latters ?(yes/no)").lower()
use_lower = input("include the lower case also :(yes/no)").lower()
use_numbers = input('include numbers ?(yes/no)').lower()
use_symbol =input("include symbols ? (yes/no)")

# we are using character groups from the string library 
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

password = []

password.append(secrets.choice(lowercase))
if use_upper == "yes":
    password.append(secrets.choice(uppercase))
if use_numbers == "yes":
    password.append(secrets.choice(digits))
if use_symbol == "yes" :
    password.append(secrets.choice(symbols))

# Step 5: Create the big pool
char_pool = lowercase

if use_upper == 'yes':
    char_pool += uppercase

if use_numbers == 'yes':
    char_pool += digits

if use_symbol == 'yes':
    char_pool += symbols



if length <len(password):
    print("password is short please enter a valid length password ")
    exit()

# Step 7: Fill remaining characters
remaining_length = length - len(password)

for _ in range(remaining_length):
    password.append(secrets.choice(char_pool))

# Step 8: Shuffle to remove pattern
random.shuffle(password)

# Step 9: Convert list to string
new_password = ''.join(password)

# Step 10: Display password
print("\nSecure Generated Password:", new_password)
