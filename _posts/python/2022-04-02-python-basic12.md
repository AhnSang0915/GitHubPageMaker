---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python for 반복문
date: 2022-04-02 22:20 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# for 반복문
<br>
<br>
'Hello, world!'문자열을 100번 출력하려면 print를 100번 사용하면 되지만, for문을 사용해 반복하는 기능을 알아보자.


---

## 1. for와 range 사용하기
<br>
<br>
파이썬의 for반복문은 다양한  사용 방법이 있지만, 먼저 range와 함께 사용하는 방법부터 알아보자. 다음과 같이 for 반복문은 range에 반복할 횟수를 지정하고 앞에 in과 변수를 입력한다. 그리고 :(클론)을 붙이고 다음 중ㄹ에 반복할 코드를 입력한다. for다음 줄에 오는 코드는 반드시 들여쓰기를 해준다.

~~~python

for 변수 in range(횟수):
     반복할 코드

~~~

'Hello, world!'를 100번 출력해 보자. range(100)과 같이 지정하면 0부터 99까지 숫자 100개를 생성한다. 그리고 for는 in으로 숫자를 하나씩 꺼내 변수i에 지정하고, print를 실행한다. 즉, range(100)에서 숫자를 100번 꺼내면서 print를 실행하므로 'Hello, world!'가 100번 출력되게 된다.

~~~python

for i in range(100) :
    print('Hello, world!')

~~~

for 변수 in range(횟수) → 반복할 코드로 순환하는 것을 루프(loop)라고 부른다.

### 반복문에서 변수의 변화 알아보기

<br>
<br>
'Hello, world!'를 100번 출력하는 동시에 i의 값을 확인해보자.

~~~python

for i in range(100) :
    print('Hello, world!',i)

~~~

변수 i를 루프 인덱스라고도 부르며 index의 첫 머리글자를 따서 i를 주로 사용한다.


---

## 2. for와 range 응용하기
<br>
<br>
이번에는 range의 다양한 기능을 활용하여 for반복문을 사용해보자.
<br>
<br>

### 시작하는 숫자와 끝나는 숫자 지정하기

range에 횟수만 지정하면 숫자가 0부터 시작하지만, 다음과 같이 시작하는 숫자와 끝나는 숫자를 지정해 반복할 수도 있다. for i in range(5, 12):와 같이 지정하면 5부터 11까지 5, 6, 7, 8, 9, 10, 11이 나오고 7번 반복한다. 즉, 마지막 숫자는 range의 끝나는 숫자보다 1이 작다(끝나는 숫자는 생성된 숫자에 포함되지 않음).

~~~python

for i in range(5, 12) : # 5부터 11까지의 숫자를 생성
    print('Hello, world!', i)

#출력
Hello, world! 5
Hello, world! 6
Hello, world! 7
Hello, world! 8
Hello, world! 9
Hello, world! 10
Hello, world! 11

~~~

### 증가폭 사용하기
<br>
<br>
range는 증가폭을 지정해서 해당 값만큼 숫자를 증가시킬 수 있다.

 - for 변수 in range(시작, 끝, 증가폭):


~~~python

for i in range(0, 10, 2) :
    print('Hello, world!', i)

#출력
Hello, world! 0
Hello, world! 2
Hello, world! 4
Hello, world! 6
Hello, world! 8

~~~

### 숫자를 감소시키기
<br>
<br>
for과 range는 숫자가 증가하면서 반복했다. 숫자를 감소시켜보자. range는 숫자가 증가하는 기본값이 양수 1이기 때문에 for i in range(10, 0)로 코드를 작성한다고 해서 숫자가 감소하지 않는다. range에 증가폭을 음수로 지정해 감소시킬 수 있다. 특히 range의 끝나는 숫자 0은 생성되는 숫자에 포함되지 않으므로 1까지만 감소한다. range는 그냥 증가, 감소에 상관없이 끝나는 숫자는 생성되는 숫자에 포함되지 않는다는 점만 기억하자.

~~~python

for i in range(0, 10, -1) : # 10에서 1까지 1씩감소
    print('Hello, world!', i)

#출력
Hello, world! 10
Hello, world! 9
Hello, world! 8
Hello, world! 7
Hello, world! 6
Hello, world! 5
Hello, world! 4
Hello, world! 3
Hello, world! 2
Hello, world! 1

~~~

증가폭을 음수로 지정하지 않고 reversed를 사용해 순서를 반대로 뒤집어 보자. reversed의 경우 range(10)을 반대로 뒤집은것 이기 때문에 0부터 9까지 숫자를 만들고 만들어진 숫자를 뒤집는다. 따라서 9~0까지의 숫자가 출력된다.

- for 변수 in reversed(range(횟수))
- for 변수 in reversed(range(시작, 끝))
- for 변수 in reversed(range(시작, 끝, 증가폭))

~~~python

for i in reversed(range(10)) :
    print('Hello, world!', i)


#출력
          
Hello, world! 9
Hello, world! 8
Hello, world! 7
Hello, world! 6
Hello, world! 5
Hello, world! 4
Hello, world! 3
Hello, world! 2
Hello, world! 1
Hello, world! 0

~~~

반복문의 i변수를 할당해 보았다. 반복할 코에서 변수 i에 10을 할당하여 10이 출력될것 같은데, 0부터 9까지 출력되었다. 변수i는 반복할 때마다 다음 값으로 덮어써지기 때문에 값을 할당해도 변수에 영향을 주지 못한다.

~~~python

for i in range(10):
     print(i, end=' ')
     i = 10 

0 1 2 3 4 5 6 7 8 9

~~~

### 입력한 횟수대로 반복하기
<br>
<br>
이번에는 입력한 횟수대로 반복을 해보자. count라는 변수에 input으로 입력값을 받아 for문에 range에 입력한 횟수를 count변수가 받아 반복문이 실행된다.

~~~python

count = int(input('반복할 횟수 입력: '))

for i in range(count) :
     print('Hello, world!', i)


# 출력
반복할 횟수 입력: 3
          
Hello, world! 0
Hello, world! 1
Hello, world! 2

~~~


---


## 3. 시퀀스 객체로 반복하기
<br>
<br>
for문에 range대신 시퀀스객체를 넣어 반복을 실행해 보자. range대신 리스트를 넣어 실행해 보았다.

~~~python

a = [10, 20, 30, 40, 50]
for i in a:
    print(i)

# 출력
10
20
30
40
50

~~~

튜플을 넣어 실행해 보았다.

~~~python

fruits = ('apple', 'orange', 'grape')
for fruits in fruits:
    print(fruits)

# 출력
apple
orange
grape

~~~

문자열을 넣어 실행해 보자.

~~~python

for i in 'Python' :
    print(i, end=' ')

# 출력
P y t h o n 

~~~

문자열을 reversed로 뒤집어 출력해 보자.

~~~python

for i in reversed('Python') :
    print(i, end=' ')

# 출력
n o h t y P 

~~~

