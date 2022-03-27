---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 불과 비교, 논리 연산자
date: 2022-03-27 17:20 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# Python 불과 비교, 논리 연산자
<br>
<br>

---

## 1.불과 비교 연산자 사용하기
<br>
<br>

if, while문에서 많이 사용하게되는 논리 연산자와 참(True), 거짓(False)을 나타내는 불리언(boolean)의 사용방법을 알아보자.
<br>
<br>
boolean은 True, False로 표현하며 1, 3.6, 'Python'처럼 값의 일종이다.


### 비교 연산자의 판단 결과

<br>
<br>

Python에서 비교 연산자와 논리 연산자의 판단 결과로 True, False를 사용한다. 즉, 비교 결과가 맞으면 True, 틀리면 False이다.


~~~python

1>2
False
1<2
True

~~~

### 숫자가 같은지 다른지 비교하기

<br>
<br>

두 숫자가 같은지 다른지 비교하는 데에는 ==(equal), !=(not equal)을 사용한다.


~~~python

10==10
True
10 != 11
True

~~~

### 문자열이 같은지 다른지 비교하기

<br>
<br>

문자열도 ==와 !=연산자로 비교 할 수 있다. 이때 문자열의 대소문자도 구분해야 한다. 같은 단어여도 대소문자가 다르면 다른 문자열로 판단한다.


~~~python

'Python' == 'Python'
True
'Python' == 'python'
False
'Python' != 'python'
True

~~~



### 부등호 사용하기

<br>
<br>
부등호는 큰지, 작은지, 크거나 작거나 같은지를 판별한다. 기준은 첫번째 값이다.


~~~python

10 > 20    # 10이 20보다 큰지 비교
False
10 < 20    # 10이 20보다 작은지 비교
True
10 >= 10    # 10이 10보다 크거나 같은지 비교
True
10 <= 10    # 10이 10보다 작거나 같은지 비교
True

~~~



### 객체가 같은지 다른지 비교하기

<br>
<br>
객체가 같은지 다른지 비교할땐 is와 is not을 사용한다. ==, !=는 값 자체를 비교하고 is와 is not은 객체를 비교한다.
<br>
<br>
1과 1.0은 정수와 실수이다. 데이터의 타입은 다르지만 값은 같기때문에 ==는 True가 나온다. 하지만 1과 1.0을 is로 비교해 보면 False가 나온다. 이유는 1은 정수 객체, 1.0은 실수객체이기 때문이다. 객체로서는 다르기 떄문에 is not으로 비교하면 True가 나온다.


~~~python

1 == 1.0
True
1 is 1.0
False
1 is not 1.0
True

~~~



### 정수객체와 실수객체가 서로 다른지 확인하기

<br>
<br>
정수 객체와 실수 객체가 서로 다른지 확인하려면 id함수를 사용한다. id는 객체의 고유한 값(메모리 주소)를 구한다.(이 값은 파이썬을 실행하는 동안에는 계속 유지되며 다시 실행하면 달라진다)

~~~python

id(1)
2156471124208
id(1.0)
2156509782960

~~~

### 값 비교에 is를 쓰지 않기

<br>
<br>
값 자체를 비교할때는 ==와 !=를 사용한다. 변수 a가 있는 상태에서 다른 값을 할당하면 메모리 주소가 달라질 수 있기 때문이다. 따라서 다른 객체가 되므로 값이 같더라고 is로 비교하면 False가 나온다. 값을 비교할 때는 is가 아닌 비교 연산자를 사용해야 한다.

~~~python

a = -5
a is -5
True
a = -6
a is -6
False
a == -6
True

~~~



---

## 2. 논리 연산자 사용하기
<br>
<br>
논리 연산자는 and, or, not을 사용한다. and는 두값이 모두 True여야 True이다. 하나라도 False이면 False가 나온다.

~~~python

True and True
# True
True and False
# False
False and True
# False
False and False
# False

~~~

or는 두 값 중 하나라도 True이면 True, 두값이 모두 False면 False가 된다.

~~~python

True or True
#True
True or False
# True
False or True
# True
False or False
# False

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

### 논리 연산자와 비교 연산자를 함께 사용하기
<br>
<br>
논리연산자와 비교 연산자를 함께 사용해보자. 이때는 비교 연산자(is, is not, ==, !=, <, >, <=, >=)를 먼저 판단하고 논리 연산자(not, and, or)를 판단하게된다.


~~~python

10 == 10 and 10 != 5    # True and True
# True
10 > 5 or 10 < 3        # True or False
# True
not 10 > 5              # not True
# False
not 1 is 1.0            # not False
# True

~~~

### 정수, 실수, 문자열을 불로 만들기
<br>
<br>
정수, 실수, 문자열을 True, False로 만들어 보자. 정수1은 True 0은 False이다. 문자열의 내용이 'False'라도 불로 만들면 Ture가 된다. 문자열의 경우 값이 있으면 True로 나타낸다. 정수0, 0.0이외의 숫자는 모두 True, 빈문자열 '', ""를 제외한 모든 문자열은 True가된다.

~~~python

bool(1)
# True
bool(0)
# False
bool(1.5)
# True
bool('False')
# True
bool('')
# False
bool("")
# False
bool(0)
# False
bool(0.0)
# False

~~~


### 단락 평가
<br>
<br>
논리 연산에서 중요한 것이 단락 평가(short-circuit evalution)이다. 단락 평가는 첫번째 값만으로 결과가 확실할 때 두 번째 값은 평가하지 않는 방법이다.

~~~python

# 첫 번째 값이 거짓이므로 두 번째 값은 확인하지 않고 거짓으로 결정
print(False and True)     # False
print(False and False)    # False
# 첫 번째 값이 참이므로 두 번째 값은 확인하지 않고 참으로 결정
print(True or True)     # True
print(True or False)    # True

~~~

True and 'Python'를 확인하면 True가 나올것 같지만 'Python'이 나온다. 파이썬에서 논리 연산자는 마지막 단락 평가를 실시한 값을 그대로 반환하기 때문이다. 마지막에 단락평가를 실시한 값이 불이면 불을 반환한다.

~~~python

True and 'Python'
# 'Python'
True and 'ansang'
# 'ansang'
'Python' and True
# True
'ansang' and True
# True

~~~

여기서는 문자열 'Python'을 True로 쳐서 and 연산자가 두 번째 값까지 확인하므로 두 번째 값이 반환된다.만약 다음과 같이 and 연산자 앞에 False나 False로 치는 값이 와서 첫 번째 값 만으로 결과가 결정나는 경우에는 첫 번째 값이 반환된다.

~~~python

False and 'Python'
#False
0 and 'Python'    # 0은 False이므로 and 연산자는 두 번째 값을 평가하지 않음
#0

~~~

or 연산자도 마찬가지로 마지막으로 단락 평가를 실시한 값이 반환된다. 다음은 or 연산자에서 첫 번째 값만으로 결과가 결정되므로 첫 번째 값이 반환된다.

~~~python

True or 'Python'
# True
'Python' or True
# 'Python'

~~~

만약 두번째 값까지 판한해야 한다면 두 번째 값이 반환된다.

~~~python

False or 'Python'
# 'Python'
0 or False
# False
~~~
