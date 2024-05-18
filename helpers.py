def get_key():
    try:
        with open('api.key', 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Key not found.")