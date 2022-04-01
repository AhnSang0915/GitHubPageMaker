---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python  else를 사용하여 두 방향으로 분기하기
date: 2022-04-01 10:20 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# Python else를 사용하여 두 방향으로 분기하기
<br>
<br>
if 조건문은 분기를 위한 문법이다. 즉, 분기는 '둘이상으로 갈라지다'라는 뜻으로 프로그램의 흐름을 둘 이상으로 나누는 것을 말한다. if조건 문은 조건식에 맞는 코드를 실행한다. if에 else를 사용하면 조건식이 만족할 때와 만족하지 않을 때 각각 다른 코드를 실행할 수 있다.


---

## 1. else 사용하기
<br>
<br>
else는 if조건문 뒤에 오며 단독으로 사용할 수 없다. if와 마찬가지로 else도 :(콜론)을 붙이며 다음 줄에 실행할 코드가 온다.

~~~python

if 조건식:
     코드1
else:
     코드2

~~~

~~~python

x = 5
    if x == 10:
         print('10입니다.')
    else:
         print('10이 아닙니다.')

# 10이 아닙니다.

~~~

###  if와 else의 기본 형태와 실행 흐름 알아보기

<br>
<br>
else는 if의 조건식이 만족하지 않을 때 코드를 실행한다. 여기에서는 x에 5를 할당해서 x == 10을 만족하지 않음으로 else의 print가 실행되어 '10이 아닙니다.'가 출력된다.

~~~python

x = 5
if x == 10:
         print('10입니다.')
    else:
         print('10이 아닙니다.')

# 10이 아닙니다.   

~~~


###  변수에 값 할당을 if, else로 축약하기

<br>
<br>

변수 x에 10이 들어있으면 y에 x를 할당하고, 아니면 y에 0을 할당하는 코드는 다음과 같이 만들수 있다.

~~~python

x = 5
    if x == 10:
        y = x
    else:
        y = 0
y
0

~~~

이렇게 if, else에서 변수에 값을 할당할 때는 변수 = 값 if 조건문 else 값 형식으로 축약할 수 있으며 이런 문법을 조건부 표현식(conditional expression)이라고 부른다.

~~~python

x = 5
y = x if x == 10 else 0
y
0

~~~


---

## 2. else와 들여쓰기
<br>
<br>
else는 if와 들여쓰기 규칙이 같다. 다음은 들여쓰기가 잘못된 코드다.

~~~python

x = 5
 
if x == 10:
    print('10입니다.') 
else:
print('x에 들어있는 숫자는')    # unexpected indent 에러 발생 
    print('10이 아닙니다.')

~~~

올바른 코드로 고쳐보자.

~~~python

if x == 10:
    print('10입니다.') 
else:
    print('x에 들어있는 숫자는')
    print('10이 아닙니다.') 

~~~

else가 여러 줄일 때는 마지막 줄의 들여쓰기를 하지 않으면 의도치 않은 동작이 된다.

~~~python

x = 10
 
if x == 10:    # x가 10이라 조건식이 참
    print('10입니다.')    # 출력
else:
     print('x에 들어있는 숫자는')
print('10이 아닙니다.')    # 출력되지 않아야 하는데 출력됨

~~~

x가 10이라는 조건식이 참이므로 '10입니다.'가 출력된다. 하지만 else의 '10이 아닙니다.'도 함께 출력되어 버렸다. print('10이 아닙니다.')는 들여쓰기가 없어서 else와는 상관없는 코드가 되었기 때문이다. print를 한 줄 띄워보면 왜 잘못되었는지 알 수 있다.

~~~python

x = 10
 
if x == 10:    # x가 10이라 조건식이 참
    print('10입니다.')
else:
    print('x에 들어있는 숫자는')
 
print('10이 아닙니다.')

~~~

---


## 3. if 조건문의 동작 방식 알아보기
<br>
<br>
이번에는 조건식이 아닌 값으로 if와 else의 코드를 동작시켜 보자. True는 if 코드가 실행되고 Fasle는 else의 코드가 실행된다. 특히 None은 Fasle로 취급되므로 else의 코드가 실행 된다. 실제 코드를 작성할 때 변수에 들어있는 값이나 함수의 결과가 None인 경우가 많으므로 이 부분은 꼭 기억해두자.

~~~python

if True:
    print('참')    # True는 참
else:
    print('거짓')
 
if False:
    print('참')
else:
    print('거짓')    # False는 거짓
 
if None:
    print('참')
else:
    print('거짓')    # None은 거짓

# 결과
# 참
# 거짓
# 거짓
~~~

### if 조건문에 숫자 지정하기
<br>
<br>
숫자는 정수(2진수, 10진수, 6진수), 실수와 관계없이 0이면 거짓, 0이 아닌 수는 참이다.

~~~python

if 0:
    print('참')
else:
    print('거짓')    # 0은 거짓
 
if 1:
    print('참')    # 1은 참
else:
    print('거짓')
 
if 0x1F:    # 16진수
    print('참')    # 0x1F는 참
else:
    print('거짓')
 
if 0b1000:    # 2진수
    print('참')    # 0b1000은 참
else:
    print('거짓')
 
if 13.5:    # 실수
    print('참')    # 13.5는 참
else:
    print('거짓')


# 결과
# 거짓
# 참
# 참
# 참
# 참

~~~

### if 조건문에 문자열 지정하기
<br>
<br>
문자열은 내용이 있을때 참, 빈 문자열은 거짓이다.

~~~python

if 'Hello':    # 문자열
    print('참')    # 문자열은 참
else:
    print('거짓')
 
if '':    # 빈 문자열
    print('참')
else:
    print('거짓')    # 빈 문자열은 거짓

# 결과
# 참
# 거짓

~~~


### 0, None, 빈 문자열을 not으로 뒤집으면?
<br>
<br>
0, None, 빈 문자열 ''을 not으로 뒤집으면 참(True)이 되므로 if를 동작시킬 수 있다.

~~~python

if not 0:
    print('참')    # not 0은 참
 
if not None:
    print('참')    # None은 참
 
if not '':
    print('참')    # not 빈 문자열은 참

# 결과
# 참
# 참
# 참

~~~


### True, False로 취급하는 것들
<br>
<br>
다음은 파이썬 문법 중에서 False로 취급하는 것들입니다.<br>

- None

- False

- 0인 숫자들: 0, 0.0, 0j

- 비어 있는 문자열, 리스트, 튜플, 딕셔너리, 세트: '', "", [], (), {}, set()

- 클래스 인스턴스의 __bool__(), __len__() 메서드가 0 또는 False를 반환할 때

앞에서 나열한 것들을 제외한 모든 요소들은 True로 취급합니다.



---

## 4. 조건식을 여러 개 지정하기
<br>
<br>
지금까지 if에 조건식을 하나만 지정했다. 만약 조건이 복잡하다면 어떻게 해야할까? if 조건문에는 논리 연산자를 사용하여 조건식을 여러 개 지정할 수 있다. x == 10이고 y == 20처럼 and 논리 연산자를 사용하면 x == 10이면서 y == 20일 때 if 코드가 실행된다.

~~~python

x = 10
y = 20
 
if x == 10 and y == 20:     # x가 10이면서 y가 20일 때
    print('참')
else:
    print('거짓')

~~~

만약 둘중 하나라도 만족했을때 '참'이 출력되도록 만드려면 or 논리 연산자를 사용하면 된다.

### 중첩 if조건문과 논리 연산자
<br>
<br>
보통 여러 조건을 판단할 때 if를 계속 나열해서 중첩 if 조건문으로 만드는 경우가 많다. 예를 들어 x가 양수이면서 20보다 작은지 판단하려고 한다. if로 x가 0보다 큰지 검사하고(0보다 크면 양수), 다시 if로 20보다 작은지 검사했다. 

~~~python

x = 10
y = 20
 
if x > 0:
    if x < 20:
        print('20보다 작은 양수입니다.')

~~~

이런 중첩 if 조건문은 and 논리 연산자를 사용해서 if 하나로 줄일 수 있다.

~~~python

x = 10
y = 20
 
if x > 0 and x < 20:
    print('20보다 작은 양수입니다.')
   
~~~

위보다 더 간단하게 만들 수 있다.


~~~python

x = 10
y = 20
 
if 0 < x < 20:
    print('20보다 작은 양수입니다.')
   
~~~

