#LIST
L=[1,4,7.4,"sai ram"]
L
[1, 4, 7.4, 'sai ram']
-----------------------------------------
#indexing
L[3]
'sai ram'
------------------------------------------
#slicing--prefers only forward direction
L[2:3]
[7.4]
L[2:4]
[7.4, 'sai ram']
L[0:]
[1, 4, 7.4, 'sai ram']
L[:4]
[1, 4, 7.4, 'sai ram']
L[-1]
'sai ram'
-------------------------------------------
#reverse
L[::-1]
['sai ram', 7.4, 4, 1]
L1
[400, 300, 200, 100, 6, 4, 2, 1, 1, 1]
L1[-9:8]
[300, 200, 100, 6, 4, 2, 1]
L1[-5:5]
[]
L1[-2:2]
[]
L1[-10:0]
[]
L1[::-5]
[1, 6]
L1[::-3]
[1, 2, 100, 400]
-----------------------------------------------
list methods:
append():adds one element at the end of the list--l.append(2)
extend():adds multiple elements at a time--l.extend([5,6])
insert():inserts at a defined index--l.insert(2,9)
remove():deletes the specified value--l.remove(6)
pop():deletes the value in the specified position ---l.pop(2)
clear():returns an empty list
sort():sorts the list in ascending order--l.sort()
count():returns the count of a particular element--l.count(9)
reverse():returns the list in the reverse order--l.reverse()
copy():copies the existing list--l1=l.copy()
L=[1,4,1,1,6,4,1,2]
L
[1, 4, 1, 1, 6, 4, 1, 2]
L.append(400)
L
[1, 4, 1, 1, 6, 4, 1, 2, 400]
L.extend(100,200,300)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    L.extend(100,200,300)
TypeError: list.extend() takes exactly one argument (3 given)
L.extend([100,200,300])
L
[1, 4, 1, 1, 6, 4, 1, 2, 400, 100, 200, 300]
L.insert(9,9)
L
[1, 4, 1, 1, 6, 4, 1, 2, 400, 9, 100, 200, 300]
L.remove(9)
L
[1, 4, 1, 1, 6, 4, 1, 2, 400, 100, 200, 300]
L.remove(4)
L
[1, 1, 1, 6, 4, 1, 2, 400, 100, 200, 300]
L.pop(2)
1
L
[1, 1, 6, 4, 1, 2, 400, 100, 200, 300]
L.count(1)
3
L.sort()
L
[1, 1, 1, 2, 4, 6, 100, 200, 300, 400]
L.reverse()
L
[400, 300, 200, 100, 6, 4, 2, 1, 1, 1]
L1[]=L.copy()
SyntaxError: invalid syntax
L1=L.copy()
L1
[400, 300, 200, 100, 6, 4, 2, 1, 1, 1]
-----------------------------------------------------
List Comprehension--(creat list using existing list)
str=[elements for elements in "GREAT AMBASSADOR"]
print(str)   #---->['G', 'R', 'E', 'A', 'T', ' ', 'A', 'M', 'B', 'A', 'S', 'S', 'A', 'D', 'O', 'R']


numbers=[2**x for x in range(1,20)]
print(numbers)  #---->[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288]

numbers=[x for x in range(100,201,20)]
print(numbers)  #---->[100, 120, 140, 160, 180, 200]

numbers=[x for x in range(2,51,2) if(x<41)]
print(numbers)   #---->[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]

places=["Hyderabad","Kakinada","Vizag","Kolkata"]
city=[]
for i in places:
    if "K" in i:
        city.append(i)
print(city)    #---->['Kakinada', 'Kolkata']
--------------------------------------------------------
--------------------------------------------------------
#SET
*Dupicates are not allowed
*Unordered
*No index
s={10,20,30,40,20,30}
s
{40, 10, 20, 30}
-------------------------------------------------------
#set methods
add():Adds an element to the set-----s.add(2)
update():Adds more than one element----s.update({9,99})
remove() and discard():Both are same but remove return error if the element is not in the list---s.discard(2) and s.remove(2)
Union():returns the union of 2 sets----s1|s2 or s1.union(s2)
Intersection:returns the intersection of 2 sets----s1&s2 or s1.intersection(s2)
Difference:returns the diff of 2 sets---s1-s2 or s1.differnce(s2)
issuperset():checks whether all the elements in s1 present in s2
symmetric_difference():returns the elements which are not common in 2 sets---s1.symmetric_difference(s2)
s.add(50)
s
{40, 10, 50, 20, 30}
s.update({60,70})
s
{70, 40, 10, 50, 20, 60, 30}
s.discard(70)
s
{40, 10, 50, 20, 60, 30}
s.remove(70)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s.remove(70)
KeyError: 70
s.remove(60)
s
{40, 10, 50, 20, 30}
s1={1,2,3,4,5}
s2={2,4,6}
s1.union(s2)
{1, 2, 3, 4, 5, 6}
s1.intersection(s2)
{2, 4}
s1.difference(s2)
{1, 3, 5}
s1-s2
{1, 3, 5}
s1.issuperset(s2)
False
s1.symmetric_difference(s2)
{1, 3, 5, 6}
-------------------------------------------------------------
#TUPLE
*Ordered
*Unchangeble
*Cant include items
*Duplication is allowed
-------------------------------------
#Tuple initialization
T=1,2,3
or
T=(1,2,3)
--------------------------------------
#Tuple methods
count():returns the count of a particular element--T.count(9)
index():returns the elements position---T.index(2)
T=(10,20,30,40)
T
(10, 20, 30, 40)
T.count(10)
1
T.index(20)
1
--------------------------------------
#list to tuple
l=[10,20,30,40,50]
T=tuple(l)
T
(10, 20, 30, 40, 50)
--------------------------------------
#nested tuple
t1=('keep','working')
t2=(10,20)
t3=(t1,t2)
t3
(('keep', 'working'), (10, 20))
-------------------------------------------------------------
-------------------------------------------------------------
#DICTIONARY
*It contains elements with two units  keys and values
*keys must be unique
d={1:'one',2:'two'}
d
{1: 'one', 2: 'two'}
-------------------------------------------------------------
#Dictionary methods
d.keys():prints the keys in the given dictionary
d.keys()
dict_keys([1, 2])
d.values():prints the values in the given dictionary
d.values()
dict_values(['one', 'two'])
d.items():prints all pairs in the dictionary
d.items()
dict_items([(1, 'one'), (2, 'two')])
d.update():add one or more items------d.update({3:'Three'})
d.update({3:'Three'})
d
{1: 'one', 2: 'two', 3: 'Three'}
d.pop():fetch and remove------d.pop(2)
d.pop(2)
'two'
d
{1: 'one', 3: 'Three'}
d.popitem():fetch and remove recently added item
d.popitem()
(3, 'Three')
d
{1: 'one'}
d.setdefault():if key is not in dic,will be added or nothing will be done
d.setdefault(4,'four')
'four'
d
{1: 'one', 4: 'four'}
d.setdefault(5)  --------->value can be optional
d
{1: 'one', 4: 'four', 5: None}
--------------------------------------------------------------
#creating dic from list,tuple
---#dic from list
l=[10,20,30]
d.fromkeys(l)
{10: None, 20: None, 30: None}
d.fromkeys(l,'Hi')
{10: 'Hi', 20: 'Hi', 30: 'Hi'}
---#dic from tuple
d.fromkeys(t,'Hi')
{10: 'Hi', 20: 'Hi', 30: 'Hi'}
