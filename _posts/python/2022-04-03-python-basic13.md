---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python while 반복문
date: 2022-04-03 17:35 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# while 반복문
<br>
<br>
while 반복문은 조건식으로만 동작하며 반복할 코드 안에 조건식에 영향을 주는 변화식이 들어간다.여기서는 조건식 → 반복할 코드 및 변화식 → 조건식으로 순환하는 부분이 루프(loop)이다.

~~~python

i = 0                     # 초기식
while i < 100:            # while 조건식
     print('Hello, world!')    # 반복할 코드
     i += 1                    # 변화식

~~~

while반복문은 초기식부터 시작해 조건식을 판별하고 이때 조건식이 참(True)이면 반복할 코드와 변화식을 함께 수행한다. 그리고 다시 조건식을 판별하여 참(True)이면 코드를 계속 반복하고, 거짓(False)이면 반복문을 끝낸 뒤 다음 코드를 실행한다.

---

## 1. while 반복문 사용하기
<br>
<br>
다음과 같이 whil반복문은 조건식을 지정하고 끝에 :(클론)을 붙여준다. 그리도 다음줄에 반복할 코드와 변화식을 넣어준다.

~~~python

초기식
while 조건식:
     반복할 코드
     변화식

~~~

while 다음줄에 오는 코드는 반드시 들여쓰기를 해줘야한다. while 반복문으로 'Hello, world!'를 100번 출력해보자. 먼저 while 반복문에 변수 i에 0을 할당하고 조건식을 지정한다. 그리고 변화식을 정해줘야하는데 이때 조건식만 지정하고 변화식을 지정하지 않으면 무한루프가 되므로 변화식을 꼭 써야한다.

~~~python


i = 0
while i < 100 :
    print('Hello, world!')
    i += 1 # i를 1씩 증가시킨다. i = i + 1

#출력
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
.....
~~~


### 초깃값을 1부터 시작하기

<br>
<br>
초기 값을 1로 할당하여 'Hello, world!'를 100번 출력해 보자. i가 0부터라면 99까지 나오면 100번이기 때문에 i < 100 이지만 1부터기 때문에 i <=100으로 작성해 줘야한다.
i가 101이 되면 i <= 100은 거짓( False)이므로 반복문을 끝낸다.

~~~python

i = 1
while i <= 100:
    print('Hello, world!', i)
    i += 1
#출력
Hello, world! 1
Hello, world! 2
Hello, world! 3
...  (생략)
Hello, world! 99
Hello, world! 100

~~~

### 초깃값을 감소시키기
<br>
<br>
지금까지 초기값을 증가시키면서 루프를 실행했다. 반대로 초깃값을 크게주고, 변수를 감소시키면서 반복해 보자. 시작 값은 100이고 조건식을 i>0과 같이 지정해 1까지만 반복하도록 만들었다. 변화식은 i-=1로 지정해 변수의 값을 1씩 감소시킨다. i가 0이되면 i>0은 거짓(False)가 되기떄문에 반복이 종료된다.

~~~python

i = 100
while i > 0:
    print('Hello, world!', i)
    i -= 1 # i = i-1
#출력
Hello, world! 100
Hello, world! 99
Hello, world! 98
... (생략)
Hello, world! 2
Hello, world! 1

~~~

### 입력한 횟수대로 반복하기
<br>
<br>
입력한 횟수대로 반복을 해보자. input입력값을 3으로 입력하고 반복을 실행하면 3번 반복하게된다. 반복문의 조건을 i < count로 지정해 count에 들어있는 값만큼 반복하도록 만들었다. 

~~~python

count = int(input('반복할 횟수를 입력하세요: '))
 
i = 0
while i < count:     # i가 count보다 작을 때 반복
    print('Hello, world!', i)
    i += 1

# 출력
Hello, world! 0
Hello, world! 1
Hello, world! 2

~~~

초깃값을 받은 뒤 초깃값만큼 출력하게 만들었다. 여기서는 변수 i 대신 count를 바로 사용하므로 변화식을 count -= 1로 지정하여 반복할 때마다 count를 감소시키고 count가 0이 되면 반복문을 끝낸다.

~~~python

count = int(input('반복할 횟수를 입력하세요: '))
 
while count > 0:     # i가 count보다 작을 때 반복
    print('Hello, world!', count)
    count -= 1

# 출력
Hello, world! 3
Hello, world! 2
Hello, world! 1

~~~


---

## 2. 반복 횟수가 정해지지 않은 경우
<br>
<br>
지금까지 조건식에서 반복 횟수를 정한 뒤 변수 i를 증가시키거나 감소시켜 while 반복문을 사용했다. 하지만 while 반복문은 반복 횟수가 정해지지 않았을 때 주로 사용한다. 이번에는 난수를 생성해서 숫자에 따라 반복을 끝내 보자. 난수(random number)란 특정 주기로 반복되지 않으며 규칙 없이 무작위로 나열되는 숫자를 뜻한다.
<br>
<br>

### 시작하는 숫자와 끝나는 숫자 지정하기
<br>
<br>
range에 횟수만 지정하면 숫자가 0부터 시작하지만, 다음과 같이 시작하는 숫자와 끝나는 숫자를 지정해 반복할 수도 있다. for i in range(5, 12):와 같이 지정하면 5부터 11까지 5, 6, 7, 8, 9, 10, 11이 나오고 7번 반복한다. 즉, 마지막 숫자는 range의 끝나는 숫자보다 1이 작다(끝나는 숫자는 생성된 숫자에 포함되지 않음).
<br>
<br>
파이썬에서 난수를 생성하려면 random 모듈이 필요하다. 모듈은 다음과 같이 import 키워드를 사용하여 가져올 수 있다. 

- import 모듈

~~~python

import random    # random 모듈을 가져옴

~~~
이제 random.random() 으로 random모듈의 random함수를 호출해 보자.

~~~python

random.random()
0.6308359530867019
random.random()
0.9884423768957599
random.random()
0.526192298540528

~~~

숫자를 알아보기 쉽도록 정수를 생성하는 random모듈의 randint함수를 사용해보자. randint 함수는 난수를 생성할 범위를 지정하며, 범위에 지정한 숫자도 난수에 포함된다.

~~~python

random. randint(1, 6)
2
random. randint(1, 6)
4
random. randint(1, 6)
3
random. randint(1, 6)
5

~~~

random.randint(1, 6)과 while반복문을 사용해보자. 아래 코드는 1에서 6사이의 난수를 생성하고 3이 나오면 반복을 끝낸다.

~~~python

i = 0
while i != 3: # i가 3이 아닐때 계속 반복
    i = random.randint(1, 6)
    print(i)

    
1
2
1
1
3 # 3이 나와 종료,

~~~

### random.choice
<br>
<br>
random.choice 함수를 사용하면 시퀀스 객체에서 요소를 무작위로 선택할 수 있다. 다음은 1, 2, 3, 4, 5, 6이 들어있는 리스트에서 무작위로 숫자를 선택한다. random.choice 함수는 시퀀스 객체를 받으므로 리스트뿐만 아니라 튜플, range, 문자열 등을 넣어도 된다.


~~~python

dice = [1, 2, 3, 4, 5, 6]
random.choice(dice)
1
random.choice(dice)
4
random.choice(dice)
3

~~~

---


## 3. while 반복문으로 무한 루프 만들기
<br>
<br>
while 반복문으로 무한 루프를 만들어 보자.

~~~python

while True:    # while에 True를 지정하면 무한 루프
    print('Hello, world!')

# 출력
... (생략)
Hello, world!
Hello, world!
Hello, world!
Hello, world!
... (계속 반복)

~~~

while에 True대신 True로 취급하는 값을 사용해도 무한 루프로 동작한다.

~~~python

while 1:    # 0이 아닌 숫자는 True로 취급하여 무한 루프로 동작
    print('Hello, world!')

~~~

~~~python

while 'Hello':    # 내용이 있는 문자열은 True로 취급하여 무한 루프로 동작
    print('Hello, world!')

~~~
