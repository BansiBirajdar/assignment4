'''Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204'''
from functools import *;
def AcceptData():
    size = int(input("Enter number of elements"))
    arr= list()
    print("Enter the elements")
    for i in range(0,size,1):
        print("Enter number",i + 1)
        no = int(input())
        arr.append(no)
    return arr

def ChkEven(no):
    if((no % 2) == 0):
        return True
    else:
        return False
def Modify(no):
    return no*no
def Add(no1,no2):
    return no1+no2
def main():
    RawData = AcceptData()
    print("Accepted data is ")
    print(RawData)
    FilteredData = list(filter(ChkEven,RawData))
    print("Filtered data is")
    print(FilteredData)
    ModfiedData = list(map(Modify,FilteredData))
    print("Modified data is ")
    print(ModfiedData)
    result = reduce(Add,ModfiedData)
    print("Final result is=",result) 
if __name__ == "__main__":
    main()