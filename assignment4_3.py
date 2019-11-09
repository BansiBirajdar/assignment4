'''3.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that
numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000'''
from functools import *

def AcceptData():
    size = int(input("Enter number of elements"))
    arr= list()
    print("Enter the elements")
    for i in range(0,size,1):
        print("Enter number",i + 1)
        no = int(input())
        arr.append(no)
    return arr

def Modify(no):
    return no+10
def mult(no1,no2):
    return no1*no2
def ChkNo(no):
    if no>=70 and no<=90:
        return no

def main():
    RawData = AcceptData()
    print("Accepted data is ")
    print(RawData)
    FilteredData = list(filter(ChkNo,RawData))
    print("Filtered data is")
    print(FilteredData)
    ModfiedData = list(map(Modify,FilteredData))
    print("Modified data is ")
    print(ModfiedData)
    result = reduce(mult,ModfiedData)
    print("Final result is=",result) 
if __name__ == "__main__":
    main()

