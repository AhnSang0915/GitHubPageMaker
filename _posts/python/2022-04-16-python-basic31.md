---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 클로저 사용하기
date: 2022-04-16 17:40 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 클로저 사용하기

<br>
<br>
변수의 사용범위와 함수를 클로저 형태로 만드는 방법을 알아보자.

---

## 1. 변수의 사용 범위 알아보기
<br>
<br>
파이썬 스크립트에서 변수를 만들면 다음과 같이 함수 안에서도 사용할 수 있다.
foo함수에서 함수 바깥에 있는 변수 x의 값을 출력할 수 있다. 이처럼 함수를 포함하여 스크립트 전체에서 접근할 수 있는 변수를 전역 변수(global variable)라고 한다. 특히 전역 변수에 접근할 수 있는 범위를 전역 범위(globla scope)라고 한다.

 
~~~python

x = 10          # 전역 변수
def foo():
    print(x)    # 전역 변수 출력
 
foo()
print(x)        # 전역 변수 출력

#결과
10
10

~~~

변수 x를 함수 foo안에서 만들고 실행을 해보면 x가 정의되지 않았다는 에러가 발생한다. 왜냐하면 변수 x는 함수 foo안에서 만들었기 때문에 foo의 지역 변수(local variable)이다. 따라서 지역 변수는 변수를 만든 함수 안에서만 접근할 수 있고, 함수 바깥에서는 접근할 수 없다. 특히 지역 변수를 접근할 수 있는 범위를 지역 범위(local scope)라고 한다.

~~~python

def foo():
    x = 10      # foo의 지역 변수
    print(x)    # foo의 지역 변수 출력
 
foo()

print(x)        # 에러. foo의 지역 변수는 출력할 수 없음

#결과
10
Traceback (most recent call last):
  File "C:\project\local_variable.py", line 6, in <module>
    print(x)        # 에러. foo의 지역 변수는 출력할 수 없음
NameError: name 'x' is not defined

~~~


### 함수 안에서 전역 변수 변경하기
<br>
<br>
함수 안에서 전역 변수의 값을 넣어보자. 분명 함수 foo 안에서 x = 20처럼 x의 값을 20으로 변경했다. 하지만 함수 바깥에서 print로 x의 값을 출력해보면 10이다. 겉으로 보기에는 foo 안의 x는 전역 변수인 것 같지만 실제로는 foo의 지역 변수다. 즉, 전역 변수 x가 있고, foo에서 지역 변수 x를 새로 만들게 된다. 이 둘은 이름만 같을 뿐 서로 다른 변수이다.

~~~python

x = 10          # 전역 변수
def foo():
    x = 20      # x는 foo의 지역 변수
    print(x)    # foo의 지역 변수 출력
 
foo()
print(x)        # 전역 변수 출력

#결과
20
10

~~~

함수 안에서 전역 변수의 값을 변경하려면 global 키워드를 사용해야 한다. 다음과 같이 함수 안에서 global에 전역 변수의 이름을 지정해준다. 그리고 함수안에서 x를 20으로 변경하면 함수 바깥에서 x를 출력했어도 20이 나온다. 이렇게 함수안에서 변수를 global로 지정하면 전역 변수를 생성하게 된다.

- global 전역변수

~~~python

x = 10          # 전역 변수
def foo():
    global x    # 전역 변수 x를 사용하겠다고 설정
    x = 20      # x는 전역 변수
    print(x)    # 전역 변수 출력
 
foo()
print(x)        # 전역 변수 출력

~~~

만약 전역 변수가 없을 때 함수 안에서 global을 사용하면 해당 변수는 전역 변수가 된다.

~~~python

# 전역 변수 x가 없는 상태
def foo():
    global x    # x를 전역 변수로 만듦
    x = 20      # x는 전역 변수
    print(x)    # 전역 변수 출력
 
foo()
print(x)        # 전역 변수 출력

~~~

### 네임스페이스
<br>
<br>
파이썬에서 변수는 네임스페이스(namespace, 이름공간)에 저장된다. 다음과 같이 locals 함수를 사용하면 현재 네임스페이스를 딕셔너리 형태로 출력할 수 있다.
<br>
출력된 네임스페이스를 보면 'x': 10처럼 변수 x와 값 10이 저장되어 있습니다. 여기서는 전역 범위에서 네임스페이스를 출력했으므로 전역 네임스페이스를 가져옵니다.

~~~python

x = 10
locals()
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 10}

~~~

마찬가지로 함수 안에서 locals를 사용할 수 있다. 네임스페이스를 보면 'x': 10만 저장되어 있다. 이때는 지역 범위에서 네임스페이스를 출력했으므로 지역 네임스페이스를 가져온다.

~~~python

def foo():
     x = 10
     print(locals())

foo()
{'x': 10}

~~~

---

## 2. 함수 안에서 함수 만들기
<br>
<br>
이번에는 함수 안에서 함수를 만드는 방법을 알아보자. 다음과 같이 def로 함수를 만들고 그 안에서 다시 def로 함수를 만들면 된다.

~~~python

def 함수이름1():
    코드
    def 함수이름2():
        코드

~~~

함수 안에서 문자열을 출력하는 함수를 만들고 호출해보자.
<br>
함수 print_hello 안에서 다시 def로 함수 print_message를 만들었다. 그리고 print_hello안에서 print_message()처럼 함수를 호출했다. 하미잔 아직 함수를 정의만 한 상태이므로 아무것도 출력되지 않는다. 두 함수가 실제로 동작하려면 바깥쪽에 있는 print_hello를 호출해주어야 한다. 즉, print_hello > print_message 순으로 실행된다.

~~~python

def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)
    print_message()
 
print_hello()

# 실행결과
Hello, world!

~~~


### 지역 변수의 범위
<br>
<br>
print_hello 함수와 print_message 함수에서 지역 변수의 범위를 살펴보자. 안쪽 함수 print_message에서는 바깥쪽 함수 print_hello의 지역 변수 hello를 사용할 수 있습니다.즉, 바깥쪽 함수의 지역 변수는 그 안에 속한 모든 함수에서 접근할 수 있다.

~~~python

def print_hello():
    hello = 'Hello, world!'
    def print_message():
        print(hello)    # 바깥쪽 함수의 지역 변수를 사용

~~~

### 지역 변수 변경하기
<br>
<br>
바깥쪽 함수의 지역 변수를 안쪽 함수에서 변경해보자. 다음과 같이 안쪽 함수 B에서 바깥쪽 함수 A의 지역 변수 x를 변경한다. 실행을 해보면 20이 나와야 할 것 같은데 10이 나온다. 왜냐하면 겉으로 보기에는 바깥쪽 함수 A의 지역 변수 x를 변경하는 것 같지만, 실제로는 안쪽 함수 B에서 이름이 같은 지역 변수 x를 새로 만들게 된다. 즉, 파이썬에서는 함수에서 변수를 만들면 항상 현재 함수의 지역 변수가 된다.

~~~python

def A():
    x = 10        # A의 지역 변수 x
    def B():
        x = 20    # x에 20 할당
 
    B()
    print(x)      # A의 지역 변수 x 출력
 
A()

#결과
10

#
def A():
    x = 10        # A의 지역 변수 x
    def B():
        x = 20    # B의 지역 변수 x를 새로 만듦

~~~

현재 함수의 바깥쪽에 있는 지역 변수의 값을 변경하려면 nonlocal 키워드를 사용해야 한다. 다음과 같이 함수 안에서 nonlocal에 지역 변수의 이름을 지정해준다.

- nonlocal 지역변수

~~~python

def A():
    x = 10        # A의 지역 변수 x
    def B():
        nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용
        x = 20        # A의 지역 변수 x에 20 할당
 
    B()
    print(x)      # A의 지역 변수 x 출력
 
A()

#결과
20

~~~

### 지역 변수 변경하기
<br>
<br>
nonlocal은 현재 함수의 바깥쪽에 있는 지역 변수를 찾을 때 가장 가까운 함수부터 먼저 찾는다. 이번에는 함수의 단계를 A, B, C로 만들었다. 함수 C에서 nonlocal x를 사용하면 가장 가까운 바깥쪽에 있는 함수 B의 지역 변수 x = 20을 사용하게 된다. 따라서 x = x + 30은 50이 나온다. 그리고 함수 C에서 nonlocal y를 사용하면 바깥쪽에 있는 함수의 지역 변수 y를 사용해야 하는데 함수 B에는 y가 없다. 이때는 한 단계 더 바깥으로 나가서 함수 A의 지역 변수 y를 사용하게 된다. 즉, 가까운 함수부터 지역 변수를 찾고, 지역 변수가 없으면 계속 바깥쪽으로 나가서 찾는다.

~~~python

def A():
    x = 10
    y = 100
    def B():
        x = 20
        def C():
            nonlocal x
            nonlocal y
            x = x + 30
            y = y + 300
            print(x)
            print(y)
        C()
    B()
 
A()

~~~

### global로 전역 변수 사용하기
<br>
<br>
함수가 몇 단계든 상관없이 global 키워드를 사용하면 무조건 전역 변수를 사용하게 된다. 함수 C에서 global x를 사용하면 전역 변수 x = 1을 사용하게 된다. 따라서 x = x + 30은 31이 나온다.

~~~python

x = 1
def A():
    x = 10
    def B():
        x = 20
        def C():
            global x
            x = x + 30
            print(x)
        C()
    B()
 
A()

# 실행결과
31

~~~

---

## 3. 클로저 사용하기
<br>
<br>
함수를 클로저 형태로 만드는 방법을 알아보자. 다음은 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 a * x + b를 계산하는 함수 mul_add를 만든 뒤에 함수 mul_add자체를 반환한다. 먼저 calc에 지역 변수 a와 b를 만들고 3과 5를 저장했다. 그다음에 함수 mul_add에서 a와 b를 사용하여 a * x + b를 계산한 뒤 반환한다.

~~~python

def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    return mul_add          # mul_add 함수를 반환
 
c = calc()
print(c(1), c(2), c(3), c(4), c(5))

#실행 결과
8 11 14 17 20

~~~

함수 mul_add를 만들고 calc함수를 바로 호출하지 않고 mul_add함수 자체를 return한다(함수를 반환할 때는 함수 이름만 반환해야 하며 ( )(괄호)를 붙이면 안 된다).

~~~python

return mul_add 

~~~

이제 클로저를 사용한다. 다음과 같이 함수 calc를 호출한 뒤 반환값을 c에 저장한다. calc에서 mul_add를 반환했음으로 c에는 함수 mul_add가 들어간다. 그리고 c에 숫자를 넣어서 호출해보면 a * x + b 계산식에 따라 값이 출력 된다.


~~~python

c = calc()
print(c(1), c(2), c(3), c(4), c(5))

~~~

코드를 보면 함수 calc가 끝났는데도 c는 calc의 지역 변수 a, b를 사용해서 계산을 하고 있다. 이렇게 함수를 둘러싼 환경(지역 변수, 코드 등)을 계속 유지하다가, 함수를 호출할 때 다시 꺼내서 사용하는 함수를 클로저(closure)라고 한다. 여기서는 c에 저장된 함수가 클로저다.

### lambda로 클로저 만들기
<br>
<br>
클로저는 다음과 같이 lambda로도 만들 수 있다. return lambda x: a * x + b처럼 람다 표현식을 만든 뒤 람다 표현식 자체를 반환했다. 이렇게 람다를 사용하면 클로저를 좀 더 간단하게 만들 수 있다.
보통 클로저는 람다 표현식과 함께 사용하는 경우가 많아 둘을 혼동하기 쉽다. 람다는 이름이 없는 익명 함수를 뜻하고, 클로저는 함수를 둘러싼 환경을 유지했다가 나중에 다시 사용하는 함수를 뜻한다.

~~~python

def calc():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환
 
c = calc()
print(c(1), c(2), c(3), c(4), c(5))

#실행 결과
8 11 14 17 20

~~~

### 클로저의 지역 변수 변경하기
<br>
<br>
지금까지 클로저의 지역 변수를 가져오기만 했는데, 클로저의 지역 변수를 변경하고 싶다면 nonlocal을 사용하면 된다. 다음은 a * x + b의 결과를 함수 calc의 지역 변수 total에 누한다.

~~~python

def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a * x + b
        print(total)
    return mul_add
 
c = calc()
c(1)
c(2)
c(3)

# 실행 결과
8
19
33

~~~

---

### 예제1
<br>
<br>
다음 소스 코드를 완성하여 함수 c를 호출할 때마다 호출 횟수가 출력되게 만드세요. 여기서는 함수를 클로저로 만들어야 합니다.

~~~python

def counter():
    i = 0
    def count():
                       
        ...
                       
 
c = counter()
for i in range(10):
    print(c(), end=' ')

# 결과
1 2 3 4 5 6 7 8 9 10 

~~~


답

~~~python

        nonlocal i
        i += 1
        return i
    return count

~~~

함수 counter를 호출해서 반환값을 c에 저장한 뒤에 c를 호출하고 있다. 그리고 c를 호출할 때마다 값이 계속 유지되게 하려면 함수를 클로저로 만들어야 한다.
함수 counter에서는 지역 변수 i에 0이 할당되어 있고, 함수 count가 만들어져 있다. 따라서 count에서 i에 1을 더한 값을 저장한 뒤 i를 반환한다. 이때 nonlocal을 사용하여 함수 바깥쪽의 지역 변수 i를 변경할 수 있도록 만들어야 한다.
마지막으로 함수 counter에서 함수 count를 반환하면 된다(함수를 반환할 때는 함수 이름만 반환해야 하며 ( )(괄호)를 붙이면 안 된다).

### 예제2
<br>
<br>
표준 입력으로 정수가 입력됩니다. 다음 소스 코드를 완성하여 함수 c를 호출할 때마다 숫자가 1씩 줄어들게 만드세요. 여기서는 함수를 클로저로 만들어야 합니다. 정답에 코드를 작성할 때는 def countdown(n):에 맞춰서 들여쓰기를 해주세요.

~~~python

def countdown(n):
________________
________________
________________
________________
________________
________________

n = int(input())
 
c = countdown(n)
for i in range(n):
    print(c(), end=' ')

#입력
10

#결과
10 9 8 7 6 5 4 3 2 1 

#입력
20

#결과
20 19 18 17 16 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1 

~~~

답

~~~python

    i = n +1
    def count():
        nonlocal i
        i -= 1
        return i
    return count

~~~

반환 값을 c에 저장하고 c를 호출한다.  먼저 함수 countdown에 지역변수를 만들고 매개변수 n에 1을 더해서 할당한다. 여기선느 입력값이 10이면 10부터 숫자가 1씩 줄어들고 있으므로 처음 시작할 값은 11로 만든다(n = 10일때 for i in ragne(11)이어야 10부터 출력). 그리고 count 함수로 지역 변수 i를 변경하기 위해 nonlacal을 사용하고 i를 호출될때마다 1씩 감소하게 한다. i를 반환하게 만든 후 count함수를 다시 리턴하게 만든다.