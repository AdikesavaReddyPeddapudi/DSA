Python 3.14.3 (tags/v3.14.3:323c59a, Feb  3 2026, 16:04:56) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={}
type(s)
<class 'dict'>
s
{}
s=set()
s
set()
type(s)
<class 'set'>
s={23,45,34,567,543,222,23}
s
{34, 567, 23, 45, 222, 543}
s.add(50)
s
{34, 50, 567, 23, 45, 222, 543}
s.remove(567)
s
{34, 50, 23, 45, 222, 543}
s.add(5.5)
s
{34, 50, 5.5, 23, 45, 222, 543}
s.add("Adi")
s
{34, 50, 5.5, 23, 'Adi', 45, 222, 543}
s.add(3+4i)
SyntaxError: invalid decimal literal
s.add(3+4j)
s
{5.5, (3+4j), 23, 222, 543, 34, 45, 50, 'Adi'}
s.add(True)
print(" set only accepts the immputable data types-int,str,tuple,complex")
 set only accepts the immputable data types-int,str,tuple,complex
print("it doesnot accepts list,dict")
it doesnot accepts list,dict
s.add(1)
s
{True, 5.5, (3+4j), 23, 222, 543, 34, 45, 50, 'Adi'}
s.update({2,3,4})
s
{True, 2, 3, 4, 5.5, (3+4j), 23, 222, 543, 34, 45, 50, 'Adi'}
s.pop()
True
s
{2, 3, 4, 5.5, (3+4j), 23, 222, 543, 34, 45, 50, 'Adi'}
s,pop(543)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    s,pop(543)
NameError: name 'pop' is not defined. Did you mean: 'pow'?
s.pop(543)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.pop(543)
TypeError: set.pop() takes no arguments (1 given)
s.remove(543)
s
{2, 3, 4, 5.5, (3+4j), 23, 222, 34, 45, 50, 'Adi'}
for i in s:
    print(i)

2
3
4
5.5
(3+4j)
23
222
34
45
50
Adi
s
{2, 3, 4, 5.5, (3+4j), 23, 222, 34, 45, 50, 'Adi'}
s.remove(4)
s
{2, 3, 5.5, (3+4j), 23, 222, 34, 45, 50, 'Adi'}
len(s)
10
a={5,6,7,2,3}
b=[2,9,8,5,1}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
b={2,9,8,5,1}
a
{2, 3, 5, 6, 7}
b
{1, 2, 5, 8, 9}
a+b
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a+b
TypeError: unsupported operand type(s) for +: 'set' and 'set'
a-b
{3, 6, 7}
a&b
{2, 5}
a|b
{1, 2, 3, 5, 6, 7, 8, 9}
{5}>a
False
>>> {5}<a
True
>>> {9}>a
False
>>> {9}<b
True
>>> a.disjoint(b)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.disjoint(b)
AttributeError: 'set' object has no attribute 'disjoint'. Did you mean: 'isdisjoint'?
>>> a.isdisjoint(b)
False
>>> a.union(b)
{1, 2, 3, 5, 6, 7, 8, 9}
>>> a.intersection(b)
{2, 5}
>>> b.intersection(a)
{2, 5}
>>> len(a)
5
>>> max(b)
9
>>> mun(b)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    mun(b)
NameError: name 'mun' is not defined. Did you mean: 'min'?
>>> min(b)
1
>>> a.sort
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    a.sort
AttributeError: 'set' object has no attribute 'sort'
>>> sorted(a)
[2, 3, 5, 6, 7]
