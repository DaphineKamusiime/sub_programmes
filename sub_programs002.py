#getting a users data and printing a message depending on their age
def get_data():
    user_name=input("Enter your name: ")
    user_age=int(input("Enter your age: "))
    data_tuple=(user_name,user_age)
    return data_tuple
def message(user_name,user_age):
    if user_age<=10:
        print("Hi ", user_name)
    else:
        print("Hello ",user_name)
def main():
    user_name,user_age=get_data()
    message(user_name,user_age)
main()
