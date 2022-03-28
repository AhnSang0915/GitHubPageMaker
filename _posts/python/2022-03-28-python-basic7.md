---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 리스트와 튜플 사용하기
date: 2022-03-28 21:20 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# Python 리스트와 튜플 사용하기
<br>
<br>

---

## 1. 리스트 만들기
<br>
<br>

지금까지는 변ㄴ수에 값을 한 개씩만 저장했다. 여러 값을 저장할 수 있는 리스트를 알아보자. 대괄호로 원하는 값들을 묶어주면 된다.

~~~python

a = [38, 21, 53, 62, 19]
a
[38, 21, 53, 62, 19]

~~~



### 리스트에 여러 가지 자료형 저장하기

<br>
<br>

리스트는 문자열, 정수, 실수, 불 등 모든 자료형을 저장할 수 있고 섞어서 저장해도 된다.


~~~python

person = ['ansang', 31, 9.15, True]
person
['ansang', 31, 9.15, True]


~~~

### 빈 리스트 만들기

<br>
<br>

빈리스트는 []또는 list()로 만들수 있다.


~~~python

a = []
a
# []
b = list()
b
# []


~~~

### range를 사용하여 리스트 만들기

<br>
<br>
range를 사용해 리스트를 만들어 보자. range는 연속된 숫자를 생성한다. range에 10을 지정하면 0에서 9까지의 숫자를 생성한다.

~~~python

range(10)
range(0, 10)

a = list(range(10))
a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

~~~

range는 시작숫자와 끝나는 숫자를 지정할 수도 있다. 이떄도 끝나는 숫자는 생성되지 않는다.

~~~python

b = list(range(5, 12))
b
[5, 6, 7, 8, 9, 10, 11]


~~~
증가폭을 다르게 할수도 있다. 이때는 range(시작, 끝, 증가폭)의 형식으로 작성해주면 된다. 음수로 작성하면 해당 값만큼 감소하는 리스트가 생성된다.

~~~python

c = list(range(-4, 10, 2))
c
[-4, -2, 0, 2, 4, 6, 8]

d = list(range(10, 0, -1))
d
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

~~~


---

## 2. 튜플 사용하기
<br>
<br>
튜플은 리스트처럼 요소를 일렬로 저장하지만, 안에 저장된 요소를 변경, 추가, 삭제할 수 없다. 튜플이 있는 이유는 요소가 변경되지 않고 유지되어야할 때 사용한다. 변수에 값을 저장할때 ()로 묶어주거나 괄호로묶지 않고 ,로 값만 콤마로 구분해도 튜플이 된다. 

~~~python

a = (1, 2, 3, 4, 5, 6, 7)
a
# (1, 2, 3, 4, 5, 6, 7)
a = 1, 2, 3, 4, 5, 6, 7
a
# (1, 2, 3, 4, 5, 6, 7)

~~~

튜플도 리스트 처럼 여러 자료형을 섞어서 저장할 수 있다.

~~~python

person = ('ansang', 31, 9.15, True)
person
('ansang', 31, 9.15, True)

~~~

not은 논리값을 뒤집는다. not True는 False가 되고, not False는 True가 된다. 여기서 and, or, not 논리 연산자가 식 하나에 들어있으면 not, and, or순으로 판단한다.

~~~python

not True and False or not False
# False and False or True
# False or True
# True

~~~

순서가 헷갈릴 때는 괄호로 판단 순서를 명확히 나타내 주는 것이 좋다.

~~~python

((not True) and False) or (not False)
# True

~~~

### 요소가 한 개 들어있는 튜플 만들기
<br>
<br>
함수 클래스를 사용하다보면 값이 아닌 튜플을 넣어야 하는 경우도 있다. 이때 요소가 하나인 튜플을 사용해야한다.<br>
아래와 같이 요소가 한개 있는 튜플을 만들면 그냥 값이된다. 

~~~python

a = (38)
a
38

~~~

요소가 하나인 튜플을 만들 때는 ()안에 값을 넣은후 ,를 붙여준다. 또는 괄호로 묶지 않고 값 한개에 ,를 붙여도 된다.

~~~python

a = (38,)
a
# (38,)
a = 38,
a
# (38,)

~~~

### range를 사용하여 튜플 만들기
<br>
<br>
리스트와 마찬가지로 range를 사용해 튜플을 만들어 보자.

~~~python

a = tuple(range(10))
a
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

b = tuple(range(5, 12))
b
(5, 6, 7, 8, 9, 10, 11)

c = tuple(range(-4, 10, 2))
c
(-4, -2, 0, 2, 4, 6, 8)

~~~


### 튜플을 리스트로 만들고 리스트를 튜플로 만들기
<br>
<br>
튜플과 리스트는 요소를 변경, 추가, 삭제할 수 있는지 없는지만 다를 뿐 기능과 형태는 같다. 따라서 튜플을 리스트로 만들거나 리스트를 튜플로 만들 수도 있다.

~~~python

a = [1, 2, 3]
a
[1, 2, 3]
tuple(a)
(1, 2, 3)

~~~

반대로 list안에 튜플을 넣으면 새 리스트가 생성된다.

~~~python

b = (4, 5, 6)
b
(4, 5, 6)
list(b)
[4, 5, 6]

~~~

list와 tuple안에 문자열을 넣으면 문자 리스트, 문자 튜플이 생성된다.

~~~python

list('hello')
['h', 'e', 'l', 'l', 'o']
tuple('hello')
('h', 'e', 'l', 'l', 'o')

~~~

리스트와 튜플을 사용하면 변수 여러개를 한번에 만들 수 있다. 이떄 변수의 갯수와 리스트의 요소 갯수는 같아야한다.

~~~python

a, b, c = [1, 2, 3]
d, e, f = (4, 5, 6)
print(a, b, c)
1 2 3
print(d, e, f)
4 5 6

~~~

리스트와 튜플 변수로도 변수 여러개를 만들 수 있다. 다음과 같이 리스트와 튜플의 요소를 변수 여러 개에 할당하는 것을 리스트 언패킹(list unpacking), 튜플 언패킹(tuple unpacking)이라고 한다.

~~~python

x = [1, 2, 3]
a, b, c = x
print(a, b, c)
1 2 3
y = (4, 5, 6)
d, e, f = y
print(d, e, f)
4 5 6

~~~

'입력 값을 변수 두 개에 저장하기'에서 사용한 input().split()은 리스트를 반환한다. 그래서 리스트 언패킹 형식으로 입력 값을 변수 여러 개에 저장할 수 있었다.

~~~python

input().split()
10 20
['10', '20']
x = input().split()
10 20
a, b = x         # a, b = input().split()과 같음
print(a, b)
10 20

~~~

리스트 패킹(list packing)과 튜플 패킹(tuple packing)은 변수에 리스트 또는 튜플을 할당하는 과정을 뜻한다.

~~~python

a = [1, 2, 3]    # 리스트 패킹
b = (1, 2, 3)    # 튜플 패킹
c = 1, 2, 3      # 튜플 패킹

~~~
