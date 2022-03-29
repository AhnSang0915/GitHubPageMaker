---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 시퀀스 자료형 활용하기
date: 2022-03-29 21:20 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# Python 시퀀스 자료형 활용하기
<br>
<br>
지금까지 사용했던 리스트, 튜플, range, 문자열을 잘 보면 공통점이 있다. 이들 모두 값이 연속적(sequence)으로 이어져 있다는 점이다. 파이썬에서는 리스트, 튜플, range, 문자열처럼 값이 연속적으로 이어진 자료형을 시퀀스 자료형(sequence types)라고 부른다.
---

## 1. 시퀀스 자료형의 공통 기능 사용하기
<br>
<br>

시퀀스 자료형의 가장 큰 특징은 공통된 동작과 기능을 제공한다는 점이다. 따라서 시퀀스 자료형의 기본적인 사용 방법을 익혀 두면 나중에 어떠한 시퀀스 자료형을 접하게 되더라도 큰 어려움 없이 바로 사용할 수 있다.
<br>
시퀀스 자료형으로 만든 객체를 시퀀스 객체라고 하며, 시퀀스 객체에 들어있는 각 값을 요소(element)라고 부른다.


### 특정 값이 있는지 확인하기

<br>
<br>

시퀀스 객체 안에 특정 값이 있는지 확인하는 방법이다. 아래 코드는 a에서 30과 100이 있는지 확인한다. 확인하려는 값이 있으면 True 없으면 False가 나온다.


~~~python

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
30 in a
True
100 in a
False

~~~

in 앞에 not을 붙이면 값이 없는지 확인한다. 없으면 True 있으면 False가 나온다.

~~~python

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
100 not in a
True
30 not in a
False

~~~

튜플, range, 문자열 에도 사용 가능하다.

~~~python

43 in (38, 76, 43, 62, 19)
True
1 in range(10)
True
'p' in 'Hello, Python'
False

~~~


### 시퀀스 객체 연결하기

<br>
<br>

시퀀스 객체는 +연산자를 사용하여 객체를 서로 연결하여 새 객체를 만들 수 있다.


~~~python

a = [0, 10, 20, 30]
b = [9, 8, 7, 6]
a + b
[0, 10, 20, 30, 9, 8, 7, 6]

~~~

range는 +연산자로 객체를 연결할 수 없다.

~~~python

range(0, 10) + range(10, 20)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    range(0, 10) + range(10, 20)
TypeError: unsupported operand type(s) for +: 'range' and 'range' 

~~~

range를 연결하고 싶다면 리스트 또는 튜플로 연결해야 한다.

~~~python

list(range(0, 10)) + list(range(10, 20))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
tuple(range(0, 10)) + tuple(range(10, 20))
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)

~~~

문자열은 +연산자로 여러 문자열을 연결할 수 있다.

~~~python

'Hello, ' + 'world!'
'Hello, world!'

~~~

문자열에 정수,실수를 연결하고 싶다면 str을 사용해 숫자를 문자열로 변환해 연결해 주면 된다.

~~~python

'Hello, ' + str(10)      # str을 사용하여 정수를 문자열로 변환
'Hello, 10'
'Hello, ' + str(1.5)     # str을 사용하여 실수를 문자열로 변환
'Hello, 1.5'
~~~

### 시퀀스 객체 반복하기

<br>
<br>
*연산자를 사용하면 시퀀스 객체를 특정 횟수만큼 반복할 수 있다. 0또는 음수를 곱하면 빈 객체가 나오며 실수는 곱할 수 없다.

~~~python

[0, 10, 20, 30] * 3
[0, 10, 20, 30, 0, 10, 20, 30, 0, 10, 20, 30]
[0, 10, 20, 30] * 0
[]
[0, 10, 20, 30] * -1
[]
[0, 10, 20, 30] * 3.2
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    [0, 10, 20, 30] * 3.2
TypeError: can't multiply sequence by non-int of type 'float'

~~~

range는 연결과 마찬가지로 *연산자를 사용해 반복할 수 없다. range를 리스트나 튜플로 만들어 연결할 수 있다.

~~~python

list(range(0, 5, 2)) * 3
[0, 2, 4, 0, 2, 4, 0, 2, 4]
tuple(range(0, 5, 2)) * 3
(0, 2, 4, 0, 2, 4, 0, 2, 4)


~~~

문자열은 *연산자를 사용해 반복이 가능하다.

~~~python

'ansang' * 3
'ansangansangansang'

~~~


---

## 2. 시퀀스 객체의 요소 개수 구하기
<br>
<br>
요소의 길이는 len함수를 사용해 구할 수 있다.

### 리스트와 튜플의 요소 개수 구하기
<br>
<br>
리스트의 요소는 아래와 같이 구할 수 있다.

~~~python

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
len(a)
10

~~~

튜플도 마찬가지 이다.

~~~python

b = (38, 76, 43, 62, 19)
len(b)
5

~~~
range에 len을 사용하면 숫자가 생성되는 개수를 구할 수 있다. 예제에서는 요소의 수가 적어 알기 쉽지만 실무에서는 요소가 많고 추가 삭제 반복을 하기 때문에 len을 사용해야한다.



### 문자열의 길이 구하기
<br>
<br>
문자열도 시퀀스 자료형이므로 len 함수를 사용하면 된다. 공백도 포함이되고 문자열을 묶은 따옴표는 제외된다. 따옴표는 문자열을 표현하는 문법일뿐 길이에는 포함되지 않는다.(문자열의 큰따옴표와 작은따옴표의 경우는 포함된다.)

~~~python

hello = 'Hello, world!'
len(hello)
13

hello = '안녕하세요'
len(hello)
5

~~~

---

## 3. 인덱스 사용하기
<br>
<br>
시퀀스 객체에 들어있는 요소에 접근하는 방법을 알아보자. 시퀀스 객체의 각 요소는 순서가 정해져 있으며, 이 순서를 인덱스라고 부른다. 인덱스의 시작 숫자는 항상 0부터 시작하는것을 기억하자.<br>
리스트

~~~python

a = [38, 21, 53, 62, 19]
a[0]    # 리스트의 첫 번째(인덱스 0) 요소 출력
38
a[2]    # 리스트의 세 번째(인덱스 2) 요소 출력
53
a[4]    # 리스트의 다섯 번째(인덱스 4) 요소 출력
19

~~~

튜플

~~~python

b = (38, 21, 53, 62, 19)
b[0]        # 튜플의 첫 번째(인덱스 0) 요소 출력
38

~~~

range

~~~python

r = range(0, 10, 2) # 02468
r[2]        # range의 세 번째(인덱스 2) 요소 출력
4

~~~

문자열

~~~python

hello = 'Ansang coding'
hello[7]    # 문자열의 여덟 번째(인덱스 7) 요소 출력
'c'

~~~

시퀀스 객체에 인덱스를 지정하지 않으면 해당 객체 전체를 뜻한다. 시퀀스 객체에서 []를 사용하면 실제로는 \__getitem__메서드를 호출하는 것과 같다. 따라서 __getitem__을 사용해 요소를 가져올 수도 있다.

~~~python

a = [38, 21, 53, 62, 19]
a.__getitem__(1)
21

~~~

### 음수 인덱스 지정하기
<br>
<br>
인덱스를 음수로 지정하면 요소의 뒤에서부터 접근한다. -1은 뒤에서 첫번째를 의미하게 되는것이다.

~~~python

# 리스트
a = [38, 21, 53, 62, 19]
a[-1]   # 리스트의 뒤에서 첫 번째(인덱스 -1) 요소 출력
19
a[-5]   # 리스트의 뒤에서 다섯 번째(인덱스 -5) 요소 출력
38

#튜플
b = (38, 21, 53, 62, 19)
b[-1]        # 튜플의 뒤에서 첫 번째(인덱스 -1) 요소 출력
19

#range
r = range(0, 10, 2)
r[-3]        # range의 뒤에서 세 번째(인덱스 -3) 요소 출력
4

#문자열
hello = 'Ansang coding'
hello[-4]    # 문자열의 뒤에서 네 번째(인덱스 -4) 요소 출력
'd'

~~~


### 인덱스의 범위를 벗어나면?
<br>
<br>
시퀀스 객체의 인덱스는 요소의 숫자보다 하나 작은 값이 마지막 인덱스 값이 된다.

~~~python

a = [38, 21, 53, 62, 19]
a[5]    # 인덱스 5는 범위를 벗어났으므로 에러
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a[5]
IndexError: list index out of range 

~~~


### 마지막 요소에 접근하기
<br>
<br>
시퀀스 객체의 인덱스를 -1로 지정하게되면 뒤에서 첫번째 요소에 접근한다. 시퀀스 객체의 마지막 요소에 접근하는 다른 방법을 알아보자.
<br>
아래와 같이 len함수를 사용해 길이를 구하고 그 값을 그대로 넣으면 에러가 발생한다. 인덱스 값은 요소의 전체 숫자보다 하나가 작기 때문이다. 

~~~python

a = [38, 21, 53, 62, 19]
a[len(a)]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a[len(a)]
IndexError: list index out of range 

~~~

요소의 길이를 구하고 -1을 해주게끔 코드를 바꿔보자.

~~~python

a = [38, 21, 53, 62, 19]
a[len(a)-1]
# 19

~~~

### 요소에 값 할당하기
<br>
<br>
시퀀스 객체중 리스트만이 요소를 수정, 변경, 삭제할 수 있다. 튜플, range, 문자열은 값 할당이 불가능하다. 시퀀스 객체는 []로 요소에 접근한뒤 = 로 값을 할당한다. 이때도 볌위를 벗어난 인덱스는 지정할 수 없다.

~~~python

a = [0, 0, 0, 0, 0]    # 0이 5개 들어있는 리스트
a[0] = 38
a[1] = 21
a[2] = 53
a[3] = 62
a[4] = 19
a
[38, 21, 53, 62, 19]
a[0]
38
a[4]
19

# 인덱스 범위를 벗어나 지정할 경우
a[5] = 90
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a[5] = 90
IndexError: list assignment index out of range 

~~~

### del로 요소 삭제하기
<br>
<br>
마찬가지로 리스트만 삭제가 가능하고 튜플, range, 문자열은 불가능하다. 삭제 방법은 del 시퀀스객체[index]로 삭제할 수 있다.

~~~python

a = [38, 21, 53, 62, 19]
del a[2]
a
[38, 21, 62, 19]

~~~