'''2.Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
Input : 4 3 Output : 12
Input : 6 3 Output : 18'''
mult=lambda no1,no2:no1*no2
def main():
    no1=int(input("enter the 1st number="))
    no2=int(input("enter the 2nd number="))
    result=mult(no1,no2);
    print("multiplication= ",result)

if __name__ == "__main__":
    main()