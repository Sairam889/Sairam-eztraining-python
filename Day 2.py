#bitwise operators
print(12&7)
print(10|4)
print(~10)
print(10^4)

#bitwise operators
num1,num2=int(input("E1:")),int(input(" E2: "))
print(num1&num2)
print(num1|num2)
print(~num2)
print(num1^num2)
print(num1>>2)
print(num1<<2)



#displaying the elements of the list
n=int(input())
m=1
list1=list(map(int,input().split()))[:n]
for i in range(0,len(list1)):
    print(list1[i],end=" ")
    
#use of sep and end
print("its","a","good","day",end=" ")
print("all","is","good",sep=" * ",end=" ")
print("joy")

#printing reverse star
print("***")
print(" *** ")
print("  *")
print("   * ")

#printing heart shape
print(" * *    * * ")
print("*   *  *   *")
print(" *    *   *")
print("  *      *")
print("    *   *")
print("     * *")
print("      *")


#printing doll
print("   * * * *  ")
print("  * o   o *   ")
print("  *   W   * ")
print("   *     *")
print("   *  *  * ")
print(" *  * * *  *")
print("*  *   *  *  *")
print("#  *   *   *  #")
print("   * * * * *  ")
print("   *       *")
print("    #   #")
print(       )

#printing dog
print("   * * * *  ")
print("  * o   o *   ")
print("  *   W   * ")
print("   *     *")
print("   *  *  * ")
print("* * * * * * * *")
print("*  *       *  *")
print(" *  *     *  * ")
print("  ##**##  ")


#checking given number is 500 or not
num=int(input("Enter the number:"))
if num==500:
    print("given number is 500")
else:
    print("Given number is not a 500")

#check the given number and classify
num=int(input("Enter the number:"))
if num%2==0:
    if num>0:
        print(num," is Even-positive")
    else:
        print(num," is Even-Negative")
else:
    if num>0:
        print(num," is Odd-positive")
    else:
        print(num," is Odd-Negative")
    
#check the greatest among the two
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
if num1>num2:
    print(num1," is biggest")
else:
    print(num2," is biggest")

#check the given number is float or not
num=50
if(type(num)==int):
    print(num," is integer")
if(type(num)==float):
    print(num," is float")

#2nd method
num=50
if(num%1==0):
    print(num," is integer")
else:
    print(num," is float")

#find the greatest among the three
num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))
if num1>num2>num3 or num1>num3>num2:
    print(num1,"is greater")
elif num2>num1>num3 or num2>num3>num1:
    print(num2,"is greater")
else:
    print(num3,"is greater")
    
    
# check if a number is disible by 11 or not
num=int(input("Enter the number:"))
if num%11==0:
    print(num," is Divisible by 11")
else:
    print(num," is Not Divisible by 11")


# check if a number is disible by 2 & 5
num=int(input("Enter the number:"))
if num%2==0 and num%5==0:
    print(num," is Divisible by 2 and 5")
else:
    print(num," is Not Divisible ")

num=int(input("Enter the number:"))
string=str(num)
if string[::-1]==string:
    print("palindrome")
else:
    print("not a palindrome")

#printing numbers accoording to even or odd
even=[]
odd=[]
for i in range(1,11):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
