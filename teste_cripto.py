import bcrypt

# store your password</strong>:
password = str(input("input password: "))

# Encode the stored password</strong>:
password = password.encode('utf-8')

# Encrypt the stored pasword</strong>:
hashed = bcrypt.hashpw(password, bcrypt.gensalt(10))

# Create an authenticating password input field to check if a user enters the correct password</strong>
check = str(input("check password: "))

# Encode the authenticating password as well</strong>
check = check.encode('utf-8')

# Use conditions to compare the authenticating password with the stored one</strong>:
print(hashed)
print(check)
if bcrypt.checkpw(check, hashed):
    print("login success")
else:
    print("incorrect password")
