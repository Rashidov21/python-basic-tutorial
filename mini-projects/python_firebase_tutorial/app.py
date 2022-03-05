from config import auth

# Authentication
email = input("E")
password = input("P")

try:
    auth.sign_in_with_email_and_password(email, password)
    print("succes")
except :
    print("error")