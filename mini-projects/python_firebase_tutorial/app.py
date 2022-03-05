from config import db

# db.child("fruit").set({"name":"kiwi"})


def write_data(table_name, values):
    try:
        db.child(table_name).set(values) # push()
    except Exception as er:
        print("Error :", er)
    else:
        print("Successfully")
    return True
data = {
    "name":"Apelsin",
    "price":15,
    "weight":"2.5 kg"
}
# write_data("fruit", data)

# d = db.child("fruit").get()
# for i, k in d.val().items():
#     print(i, k)








# from config import auth
# try:
#     email = input("Email >> ")
#     password = input("Password >> ")
#     comfirm = input("Comfirm Password >> ")
#     if password == comfirm:
#         auth.create_user_with_email_and_password(email, password)
#     else:
#         print("Password doesnt match")
#     print("Successfully !")
# except:
#     print("Error !")
#     # auth.sign_in_with_email_and_password(email,password) #kirish
# print("Successfully")