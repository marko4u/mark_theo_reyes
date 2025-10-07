#task 1
full_name = input("Enter your full name (first and last): ").strip()
# Split and clean
parts = full_name.split()
first_name = parts[0].capitalize()
last_name = parts[-1].capitalize()

print("First Name:", first_name)
print("Last Name:", last_name)

#task 2
timestamp = "20241006"
file_name = f"{first_name.lower()}_{last_name.lower()}_report_{timestamp}.txt"
print("Formatted File Name:", file_name)

#task 3
def is_valid_password(password: str) -> bool:
    has_digit = any(char.isdigit() for char in password)
    return len(password) >= 8 and has_digit

print("Password Validity:", is_valid_password("abc12345"))  # True
print("Password Validity:", is_valid_password("abcdefg"))   # False

#task 4
def reverse_words(sentence: str) -> str:
    words = sentence.strip().split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

print("Reversed Sentence:", reverse_words("Python is fun"))