#requires a user to enter a number and prints from 1 to the number
def ask_value():
    num=int(input("enter number: "))
    return num
def count(num):
    n=1
    while n<=num:
        print(n)
        n=n+1
def main():
    num=ask_value()
    count(num)
main()