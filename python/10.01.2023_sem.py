Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
[DEBUG ON]
[DEBUG OFF]
a
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a
NameError: name 'a' is not defined
try:
    a = 10/0
except Exception:
    a = 0

a
0
try:
    raise ZeroDivisionError
except ZeroDivisionError:
    a = 100500

    
a
100500
try:
    raise ZeroDivisionError("div by 0")
except ZeroDivisionError as E:
    a = 100500
    print(E)

    
div by 0

try:
    raise ZeroDivisionError("div by 0")
except ZeroDivisionError as E:
    a = 100500
    D = E

    
d
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'D'?
D
ZeroDivisionError('div by 0')
E
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    E
NameError: name 'E' is not defined
try:
    raise ZeroDivisionError("div by 0")
except EOFError as E:
    a = 100500
    D = E
else:
    print("QQ")
finally:
    print("fin")

    
fin
Traceback (most recent call last):
  File "<pyshell#28>", line 2, in <module>
    raise ZeroDivisionError("div by 0")
ZeroDivisionError: div by 0
raise Exception("QQ")
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    raise Exception("QQ")
Exception: QQ
for i in range(10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
dir(range)
['__bool__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index', 'start', 'step', 'stop']
iter(range(10))
<range_iterator object at 0x000002AE2DBA6C30>
a = iter(range(10))
dir(a)
['__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__length_hint__', '__lt__', '__ne__', '__new__', '__next__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__', '__subclasshook__']
next(a)
0
next(a)
1
next(a)
2
next(a)
3
next(a)
4
next(a)
5
next(a)
6
next(a)
7
next(a)
8
next(a)
9
next(a)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    next(a)
StopIteration
next(a)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    next(a)
StopIteration
for i in iter(range(10)):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
range(10)[2]
2
iter(range(10))[2]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    iter(range(10))[2]
TypeError: 'range_iterator' object is not subscriptable
for i, j in enumerate("QWERTY'):
                      
SyntaxError: unterminated string literal (detected at line 1)
for i, j in enumerate("QWERTY"):
                      print(i, j)

                    
0 Q
1 W
2 E
3 R
4 T
5 Y
for i, j range(len(S)):
                      
SyntaxError: invalid syntax
S = "QWERTY"
                      
for i, j range(len(S)):
                      
SyntaxError: invalid syntax
for i range(len(S)):
                      
SyntaxError: invalid syntax
for i in range(len(S)):
                      print(i)

                      
0
1
2
3
4
5
for i in range(len(S)):
                      print(i, S[i])

                      
0 Q
1 W
2 E
3 R
4 T
5 Y
reversed("QWERTY")
                      
<reversed object at 0x000002AE2DC6C340>
KeyboardInterrupt
list(reversed("QWERTY"))
                      
['Y', 'T', 'R', 'E', 'W', 'Q']
S = reversed("QWERTY")
                      
next(S)
                      
'Y'
next(S)
                      
'T'
for i in reversed("QWERTY")
                      
SyntaxError: expected ':'
for i in reversed("QWERTY"):
                      print(i, S[i])

                      
Traceback (most recent call last):
  File "<pyshell#75>", line 2, in <module>
    print(i, S[i])
TypeError: 'reversed' object is not subscriptable
for i in reversed("QWERTY"):
                      print(i)

                      
Y
T
R
E
W
Q
list(S)
                      
['R', 'E', 'W', 'Q']
list(S)
                      
[]
zip("123", "ABC", "abc")
                      
<zip object at 0x000002AE2BF126C0>
a = zip("123", "ABC", "abc")
                      
next(a)
                      
('1', 'A', 'a')
next(a)
                      
('2', 'B', 'b')
next(a)
                      
('3', 'C', 'c')
next(a)
                      
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    next(a)
StopIteration
list(a)
                      
[]
a = zip("123", "ABC", "abc")
                      
list(a)
                      
[('1', 'A', 'a'), ('2', 'B', 'b'), ('3', 'C', 'c')]
for i, j in zip("123", "ABC"):
                      print(i, j)

                      
1 A
2 B
3 C
map(int, input().split())
                      
12 45 64 12435
<map object at 0x000002AE2DD07C70>
a = map(int, input().split())
                      

a
                      
<map object at 0x000002AE2DD4CB50>
next(a)
                      
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    next(a)
StopIteration
a
                      
<map object at 0x000002AE2DD4CB50>
b = next(a)
                      
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    b = next(a)
StopIteration
type(a)
                      
<class 'map'>
type(b)
                      
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    type(b)
NameError: name 'b' is not defined
filter([1,2,3,4,5], lambda x: return x%2)
                      
SyntaxError: invalid syntax
help
                      
Type help() for interactive help, or help(object) for help about object.
filter(lambda x: x%2, [1,2,3,4,5])
                      
<filter object at 0x000002AE2DD4D5D0>
s = filter(lambda x: x%2, [1,2,3,4,5])
                      
next(s)
                      
1
next(s)
                      
3
a = [1, 2, 3]
                      
dir(a)
                      
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
import random


a = iter(random.randint(10), 5)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a = iter(random.randint(10), 5)
TypeError: Random.randint() missing 1 required positional argument: 'b'
a = iter(lambda: random.randint(10), 5)
a = iter(random.randint(0, 10), 5)
Traceback (most recent call last):
  File "<pyshell#113>", line 1, in <module>
    a = iter(random.randint(0, 10), 5)
TypeError: iter(v, w): v must be callable
a = iter(lambda: random.randint(0, 10), 5)
list(a)
[3, 2, 7, 1, 8, 7, 6, 10, 1, 10, 1]
a, b, c = 1, 2, 3
a, *b, c = range(0, 50)
a
0
c
49
b
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
a, a1, a2, a3, *b, c = range(0, 50)
a1
1
b
[4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
a3
3
*a, b = range(0, 50)
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
a = [ i for i in range(10)]
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = (i for i in range(10))
a
<generator object <genexpr> at 0x000002AE2DD19E70>
b = [a]
b
[<generator object <genexpr> at 0x000002AE2DD19E70>]
b = list(a)
b
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a
<generator object <genexpr> at 0x000002AE2DD19E70>
dir(a)
['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']
def gen1():
    print("l")
    yield 1
    yield 2
    yield 3

    
a = gen1
a
<function gen1 at 0x000002AE2DCB31C0>
a1 = next(a)
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    a1 = next(a)
TypeError: 'function' object is not an iterator
a1 = next(a)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    a1 = next(a)
TypeError: 'function' object is not an iterator
def gen1():
    print("первый вызов")
    for i in range(5):
        print(i, "yeld")
        yield i

        
list(a)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    list(a)
TypeError: 'function' object is not iterable
next(a)
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    next(a)
TypeError: 'function' object is not an iterator
a1
1
a1
1
a1 = next(a)
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    a1 = next(a)
TypeError: 'function' object is not an iterator
a = gen1()
a
<generator object gen1 at 0x000002AE2DD19E70>
a1 = next(a)
первый вызов
0 yeld
def gen1():
    print("первый вызов")
    for i in range(5):
        print(i, "yeld")
        yield i
        return 0

    
a
<generator object gen1 at 0x000002AE2DD19E70>
a1
0
list(a)
1 yeld
2 yeld
3 yeld
4 yeld
[1, 2, 3, 4]
def gen1():
    print("первый вызов")
    for i in range(5):
        print(i, "yeld")
        yield i
        return 0
        yield 100

        
list(a)
[]
def gen1():
   i = 0
   while True:
       i += 1
       yield i

list(a)
[]
list(gen)
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    list(gen)
NameError: name 'gen' is not defined. Did you mean: 'gen1'?
a = gen1()
list(a)
Traceback (most recent call last):
  File "<pyshell#171>", line 1, in <module>
    list(a)
MemoryError

da
a
s
d
gen1
a= list()

def gen2():
    yield from gen1(0)
    yield from gen1(10)

a = gen2()
Traceback (most recent call last):
  File "<pyshell#172>", line 1, in <module>
    a = gen2()
NameError: name 'gen2' is not defined. Did you mean: 'gen1'?
def gen2():
    yield from gen1(0)
    yield from gen1(10)

    
a = gen2()

next(a)
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    next(a)
  File "<pyshell#174>", line 2, in gen2
    yield from gen1(0)
TypeError: gen1() takes 0 positional arguments but 1 was given
def gen3():
    print("l")
    s = yield 100
    print("Пришло значение ", s)
    s = yield 0
    print("Пришло значение ", s)

    
a = gen3
a
<function gen3 at 0x000002AE2DD5D3F0>
a = gen3()
a
<generator object gen3 at 0x000002AE2DD1A030>
a1 = next(a)
l
a.send("QQ")
Пришло значение  QQ
0
a.send(123)
Пришло значение  123
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    a.send(123)
StopIteration
a = gen3()
a.send(None)
l
100
a1 = a.send(None)
Пришло значение  None
a.send(100)
Пришло значение  100
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    a.send(100)
StopIteration
a.send(100)
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    a.send(100)
StopIteration
