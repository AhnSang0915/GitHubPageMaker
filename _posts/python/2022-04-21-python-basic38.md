---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 제너레이터 사용하기
date: 2022-04-20 13:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 제너레이터 사용하기

<br>
<br>
제너레이터는 이터레이터를 생서해주는 함수다. 이터레이터는 클래스에 \__iter__, \__next__ 또는 \__getitem__ 메서드를 구현해야 하지만 제너레이터는 함수 안에서 yield라는 키워드만 사용하면 끝난다. 그래서 제너레이터는 이터레이터보다 훨씬 간단하게 작성할 수 있다. 제너레이터는 발생자 라고 부르기도 한다.

---

## 1.제너레이터와 yield 알아보기
<br>
<br>
함수 안에서 yield를 사용하면 함수는 제너레이터가 되며 yield에는 값(변수)을 지정한다.

- yield 값

yield를 사용해서 제너레이터를 만들고 for 반복문에 0, 1, 2숫자 세 개를 출력해 보자.

for 반복문에 number_generator()를 지정해서 값을 출력해보면 yield에 지정했던 0, 1, 2가 나온다. 이터레이터와 사용 방법이 똑같다.

~~~python

def number_generator():
    yield 0
    yield 1
    yield 2
 
for i in number_generator():
    print(i)

# 실행 결과
0
1
2

~~~

### 제너레이터 객체가 이터레이터인지 확인하기
<br>
<br>
그럼 number_generator 함수로 만든 객체가 정말 이터레이터인지 살펴보자. 다음과 같이 dir 함수로 메서드 목록을 확인한다. number_generator 함수를 호출하면 제너레이터 객체(generator object)가 반환된다. 이 객체를 dir 함수로 살펴보면 이터레이터에서 볼 수 있는 __iter__, __next__ 메서드가 들어있다.

~~~python

def number_generator():
    yield 0
    yield 1
    yield 2
 
for i in number_generator():
    print(i)

g = number_generator()
g
<generator object number_generator at 0x03A190F0>
dir(g)
['__class__', '__del__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__name__', '__ne__', '__new__', '__next__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'gi_code', 'gi_frame', 'gi_running', 'gi_yieldfrom', 'send', 'throw']

~~~

실제로 제너레이터 객체의 __next__를 호출해보면 숫자 0, 1, 2가 나오다가 StopIteration 예외가 발생한다.

~~~python

g.__next__()
0
g.__next__()
1
g.__next__()
2
g.__next__()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    g.__next__()
StopIteration

~~~

위코드를 보면 제너레이터와 이터레이터의 동작이 같은걸 알 수 있다. 이렇게 yield를 사용해 간단한게 이터레이터를 구현할 수 있다. 단, 이터레이터는 \__next__메서드 안에서 직접 return으로 값을 반환했지만 제너레이터는 yield에 지정한 값이 \__next__ 메서드(next 함수)의 반환값으로 나온다. 또한, 이터레이터는 raise로 StopIteration 예외를 직접 발생시켰지만 제너레이터는 함수의 끝까지 도달하면 StopIteration 예외가 자동으로 발생한다. 제너레이터는 제너레이터 객체에서 \__next__ 메서드를 호출할 때마다 함수 안의 yield까지 코드를 실행하며 yield에서 값을 발생시킨다(generate). 그래서 이름이 제너레이터(generator)이다.


### for와 제너레이터
<br>
<br>

for 반복문과 제너레이터를 살펴보자. for 반복문은 반복할 때마다 \__next__를 호출하므로 yield에서 발생시킨 값을 가져온다. 그리고 StopIteration 예외가 발생하면 반복을 끝낸다.
참고로 제너레이터 객체에서 \__iter__를 호출하면 self를 반환하므로 같은 객체가 나온다(제너레이터 함수 호출 > 제너레이터 객체 > \__iter__는 self 반환 > 제너레이터 객체).
(yield는 생산하다라는 뜻과 함께 양보하다라는 뜻도 가지고 있다. 즉, yield를 사용하면 값을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보한다. 따라서 yield는 현재 함수를 잠시 중단하고 함수 바깥의 코드가 실행되도록 만든다.)

### yield의 동작 과정 알아보기
<br>
<br>

yield의 동작 과정을 알아보기 위해 for반복문 대신 next함수로 \__next__메서드를 직접 호출해 보자.

- 변수 = next(제너레이터객체)

~~~python

def number_generator():
    yield 0    # 0을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 1    # 1을 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
    yield 2    # 2를 함수 바깥으로 전달하면서 코드 실행을 함수 바깥에 양보
 
g = number_generator()
 
a = next(g)    # yield를 사용하여 함수 바깥으로 전달한 값은 next의 반환값으로 나옴
print(a)       # 0
 
b = next(g)
print(b)       # 1
 
c = next(g)
print(c)       # 2

~~~

yield를 사용하여 바깥으로 전달한 값은 next 함수(\__next__ 메서드)의 반환값으로 나온다고 했다. 따라서 next(g)의 반환값을 출력해보면 yield에 지정한 값 0, 1, 2가 차례대로 나옵니다. 즉, 제너레이터 함수가 실행되는 중간에 next로 값을 가져온다.

### 제너레이터와 return
<br>
<br>
제너레이터는 함수 끝까지 도달하면 StopIteration 예외가 발생한다. 마찬가지로 return도 함수를 끝내므로 return을 사용해서 함수 중간에 빠져나오면 StopIteration 예외가 발생한다.

특히 제너레이터 안에서 return에 반환값을 지정하면 StopIteration 예외의 에러 메시지로 들어간다.

~~~python

def one_generator():
    yield 1
    return 'return에 지정한 값'
 
try:
    g = one_generator()
    next(g)
    next(g)
except StopIteration as e:
    print(e)    # return에 지정한 값

#실행 결과
return에 지정한 값

~~~

---

## 2.제너레이터 만들기
<br>
<br>
range(횟수)처럼 동작을 하는 제너레이터를 만들어 보자. 
제너레이터 안에서 변수n을 만들고 초기값으로 0을 저장한다. 그리고 while n < stop:과 같이 반복을 끝낼 숫자보다 작을 때 반복하도록 만든다. 반복문 안에서는 yield n으로 숫자를 바깥으로 전달한 뒤 n을 1 증가시키게 한다. 여기서 stop에 3이들어가기 떄문에 for 반복문도 3번 반복한다.

~~~python

def number_generator(stop):
    n = 0              # 숫자는 0부터 시작
    while n < stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때 반복
        yield n        # 현재 숫자를 바깥으로 전달
        n += 1         # 현재 숫자를 증가시킴
 
for i in number_generator(3):
    print(i)

# 실행 결과
0
1
2

~~~

next 함수(\__next__ 메서드)도 3번 사용할 수 있다.

~~~python

g = number_generator(3)
next(g)
0
next(g)
1
next(g)
2
next(g)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    next(g)
StopIteration

~~~

### yield에서 함수 호출하기
<br>
<br>

yield에 함수(메서드)를 호출해보자.
yield i.upper()와 같이 yield에서 함수(메서드)를 호출하면 해당 함수의 반환값을 바깥으로 전달한다. upper는 호출했을 때 대문자로 된 문자열을 반환하므로 yield는 이 문자열을 바깥으로 전달한다. 즉, yield에 무엇을 지정하든 결과만 바깥으로 전달한다(함수의 반환값, 식의 결과).

~~~python

def upper_generator(x):
    for i in x:
        yield i.upper()    # 함수의 반환값을 바깥으로 전달
 
fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
for i in upper_generator(fruits):
    print(i)

# 실행 결과
APPLE
PEAR
GRAPE
PINEAPPLE
ORANGE

~~~


---

## 3.yield from으로 값을 여러 번 바깥으로 전달하기
<br>
<br>
값을 여러 번 바깥으로 전달할 때는 for 또는 while 반복문으로 반복하면서 yield를 사용했다. 아래 코드는 리스트의 요소를 바깥으로 전달한다.

~~~python

def number_generator():
    x = [1, 2, 3]
    for i in x:
        yield i
 
for i in number_generator():
    print(i)

#실행 결과
1
2
3
~~~

위와 같은 경우엔 매번 반복문을 사용하지 않고, yield from을 사용하면 된다. yield from에는 반복 가능한 객체, 이터레이터, 제너레이터 객체를 지정한다.

- yield from 반복가능한객체
- yield from 이터레이터
- yield from 제너레이터객체

그럼 yield from에 리스트를 지정해서 숫자 1, 2, 3을 바깥으로 전달해 보자. yield from x와 같이 yield from에 리스트(반복 가능한 객체)를 지정했다. 이렇게 하면 리스트에 들어있는 요소를 한 개씩 바깥으로 전달한다. 즉, yield from을 한 번 사용하여 값을 세 번 바깥으로 전달한다. 따라서 next 함수(\__next__ 메서드)를 세 번 호출할 수 있다.

~~~python

def number_generator():
    x = [1, 2, 3]
    yield from x    # 리스트에 들어있는 요소를 한 개씩 바깥으로 전달
 
for i in number_generator():
    print(i)

# 실행 결과
1
2
3

~~~

~~~python

>>> g = number_generator()
>>> next(g)
1
>>> next(g)
2
>>> next(g)
3
>>> next(g)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    next(g)
StopIteration

~~~

### yield from에 제너레이터 객체 지정하기
<br>
<br>
yield from에 제너레이터 객체를 지정해보자. 제너레이터 number_generator는 매개변수로 받은 숫자 직전까지 숫자를 만들어낸다. three_generator에서는 yield from number_generator(3)과 같이 yield from에 제너레이터 객체를 지정했다.number_generator(3)은 숫자를 세 개를 만들어내므로 yield from number_generator(3)은 숫자를 세 번 바깥으로 전달한다. 따라서 for 반복문에 three_generator()를 사용하면 숫자를 세 번 출력한다(next 함수 또는 __next__ 메서드도 세 번 호출 가능).

~~~python

def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1
 
def three_generator():
    yield from number_generator(3)    # 숫자를 세 번 바깥으로 전달
 
for i in three_generator():
    print(i)

#실행 결과
0
1
2

~~~

### 제너레이터 표현식
<br>
<br>
리스트 표현식을 사용할 때 [ ](대괄호)를 사용했다. 같은 리스트 표현식을 ( )(괄호)로 묶으면 제너레이터 표현식이 된다. 리스트 표현식은 처음부터 리스트의 요소를 만들어내지만 제너레이터 표현식은 필요할 때 요소를 만들어내므로 메모리를 절약할 수 있다.

- (식 for 변수 in 반복가능한객체)

~~~python

>>> [i for i in range(50) if i % 2 == 0]
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
>>> (i for i in range(50) if i % 2 == 0)
<generator object <genexpr> at 0x024F02A0>

~~~

---


### 예제1
<br>
<br>
다음 소스 코드에서 words.txt 파일을 한 줄씩 읽은 뒤 내용을 함수 바깥에 전달하는 제너레이터를 작성하세요. 파일의 내용을 출력할 때 파일에서 읽은 \n은 출력되지 않아야 합니다(단어 사이에 줄바꿈이 두 번 일어나면 안 됨).

~~~python

# words.txt
compatibility
experience
photography
spotlight


def file_read():
    with open('words.txt') as file:
        ______________________                          
        ...
        ______________________                           
 
for i in file_read():
    print(i)
                                                     
 

#실행 결과
compatibility
experience
photography
spotlight

~~~


답

~~~python

while True:
    line = file.readline()
    if line == '':
        break
    yield line.strip('\n')

~~~




### 예제2
<br>
<br>
표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 10~1000, 두 번째 입력 값의 범위는 100~1000이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 다음 소스 코드에서 첫 번째 정수부터 두 번째 정수 사이의 소수(prime number)를 생성하는 제너레이터를 만드세요. 소수는 1과 자기자신만으로 나누어 떨어지는 1보다 큰 양의 정수입니다.

~~~python

________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________

start, stop = map(int, input().split())
 
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')

#입력
50 100
#결과
<class 'generator'>
53 59 61 67 71 73 79 83 89 97 
#입력
950 1000
#결과
<class 'generator'>
953 967 971 977 983 991 997 

~~~

답

~~~python

def isPrime(number): # 아래 prime_number_generator함수에서 i의 값이 매개변수로 들어간다.
    if number == 1:
        return False #소수는 1보다 큰 자연수 중 1과 자기자신만을 약수로 가지는 수이다. 
                     #1은 1보다 크지 않기 때문에 소수가 아니다.
    for i in range(2, number): # 2부터 전달된 number의 값까지 i에 전달하고 
        if number % i == 0: # 전달된 number를 number전의 수까지로 나누어 0이 되면 소수가 아니다.
            return False
    return True

def prime_number_generator(start, stop):
    for i in range(start, stop+1):
        if isPrime(i):
            yield i

~~~



