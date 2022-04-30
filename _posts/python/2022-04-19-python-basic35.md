---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 두 점 사이의 거리 구하기
date: 2022-04-19 01:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 두 점 사이의 거리 구하기

<br>
<br>
클래스를 활용하여 2차원 평면에서 위치를 표현한 뒤 두 점 사이의 거리를 구해보자.

---

## 1. 두 점 사이의 거리 구하기
<br>
<br>
두 점 사이의 거리를 구하기 전에 먼저 클래스로 점을 구현해보자.
<br>
<br>

### 클래스로 점 구현하기
<br>
<br>
2차원 평면에서 위치를 표현하려면 x와 y값이 필요하다. 다음과 같이 Point2D 클래스를 구현하고 x와 y를 속성으로 넣었다.

~~~python

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

~~~

이제 Point2D 클래스로 점 두 개를 만든다.

~~~python

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
p1 = Point2D(x=30, y=20)    # 점1
p2 = Point2D(x=60, y=50)    # 점2
 
print('p1: {} {}'.format(p1.x, p1.y))    # 30 20
print('p2: {} {}'.format(p2.x, p2.y))    # 60 50

#실행 결과
p1: 30 20
p2: 60 50

~~~

### 피타고라스의 정리로 두 점의 거리 구하기
<br>
<br>
여기서 두 점의 거리를 구하려면 어떻게 해야 할까요? 학교에서 배운 피타고라스의 정리를 이용하면 된다.

- 임의의 직각삼각형에서 빗변을 한 변으로 하는 정사각형의 넓이는 다른 두 변을 각각 한 변으로 하는 정사각형의 넓이의 합과 같다.
- a2(제곱) + b2(제곱) = c2(제곱)

피타고라스의 정리에 대입하려면 먼저 선 a와 b의 길이를 구해야 한다. 우리는 Point2D 클래스의 인스턴스에 두 점의 좌표 정보가 들어있으므로 인스턴스(변수)를 활용하면 된다

~~~python

a = p2.x - p1.x    # 선 a의 길이
b = p2.y - p1.y    # 선 b의 길이

~~~

a는 p2의 x에서 p1의 x를 빼면 되고, b는 p2의 y에서 p1의 y를 빼면 된다.

그다음에 피타고라스의 정리에서 c의 길이를 계산하려면 제곱근을 구해야 한다.

그럼 √(루트)는 를 구현해야한다. 이때는 math 모듈의 sqrt 함수를 사용하면 편리하다. sqrt는 제곱근을 뜻하는 square root에서 따왔다.

- math.sqrt(값)
n  제곱근을 반환, 값이 음수이면 에러 발생

이제 sqrt 함수까지 사용해서 p1과 p2의 거리를 구해보자.

~~~python

import math
 
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
p1 = Point2D(x=30, y=20)    # 점1
p2 = Point2D(x=60, y=50)    # 점2
 
a = p2.x - p1.x    # 선 a의 길이
b = p2.y - p1.y    # 선 b의 길이
 
c = math.sqrt((a * a) + (b * b))    # (a * a) + (b * b)의 제곱근을 구함
print(c)    # 42.42640687119285

#실행 결과
42.42640687119285

~~~

이처럼 sqrt 함수에 값을 넣으면 해당 값의 제곱근을 구해준다. 여기서는 a의 제곱과 b의 제곱의 합을 (a * a) + (b * b)처럼 표현했는데 거듭제곱(power)을 구하는 pow 함수를 사용해도 된다.(math 모듈).

- math.pow(값, 지수)
n  값을 지수만큼 거듭제곱한 값을 반환

즉, a2를 구하고 싶다면 pow(a, 2)처럼 사용한다. 앞에서 작성한 코드를 pow 함수로 다시 작성하면 다음과 같은 모양이 된다.

~~~python

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

~~~

물론 파이썬의 거듭제곱 연산자 **를 사용해도 됩니다.

~~~python

c = math.sqrt((a ** 2) + (b ** 2))

~~~

만약 선의 위치를 구할 때 p2에서 p1을 빼는 것이 아닌 p1에서 p2를 빼도 상관없다. 30 - 60은 -30이고 20 - 50도 -30이다. 하지만 a2 + b2 = c2 식에서 a와 b는 같은 값을 두 번 곱하는데 음수(-)끼리 곱하면 항상 양수(+)가 되므로 부호는 상관하지 않아도 된다. 즉, 양수(+) * 양수(+) 또는 음수(-) * 음수(-) 상황밖에 없기 때문이다.

~~~python

a = p1.x - p2.x    # 선 a의 길이
b = p1.y - p2.y    # 선 b의 길이

~~~

### 절댓값 함수
<br>
<br>
내장 함수 abs 또는 math 모듈의 fabs 함수를 사용하면 양수 또는 음수를 절댓값(absolute value)으로 만들 수 있다.

- abs(값)

정수는 절댓값을 정수로 반환, 실수는 절댓값을 실수로 반환

- math.fabs(값)

절댓값을 실수로 반환

### 절댓값 함수
<br>
<br>
파이썬에서는 각 요소에 이름을 지정해 줄 수 있는 튜플인 namedtuple을 제공한다( collections 모듈). namedtuple은 자료형 이름과 요소의 이름을 지정하면 클래스를 생성해준다. 여기서 자료형 이름은 문자열, 요소의 이름은 문자열 리스트로 넣어준다.

- 클래스 = collections.namedtuple('자료형이름', ['요소이름1', '요소이름2'])

namedtuple로 생성한 클래스는 값을 넣어서 인스턴스를 만들 수 있으며 인스턴스.요소이름 또는 인스턴스[인덱스] 형식으로 요소에 접근할 수 있다.

- 인스턴스 = 클래스(값1, 값2)

- 인스턴스 = 클래스(요소이름1=값1, 요소이름2=값2)

- 인스턴스.요소이름1

- 인스턴스[인덱스]

다음은 namedtuple을 사용하여 점을 표현한 뒤 두 점의 거리를 구한다.

~~~python

import math
import collections
 
Point2D = collections.namedtuple('Point2D', ['x', 'y'])    # namedtuple로 점 표현
 
p1 = Point2D(x=30, y=20)    # 점1
p2 = Point2D(x=60, y=50)    # 점2
 
a = p1.x - p2.x    # 선 a의 길이
b = p1.y - p2.y    # 선 b의 길이
 
c = math.sqrt((a * a) + (b * b))
print(c)    # 42.42640687119285

~~~


---


### 예제1
<br>
<br>
다음 소스 코드를 완성하여 사각형의 넓이가 출력되게 만드세요.

~~~python

class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
 
rect = Rectangle(x1=20, y1=20, x2=40, y2=30)
 
①                              
②                              
③                              
print(area)

# 실행 결과
200

~~~


답

~~~python

① width = abs(rect.x2 - rect.x1)
② height = abs(rect.y2 - rect.y1)
③ area = width * height

~~~


### 예제2
<br>
<br>
표준 입력으로 x, y 좌표 4개가 입력되어 Point2D 클래스의 인스턴스 리스트에 저장됩니다. 여기서 점 4개는 첫 번째 점부터 마지막 점까지 순서대로 이어져 있습니다. 다음 소스 코드를 완성하여 첫 번째 점부터 마지막 점까지 연결된 선의 길이가 출력되게 만드세요

~~~python

import math
 
class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
 
length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())
________________
________________
________________
________________
print(length)

#입력
10 10 20 20 30 30 40 40
#결과
42.42640687119285
#입력
100 100 200 200 300 300 400 400
#결과
424.26406871192853

~~~

내가 쓴 답

~~~python

for i in range(len(p)-1):
    a = p[i + 1].x - p[i].x
    b = p[i + 1].y - p[i].y
    length += math.sqrt(math.pow(a, 2) + math.pow(b, 2))

~~~



