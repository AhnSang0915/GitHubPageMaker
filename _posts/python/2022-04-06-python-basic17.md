---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python FizzBuzz 문제
date: 2022-04-06 12:35 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# FizzBuzz 문제
<br>
<br>
FizzBuzz는 매우 간단한 프로그래밍 문제이며 규칙은 다음과 같다.

- 1에서 100까지 출력
- 3의 배수는 Fizz 출력
- 5의 배수는 Buzz 출력
- 3과 5의 공배수는 FizzBuzz 출력


---

## 1. 1부터 100까지 숫자 출력하기
<br>
<br>
FizzBuzz 문제는 반복문, 조건문, 나머지 연산자, 비교 연산자를 모두 동원해야 풀 수 있다. 먼저 1부터 100까지 숫자를 출력해보자. 

~~~python

for i in range(1, 101):    # 1부터 100까지 100번 반복
    print(i)

# 출력
1
2
3
... (생략)
98
99
100

~~~


---

## 2. 3의 배수일 때와 5의 배수일 때 처리하기
<br>
<br>
이제 3의 배수와 5의 배수일 때 숫자 대신 'Fizz', 'Buzz'를 출력해보자. i를 3으로 나눈 나머지가 0이면 Fizz를 출력하고 i를 5를 나눈 나머지가 0이면 Buzz를 출력한다. 3과5를 나누었을때 나머지가 0이 아닌i는 그대로 출력하게 한다.

~~~python

for i in range(1, 101):    # 1부터 100까지 100번 반복
    if i % 3 == 0:         # 3의 배수일 때
        print('Fizz')      # Fizz 출력
    elif i % 5 == 0:       # 5의 배수일 때
        print('Buzz')      # Buzz 출력
    else:
        print(i)           # 아무것도 해당되지 않을 때 숫자 출력

# 출력    
1
2
Fizz
... (생략)
97
98
Fizz
Buzz

~~~



---


## 3. 3과 5의 공배수 처리하기
<br>
<br>
3과 5의 공배수를 처리하는 코드를 작성하자. 3과 5의 배수이면 FizzBuzz를 출력하려면 and 연산자를 사용한다. and는 두 값이 모두 True여야 True로 판정한다. i % 3 == 0 and i % 5 == 0로 작성해줘야하고 만약 i가 30일때 3의 배수를 먼저 검사하면 3과 5의 공배수는 검사하지 않고 넘어가기 때문에 3과 5의 공배수를 먼저 검사한뒤 elif로 3의 배수, 5의 배수를 검사해야 한다.

~~~python

for i in range(1, 101):              # 1부터 100까지 100번 반복
    if i % 3 == 0 and i % 5 == 0:    # 3과 5의 공배수일 때
        print('FizzBuzz')            # FizzBuzz 출력
    elif i % 3 == 0:                 # 3의 배수일 때
        print('Fizz')                # Fizz 출력
    elif i % 5 == 0:                 # 5의 배수일 때
        print('Buzz')                # Buzz 출력
    else:
        print(i)                     # 아무것도 해당되지 않을 때 숫자 출력
#출력
1
2
Fizz
... (생략)
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
~~~

---

## 4. 논리 연산자를 사용하지 않고 3과 5의 공배수 처리하기
<br>
<br>
and를 사용하지 않고 3과 5의 공배수를 검사하게 만들어보자. 3과5의 최소공배수는 15임으로 15로 나누었을때 나머지가 0인 i를 FizzBuzz로 출력해주면 된다. 하지만 실무에서는 i % 3 == 0 and i % 5 == 0처럼 의미를 명확하게 드러내는 것이 좋다.

~~~python

for i in range(1, 101):      # 1부터 100까지 100번 반복
    if i % 15 == 0:          # 15의 배수(3과 5의 공배수)일 때
        print('FizzBuzz')    # FizzBuzz 출력
    elif i % 3 == 0:         # 3의 배수일 때
        print('Fizz')        # Fizz 출력
    elif i % 5 == 0:         # 5의 배수일 때
        print('Buzz')        # Buzz 출력
    else:
        print(i)             # 아무것도 해당되지 않을 때 숫자 출력

# 결과 
1
2
Fizz
... (생략)
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
~~~

---

## 5. 코드 단축하기
<br>
<br>
이번에는 코드를 단축해 문제를 해결해 보자. 파이썬에선 문자열에 True를 곱하면 문자열이 그대로 출력되고, False를 곱하면 문자열이 출력되지 않는다. True는 1, False는 0으로 연산되기 때문이다. Fizz뒤의 불과, Buzz뒤의 불이 모두 충족되면 +를 사용해 FizzBuzz를 출력하게 하고, or 연산자로 앞의 두 불이 False여도 i를 출력하게 만들었다. 0이 아닌 숫자가 i에 오면 True이기 때문에 3과 5의 배수나 공배수가 아니더라도 i의 값이 출력된다.

~~~python

for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
    # 문자열 곱셈과 덧셈을 이용하여 print 안에서 처리

# 결과 
1
2
Fizz
... (생략)
FizzBuzz
91
92
Fizz
94
Buzz
Fizz
97
98
Fizz
Buzz
~~~


