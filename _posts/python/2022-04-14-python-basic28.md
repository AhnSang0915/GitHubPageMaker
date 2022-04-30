---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 함수에서 위치 인수와 키워드 인수 사용하기
date: 2022-04-14 15:50 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 함수에서 위치 인수와 키워드 인수 사용하기

<br>
<br>
파이썬에서는 함수를 좀 더 편리하게 사용할 수 있도록 다양한 기능을 제공한다. 이번에는 함수에서 위치 인수, 키워드 인수를 사용하는 방법과 리스트, 딕셔너리 언패킹(unpacking)을 활용하는 방법을 알아보자.

---

## 1. 위치 인수와 리스트 언패킹 사용하기
<br>
<br>
다음과 같이 함수에 인수를 순서대로 넣는 방식을 위치 인수(positional argument)라고 한다. 즉, 인수의 위치가 정해져 있다. print에 10, 20, 30 순으로 넣었으므로 출력될 때도 10 20 30으로 출력된다.
 
~~~python

print(10, 20, 30)
10 20 30

~~~


### 위치 인수를 사용하는 함수를 만들고 호출하기
<br>
<br>
숫자 세 개를 각 줄에 출력하는 함수를 만들어보자. print_numbers에 숫자 세개를 넣으면 각 줄에 숫자가 출력된다.

~~~python

def print_numbers(a, b, c):
     print(a)
     print(b)
     print(c)

print_numbers(10, 20, 30)
#출력
10
20
30

~~~

### 언패킹 사용하기
<br>
<br>
이렇게 인수를 순서대로 넣을 때는 리스트나 튜플을 사용할 수도 있다. 다음과 같이 리스트 또는 튜플 앞에 *를 붙여서 함수에 넣어주면 된다. print_numbers에 10, 20, 30이 들어있는 리스트 x를 넣고 *만 붙였는데도 숫자가 각 줄에 출력되었다. 즉, 리스트(튜플) 앞에 *를 붙이면 언패킹(unpacking)이 되어서 print_numbers(10, 20, 30)과 똑같은 동작이다. 말 그대로 리스트의 포장을 푼다는 뜻이다.

- 함수(*리스트)
- 함수(*튜플)

~~~python

x = [10, 20, 30]
print_numbers(*x)
10
20
30

~~~

리스트 변수 대신 리스트 앞에 바로 *를 붙여도 동작은 같다. 단, 이때 함수의 매개변수 개수와 리스트의 요소 개수는 같아야 한다. 만약 개수가 다르면 함수를 호출할 수 없다. 단 이때 함수의 매개변수 개수와 리스트의 요소 개수는 같아야 한다. 여기서는 함수를 def print_numbers(a, b, c):로 만들었으므로 리스트에는 요소를 3개 넣어야 한다.

~~~python

print_numbers(*[10, 20, 30])
# 출력
10
20
30

# 매개변수를 2개 넣었을때
print_numbers(*[10, 20])
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    print_numbers(*[10, 20])
TypeError: print_numbers() missing 1 required positional argument: 'c'
~~~ 

### 가변 인수 함수 만들기
<br>
<br>
가변인수와 리스트 언패킹은 인수의 개수가 정해지지 않은 가변 인수(variable argument)에 사용한다. 즉, 같은 함수에 인수 한개를 넣을 수도 있고, 열 개를 넣을 수도 있다. 또는 인수를 넣지 않을 수도 있다. 다음과 같이 가변 인수 함수는 매개변수 앞에 *를 붙여서 만든다.

~~~python

def 함수이름(*매개변수):
    코드

~~~

이제 숫자 여러 개를 받고, 숫자를 각 줄에 출력하는 함수를 만들어보자. 다음과 같이 함수를 만들 때 괄호 안에 *args와 같이 매개변수 앞에 *를 붙인다. 그리고 함수 안에서는 for로 args를 반복하면서 print로 값을 출력한다. 매개변수 이름은 원하는 대로 지어도 되지만 관례적으로 arguments를 줄여서 args로 사용힌다. 특히 이 args는 튜플이라서 for로 반복할 수 있다.

~~~python

def print_numbers(*args):
     for arg in args:
         print(arg)

~~~

그럼 print_numbers 함수에 숫자를 넣어서 호출해보자. 숫자를 한 개 넣으면 한 개 출력되고, 네 개 넣으면 네 개가 출력된다. 즉, 넣은 숫자 개수만큼 출력한다.

~~~python

print_numbers(10)
10
print_numbers(10, 20, 30, 40)
10
20
30
40

~~~

리스트(튜플)언패킹을 사용해도 된다. 다음과 같이 숫자가 들어있는 리스트를 만들고 앞에 \*를 붙여서 넣어보면 리스트에 들어있는 값이 그대로 출력된다. 즉, 리스트 x는 \[10]이므로 print_numbers(*x)로 호출하면 print_numbers(10)과 같고 리스트 y는 [10, 20, 30, 40]이므로 print_numbers(10, 20, 30, 40)과 같다.

~~~python

x = [10]
print_numbers(*x)
10
y = [10, 20, 30, 40]
print_numbers(*y)
10
20
30
40

~~~

### 고정 인수와 가변 인수를 함께 사용하기
<br>
<br>
고정 인수와 가변 인수를 함께 사용할 때는 다음과 같이 고정 매개변수를 먼저 지정하고, 그 다음 매개변수에 *를 붙여주면 된다. 단, 이때 def print_numbers(*args, a):처럼 *args가 고정 매개변수보다 앞쪽에 오면 안된다. 매개변수 순서에서 *args는 반드시 가장 뒤쪽에 와야 한다.

~~~python

def print_numbers(a, *args):
     print(a)
     print(args)

print_numbers(1)
1
()
print_numbers(1, 10, 20)
1
(10, 20)
print_numbers(*[10, 20, 30])
10
(20, 30)

~~~

---

## 2. 키워드 인수 사용하기
<br>
<br>
지금까지 함수에 인수를 넣을 때 값이나 변수를 그대로 넣었다. 그러다 보니 각각의 인수가 무슨 용도인지 알기 어려웠다. 보통은 함수의 사용 방법을 익힐 때 인수의 순서와 용도를 함께 외운다. 예를 들어 개인정보를 출력하는 함수를 만들어 보자. 이 함수를 사용할 때는 첫 번째 인수에 이름(name), 두 번째 인수에 나이( age), 세 번째 인수에 주소(address)를 넣어야 한다. 만약 인수의 순서가 달라지면 잘못된 결과가 출력될것이다.

~~~python

def personal_info(name, age, address):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)

personal_info('홍길동', 30, '서울시 용산구 이촌동')
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동

~~~

이처럼 인수의 순서와 용도를 모두 기억해야 해서 불편하다. 그래서 파이썬에서는 인수의 순서와 용도를 매번 기억하지 않도록 키워드 인수(keyword argument)라는 기능을 제공한다. 키워드 인수는 말 그대로 인수에 이름(키워드)을 붙이는 기능인데 키워드 = 값 형식으로 사용한다.

- 함수(키워드=값)

그럼 personal_info 함수를 키워드 인수 방식으로 호출해보자.

~~~python

personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동

~~~

위에처럼 키워드 인수를 사용하니 함수를 호출할 때 인수의 용도가 명확하게 보인다. 특히 키워드 인수를 사용하면 인수의 순서를 맞추지 않아도 키워드에 해당하는 값이 들어간다. personal_info 함수는 이름, 나이, 주소 순으로 인수를 넣어야 하지만, 키워드 인수를 사용해서 순서를 지키지 않고 값을 넣었다. 참고로 print 함수에서 사용했던 sep, end도 키워드 인수이다.

~~~python

personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동')
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동

print(10, 20, 30, sep=':', end='')

~~~

---

## 3. 키워드 인수와 딕셔너리 언패킹 사용하기
<br>
<br>
딕셔너리를 사용해서 키워드 인수로 값을 넣는 딕셔너리 언패킹을 사용해보자. 다음과 같이 딕셔너리 앞에 **를 붙여서 함수에 넣어준다.

- 함수(**딕셔너리)

먼저 personal_info 함수를 만든다.

~~~python

def personal_info(name, age, address):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)

~~~

딕셔너리에 '키워드 : 값' 형식으로 인수를 저장하고, 앞에 **를 붙여서 함수에 넣어준다. 이때 딕셔너리의 키워드(키)는 반드시 문자열 형태여야 한다.

~~~python

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동

~~~

**x처럼 딕셔너리를 언패킹하면 딕셔너리의 값들이 함수의 인수로 들어간다. 즉, personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동') 또는 personal_info('홍길동', 30, '서울시 용산구 이촌동')과 똑같은 동작이 된다.
<br>
딕셔너리 변수 대신 딕셔너리 바로 앞에 **를 붙여도 동작은 같다. 딕셔너리 언패킹을 사용할 때는 함수의 매개변수 이름과 딕셔너리의 키 이름이 같아야 한다. 또한, 매개변수 개수와 딕셔너리 키의 개수도 같아야 한다.

~~~python

personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동

~~~

만약 이름과 개수가 다르면 함수를 호출할 수 없다.  함수를 def personal_info(name, age, address):로 만들었으므로 딕셔너리도 똑같이 맞춰주어야한다. 다음과 같이 매개변수 이름, 개수가 다른 딕셔너리를 넣으면 에러가 발생한다.

~~~python

personal_info(**{'name': '홍길동', 'old': 30, 'address':'서울시 용산구 이촌동'})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: personal_info() got an unexpected keyword argument 'old'
personal_info(**{'name': '홍길동', 'age': 30})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: personal_info() missing 1 required positional argument: 'address'

~~~


### **를 두 번 사용하는 이유
<br>
<br>
딕셔너리는 키-값 쌍형태로 값이 저장되어 있기때문에 **를 두번 사용한다. *를 한번만 사용해서 함수를 호출하면 아래와 같은 결과가 나온다.

~~~python

def personal_info(name, age, address):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(*x)
이름:  name
나이:  age
주소:  address

~~~

personal_info에 *x를 넣으면 x의 키가 출력됩니다. 즉, 딕셔너리를 한 번 언패킹하면 키를 사용한다는 뜻이 된다. 따라서 **처럼 딕셔너리를 두 번 언패킹하여 값을 사용하도록 만들어야 한다.

~~~python

x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**x)
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동

~~~

### 키워드 인수를 사용하는 가변 인수 함수 만들기
<br>
<br>
이번에는 키워드 인수를 사용하는 가변 인수 함수를 만들어보자. 다음과 같이 키워드 인수를 사용하는 가변 인수 함수는 매개변수 앞에 **를 붙여서 만든다.

~~~python

def 함수이름(**매개변수):
    코드

~~~

이제 값 여러 개를 받아서 매개 변수 이름과 값을 각 줄에 출력하는 함수를 만들어보자.
함수를 만들 때 괄호 안에 **kwargs와 같이 매개변수 앞에 **를 붙인다. 함수 안에서는 for로 kwargs.items()를 반복하면서 print로 값을 출력한다. 매개변수 이름은 원하는 대로 지어도 되지만 관례적으로 keyword arguments를 줄여서 kwargs로 사용한다. 특히 이 kwargs는 딕셔너리라서 for로 반복할 수 있다.

~~~python

def personal_info(**kwargs):
     for kw, arg in kwargs.items():
         print(kw, ': ', arg, sep='')

~~~

personal_info 함수에 키워드와 값을 넣어서 실행해보자. 값을 한 개 넣어도 되고, 세 개 넣어도 된다.

~~~python

personal_info(name='홍길동')
name: 홍길동
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
name: 홍길동
age: 30
address: 서울시 용산구 이촌동)

~~~

위에처럼 인수를 직접 넣어도 되고, 딕셔너리 언패킹을 사용해도 된다. 다음과 같이 딕셔너리를 만들고 앞에 \**를 붙여서 넣어보면 딕셔너리에 있는 값들이 그대로 출력된다. 즉, 딕셔너리 x는 {'name': '홍길동'}이므로 personal_info(**x)로 호출하면 personal_info(name='홍길동')과 같고, 딕셔너리 y는 {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}이므로 personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')과 같다.

~~~python

x = {'name': '홍길동'}
personal_info(**x)
name: 홍길동
y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**y)
name: 홍길동
age: 30
address: 서울시 용산구 이촌동

~~~

이처럼 함수를 만들 때 def personal_info(**kwargs):와 같이 매개변수에 **를 붙여주면 키워드 인수를 사용하는 가변 인수 함수를 만들 수 있다. 그리고 이런 함수를 호출할 때는 키워드와 인수를 각각 넣거나 딕셔너리 언패킹을 사용하면 된다. 보통 **kwargs를 사용한 가변 인수 함수는 다음과 같이 함수 안에서 특정 키가 있는지 확인한 뒤 해당 기능을 만든다.

~~~python

def personal_info(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

~~~

### 고정 인수와 가변 인수(키워드 인수)를 함께 사용하기
<br>
<br>
고정인수와 가변인수를 함께 사용 하려면 다음과 같이 고정 매개변수를 먼저 지정하고, 그 다음 매개변수에 **를 붙여주면 된다. 단, 이때 def personal_info(**kwargs, name):처럼 **kwargs가 고정 매개변수보다 앞쪽에 오면 안된다. 매개변수 순서에서 **kwargs는 반드시 가장 뒤쪽에 와야 한다.

~~~python

def personal_info(name, **kwargs):
     print(name)
     print(kwargs)

personal_info('홍길동')
홍길동
{}
personal_info('홍길동', age=30, address='서울시 용산구 이촌동')
홍길동
{'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
홍길동
{'age': 30, 'address': '서울시 용산구 이촌동'}

~~~

### 위치 인수와 키워드 인수를 함께 사용하기
<br>
<br>
함수에서 위치인수를 받는 *args와 키워드 인수를 받는 **kwargs를 함께 사용하려면 다음과 같이 함수의 매개변수를 *args, **kwargs로 지정하여 위치 인수와 키워드 인수를 함께 사용할수 있다.
대표적인 함수가 print인데 print는 출력할 값을 위치 인수로 넣고 sep, end 등을 키워드 인수로 넣는다. 고정인수와 마찬가지로  def custom_print(**kwargs, *args):처럼 **kwargs가 *args보다 앞쪽에 오면 안된다. 매개변수 순서에서 **kwargs는 반드시 가장 뒤쪽에 와야 한다. 특히 고정 매개변수와 *args, **kwargs를 함께 사용한다면 def custom_print(a, b, *args, **kwargs):처럼 매개변수는 고정 매개변수, *args, **kwargs 순으로 지정해야 한다.

~~~python

>>> def custom_print(*args, **kwargs):
     print(*args, **kwargs)

>>> custom_print(1, 2, 3, sep=':', end='')
1:2:3
~~~

---

## 4. 매개변수에 초깃값 지정하기
<br>
<br>

지금까지 함수를 호출할때 인수를 넣어 값을 전달했다. 그러면 인수를 생략할 수는 없을까? 이때는 함수의 매개변수에 초깃값을 지정하면 된다. 초깃값은 다음과 같이 함수를 만들때 **매개변수=값** 형식으로 지정한다.

~~~python

def 함수이름(매개변수=값):
    코드

~~~

매개변수의 초깃값은 주로 사용하는 값이 있으면서 가끔 다른 값을 사용해야 할 떄 활용한다. 대표적 예가 print 함수인데, print함수의 sep는 초깃값이 ' '(공백)으로 지정되어 있어서 대부분 그대로 사용하고 가끔 sep에 다른 값을 넣어서 사용한다.
<br>
이제 personal_info 함수에서 매개변수 address의 초깃값을 '비공개'로 지정해보자.

~~~python

def personal_info(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

def personal_info(name, age, address='비공개'):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)

   
~~~

address는 초깃값이 있으므로 personal_info는 다음과 같이 address부분을 비워 두고 호출할 수 있다.

~~~python

personal_info('홍길동', 30)
이름:  홍길동
나이:  30
주소:  비공개

~~~

매개변수에 초깃값이 있더라도 값을 넣으면 해당 값이 전달된다.

~~~python

personal_info('홍길동', 30, '서울시 용산구 이촌동')
이름:  홍길동
나이:  30
주소:  서울시 용산구 이촌동

~~~


### 초깃값이 지정된 매개변수의 위치
<br>
<br>
매개변수의 초깃값을 지정할때는 초깃값이 지정된 매개변수 다음에는 초깃값이 없는 매개변수가 올 수 없다. ersonal_info 함수에서 address가 가장 마지막 매개변수였는데 이번에는 address를 두 번째 매개변수로 만들고, 그 다음에 초깃값을 지정하지 않은 age가 오도록 만들면 에러가 발생한다. 그이유는 personal_info('홍길동', 30)으로 함수를 호출했을 때 30이 어디로 들어가야 할지 알 수가 없기 떄문이다. address에 들어가려니 age부분이 비어 버린다. 잘못된 문법이므로 이렇게 만들면 안된다.



~~~python

def personal_info(name, address='비공개', age):
     print('이름: ', name)
     print('나이: ', age)
     print('주소: ', address)

  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument

~~~

즉, 다음과 같이 초깃값이 지정된 매개변수는 뒤쪽에 몰아주면 된다.

~~~python

def personal_info(name, age, address='비공개'):
def personal_info(name, age=0, address='비공개'):
def personal_info(name='비공개', age=0, address='비공개'):

~~~

따라서 return 1, 2는 return (1, 2)와 의미가 같다. def personal_info(name='비공개', age=0, address='비공개'):와 같이 모든 매개변수에 초깃값을 지정하면 personal_info()처럼 인수를 넣지 않고 호출할 수 있습니다.

~~~python

def one_two():
    return 1, 2    # return (1, 2)와 같음

~~~


---

### 예제
<br>
<br>
표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 다음 소스 코드를 완성하여 가장 높은 점수, 가장 낮은 점수, 평균 점수가 출력되게 만드세요. 평균 점수는 실수로 출력되어야 합니다.


~~~python

korean, english, mathematics, science = map(int, input().split())

________________
________________
________________
________________

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                            mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))
 
min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))



#입력

76 82 89 84

#결과

낮은 점수: 76.00, 높은 점수: 89.00, 평균 점수: 82.75
낮은 점수: 82.00, 높은 점수: 84.00, 평균 점수: 83.0

#입력

89 92 73 83

#결과

낮은 점수: 73.00, 높은 점수: 92.00, 평균 점수: 84.25
낮은 점수: 83.00, 높은 점수: 92.00, 평균 점수: 87.50

~~~

답

~~~python

def get_min_max_score(*args):
    return min(args), max(args) 
    
def get_average(**kwargs):
    average = sum(kwargs.values())/len(kwargs) #dict.values() 딕셔너리의 모든 값을 가져온다.
    return average

~~~