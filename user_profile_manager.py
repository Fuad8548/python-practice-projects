# Practice project for handling object attributes dynamically
class UserProfile:
    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)   # routes through __setattr__ for validation

    # validation 
    def __setattr__(self, name, value):
        if name == "email" and "@" not in value:
            raise ValueError(f"Invalid email: {value}")
        if name == "name" and (not isinstance(value, str) or not value.strip()):
            raise ValueError(f"Invalid name: {value!r}")    # !r uses repr() to show empty string
        print(f"Setting {name} = {value}")
        super().__setattr__(name, value)


form_data = {"name": "Fuad", "email": "fuad@email.com", "country": "BD"}
user = UserProfile(form_data)

# Attempt invalid updates -- each caught individually, program keeps running
try:
    user.email = "not an email!"
except ValueError as e:
    print(f"Blocked: {e}")

try:
    user.name = ""
except ValueError as e:
    print(f"Blocked: {e}")

# Dynamically delete 'country' at the end
if hasattr(user, "country"):
    delattr(user, "country")
    print("Removed attribute: country")

# Print only real, remaining user data (skip internal dunder methods)
for attr in dir(user):
    if not attr.startswith("__") and not callable(getattr(user, attr)):
        print(f"{attr}: {getattr(user, attr)}")