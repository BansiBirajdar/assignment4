'''Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62'''
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
def ChekPrime(no):
    i=0
    for i in range(2,no+1):
        if(no%i==0):
            break
    if no==i:
        return True
    else: 
        return False
    
def Modify(no):
    return no*2
def Max(data):
    max=data[0]
    for i in range(1,len(data),1):
        if max<data[i]:
            max=data[i]
    return max
def main():
    RawData = AcceptData()
    print("Accepted data is ")
    print(RawData)
    FilteredData = list(filter(ChekPrime,RawData))
    print("Filtered data is")
    print(FilteredData)
    ModfiedData = list(map(Modify,FilteredData))
    print("Modified data is ")
    print(ModfiedData)
    #print("final result is =",max(ModfiedData));
    result =Max(ModfiedData)
    print("Final result is=",result) 
if __name__ == "__main__":
    main()