'''1.Write a program which contains one lambda function which accepts one parameter and return
power of two.
Input : 4 Output : 16
Input : 6 Output : 64'''

power=lambda no:no*no
def main():
    no=int(input("enter the number="))
    result=power(no);
    print("power of {} is ".format(no),result)

if __name__ == "__main__":
    main()