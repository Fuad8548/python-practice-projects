# Practice project for handling object attributes dynamically
class UserProfile:
    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)

    def __setattr__(self, name, value):
        # if name == "email" and "@" not in value:
        #     raise ValueError(f"Invalid email: {value}")
        print(f"Setting {name} = {value}")
        super().__setattr__(name, value)

form_data = {"name": "Fuad", "email": "fuad@email.com", "country": "BD"}
user = UserProfile(form_data)

# Try an invalid email, but don't let it kill the script
# try:
#     user.email = "not an email!"
# except ValueError as e:
#     print(f"Blocked: {e}")

attribute_to_clean = ["email"]
for attr in attribute_to_clean:
    if hasattr(user, attr):
        delattr(user, attr)
        print(f"Removed attribute: {attr}")

for attr in dir(user):
    if not attr.startswith("__") and not callable(getattr(user, attr)):
        print(f"{attr}: {getattr(user, attr)}")