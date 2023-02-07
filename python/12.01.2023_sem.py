Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def rsum():
    s = 1
    e = 1
    while True:
        yield s
        e /= i^2
        s += e
        i += 1

        
a = rsum()
a
<generator object rsum at 0x000001F345BB6D50>
next(a)
1
def rsum():
    s = 1
    e = 1
    i = 1
    while True:
        yield s
        e /= i^2
        s += e
        i += 1

        
next(a)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    next(a)
  File "<pyshell#6>", line 6, in rsum
    e /= i^2
UnboundLocalError: local variable 'i' referenced before assignment
a = rsum()
a
<generator object rsum at 0x000001F345BB7990>
next(a)
1
def rsum():
    s = 1
    
    i = 1
    while True:
        yield s
        
        s = 1 / i ** 2
        i += 1

        
a = rsum()
next(a)
1
next(a)
1.0
next(a)
0.25
next(a)
0.1111111111111111
next(a)
0.0625
next(a)
0.04
b = (next(a) for i)
SyntaxError: invalid syntax
list(b)[-1]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    list(b)[-1]
NameError: name 'b' is not defined
b = (next(a) for i in range(10000))
c = list(b)
c

c

c[-1]
9.990007495003124e-09

def fib(m,n):
    f1 = 1
    f2 = 1
    if m <= 2:
        yield 1
        if m == 1:
            yield 1
    for i in range(m, m + n + 1):
        f = f1 + f2
        f1 = f2
        f2 = f
        yield f

        
fib
<function fib at 0x000001F345C06560>
next(fib)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    next(fib)
TypeError: 'function' object is not an iterator
def fib(m,n):
    f1 = 1
    f2 = 1
    if m == 2:
        yield 1
        n -= 1
    if m == 1:
        yield 1
            if n > 1:
                yield 1
        n -= 2
    for i in range(m, m + n + 1):
        f = f1 + f2
        f1 = f2
        f2 = f
        yield f
        
SyntaxError: unexpected indent

def fib(m,n):
    f1 = 1
    f2 = 1
    if n < 1:
        return
    if m == 2:
        yield 1
        n -= 1
    if m == 1:
        yield 1
            if n > 1:
                yield 1
        n -= 2
    for i in range(m, m + n + 1):
        f = f1 + f2
        f1 = f2
        f2 = f
        yield f
        
SyntaxError: unexpected indent
def fib(m,n):
    f1 = 1
    f2 = 1
    if n < 1:
        return
    if m == 2:
        yield 1
        n -= 1
    if m == 1:
        yield 1
        if n > 1:
                yield 1
        n -= 2
    for i in range(m, m + n + 1):
        f = f1 + f2
        f1 = f2
        f2 = f
        yield f

        
def fib(m,n):
    f1 = 1
    f2 = 1
    i = 2
    if n < 1:
        return
    for i in range(2):
        if i >= m
             yield 1
    for i in range(2, m + n):
        f = f1 + f2
        f1 = f2
        f2 = f
       if i >= m:
           
SyntaxError: expected ':'
def fib(m,n):
    f1 = 1
    f2 = 1
    i = 2
    if n < 1:
        return
    for i in range(2):
        if i >= m:
             yield 1
    for i in range(2, m + n):
        f = f1 + f2
        f1 = f2
        f2 = f
       if i >= m:
           
SyntaxError: unindent does not match any outer indentation level
def fib(m,n):
    f1 = 1
    f2 = 1
    i = 2
    if n < 1:
        return
    for i in range(2):
        if i >= m:
             yield 1
    for i in range(2, m + n):
        f = f1 + f2
        f1 = f2
        f2 = f
        if i >= m:
            yield 1

            
def turtle():
    coor = [0, 0]
    n = 0
    while True:
        s = yield coor
        if s == "r":
            n += 1
        elif s == "1":
            n -= 1
        elif s == "f":
            n %= 4
            if n = 0:
                
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
def turtle():
    coor = [0, 0]
    n = 0
    while True:
        s = yield coor
        if s == "r":
            n += 1
        elif s == "1":
            n -= 1
        elif s == "f":
            n %= 4
            if n == 0:
                coor[1] += 1
            if n == 1:
                coor[1] += 1
            if n == 2:
                coor[1] += 1
            if n == 3:
                coor[1] += 1

                
t = turtle()
t.send("f")
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    t.send("f")
TypeError: can't send non-None value to a just-started generator
t.send(None)
[0, 0]
t.send("f")
[0, 1]
t.send("r")
[0, 1]
t.send("f")
[0, 2]
t.send("l")
[0, 2]
def turtle():
    coor = [0, 0]
    n = 0
    while True:
        s = yield coor
        if s == "r":
            n += 1
        elif s == "1":
            n -= 1
        elif s == "f":
            n %= 4
            if n == 0:
                coor[1] += 1
            if n == 1:
                coor[0] += 1
            if n == 2:
                coor[1] -= 1
            if n == 3:
                coor[0] -= 1

                
t = turtle()
t.send(None)
[0, 0]
t.send("f")
[0, 1]
t.send("l")
[0, 1]
class Undead(Exception):
    pass
class Skeleton(Undead):
    
SyntaxError: invalid syntax
class Undead(Exception):
    pass

class Skeleton(Undead):
    
SyntaxError: invalid syntax
class Undead(Exception):
    pass

class Skeleton(Undead):
    pass

class Zombie(Undead):
    pass

class Ghoul(Undead):
    pass

class Undead(Exception):
    pass

class Skeleton(Undead):
    pass

class Zombie(Undead):
    pass

class Ghoul(Undead):
    pass
SyntaxError: invalid syntax
def necro(n):
    if n % 3 == 0:
        raise Skeleton
    if n % 3 == 1:
        raise Zombie
    if n % 3 == 0:
        raise Undead

    
for i in range(2,7):
    try:
        necro(i)
        except Undead:
            
SyntaxError: invalid syntax
for i in range(2,7):
    try:
        necro(i)
    except Undead:
        print("Undead")
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")

        
Undead
Undead
Undead
class Undead(Exception):
    pass

class Skeleton(Undead):
    pass

class Zombie(Undead):
    pass

class Ghoul(Undead):
    pass
    for i in range(2,7):
    try:
        necro(i)
    except Undead:
        print("Undead")
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
        
SyntaxError: invalid syntax



class Skeleton(Undead):
    pass

class Zombie(Undead):
    pass

class Ghoul(Undead):
    pass
    for i in range(2,7):
    try:
        necro(i)
    except Undead:
        print("Undead")
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
        
SyntaxError: invalid syntax
class Skeleton(Undead):
    pass

class Zombie(Undead):
    pass

class Ghoul(Undead):
    pass
    for i in range(2,7):
    try:
        necro(i)
    except Undead:
        print("Undead")
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
class Skeleton(Undead):
    pass

class Zombie(Undead):
    pass

class Ghoul(Undead):
    pass

def spis
SyntaxError: invalid syntax
def spis()
SyntaxError: expected ':'
def spis():
    a = 1
    b = 1

    

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
filter(lambda (a)):
    
SyntaxError: invalid syntax
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
filter(lambda x: if x < 5):
    
SyntaxError: multiple statements found while compiling a single statement
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
print(*filter(lambda x: True if x <= 5 else False, a))
1 1 2 3 5
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(*filter(lambda x: True if x1 == x2 else False, a, b))
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    print(*filter(lambda x: True if x1 == x2 else False, a, b))
TypeError: filter expected 2 arguments, got 3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(*filter(lambda x: True if x1 == x2 else False, a, b))
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    print(*filter(lambda x: True if x1 == x2 else False, a, b))
TypeError: filter expected 2 arguments, got 3
print(list(set(a) & set(b)))
[1, 2, 3, 5, 8, 13]
{1: 24; 2 : 4}
SyntaxError: invalid syntax
a = {1: 24, 2 : 4}
b = {3: 5, 5: 2}
print(list(set(a) + set(b)))
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    print(list(set(a) + set(b)))
TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(list(set(a), set(b)))
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    print(list(set(a), set(b)))
TypeError: list expected at most 1 argument, got 2
print(list(a, b))
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    print(list(a, b))
TypeError: list expected at most 1 argument, got 2
print(a, b)
{1: 24, 2: 4} {3: 5, 5: 2}
print(a + b)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    print(a + b)
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print(dict(a), dict(b))
{1: 24, 2: 4} {3: 5, 5: 2}
print(update(a, b))
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    print(update(a, b))
NameError: name 'update' is not defined
c = dict()
c.update(a)
c.update(b)
c
{1: 24, 2: 4, 3: 5, 5: 2}
d = {**a, **b}
d
{1: 24, 2: 4, 3: 5, 5: 2}
a.items()
dict_items([(1, 24), (2, 4)])
d = {a,b}
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    d = {a,b}
TypeError: unhashable type: 'dict'
c
{1: 24, 2: 4, 3: 5, 5: 2}
c.values()
dict_values([24, 4, 5, 2])
sorted(c.values())
[2, 4, 5, 24]
sorted(c.values())[-3:]
[4, 5, 24]
sorted(c)
[1, 2, 3, 5]
c.items()
dict_items([(1, 24), (2, 4), (3, 5), (5, 2)])
import operator
operator.itemgetter()
Traceback (most recent call last):
  File "<pyshell#167>", line 1, in <module>
    operator.itemgetter()
TypeError: itemgetter expected 1 argument, got 0
sorted(c.items(), key = operator.itemgetter())
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    sorted(c.items(), key = operator.itemgetter())
TypeError: itemgetter expected 1 argument, got 0
sorted(c.items(), key = operator.itemgetter(1))
[(5, 2), (2, 4), (3, 5), (1, 24)]
dict(sorted(c.items(), key = operator.itemgetter(1)))
{5: 2, 2: 4, 3: 5, 1: 24}
dict(sorted(c.items(), key = operator.itemgetter(1), reverse = True))
{1: 24, 3: 5, 2: 4, 5: 2}
d = dict(sorted(c.items(), key = operator.itemgetter(1), reverse = True))
d.keys()
dict_keys([1, 3, 2, 5])
list(d.keys()[:3])
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    list(d.keys()[:3])
TypeError: 'dict_keys' object is not subscriptable
list(d.keys())[:3]
[1, 3, 2]
def binsearch(a, X):
    Xdown = 0
    Xup = len(X) - 1
    Xmid = Xup // 2
    while a != X[Xmid]:
        if a > X[Xmid]:
            Xdown = Xmid + 1
            Xmid += (Xup + 1 - Xdown) // 2
        else:
            Xup = Xmid
            Xmid -= (Xup + 1 - Xdown) // 2
        if Xup - Xdown == 1:
            if Xup == a or Xdown == a:
                return True
            else return False
            
SyntaxError: expected ':'
def binsearch(a, X):
    Xdown = 0
    Xup = len(X) - 1
    Xmid = Xup // 2
    while a != X[Xmid]:
        if a > X[Xmid]:
            Xdown = Xmid + 1
            Xmid += (Xup + 1 - Xdown) // 2
        else:
            Xup = Xmid
            Xmid -= (Xup + 1 - Xdown) // 2
        if Xup - Xdown == 1:
            if Xup == a or Xdown == a:
                return True
            else: return False

            
a = [x for x in range(100)]
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
binsearch(50, a)
True
binsearch(1000, a)
False
a = [x for x in range(0, 100, 3)]
a
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
def binsearch(a, X):
    Xdown = 0
    Xup = len(X) - 1
    Xmid = Xup // 2
    while a != X[Xmid]:
        if a > X[Xmid]:
            Xdown = Xmid + 1
            Xmid += (Xup + 1 - Xdown) // 2
        else:
            Xup = Xmid
            Xmid -= (Xup + 1 - Xdown) // 2
        if Xup - Xdown == 1:
            if X[Xup] == a or X[Xdown] == a:
                return True
            else: return False

            
a = [x for x in range(0, 100, 3)]
a
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
binsearch(30, a)

