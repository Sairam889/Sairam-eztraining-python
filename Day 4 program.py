#CALCULATING PRODUCT PRICE FOR 5 units
old={'rice':160,'daal':120,'oil':150}
new={product:price*5 for (product,price)in
     old.items()}
print(new)


#WITH CHECKS
real={'sam':24,'angel':18,'kumar':35}
now={name:age for (name,age) in real.items()
     if age>20}
print(now)

#D={n:n*n for n in range(1,5)}
print(d)

#CREATE A LIST WITH 8 CUSTOMERS NAMES.DISPLAY A DICTIONARY WHICH HAS CUSTOMER NAMES ALONG WITH DISCOUNTS FOR THEM FROM A PARTICULAR SHOP
import random
cust=["prabhas","brownie","dad"]
cust_dict={names:random.randint(1,100) for names in cust}
print(cust_dict)


#GET 1 STRING AS A INPUT ALONG  WITH A CHARACTER FIND OUT AND DISPLAY WHETHER THE PARTICULAR CHARACTER IS PRESENT OR NOT
#CHECK WEATHER THE STRING IS PALANDROME OR NOT
#CHECK STRING CONTAINS SPACE OR NOT IF YES THEN COUNT NUM OF SPACES AND PRINT

#CREATE 2 LIST...1ST STUDENTS NAMES AND 2ND LIST MUST HAS TOTAL SUBJCTS AND MARKS SHOULD BE 1 TO 100...STUDENT % AS VALUES..
names=['prabhas','brownie','tahseen','meghana','sushmitha']
marks=[200,300,400,460,500]
d={names:(marks/5) for (names,marks) in zip(names,marks)}
print(d)
 

STRINGS:
n="hi i'am "sylvia""
SyntaxError: invalid syntax
n="hi i'am"
n
"hi i'am"
nm='hi i'am'
SyntaxError: unterminated string literal (detected at line 1)
m='hi i\'am'
m
"hi i'am"


#GET 1 STRING AS A INPUT ALONG  WITH A CHARACTER FIND OUT AND DISPLAY WHETHER THE PARTICULAR CHARACTER IS PRESENT OR NOT
n=input("enter a string:")
chr=input("enter a charcter:")
chr='s'
if n in chr:
    print("yes")
else:
    print("no")

OUTPUT:
Enter a string:hello
enter a character:1
no


#CHECK WEATHER THE STRING IS PALANDROME OR NOT
string=input("Enter a string:")
m=string[::-1]
if m==string:
    print("palindrome")
else:
        print("not palindrome")

OUTPUT:
Enter the string:malayalam
palindrome


#CHECK STRING CONTAINS SPACE OR NOT IF YES THEN COUNT NUM OF SPACES AND PRINT
