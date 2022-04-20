---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 이터레이터 사용하기
date: 2022-04-19 18:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 이터레이터 사용하기

<br>
<br>
이터레이터((iterator)는 값을 차례대로 꺼낼 수 있는 객체(object)이다. 지금까지 for반복문을 사용할 때 range를 사용했다. 만약 100번을 반복한다면 for i in range(100): 처럼 만들었다. 이 for 반복문을 설명할 때 for i in range(100):은 0부터 99까지 연속된 숫자를 만들어 낸다고 했는데, 사실은 숫자를 모두 만들어 내는 것이 아니라 0부터 99까지 값을 차례대로 꺼낼 수 있는 이터레이터를 하나만 만들어낸다. 이후 반복할 때만다 이터레이터에서 숫자를 하나씩 꺼내서 반복한다.

만약 연속된 숫자를 미리 만들면 숫자가 적을 때는 상관없지만 숫자가 아주 많을 때는 메모리를 많이 사용하게 되므로 성능에도 불리하다. 그래서 파이썬에서는 이터레이터만 생성하고 값이 필요한 시점이 되었을 때 값을 만드는 방식을 사용한다. 즉, 데이터 생성을 뒤로 미루는 것인데 이런 방식을 지연 평가(lazy evaluation)라고 한다.

참고로 이터레이터는 반복자라고 부르기도 한다.



---

## 1. 반복 가능한 객체 알아보기
<br>
<br>
이터레이터를 만들기 전에 먼저 반복 가능한 객체(iterable)에 대해 알아보자. 반복 가능한 객체는 말 그대로 반복할 수 있는 객체인데 우리가 흔히 사용하는 문자열, 리스트, 딕셔너리, 세트가 반복 가능한 객체이다. 즉, 요소가 여러 개 들어가있고, 한 번에 하나씩 꺼낼 수 있는 객체이다.

객체가 반복 가능한 객체인지 알아보는 방법은 객체에 \__iter__ 메서드가 들어있는지 확인해보면 된다. 다음과 같이 dir 함수를 사용하면 객체의 메서드를 확인할 수 있다.

- dir(객체)

리스트 [1, 2, 3]을 dir로 살펴보면 \__iter__ 메서드가 들어있습니다. 이 리스트에서 \__iter__를 호출해보면 이터레이터가 나온다.

~~~python

dir([1, 2, 3])
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

[1, 2, 3].__iter__()
<list_iterator object at 0x03616630>

~~~

리스트의 이터레이터를 변수에 저장한 뒤 \__next__ 메서드를 호출해보면 요소를 차례대로 꺼낼 수 있다. it에서 __next__를 호출할 때마다 리스트에 들어있는 1, 2, 3이 나옵니다. 그리고 3 다음에 __next__를 호출하면 StopIteration 예외가 발생한다. 즉, [1, 2, 3]이므로 1, 2, 3 세 번 반복한다.

이처럼 이터레이터는 __next__로 요소를 계속 꺼내다가 꺼낼 요소가 없으면 StopIteration 예외를 발생시켜서 반복을 끝낸다.

~~~python

it = [1, 2, 3].__iter__()
it.__next__()
1
it.__next__()
2
it.__next__()
3
it.__next__()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    it.__next__()
StopIteration

~~~

물론, 리스트뿐만 아니라 문자열, 딕셔너리, 세트도 __iter__를 호출하면 이터레이터가 나온다. 그리고 이터레이터에서 __next__를 호출하면 차례대로 값을 꺼낸다.

~~~python

'Hello, world!'.__iter__()
<str_iterator object at 0x03616770>
{'a': 1, 'b': 2}.__iter__() # key만 출력
<dict_keyiterator object at 0x03870B10>
{1, 2, 3}.__iter__()
<set_iterator object at 0x03878418>

~~~

리스트, 문자열, 딕셔너리, 세트는 요소가 눈에 보이는 반복 가능한 객체다. 이번에는 요소가 눈에 보이지 않는 range를 살펴보자. 다음과 같이 range(3)에서 \__iter__로 이터레이터를 얻어낸 뒤 \__next__ 메서드를 호출했다.

~~~python

it = range(3).__iter__()
it.__next__()
0
it.__next__()
1
it.__next__()
2
it.__next__()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    it.__next__()
StopIteration

~~~

it에서 __next__를 호출할 때마다 0부터 숫자가 증가해서 2까지 나왔다. 그리고 2 다음에 __next__를 호출했을 때 StopIteration 예외가 발생했다. 즉, range(3)이므로 0, 1, 2 세 번 반복하며 요소가 눈에 보이지 않지만 지정된 만큼 숫자를 꺼내서 반복할 수 있다.

### for와 반복 가능한 객체
<br>
<br>
이제 for에 반복 가능한 객체를 사용했을 때 동작 과정을 알아보겠다. 다음과 같이 for에 range(3)을 사용했다면 먼저 range에서 __iter__로 이터레이터를 얻는다. 그리고 한 번 반복할 때마다 이터레이터에서 __next__로 숫자를 꺼내서 i에 저장하고, 지정된 숫자 3이 되면 StopIteration을 발생시켜서 반복을 끝낸다.

이렇듯 반복 가능한 객체는 \__iter__ 메서드로 이터레이터를 얻고, 이터레이터의 \__next__ 메서드로 반복한다. 여기서는 반복 가능한 객체와 이터레이터가 분리되어 있지만 클래스에 \__iter__와 \__next__ 메서드를 모두 구현하면 이터레이터를 만들 수 있다. 특히 \__iter__, \__next__를 가진 객체를 이터레이터 프로토콜(iterator protocol)을 지원한다고 말한다.

정리하자면 반복 가능한 객체는 요소를 한 번에 하나씩 가져올 수 있는 객체이고, 이터레이터는 \__next__ 메서드를 사용해서 차례대로 값을 꺼낼 수 있는 객체다. 반복 가능한 객체(iterable)와 이터레이터(iterator)는 별개의 객체이므로 둘은 구분해야 힌다. 즉, 반복 가능한 객체에서 \__iter__ 메서드로 이터레이터를 얻는다.

### 시퀀스 객체와 반복 가능한 객체의 차이
<br>
<br>
리스트, 튜플, range, 문자열은 시퀀스 객체라고 했는데, 이 유닛에서는 반복 가능한 객체라고 했다.
시퀀스 객체와 반복 가능한 객체의 차이는 리스트, 튜플, range, 문자열은 반복 가능한 객체이면서 시퀀스 객체다. 하지만, 딕셔너리와 세트는 반복 가능한 객체이지만 시퀀스 객체는 아니다. 왜냐하면 시퀀스 객체는 요소의 순서가 정해져 있고 연속적(sequence)으로 이어져 있어야 하는데, 딕셔너리와 세트는 요소(키)의 순서가 정해져 있지 않기 때문이다. 따라서 시퀀스 객체가 반복 가능한 객체보다 좁은 개념이다. 즉, 요소의 순서가 정해져 있고 연속적으로 이어져 있으면 시퀀스 객체, 요소의 순서와는 상관없이 요소를 한 번에 하나씩 꺼낼 수 있으면 반복 가능한 객체다.

---

## 2.이터레이터 만들기
<br>
<br>
__iter__, __next__ 메서드를 구현해서 직접 이터레이터를 만들어보자. 간단하게 range(횟수)처럼 동작하는 이터레이터다.

~~~python

class 이터레이터이름:
    def __iter__(self):
        코드
 
    def __next__(self):
        코드

~~~

코드를 실행하면 012가 나온다. 이렇게 0부터 지정된 숫자 직전까지 반복하는 이터레이터 counter를 정의헀다. 

~~~python

class Counter:
    def __init__(self, stop):
        self.current = 0    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop    # 반복을 끝낼 숫자
 
    def __iter__(self):
        return self         # 현재 인스턴스를 반환
 
    def __next__(self):
        if self.current < self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current            # 반환할 숫자를 변수에 저장
            self.current += 1           # 현재 숫자를 1 증가시킴
            return r                    # 숫자를 반환
        else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration         # 예외 발생
 
for i in Counter(3):
    print(i, end=' ')


# 실행 결과
0 1 2

~~~

먼저 클래스로 이터레이터를 작성하려면 \__init__ 메서드를 만든다. 여기서는 Counter(3)처럼 반복을 끝낼 숫자를 받았으므로 self.stop에 stop을 넣어준다. 그리고 반복할 때마다 현재 숫자를 유지해야 하므로 속성 self.current에 0을 넣어준다(0부터 지정된 숫자 직전까지 반복하므로 0을 넣는다).

~~~python

    def __init__(self, stop):
        self.current = 0    # 현재 숫자 유지, 0부터 지정된 숫자 직전까지 반복
        self.stop = stop    # 반복을 끝낼 숫자

~~~

그리고 \__iter__ 메서드를 만드는데 여기서는 self만 반환하면 끝이다. 이 객체는 리스트, 문자열, 딕셔너리, 세트, range처럼 \__iter__를 호출해줄 반복 가능한 객체(iterable)가 없으므로 현재 인스턴스를 반환하면 된다. 즉, 이 객체는 반복 가능한 객체이면서 이터레이터다.

~~~python

    def __iter__(self):
        return self         # 현재 인스턴스를 반환

~~~

그다음에 \__next__ 메서드를 만든다. __next__에서는 조건에 따라 숫자를 만들어내거나 StopIteration 예외를 발생시킨다. 현재 숫자 self.current가 반복을 끝낼 숫자 self.stop보다 작을 때는 self.current를 1 증가시키고 현재 숫자를 반환한다. 이때 1 증가한 숫자를 반환하지 않도록 숫자를 증가시키기 전에 r = self.current처럼 반환할 숫자를 변수에 저장해 놓는다. 그다음에 self.current가 self.stop보다 크거나 같아질 때는 raise StopIteration으로 예외를 발생시킨다.

~~~python

    def __next__(self):
        if self.current < self.stop:    # 현재 숫자가 반복을 끝낼 숫자보다 작을 때
            r = self.current            # 반환할 숫자를 변수에 저장
            self.current += 1           # 현재 숫자를 1 증가시킴
            return r                    # 숫자를 반환
        else:                           # 현재 숫자가 반복을 끝낼 숫자보다 크거나 같을 때
            raise StopIteration         # 예외 발생

~~~

for 반복문에 Counter(3)을 지정해 실행하면 3번 반복하면서 0, 1, 2가 출력된다.

~~~python

for i in Counter(3):
    print(i)

~~~

이터레이터를 만들 때는 \__init__ 메서드에서 초깃값, \__next__ 메서드에서 조건식과 현재값 부분을 주의해야 한다.

### 이터레이터 언패킹
<br>
<br>
참고로 이터레이터는 언패킹(unpacking)이 가능하다. 즉, 다음과 같이 Counter()의 결과를 변수 여러 개에 할당할 수 있다. 물론 이터레이터가 반복하는 횟수와 변수의 개수는 같아야 한다.

~~~python

a, b, c = Counter(3)
print(a, b, c)
0 1 2
a, b, c, d, e = Counter(5)
print(a, b, c, d, e)
0 1 2 3 4

~~~

자주 사용하는 map도 이터레이터다. 그래서 a, b, c = map(int, input().split())처럼 언패킹으로 변수 여러 개에 값을 할당할 수 있다.

### 반환값을 _에 저장하는 이유
<br>
<br>
함수를 호출한 뒤 반환값을 저장할 때 _(밑줄 문자)를 사용하는 경우가 있다.

~~~python

_, b = range(2)
b
1

~~~

사실 이 코드는 a, b = range(2)와 같다. 반환값을 언패킹했을 때 _에 할당하는 것은 특정 순서의 반환값 사용하지 않고 무시하겠다는 관례적 표현이다. 예를 들어 다음과 같은 코드는 언패킹 했을 때 두 번째 변수는 사용하지 않겠다는 뜻이다.

~~~python

a, _, c, d =  range(4)
a, c, d
(0, 2, 3)

~~~


---

## 3.인덱스로 접근할 수 있는 이터레이터 만들기
<br>
<br>
__getitem__ 메서드를 구현하여 인덱스로 접근할 수 있는 이터레이터를 만들어보자.
앞에서 만든 Counter 이터레이터를 인덱스로 접근할 수 있도록 다시 만들었다.

~~~python

class 이터레이터이름:
    def __getitem__(self, 인덱스):
        코드

~~~

Counter(3)[0]을 출력했을 때 0이 나왔다. 마찬가지로 Counter(3)[1]은 1, Counter(3)[2]는 2가 나왔다. 그리고 for 반복문에 Counter를 사용했을 때도 1, 2, 3이 나왔다.

~~~python

class Counter:
    def __init__(self, stop):
        self.stop = stop
 
    def __getitem__(self, index):
        if index < self.stop:
            return index
        else:
            raise IndexError
 
print(Counter(3)[0], Counter(3)[1], Counter(3)[2])
 
for i in Counter(3):
    print(i, end=' ').

#실행 결과
0 1 2
0 1 2

~~~

소스 코드를 잘 보면 \__init__ 메서드와 \__getitem__ 메서드만 있는데도 동작이 잘 된다. 클래스에서 __getitem__만 구현해도 이터레이터가 되며 \__iter__, __next__는 생략해도 된다(초깃값이 없다면 __init__도 생략 가능). 그럼 \__init__ 메서드부터 살펴보겠습니다. 여기서는 Counter(3)처럼 반복을 끝낼 숫자를 받았으므로 self.stop에 stop을 넣어준다.

~~~python

class Counter:
    def __init__(self, stop):
        self.stop = stop             # 반복을 끝낼 숫자

~~~

이제 클래스에서 \__getitem__ 메서드를 구현하면 인덱스로 접근할 수 있는 이터레이터가 된다. 먼저 \__getitem__은 매개변수로 인덱스 index를 받는다. 그리고 지정된 index가 반복을 끝낼 숫자 self.stop보다 작을 때 index를 반환한다. index가 self.stop보다 크거나 같으면 IndexError를 발생시킨다. 즉, Counter(3)과 같이 반복을 끝낼 숫자가 3이면 인덱스는 2까지 지정할 수 있다.

~~~python

    def __getitem__(self, index):    # 인덱스를 받음
        if index < self.stop:        # 인덱스가 반복을 끝낼 숫자보다 작을 때
            return index             # 인덱스를 반환
        else:                        # 인덱스가 반복을 끝낼 숫자보다 크거나 같을 때
            raise IndexError         # 예외 발생

~~~

이렇게 하면 Counter(3)[0]처럼 이터레이터를 인덱스로 접근할 수 있다.



---

## 4.iter, next 함수 활용하기
<br>
<br>
이번에는 파이썬 내장 함수 iter, next에 대해 알아보자. iter는 객체의 __iter__ 메서드를 호출해주고, next는 객체의 __next__ 메서드를 호출해준다. 그럼 range(3)에 iter와 next를 사용해보자.

~~~python

it = iter(range(3))
next(it)
0
next(it)
1
next(it)
2
next(it)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    next(it)
StopIteration

~~~

반복 가능한 객체에서 \__iter__를 호출하고 이터레이터에서 \__next__를 호출한 것과 똑같다. 즉 iter는 반복 가능한 객체에서 이터레이터를 반환하고, next는 이터레이터에서 값을 차례대로 꺼낸다. iter와 next는 이런 기능 이외에도 다양한 방식으로 사용할 수 있다.

### iter
<br>
<br>
iter는 반복을 끝낼 값을 지정하면 특정 값이 나올 때 반복을 끝낸다. 이 경우에는 반복 가능한 객체 대신 호출 가능한 객체(callable)를 넣어준다. 참고로 반복을 끝낼 값은 sentinel이라고 부르는데 감시병이라는 뜻이다. 즉, 반복을 감시하다가 특정 값이 나오면 반복을 끝낸다고 해서 sentinel이다.

- iter(호출가능한객체, 반복을끝낼값)

 random.randint(0, 5)와 같이 0부터 5까지 무작위로 숫자를 생성할 때 2가 나오면 반복을 끝내도록 만들었다. 이때 호출 가능한 객체를 넣어야 하므로 매개변수가 없는 함수 또는 람다 표현식으로 만들어준다.

~~~python

import random
it = iter(lambda : random.randint(0, 5), 2)
next(it)
0
next(it)
3
next(it)
1
next(it)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    next(it)
StopIteration

~~~

next(it)로 숫자를 계속 만들다가 2가 나오면 StopIteration이 발생한다. 물론 숫자가 무작위로 생성되므로 next(it)를 호출하는 횟수도 매번 다르다. 물론 다음과 같이 for 반복문에 넣어서 사용할 수도 있다.

~~~python

import random
for i in iter(lambda : random.randint(0, 5), 2):
     print(i, end=' ')

3 1 4 0 5 3 3 5 0 4 1 

~~~

이렇게 iter 함수를 활용하면 if 조건문으로 매번 숫자가 2인지 검사하지 않아도 되므로 코드가 좀 더 간단해진다. 즉, 다음 코드와 동작이 같다.

~~~python

import random
 
while True:
    i = random.randint(0, 5)
    if i == 2:
        break
    print(i, end=' ')

~~~

### next
<br>
<br>
next는 기본값을 지정할 수 있다. 기본값을 지정하면 반복이 끝나더라도 StopIteration이 발생하지 않고 기본값을 출력한다. 즉, 반복할 수 있을 때는 해당 값을 출력하고, 반복이 끝났을 때는 기본값을 출력한다. 다음은 range(3)으로 0, 1, 2세번 반복하는데 next에 기본값을 10으로 지정했다.

- next(반복가능한객체, 기본값)

~~~python

it = iter(range(3))
next(it, 10)
0
next(it, 10)
1
next(it, 10)
2
next(it, 10)
10
next(it, 10)
10

~~~

0, 1, 2까지 나온 뒤에도 next(it, 10)을 호출하면 예외가 발생하지 않고 계속 10이 나온다.

지금까지 반복 가능한 객체의 개념과 이터레이터를 만드는 방법을 배웠다. 여기서는 이터레이터를 만들 때 \__iter__, \__next__ 메서드 또는 \__getitem__ 메서드를 구현해야 한다는 점만 기억하면 된다.

---


### 예제1
<br>
<br>
다음 소스 코드에서 특정 수의 배수를 만드는 이터레이터를 작성하세요. 배수는 0부터 지정된 숫자보다 작을 때까지 만들어야 합니다.

~~~python

class MultipleIterator:
    def __init__(self, stop, multiple):
        ①                        
        ...
                                 
 
    def __iter__(self):
        return self
 
    def __next__(self):
        ②                                            
        ...
                                                     
 
for i in MultipleIterator(20, 3):
    print(i, end=' ')
 
print()
for i in MultipleIterator(30, 5):
    print(i, end=' ')

#실행 결과
3 6 9 12 15 18 
5 10 15 20 25 
~~~


답

~~~python

①  self.stop = stop
   self.multiple = multiple
   self.current = 0
②  self.current += 1
   if self.current * self.multiple < self.stop:
       return self.current * self.multiple
   else:
       raise StopIteration

~~~

반복을 끝낼숫자는 20(stop)이고 배수는3(multiple)이다. 먼저 \__init__ 메서드에서 self.stop에 stop을 저장하고, self.multiple에 multiple을 저장한다. 그리고 몇 번 반복했는지를 저장해야 하므로 self.current를 만들고 0을 저장한다.
\__next__ 메서드에서 배수를 구한다. 배수는 self.current와 self.multiple의 곱을 구하면된다. 단,self.current가 0부터 시작했음으로 0에 self.multiple을 곱하면 0이되기 때문에 self.current += 1을 해 1부터 곱하도록 만든다. 반복을 끝내는 조건은 stop보다 작을떄 반복하고 커지면 중단하게 헤애 하기 때문에 if self.current * self.multiple < self.stop: 이된다.


### 예제2
<br>
<br>
표준 입력으로 정수 세 개가 입력됩니다(첫 번째 정수는 시작하는 초, 두 번째 정수는 반복을 끝낼 초, 세 번째 정수는 인덱스이며 입력되는 초의 범위는 0~100000, 입력되는 인덱스의 범위는 0~10입니다). 다음 소스 코드에서 시간 값을 생성하는 이터레이터를 만드세요.

- 시간 값은 문자열이고 시:분:초 형식입니다. 만약 숫자가 한 자리일 경우 앞에 0을 붙입니다(예: 12:01:08).
- 1초는 00:00:01입니다. 23:59:59를 넘길 경우 00:00:00부터 다시 시작해야 합니다.
- 시간은 반복을 끝낼 초 직전까지만 출력해야 합니다(반복을 끝낼 초는 포함되지 않음).

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

start, stop, index = map(int, input().split())
 
for i in TimeIterator(start, stop):
    print(i)
 
print('\n', TimeIterator(start, stop)[index], sep='')

#입력
10 10 20 20 30 30 40 40
#결과
42.42640687119285
#입력
100 100 200 200 300 300 400 400
#결과
424.26406871192853

~~~

답

~~~python

class TimeIterator:
  def __init__(self, start, stop):
    self.start = start
    self.stop = stop

  def __getitem__(self, index):
    hour = (self.start + index) // 60 // 60 % 24
    min = (self.start + index) // 60 % 60
    sec = (self.start + index) % 60
    if index < self.stop - self.start:
      return '{0:02d}:{1:02d}:{2:02d}'.format(hour, min, sec)
    else:
      raise IndexError

~~~



