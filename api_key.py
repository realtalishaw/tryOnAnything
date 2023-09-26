import secrets

def generate_api_key():
    return secrets.token_hex(16)  # 16 bytes = 32 characters

api_key = generate_api_key()
print("Generated API Key:", api_key)
