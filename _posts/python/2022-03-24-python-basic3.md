---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 변수 만들기
date: 2022-03-23 10:20 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# Python 변수 만들기
<br>
<br>

---

## 1.변수와 입력 사용하기
<br>
<br>

변수(variable)을 만들고 결과를 저장하는 방법을 알아보자.
<br>
<br>

### 변수 만들기
<br>
<br>

x = 100 이라고 입력하면 100이 들어있는 변수 x가 만들어진다. 즉, 변수이름 = 값 형식이다. 이렇게 하면 변수가 생성되는 동시에 값이 할당(저장)된다.

<br>

- 영문 문자와 숫자를 사용할 수 있습니다.
- 대소문자를 구분합니다.
- 문자부터 시작해야 하며 숫자부터 시작하면 안 됩니다.
- _(밑줄 문자)로 시작할 수 있습니다.
- 특수 문자(+, -, *, /, $, @, &, % 등)는 사용할 수 없습니다.
- 파이썬의 키워드(if, for, while, and, or 등)는 사용할 수 없습니다.


~~~python

x = 100

y = "Hello, world"

~~~

### 변수의 자료형 알아내기

변수도 마찬가지로 type을 넣어 변수(객체)의 타입이 나온다.

~~~python

type(x)
<class 'int'>
type(y)
<class 'str'>

~~~



### 변수 여러 개를 한 번에 만들기
<br>
<br>

변수를 한번에 여러개 만드는 방법은 아래와 같다. 변수이름1, 변수이름2, 변수이름3 = 값1, 값2, 값3 형식으로 변수를 ,(콤마)로 구분한 뒤 각 변수에 할당될 값을 지정해주면 된다. 변수와 값의 갯수는 동일하게 맞춰주어야 한다.

~~~python

x, y, z = 10, 20, 30
x
# 10
y
# 20
z
# 30

~~~

여러개의 변수를 만들때 값이 같다면 = 같은 값을 지정할수 있다.변수1 = 변수2 = 변수3 = 값 형식으로 변수 여러 개를 =로 연결하고 마지막에 값을 할당해주면 같은 값을 가진 변수 3개가 만들어진다.

~~~python

x = y = z = 20
x
#20
y
#20
z
#20

~~~

두 변수의 값을 바꿀 수 있다. 변수1, 변수2 = 변수2, 변수1 형식으로 두 변수의 값을 바꿀 수 있다.

~~~python

x, y = 10, 20
x, y = y, x
x
# 20
y
# 10

~~~

변수를 삭제하려면 del을 사용하면 되고 확인 해 보면 아래와 같이 찾을수 없다고 나온다. 

~~~python

del x
x
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x
NameError: name 'x' is not defined

~~~

값이 들어있지 않은 빈 변수도 만들 수 있다. 변수 = None형식으로 만든다. 파이썬에서 None은 아무것도 없는 상태를 말하고 다른 언어에서는 null이라고 표현한다.

~~~python

x = None
x
# 아무것도 출력되지 않는다.
~~~



---

## 2.변수로 계산하기
<br>
<br>
계산값을 변수로 지정해 저장하는 방법을 알아보자. 변수 a, b에 숫자를 할당한 뒤에 a와 b의 값을 더해서 변수 c에 할당했다. 이렇게 변수는 변수끼리 계산할 수 있고, 계산 결과를 다른 변수에 할당할 수 있다.

~~~python

a=10
b=20
c=a+b
c
30

~~~

### 산술 연산 후 할당 연산자 사용하기
<br>
<br>
변수의 값을 증가시키는 방법이다. a의 값에20을 더할뿐 결과를 저장히지는 않는다.

~~~python

a=10
a+20
30
a
10

~~~

변수의 값을 저장하려면 결과를 다시 변수에 저장해야 한다.

~~~python

a = 10
a += 20 # a = a + 20
a
30

~~~

a를 다시 입력하지 않고 결과를 저장하는 방법이다. +=처럼 산술연신자 앞에 할당연산자(+)를 붙이면 연산 결과를 변수에 저장한다. -=, /=, //=, %=, *=도 사용 가능하다.

~~~python

a=10
a=a+20
a
30

~~~

할당 연산자를 만들때 주의할 점이다. 변수d를 지정하지 않고 코드를 입력하면 아래와 같은 에러가 나온다. 변수를 지정하고 변수를 사용해 계산을 해야한다.

~~~python

d = d +10
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    d = d +10
NameError: name 'd' is not defined. Did you mean: 'id'?

~~~

### 값을 실수로 만들기
<br>
<br>
어떤 값을 강제로 실수로 만드는 방법을 알아보자.float는 부동소수점(floating point)에서 따왔으며 값을 실수로 만들어준다. 즉, 실수는 float 자료형이며 type에 실수를 넣어보면 <class 'float'>가 나온다.

~~~python

float(1+2)
#3.0
float('5')
# 5.0
float(5.3)
# 5.3

type(3.5)
      
<class 'float'>

~~~

계산을 하다보면 부호를 붙여야 할 때도 있다. 이때는 값이나 변수 앞에 양수, 음수 부호를 붙이면 된다.

~~~python

x = -10
+x
-10
-x
10

~~~

### 복소수
<br>
<br>
파이썬에서는 실수부와 허수부로 이루어진 복소수(complex number)도 사용할 수 있다. 이때 허수부는 숫자 뒤에 j를 붙인다(수학에서는 허수를 i로 표현하지만 공학에서는 j를 사용한다).두 실수를 복소수로 만들 때는 complex를 사용하면 된다.

~~~python

1.2+1.3j
# (1.2+1.3j)
#두 실수를 복소수로 만들 때
complex(1.2, 1.3)
# (1.2+1.3j)

~~~

---

## 3.입력 값을 변수에 저장하기
<br>
<br>
매번 다른 값을 변수에 할당하는 방법을 알아보자. input()을 사용하면 사용자가 입력한 값을 가져올 수 있다.


~~~python

input()
hello, world!
'hello, world!'
input()
안상현
'안상현'

~~~

### 함수의 결과를 변수에 할당하기
<br>
<br>
input함수의 결과를 변수에 할당했다. 

~~~python

x = input()
hello world!
x
'hello world!'


~~~

위 코드에서 불편한점은 input함수가 실행된 다음에 아무 내용이 없어서 입력을 받는 상태인지 출력이 없는 상태인지 알 수가 없다는 점이다. 이때는 input의 괄호 안에 문자열을 지정해준다.

~~~python

x = input('문자열을 입력하세요')
문자열을 입력하세요우리집 강아지는 보름이
x
'우리집 강아지는 보름이'

~~~


위 코드는 사용자에게 입력받는 값의 용도를 미리 알려줄 때 사용한다. 다른 말로는 prompt라고도 부른다.

<br>
<br>

### 두 숫자의 합 구하기

<br>
<br>

숫자 두개를 입력받은 뒤에 두  숫자의 합을 구해보자. 아래 코드를 실행한 결과는 1020이다. input에서 입력받은 값은 항상 문자열 형태이기 때문이다.

~~~python

a = input('첫 번째 숫자를 입력하세요: ')
첫 번째 숫자를 입력하세요: 10
b = input('두 번째 숫자를 입력하세요: ')
두 번째 숫자를 입력하세요: 20
print(a + b)
1020

~~~~

변수에 값을 input으로 할당하고 데이터 타입을 확인하면 아래와 같이str(string)이 출력되게 된다.

~~~python

a = input()
10
type(a)
# <class 'str'>

~~~

<br>
<br>