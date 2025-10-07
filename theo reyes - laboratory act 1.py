#task 1
def calculate_area(length, width):
    return length * width

print(calculate_area(23, 5))

#task 2
def greet_user(name, message = "hello"):
    return f"{message}, {name}!"

output = greet_user("theo")

print(output)

#task 3
def find_max(*args):
    if not args:
        return None
    max_val = args[0]
    for num in args[1:]:
        if num > max_val:
            max_val = num
    return max_val

output2 = find_max(3, 5, 2, 8, 1)
print(output2)

#task 4
def create_user_profile(first_name, last_name, **kwargs):
    profile = {
        'first_name': first_name,
        'last_name': last_name
    }
    profile.update(kwargs)
    return profile

# Example usage
user = create_user_profile("Jane", "Doe", age=28, city="Paris", role="Engineer")
print(user)

