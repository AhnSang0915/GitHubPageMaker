---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 터틀 그래픽스로 그림 그리기
date: 2022-04-06 12:35 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 터틀 그래픽스로 그림 그리기
<br>
<br>
터틀 그래픽스(Turtle graphics) 모듈을 사용해서 간단한 그림을 그려보자.


---

## 1. 사각형 그리기
<br>
<br>
t.shape('turtle')까지 입력하면 파이썬 터틀 그래픽스(Python Turtle Graphics) 창이 표시되고 오른쪽을 바라보는 거북이가 나온다.

~~~python

import turtle as t
t.shape('turtle')

t.forward(100)

~~~

t.forward(100)을 입력하면 거북이를 100픽셀만큼 앞으로 이동시킨다. t.right(90)를 입력하면 거북이가 오른쪽으로 90도 회전한다. 다시 t.forward(100)을 입력하면 회전한 방향에서 100픽셀 만큼 이동하게된다. 이런식으로 반복하여 사각형을 그려보자.  fd, bk, lt, rt 같이 짧게 줄여서 입력할 수 있다.

- 앞으로 이동: forward, fd
- 뒤로 이동: backward, bk, back
- 왼쪽으로 회전: left, lt
- 오른쪽으로 회전: right, rt

~~~python

import turtle as t
 
t.shape('turtle')
 
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)

~~~

---

## 2. 다각형 그리기
<br>
<br>
이번에는 반복문을 사용해 사각형을 그려보자.

~~~python

import turtle as t
 
t.shape('turtle')
for i in range(4):    # 사각형이므로 4번 반복
    t.forward(100)
    t.right(90)


~~~

### 오각형 그리기
<br>
<br>
오각형의 한각의 크기는 360/5를 하여 구할 수 있다.


~~~python

import turtle as t
 
t.shape('turtle')
for i in range(5):      # 오각형이므로 5번 반복
    t.forward(100)
    t.right(360 / 5)    # 360을 5로 나누어서 외각을 구함

~~~

### 입력값에 해당하는 다각형 그리기
<br>
<br>
이 소스 코드를 응용해서 사용자가 숫자를 입력하면 해당 숫자에 해당하는 다각형을 그려보자.


~~~python

import turtle as t
 
n = int(input())        # 사용자의 입력을 받음
t.shape('turtle')
for i in range(n):      # n번 반복
    t.forward(100)
    t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함

~~~

### 다각형에 색칠하기
<br>
<br>
소스 코드를 실행해보면 빨간색 육각형이 나온다. 먼저 color는 펜의 색을 설정한다. 여기서는 'red'를 지정하여 빨간색으로 만들었다. 그리고 도형을 그리기 전에 t.begin_fill()로 색칠할 준비를 한다. 그다음에 for 반복문으로 도형을 그린 뒤에 t.end_fill()을 사용하면 도형에 현재 펜 색이 칠해진다. 색은 rgb 코드로도 입력할 수 있다.


~~~python

import turtle as t
 
n = 6    # 육각형
t.shape('turtle')
t.color('red')          # 펜의 색을 빨간색으로 설정
t.begin_fill()          # 색칠할 영역 시작
for i in range(n):      # n번 반복
    t.forward(100)
    t.right(360 / n)    # 360을 n으로 나누어서 외각을 구함
t.end_fill()            # 색칠할 영역 끝
    
~~~

---


## 3. 복잡한 도형 그리기
<br>
<br>
이번에는 원을 그려보자. 터틀에서 원을 그릴 때는 circle을 사용한다. t.circle에 120을 지정하여 반지름이 120인 원을 그렸다.

~~~python

import turtle as t
t.shape('turtle')
t.circle(120)

~~~

### 원을 반복해서 그리기
<br>
<br>
for 반복문을 사용해 원을 반복해서 그려보자. 오른쪽으로 6도씩 회전하면서 원을 그리게 된다. speed는 거북이의 속도를 설정한다. 속도는 다음과 같이 문자열 또는 숫자로 설정할 수 있다(숫자는 0.5부터 10까지 설정할 수 있다). 여기서는 'fastest'를 지정해서 가장 빠른 속도로 그렸다.

- 'fastest': 0
- 'fast': 10
- 'normal': 6
- 'slow': 3
- 'slowest': 1

~~~python

import turtle as t
 
n = 60    # 원을 60번 그림
t.shape('turtle')
t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
for i in range(n):
    t.circle(120)       # 반지름이 120인 원을 그림
    t.right(360 / n)    # 오른쪽으로 6도 회전

~~~


### 선으로 복잡한 무늬 그리기
<br>
<br>
이번에는 선을 이용해서 복잡한 무늬를 그려보자. 소스 코드를 실행해보면 복잡한 무늬가 그려진다. 먼저 for로 i가 0부터 299까지 반복하는데 forward로 i만큼 앞으로 이동하도록 만들었다. 즉, 반복할 때마다 선이 길어진다. 그리고 right로 91도 회전했다. 이렇게 하면 미세하게 틀어진 사각형이 그려지면서 바깥으로 퍼져 나가게 된다. 각자 반복 횟수, 선의 길이, 각도를 조금씩 바꿔가면서 그려보자.


~~~python

import turtle as t
 
t.shape('turtle')
t.speed('fastest')      # 거북이 속도를 가장 빠르게 설정
for i in range(300):    # 300번 반복
    t.forward(i)        # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐
    t.right(91)         # 오른쪽으로 91도 회전

~~~

### 예제
<br>
<br>
표준 입력으로 삼각형의 높이가 입력됩니다. 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 이때 출력 결과는 예제와 정확히 일치해야 합니다. 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.

~~~python

count = int(input())
for i in range(count): # 0~4
    for j in reversed(range(count)): #4~0
        if j > i:
            print(' ', end='')
        else :
            print('*', end='')
    print('*'*i)

~~~