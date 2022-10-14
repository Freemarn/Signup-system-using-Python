print("Create an account")

username = str(input("Enter username"))
password = str(input("Enter password"))


print("Account has been created successfully")
print("login Account now")

username2 = str(input("Enter username"))
password2 = str(input("Enter password"))

if username == username2 and password == password2:
    print("logged in successful")

else:
    print("wrong username or password")