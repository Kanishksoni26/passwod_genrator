# 🔐 Password Generator

A simple yet secure command-line password generator written in Python. It uses the `secrets` module for cryptographically strong random character selection, making it suitable for generating real-world passwords.

---

## Features

- Cryptographically secure password generation using Python's `secrets` module
- Customizable character sets — uppercase, lowercase, digits, and symbols
- Enforces a minimum password length of 8 characters
- Guarantees at least one character from each selected character type
- Shuffles the final password to eliminate predictable patterns

---

## Requirements

- Python 3.6 or higher (no external dependencies)

---

## Usage

Run the script from the terminal:

```bash
python password_genrator.py
```

You will be prompted with the following questions:

```
Enter the length of the password min(8): 12
Include upper case letters? (yes/no): yes
Include the lower case also: (yes/no): yes
Include numbers? (yes/no): yes
Include symbols? (yes/no): no
```

**Example output:**

```
Secure Generated Password: aB3xkR7mNqLp
```

---

## How It Works

1. **Input collection** — The user provides the desired password length and which character types to include.
2. **Guaranteed characters** — At least one character from each selected type is added first to ensure the password meets the chosen criteria.
3. **Character pool** — All selected character sets are combined into a single pool.
4. **Fill remaining slots** — The rest of the password is filled by randomly picking from the pool using `secrets.choice()`.
5. **Shuffle** — The password list is shuffled with `random.shuffle()` to remove any positional patterns.
6. **Output** — The final password is printed to the terminal.

---

## Security Notes

- Character selection uses Python's `secrets` module, which is designed for generating cryptographically strong random values.
- The final shuffle uses `random.shuffle()`, which is not cryptographically secure, but since the characters themselves are already securely selected, this does not weaken the overall entropy.

---

## File Structure

```
password_genrator.py   # Main script
README.md              # Project documentation
```

---

## License

This project is open source and free to use.

## Author 
kanishk soni
