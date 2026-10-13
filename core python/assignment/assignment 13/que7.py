user_data = {"name": "Shantanu", "age": 25, "city": "Pune"}

key_to_remove = "age"
if key_to_remove in user_data:
    del user_data[key_to_remove]

print("Updated Dictionary:", user_data)