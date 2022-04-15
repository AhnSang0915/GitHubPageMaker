---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 람다 표현식 사용하기
date: 2022-04-15 20:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 람다 표현식 사용하기

<br>
<br>
람다 표현식은 식 형태로 되어 있다고 해서 람다 표현식(lambda expression) 이라고 부든다. 특히 람다 표현식은 함수를 간편하게 작성할 수 있어서 다른 함수의 인수러 넣을 떄 주로 사용한다.

---

## 1. 람다 표현식으로 함수 만들기
<br>
<br>
람다 표현식을 사용하기 전에 먼저 숫자를 받은 뒤 10을 더해서 반환하는 함수 plus_ten을 만들어 보자. return x + 10으로 매개변수 x에 10을 더한 값을 반환하는 간단한 함수다.

 
~~~python

def plus_ten(x):
    return x + 10

plus_ten(1)
11


~~~

plus_ten함수를 람다 표현식으로 작성해보자. 람다 표현식은 아래와 같이 lambda에 매개변수를 지정하고 :(클론)뒤에 반환값으로 사용할 식을 지정한다.

- lambda 매개변수들: 식

실행하면 함수 객체가 나온다. 이상태로는 함수를 호출할 수 없다. 람다 표현식은 이름이 없는 함수를 만들기 때문이다. 그래서 람다표현식을 익명함수(anonymous function)라고도 한다.

~~~python

lambda x: x + 10
<function <lambda> at 0x02C27270>

~~~

lambda로 만든 익명 함수를 호출하려면 다음과 같이 람다 표현식을 변수에 할당해줘야한다. lambda x: x + 10은 매개변수 x 하나를 받고, x에 10을 더해서 반환한다는 뜻이다. 즉, 매개변수, 연산자, 값 등을 조합한 식으로 반환값을 만드는 방식이다. 

~~~python

plus_ten = lambda x: x + 10
plus_ten(1)
11

~~~

### 람다 표현식 자체를 호출하기
<br>
<br>
람다 표현식은 변수에 할당하지 않고 람다 표현식 자체를 바로 호출할 수 있다. 다음과 같이 람다 표현식을 ()로 묶은 뒤에 다시 ()를 붙이고 인수를 넣어서 호출하면 된다.

- (lambda 매개변수들: 식)(인수들)

~~~python

(lambda x: x + 10)(1)
11

~~~

### 람다 표현식 안에서는 변수를 만들 수 없다
<br>
<br>
람다 표현식에서 주의할 점은 람다 표현식 안에서는 새 변수를 만들 수 없다는 점이다. 따라서 반환값 부분은 변수 없이 식 한 줄로 표현할 수 있어야 한다. 변수가 필요한 코드일 경우에는 def로 함수를 작성하는 것이 좋다.

~~~python

(lambda x: y = 10; x + y)(1)
SyntaxError: invalid syntax

~~~

단, 람다 표현식 바깥에 있는 변수는 사용할 수 있다. 다음은 매개변수 x와 람다 표현식 밖의 y변수를 더해서 반환한다.

~~~python

>>> y = 10
>>> (lambda x: x + y)(1)
11

~~~

### 람다 표현식을 인수로 사용하기
<br>
<br>
람다 표현식을 사용하는 이유는 함수의 인수 부분에서 간단하게 함수를 만들기 위해서 이다. 이런 방식으로 사용하는 대표적인 예가 map이다.
<br>
람다 표현식을 사용하기 전에 먼저 def로 함수를 만들어서 map을 사용하게 만들어보자. 다음과 같이 숫자를 받은 뒤 10을 더해서 반환하는 함수 plus_ten을 작성한다. 그리도 map에 plus_ten함수와 리스트 [1, 2, 3]을 넣는다. 물론 map의 결과는 map 객체이므로 눈으로 확인할 수 있도록 list를 사용해서 리스트로 변환해준다.


~~~python

def plus_ten(x):
     return x + 10

list(map(plus_ten, [1, 2, 3]))
[11, 12, 13]

~~~

plus_ten 함수는 매개변수 x에 10을 더해서 반환하므로 리스트 [1, 2, 3]이 [11, 12, 13]으로 바뀌었다. 지금까지 map을 사용할 때 map(str, [1, 2, 3])과 같이 자료형 int, float, str등을 넣었다. plus_ten함수를 직접 만들어 넣어도 된다.
<br>
plus_ten함수 대신 람다 표현식 lambda x: x + 10을 넣었다. 적체적으로 보면 코드가 세줄에서 한 줄로 줄었다. 이처럼 란다 표현식은 함수를 다른 함수의 인수로 넣을 때 매우 편리하다.


~~~python

list(map(lambda x: x + 10, [1, 2, 3]))
[11, 12, 13]

~~~

### 람다 표현식으로 매개변수가 없는 함수 만들기
<br>
<br>
람다 표현식으로 매개변수가 없는 함수를 만들 때는 lambda 뒤에 아무것도 지정하지 않고 :(콜론)을 붙인다. 단, 콜론 뒤에는 반드시 반환할 값이 있어야 한다. 왜냐하면 표현식(expression)은 반드시 값으로 평가되어야 하기 때문이다.

~~~python

(lambda : 1)()
1
x = 10
>>> (lambda : x)()
10

~~~

---

## 2. 람다 표현식과 map, filter, reduce 함수 활용하기
<br>
<br>
람다 표현식과 map, filter, reduce 함수를 함께 사용해보자.


### 람다 표현식에 조건부 표현식 사용하기
<br>
<br>
람다 표현식에서 조건부 표현식을 사용하는 방법을 알아보자.

- lambda 매개변수들: 식1 if 조건식 else 식2

다음은 map을 사용하여 리스트 a에서 3의 배수를 문자열로 변환한다. map은 리스트의 요소를 각각 처리하므로 lambda의 반환값도 요소여야 한다. 여기서는 요소가 3의 배수일 때는 str(x)로 요소를 문자열로 만들어서 반환했고, 3의 배수가 아닐 때는 x로 요소를 그대로 반환했다.

~~~python

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a)) 
# 람다 표현식 안에서의 if와 else를 사용할떄는 :을 붙이지 않는다
[1, 2, '3', 4, 5, '6', 7, 8, '9', 10]

~~~

람다 표현식 안에서 조건=부 표현식 if, else를 사용할 때는 :(콜론)을 붙이지 않는다. 일반적인 if, else와 문법이 다르므로 주의해야 한다. 조건부 표현식은 식1 if 조건식 else 식2 형식으로 사용하며 식1은 조건이 참일때, 식2는 조건식이 거짓일 때 사용할 식이다.
특히 람다 표현식에서 if를 사용했다면 반드시 else를 사용해야 한다. 다음과 같이 if만 사용하면 문법 에러가 발생하므로 주의해야 한다.

~~~python

list(map(lambda x: str(x) if x % 3 == 0, a))
SyntaxError: invalid syntax

~~~

그리도 람다 표현식 안에서는 elif를 사용할 수 없다. 따라서 조건부 표현식은 식1 if 조건식1 else 식2 if 조건식2 else 식3 형식처럼 if를 연속으로 사용해야 한다. 예를 들어 리스트에서 1은 무자열로 반환하고, 2는 실수로 변환, 3이상은 10을 더하는 식은 다음과 같이 만든다.

- lambda 매개변수들: 식1 if 조건식1 else 식2 if 조건식2 else 식3

~~~python

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]

~~~

def로 함수를 만들고 if, elif, else를 사용해 나타내면 아래와 같다.

~~~python

def f(x):
     if x == 1:
         return str(x)
     elif x == 2:
         return float(x)
     else:
         return x + 10

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list(map(f, a))
['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]

~~~

### map에 객체를 여러 개 넣기
<br>
<br>
map은 리스트 등의 반복 가능한 객체를 여러 개 넣을 수도 있다. 다음은 두 리스트의 요소를 곱해서 새 리스트를 만든다.

~~~python

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
list(map(lambda x, y: x * y, a, b))
[2, 8, 18, 32, 50]

~~~

이렇게 리스트 두 개를 처리할 때는 람다 표현식에서 lambda x, y: x*y처럼 매개변수를 두개로 지정하면 된다. 그리고 map에 람다 표현식을 넣고 그 다음에 리스트 두 개를 콤마로 구분해서 넣어준다. 즉, 람다 표현식의 매개변수 개수에 맞게 반복 가능한 객체도 콤마로 구분해서 넣어준다.

### filter 사용하기
<br>
<br>
이번에는 filter를 사용해보자. filter는 반복 가능한 객체에서 특정 조건에 맞는 요소만 가져오는데, filter에 지정한 함수의 반환값이 True일 때만 해당 요소를 가져온다.

- filter(함수, 반복가능한객체)

먼저 def로 함수를 만들어서 filter를 사용해보자. 다음은 리스트에서 5보다 크면서 10보다 작은 숫자를 가져온다. 리스트 a에서 8, 7, 9를 가져왔다. 즉, filter는 x > 5 and x < 10의 결과가 참인 요소만 가져오고 거짓인 요소는 버린다.

~~~python

def f(x):
     return x > 5 and x < 10

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(f, a))
[8, 7, 9]
# 리스트 a는 여전히 [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]

~~~

그럼 함수 f를 람다 표현식으로 만들어 보자.

~~~python

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
list(filter(lambda x: x > 5 and x < 10, a))

~~~

### reduce 사용하기
<br>
<br>
reduce를 사용해 보자. reduce는 반복 가능한 객체의 각 요소를 지정된 함수로 처리한 뒤 이전 결과와 누적해서 반환하는 함수이다.

- from functools import reduce
- reduce(함수, 반복가능한객체)

다음은 리스트에 저장된 요소를 순서대로 더한 뒤 누적된 결과를 반환한다. reduce의 반환값이 15가 나왔다. 함수 f에서 x + y를 반환하도록 만들었으므로 reduce는 그림과 같이 요소 두 개를 계속 더하면서 결과를 누적한다.

~~~python

def f(x, y):
     return x + y

a = [1, 2, 3, 4, 5]
from functools import reduce
reduce(f, a) #1과2를 더하고 더한값인 3과 3을 더하고 6과4를 더하고 10과 5를 더한다.
15

~~~

이제는 함수 f를 람다 표현식으로 만들어서 reduce에 넣어보자.

~~~python

a = [1, 2, 3, 4, 5]
from functools import reduce
reduce(lambda x, y: x + y, a)
15

~~~

### map, filter, reduce와 리스트 표현식
<br>
<br>
리스트(딕셔너리, 세트)표현식으로 처리할 수 있는 경우에는 map, filter와 람다 표현식 대신 리스트 표현식을 사용하는 것이 좋다. list(filter(lambda x: x > 5 and x < 10 ,a>))는 다음과 같이 리스트 표현식으로도 만들 수 있다.

~~~python

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
[i for i in a if i > 5 and i < 10]
[8, 7, 9]

~~~

또한, for, while 반복문으로 처리할 수 있는 경우에도 reduce 대신 for, while을 사용하는 것이 좋다. 왜냐하면 reduce는 코드가 조금만 복잡해져도 의미하는 바를 한 눈에 알아보기가 힘들기 때문이다. 이러한 이유로 파이썬 3부터는 reduce가 내장 함수에서 제외되었다.
reduce(lambda x, y: x + y, a)는 다음과 같이 for 반복문으로 표현할 수 있습니다.

~~~python

a = [1, 2, 3, 4, 5]
x = a[0]
for i in range(len(a) - 1):
     x = x + a[i + 1]

x
15

~~~

---

### 예제1
<br>
<br>
다음 소스 코드를 완성하여 확장자가 .jpg, .png인 이미지 파일만 출력되게 만드세요. 여기서는 람다 표현식을 사용해야 하며 출력 결과는 리스트 형태라야 합니다. 람다 표현식에서 확장자를 검사할 때는 문자열 메서드를 활용하세요..

~~~python

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
 
print(                                                                           )

#실행결과
['1.png', '10.jpg', '2.jpg', '3.png']

~~~


답

~~~python

list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files))
 # find(x)는 찾을 문자열 x가 있으면 인덱스 값을 반환하고 없으면 -1을 반환한다.
~~~

### 예제2
<br>
<br>
표준 입력으로 숫자.확장자 형식으로 된 파일 이름 여러 개가 입력됩니다. 다음 소스 코드를 완성하여 파일 이름이 숫자 3개이면서 앞에 0이 들어가는 형식으로 출력되게 만드세요. 예를 들어 1.png는 001.png, 99.docx는 099.docx, 100.xlsx는 100.xlsx처럼 출력되어야 합니다. 그리고 람다 표현식을 사용해야 하며 출력 결과는 리스트 형태라야 합니다. 람다 표현식에서 파일명을 처리할 때는 문자열 포매팅과 문자열 메서드를 활용하세요.

~~~python

files = input().split()
 
print(________________)

#예
1.jpg 10.png 11.png 2.jpg 3.png
#결과
['001.jpg', '010.png', '011.png', '002.jpg', '003.png']

#예
97.xlsx 98.docx 99.docx 100.xlsx 101.docx 102.docx
#결과
['097.xlsx', '098.docx', '099.docx', '100.xlsx', '101.docx', '102.docx']

~~~

답

~~~python

list(map(lambda x: '{0:03d}'.format(int(x.split('.')[0])) + '.' + x.split('.')[1],files))

~~~

주어진 값을 살펴보면 '1.jpg'로 .기준으로 숫자와 문자로 나눌 수 있다. 따라서 split을 이용해 files의 각 요소를 .을 기준으로 나누어 ['1', 'jgp']식으로 리스트로 만든다. 그 다음 첫번쨰 요소를 숫자로 포매팅 해야하기 때문에 int로 정수형으로 바꿔준다. 그후 숫자형 포매팅 방법중 ‘{인덱스:0개수d’}’.format(숫자) 으로 0을 붙여준다. 이후 .를 더해주고 거기에 다시 아까 나누어 놓았던 문자열 x.split('.')[1]을 더해준다.