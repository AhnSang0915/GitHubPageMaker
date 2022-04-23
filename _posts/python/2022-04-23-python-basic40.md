---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 데코레이터 사용하기
date: 2022-04-23 16:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 데코레이터 사용하기

<br>
<br>
파이썬은 데코레이터(decorator)라는 기능을 제공한다. 장식하는 도구 정도로 생각하면 되고 전에 배운 내용중 클래스에서 메서드를 만들 때 @staticmethod, @classmethod, @abstractmethod 등을 붙여 사용했는데 이렇게 @로 시작하는 것들이 데코레이터 이다. 데이코레이터는 장식자 라고도 부른다.

~~~python

class Calc:
    @staticmethod    # 데코레이터
    def add(a, b):
        print(a + b)

~~~


---

## 1.데코레이터 만들기
<br>
<br>
데코레이터는 함수를 수정하지 않은 상태에서 추가 기능을 구현할 때 사용한다. 예를 들어서 함수의 시작과 끝을 출력하고 싶다면 다음과 같이 함수 시작, 끝 부분에 print를 넣어준다.

~~~python

def hello():
    print('hello 함수 시작')
    print('hello')
    print('hello 함수 끝')
 
def world():
    print('world 함수 시작')
    print('world')
    print('world 함수 끝')
 
hello()
world()


# 실행 결과
hello 함수 시작
hello
hello 함수 끝
world 함수 시작
world
world 함수 끝

~~~

위 코드에서 다른 함수도 시작과 끝을 출력하고 싶다면 함수를 만들 때마다 print를 넣어야 한다. 따라서 함수가 많아지면 번거롭기 때문에 이런 경우는 데코레이터를 활용한다. 다음은 함수 시작과 끝을 출력하는 데코레이터이다.

~~~python

def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():                           # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
 
def hello():
    print('hello')
 
def world():
    print('world')
 
trace_hello = trace(hello)    # 데코레이터에 호출할 함수를 넣음
trace_hello()                 # 반환된 함수를 호출
trace_world = trace(world)    # 데코레이터에 호출할 함수를 넣음
trace_world()                 # 반환된 함수를 호출


# 실행 결과
hello 함수 시작
hello
hello 함수 끝
world 함수 시작
world
world 함수 끝

~~~

먼저 데코레이터 trace는 호출할 함수를 매개변수로 받는다. trace함수 안에서는 호출할 함수를 감싸는 함수 wrapper를 만든다. 이제 wrapper함수 에서는 함수의 시작을 알리는 문자열을 출력하고, trace에서 매개변수로 받은 func를 호출한다. 그다음에 함수의 끝을 알리는 문자열을 출력한다. 여기서 매개변수로 받은 함수의 원래 이름을 출력할 때는 \__name__ 속성을 활용한다. 마지막으로 wrapper 함수를 다 만들었으면 return을 사용하여 wrapper 함수 자체를 반환한다.

~~~python

def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():                           # 호출할 함수를 감싸는 함수
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환

~~~

즉, 함수 안에서 함수를 만들고 반환하는 클로저 이다. 

데코레이터를 사용할 때는 trace에 호출할 함수 hello또는 world를 넣는다. 그다음에 데코레이터에서 반환된 함수를 호출한다. 이렇게 하면 데코레이터에 인수로 넣은 함수를 호출하고 시작과 끝을 출력한다.



### @로 데코레이터 사용하기
<br>
<br>
이제 @을 사용하여 좀 더 간편하게 데코레이터를 사용해보자. 다음과 같이 호출할 함수 위에 @데코레이터 형식으로 지정한다.

~~~python

@데코레이터
def 함수이름():
    코드

~~~

~~~python

def trace(func):                             # 호출할 함수를 매개변수로 받음
    def wrapper():
        print(func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        func()                               # 매개변수로 받은 함수를 호출
        print(func.__name__, '함수 끝')
    return wrapper                           # wrapper 함수 반환
 
@trace    # @데코레이터
def hello():
    print('hello')
 
@trace    # @데코레이터
def world():
    print('world')
 
hello()    # 함수를 그대로 호출
world()    # 함수를 그대로 호출

# 실행 결과
hello 함수 시작
hello
hello 함수 끝
world 함수 시작
world
world 함수 끝

~~~

hello와 world함수 위에 @trace를 붙인 뒤에 hello 와 world함수를 그대로 호출하면 끝이다.

~~~python

@trace    # @데코레이터
def hello():
    print('hello')
 
@trace    # @데코레이터
def world():
    print('world')
 
hello()    # 함수를 그대로 호출
world()    # 함수를 그대로 호출

~~~

### 데코레이터를 여러 개 지정하기
<br>
<br>
함수에는 데코레이터를 여러 개 지정할 수 있다. 다음과 같이 함수 위에 데코레이터를 여러 줄로 지정해준다. 이때 데코레이터가 실행되는 순서는 위에서 아래 순서.

~~~python

@데코레이터1
@데코레이터2
def 함수이름():
    코드

def decorator1(func):
    def wrapper():
        print('decorator1')
        func()
    return wrapper
 
def decorator2(func):
    def wrapper():
        print('decorator2')
        func()
    return wrapper
 
# 데코레이터를 여러 개 지정
@decorator1
@decorator2
def hello():
    print('hello')
 
hello()

# 실행 결과
decorator1
decorator2
hello

~~~



--

## 2.매개변수와 반환값을 처리하는 데코레이터 만들기 
<br>
<br>
지금까지 매개변수와 반환값이 없는 함수의 데코레이터를 만들었다. 이번에는 매개변수와 반환값을 처리하는 데코레이터 만드는 방법에 대해 알아보자. 다음은 함수의 매개변수와 반환값을 출력하는 데코레이터다.

~~~python

def trace(func):          # 호출할 함수를 매개변수로 받음
    def wrapper(a, b):    # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
        r = func(a, b)    # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))  # 매개변수와 반환값 출력
        return r          # func의 반환값을 반환
    return wrapper        # wrapper 함수 반환
 
@trace              # @데코레이터
def add(a, b):      # 매개변수는 두 개
    return a + b    # 매개변수 두 개를 더해서 반환
 
print(add(10, 20))

# 실행 결과
add(a=10, b=20) -> 30
30

~~~

add 함수를 호출했을 때 데코레이터를 통해서 매개변수와 반환값이 출력되었다. 매개변수와 반환값을 처리하는 데코레이터를 만들때는 먼저 안쪽 wrapper함수의 개개변수를 호출할 함수 add(a, b)의 매개변수와 똑같이 만들어준다.

~~~python

def trace(func):          # 호출할 함수를 매개변수로 받음
    def wrapper(a, b):    # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정

~~~

wrapper 함수 안에서는 func를 호출하고 반환값을 변수에 저장한다. 그다음에 print로 매개변수와 반환값을 출력한다. 이때 func에는 매개변수 a와 b를 그대로 넣어준다. 또한, add 함수는 두 수를 더해서 반환해야 하므로 func의 반환값을 return으로 반환해준다.

~~~python

def trace(func):          # 호출할 함수를 매개변수로 받음
    def wrapper(a, b):    # 호출할 함수 add(a, b)의 매개변수와 똑같이 지정
        r = func(a, b)    # func에 매개변수 a, b를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))    # 매개변수와 반환값 출력
        return r          # func의 반환값을 반환
    return wrapper        # wrapper 함수 반환

~~~

만약 wrapper 함수에서 func의 반환값을 반환하지 않으면 add 함수를 호출해도 반환값이 나오지 않으므로 주의해야 한다. 참고로 wrapper 함수에서 func의 반환값을 출력할 필요가 없으면 return func(a, b)처럼 func를 호출하면서 바로 반환해도 된다.

데코레이터를 사용할 때는 @로 함수 위에 지정해주면 된다. 또한, @로 데코레이터를 사용했으므로 add 함수는 그대로 호출해준다.

~~~python

@trace              # @데코레이터
def add(a, b):      # 매개변수는 두 개
    return a + b    # 매개변수 두 개를 더해서 반환

~~~

### 가변 인수 함수 데코레이터
<br>
<br>
def add(a, b):는 매개변수의 개수가 고정된 함수다. 그러면 매개변수(인수)가 고정되지 않은 함수는 어떻게 처리할까? 이때는 wrapper 함수를 가변 인수 함수로 만들면 된다.

~~~python

def trace(func):                     # 호출할 함수를 매개변수로 받음
    def wrapper(*args, **kwargs):    # 가변 인수 함수로 만듦
        r = func(*args, **kwargs)    # func에 args, kwargs를 언패킹하여 넣어줌
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
                                     # 매개변수와 반환값 출력
        return r                     # func의 반환값을 반환
    return wrapper                   # wrapper 함수 반환
 
@trace                   # @데코레이터
def get_max(*args):      # 위치 인수를 사용하는 가변 인수 함수
    return max(args)
 
@trace                   # @데코레이터
def get_min(**kwargs):   # 키워드 인수를 사용하는 가변 인수 함수
    return min(kwargs.values())
 
print(get_max(10, 20))
print(get_min(x=10, y=20, z=30))

# 실행 결과
get_max(args=(10, 20), kwargs={}) -> 20
20
get_min(args=(), kwargs={'x': 10, 'y': 20, 'z': 30}) -> 10
10

~~~

get_max 함수와 get_min 함수는 가변 인수 함수다. 따라서 데코레이터도 가변 인수 함수로 만들어준다. 이때 위치 인수와 키워드 인수를 모두 받을 수 있도록 *args와 **kwargs를 지정해준다.

~~~python

def trace(func):                     # 호출할 함수를 매개변수로 받음
    def wrapper(*args, **kwargs):    # 가변 인수 함수로 만듦
        r = func(*args, **kwargs)    # func에 args, kwargs를 언패킹하여 넣어줌
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))
                                     # 매개변수와 반환값 출력
        return r                     # func의 반환값을 반환
    return wrapper                   # wrapper 함수 반환

~~~

이렇게 만든 데코레이터 trace는 위치 인수와 키워드 인수를 모두 처리할 수 있다. 따라서 가변 인수 함수뿐만 아니라 일반적인 함수에도 사용할 수 있다.

~~~python

@trace
 def add(a, b):
    return a + b

add(10, 20)
add(args=(10, 20), kwargs={}) -> 30
30

~~~

### 메서드에 데코레이터 사용하기
<br>
<br>
클래스를 만들면서 메서드에 데코레이터를 사용할 때는 self를 주의해야 한다. 인스턴스 메서드는 항상 self를 받으므로 데코레이터를 만들 때도 wrapper 함수의 첫 번째 매개변수는 self로 지정해야 한다(클래스 메서드는 cls). 마찬가지로 func를 호출할 때도 self와 매개변수를 그대로 넣어야 한다.

~~~python

def trace(func):
    def wrapper(self, a, b):   # 호출할 함수가 인스턴스 메서드이므로 첫 번째 매개변수는 self로 지정
        r = func(self, a, b)   # self와 매개변수를 그대로 넣어줌
        print('{0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))   # 매개변수와 반환값 출력
        return r               # func의 반환값을 반환
    return wrapper
 
class Calc:
    @trace
    def add(self, a, b):    # add는 인스턴스 메서드
        return a + b
 
c = Calc()
print(c.add(10, 20))


# 실행 결과
add(a=10, b=20) -> 30
30

~~~

---

## 3. 매개변수가 있는 데코레이터 만들기
<br>
<br>
매개변수가 있는 데코레이터를 만들어 보자. 이런 방식의 데코레이터는 값을 지정해서 동작을 바꿀 수 있다. 다음은 함수의 반환값이 특정 수의 배수인지 확인하는 데코레이터아다.

~~~python

def is_multiple(x):              # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):    # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):       # 호출할 함수의 매개변수와 똑같이 지정
            r = func(a, b)       # func를 호출하고 반환값을 변수에 저장
            if r % x == 0:       # func의 반환값이 x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r             # func의 반환값을 반환
        return wrapper           # wrapper 함수 반환
    return real_decorator        # real_decorator 함수 반환
 
@is_multiple(3)     # @데코레이터(인수)
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add(2, 5))

# 실행 결과
add의 반환값은 3의 배수입니다.
30
add의 반환값은 3의 배수가 아닙니다.
7

~~~

실행을 해보면 add 함수의 반환값이 3의 배수인지 아닌지 알수있다. 지금까지 데코레이터를 만들 때 함수 안에 함수를 하나만 만들었다. 하지만 매개변수가 있는 데코레이터를 만들 때는 함수를 하나 더 만들어야 한다.

먼저 is_multiple 함수를 만들고 데코레이터가 사용할 매개변수 x를 지정하고 is_multiple 함수 안에서 실제 데코레이터 역할을 하는 real_decorator를 만든다. 즉, 이 함수에서 호출할 함수를 매개변수로 받는다. 그다음에 real_decorator 함수 안에서 wrapper 함수를 만들어주면 된다.


~~~python

def is_multiple(x):              # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):    # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):       # 호출할 함수의 매개변수와 똑같이 지정

~~~

wrapper함수 안에서는 먼저 func의 결과가 데코레이터 매개변수 x의 배수인지 확인한다. 그다음에 func의 반환값을 반환하게된다.

~~~python

def is_multiple(x):              # 데코레이터가 사용할 매개변수를 지정
    def real_decorator(func):    # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):       # 호출할 함수의 매개변수와 똑같이 지정
            r = func(a, b)       # func를 호출하고 반환값을 변수에 저장
            if r % x == 0:       # func의 반환값이 x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r             # func의 반환값을 반환

~~~

여기서는 real_decorator, wrapper 함수를 두 개 만들었으므로 함수를 만든 뒤에 return으로 두 함수를 반환해준다.

~~~python

        return wrapper           # wrapper 함수 반환
    return real_decorator        # real_decorator 함수 반환

~~~

데코레이터를 사용할 때는 데코레이터에 ( )(괄호)를 붙인 뒤 인수를 넣어주면 된다.

~~~python

@데코레이터(인수)
def 함수이름():
    코드

~~~

~~~python

@is_multiple(3)     # @데코레이터(인수)
def add(a, b):
    return a + b

~~~

여기서는 is_multiple에 3을 지정해서 add 함수의 반환값이 3의 배수인지 확인했다. 물론 is_multiple에 다른 숫자를 넣으면 함수의 반환값이 해당 숫자의 배수인지 확인해준다.


### 매개변수가 있는 데코레이터를 여러 개 지정하기

매개변수가 있는 데코레이터를 여러 개 지정할 때는 다음과 같이 인수를 넣은 데코레이터를 여러 줄로 지정해준다.

~~~python

@데코레이터1(인수)
@데코레이터2(인수)
def 함수이름():
    코드

~~~

~~~python

@is_multiple(3)
@is_multiple(7)
def add(a, b):
    return a + b
 
add(10, 20)
실행 결과
add의 반환값은 7의 배수가 아닙니다.
wrapper의 반환값은 3의 배수입니다.

~~~

@을 사용하지 않았을 때는 다음 코드와 동작이 같다.

~~~python

decorated_add = is_multiple(3)(is_multiple(7)(add))
decorated_add(10, 20)

~~~

### 원래 함수 이름이 안나온다면?
<br>
<br>
데코레이터를 여러 개 사용하면 데코레이터에서 반환된 wrapper 함수가 다른 데코레이터로 들어간다. 따라서 함수의 __name__을 출력해보면 wrapper가 나온다.

~~~python

add의 반환값은 7의 배수가 아닙니다.
wrapper의 반환값은 3의 배수입니다.

~~~

함수의 원래 이름을 출력하고 싶다면 functools 모듈의 wraps 데코레이터를 사용해야 한다. 다음과 같이 @functools.wraps에 func를 넣은 뒤 wrapper 함수 위에 지정해준다(from functools import wraps로 데코레이터를 가져왔다면 @wraps(func)를 지정).

~~~python

import functools
 
def is_multiple(x):
    def real_decorator(func):
        @functools.wraps(func)    # @functools.wraps에 func를 넣은 뒤 wrapper 함수 위에 지정
        def wrapper(a, b):
            r = func(a, b)
            if r % x == 0:
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, x))
            return r
        return wrapper
    return real_decorator
 
@is_multiple(3)
@is_multiple(7)
def add(a, b):
    return a + b
 
add(10, 20)

# 실행 결과
add의 반환값은 7의 배수가 아닙니다.
add의 반환값은 3의 배수입니다.

~~~

@functools.wraps는 원래 함수의 정보를 유지시켜준다. 따라서 디버깅을 할 때 유용하므로 데코레이터를 만들 때는 @functools.wraps를 사용하는 것이 좋다.


## 4. 클래스로 데코레이터 만들기
<br>
<br>
클래스로 데코레이터를 만드는 방법을 알아보자. 특히 클래스를 활용할 때는 인스턴스를 함수처럼 호출하게 해주는 __call__메서드를 구현해야 한다.

다음은 함수의 시작과 끝을 출력하는 데코레이터 이다.

~~~python

class Trace:
    def __init__(self, func):    # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func         # 호출할 함수를 속성 func에 저장
 
    def __call__(self):
        print(self.func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        self.func()                               # 속성 func에 저장된 함수를 호출
        print(self.func.__name__, '함수 끝')
 
@Trace    # @데코레이터
def hello():
    print('hello')
 
hello()    # 함수를 그대로 호출


# 실행 결과
hello 함수 시작
hello
hello 함수 끝

~~~

클래스로 데코레이터를 만들 때는 먼저 \__init__ 메서드를 만들고 호출할 함수를 초깃값으로 받는다. 그리고 매개변수로 받은 함수를 속성으로 저장한다.


~~~python

class Trace:
    def __init__(self, func):    # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func         # 호출할 함수를 속성 func에 저장

~~~

이제 인스턴스를 호출할 수 있도록 \__call__ 메서드를 만든다. \__call__ 메서드에서는 함수의 시작을 알리는 문자열을 출력하고, 속성 func에 저장된 함수를 호출한다. 그다음에 함수의 끝을 알리는 문자열을 출력한다.

~~~python

    def __call__(self):
        print(self.func.__name__, '함수 시작')    # __name__으로 함수 이름 출력
        self.func()                               # 속성 func에 저장된 함수를 호출
        print(self.func.__name__, '함수 끝')

~~~

데코레이터를 사용하는 방법은 클로저 형태의 데코레이터와 같다. 호출할 함수 위에 @을 붙이고 데코레이터를 지정하면 된다.

~~~python

@데코레이터
def 함수이름():
    코드

~~~
~~~python

@Trace    # @데코레이터
def hello():
    print('hello')

~~~

@으로 데코레이터를 지정했으므로 함수는 그대로 호출해줍니다.

~~~python

hello()    # 함수를 그대로 호출

~~~

참고로 클래스로 만든 데코레이터는 @을 지정하지 않고, 데코레이터의 반환값을 호출하는 방식으로도 사용할 수 있다. 다음과 같이 데코레이터에 호출할 함수를 넣어서 인스턴스를 생성한 뒤 인스턴스를 호출해주면 된다. 즉, 클래스에 \__call__ 메서드를 정의했으므로 함수처럼 ( )(괄호)를 붙여서 호출할 수 있다.

~~~python

def hello():    # @데코레이터를 지정하지 않음
    print('hello')
 
trace_hello = Trace(hello)    # 데코레이터에 호출할 함수를 넣어서 인스턴스 생성
trace_hello()                 # 인스턴스를 호출. __call__ 메서드가 호출됨

~~~

---

## 5. 클래스로 매개변수와 반환값을 처리하는 데코레이터 만들기
<br>
<br>
클래스로 만든 데코레이터도 매개변수와 반환값을 처리할 수 있다. 다음은 함수의 매개변수를 출력하는 데코레이터다(여기서는 위치 인수와 키워드 인수를 모두 처리하는 가변 인수로 만들었다).

~~~python

class Trace:
    def __init__(self, func):    # 호출할 함수를 인스턴스의 초깃값으로 받음
        self.func = func         # 호출할 함수를 속성 func에 저장
 
    def __call__(self, *args, **kwargs):    # 호출할 함수의 매개변수를 처리
        r = self.func(*args, **kwargs) # self.func에 매개변수를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
                                            # 매개변수와 반환값 출력
        return r                            # self.func의 반환값을 반환
 
@Trace    # @데코레이터
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add(a=10, b=20))

# 실행 결과
add(args=(10, 20), kwargs={}) -> 30
30
add(args=(), kwargs={'a': 10, 'b': 20}) -> 30
30

~~~

클래스로 매개변수와 반환값을 처리하는 데코레이터를 만들 때는 \__call__ 메서드에 매개변수를 지정하고, self.func에 매개변수를 넣어서 호출한 뒤에 반환값을 반환해주면 된다. 여기서는 매개변수를 *args, **kwargs로 지정했으므로 self.func에 넣을 때는 언패킹하여 넣어준다.

~~~python

    def __call__(self, *args, **kwargs):    # 호출할 함수의 매개변수를 처리
        r = self.func(*args, **kwargs) # self.func에 매개변수를 넣어서 호출하고 반환값을 변수에 저장
        print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))
                                            # 매개변수와 반환값 출력
        return r                            # self.func의 반환값을 반환

~~~

물론 가변 인수를 사용하지 않고, 고정된 매개변수를 사용할 때는 def \__call__(self, a, b):처럼 만들어도 된다.

### 클래스로 매개변수가 있는 데코레이터 만들기
<br>
<br>
마지막으로 매개변수가 있는 데코레이터를 만들어보자. 다음은 함수의 반환값이 특정 수의 배수인지 확인하는 데코레이터다.

~~~python

class IsMultiple:
    def __init__(self, x):         # 데코레이터가 사용할 매개변수를 초깃값으로 받음
        self.x = x                 # 매개변수를 속성 x에 저장
 
    def __call__(self, func):      # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):         # 호출할 함수의 매개변수와 똑같이 지정(가변 인수로 작성해도 됨)
            r = func(a, b)         # func를 호출하고 반환값을 변수에 저장
            if r % self.x == 0:    # func의 반환값이 self.x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, self.x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r               # func의 반환값을 반환
        return wrapper             # wrapper 함수 반환
 
@IsMultiple(3)    # 데코레이터(인수)
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add(2, 5))

# 실행 결과
add의 반환값은 3의 배수입니다.
30
add의 반환값은 3의 배수가 아닙니다.
7

~~~

먼저 \__init__ 메서드에서 데코레이터가 사용할 매개변수를 초깃값으로 받습니다. 그리고 매개변수를 \__call__ 메서드에서 사용할 수 있도록 속성에 저장합니다.

~~~python

    def __init__(self, x):         # 데코레이터가 사용할 매개변수를 초깃값으로 받음
        self.x = x                 # 매개변수를 속성 x에 저장

~~~

지금까지 __init__에서 호출할 함수를 매개변수로 받았는데 여기서는 데코레이터가 사용할 매개변수를 받는다는 점 꼭 기억하자.

이제 \__call__ 메서드에서는 호출할 함수를 매개변수로 받는다. 그리고 \__call__ 메서드 안에서 wrapper 함수를 만들어준다. 이때 wrapper 함수의 매개변수는 호출할 함수의 매개변수와 똑같이 지정해준다(가변 인수로 작성해도 됨).

~~~python

    def __call__(self, func):      # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):         # 호출할 함수의 매개변수와 똑같이 지정(가변 인수로 작성해도 됨)

~~~

wrapper 함수 안에서는 func의 반환값이 데코레이터 매개변수 x의 배수인지 확인한다. 이때 데코레이터 매개변수 x는 속성에 저장되어 있으므로 self.x와 같이 사용해야 한다. 그리고 배수 확인이 끝났으면 func의 반환값을 반환한다. 마지막으로 wrapper 함수를 다 만들었으면 return으로 wrapper 함수를 반환한다.

~~~python

    def __call__(self, func):      # 호출할 함수를 매개변수로 받음
        def wrapper(a, b):         # 호출할 함수의 매개변수와 똑같이 지정(가변 인수로 작성해도 됨)
            r = func(a, b)         # func를 호출하고 반환값을 변수에 저장
            if r % self.x == 0:    # func의 반환값이 self.x의 배수인지 확인
                print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, self.x))
            else:
                print('{0}의 반환값은 {1}의 배수가 아닙니다.'.format(func.__name__, self.x))
            return r               # func의 반환값을 반환
        return wrapper             # wrapper 함수 반환

~~~

데코레이터를 사용할 때는 데코레이터에 ( )(괄호)를 붙인 뒤 인수를 넣어주면 됩니다.


~~~python

@데코레이터(인수)
def 함수이름():
    코드


@IsMultiple(3)    # 데코레이터(인수)
def add(a, b):
    return a + b

~~~


---


### 예제1
<br>
<br>
다음 소스 코드에서 데코레이터 type_check를 작성하세요. type_check는 함수의 매개변수가 지정된 자료형(클래스)이면 함수를 정상적으로 호출하고, 지정된 자료형과 다르면 RuntimeError 예외를 발생시키면서 '자료형이 다릅니다.' 에러 메시지를 출력해야 합니다. 여기서 type_check에 지정된 첫 번째 int는 호출할 함수에서 첫 번째 매개변수의 자료형을 뜻하고, 두 번째 int는 호출할 함수에서 두 번째 매개변수의 자료형을 뜻합니다.

~~~python

_________________________________
...
_________________________________
 
@type_check(int, int)
def add(a, b):
    return a + b
 
print(add(10, 20))
print(add('hello', 'world'))


# 실행 결과
30
Traceback (most recent call last):
  File "C:\project\practice_decorator.py", line 16, in <module>
    print(add('hello', 'world'))
  File "C:\project\practice_decorator.py", line 7, in wrapper
    raise RuntimeError('자료형이 올바르지 않습니다.')
RuntimeError: 자료형이 올바르지 않습니다.

~~~


답

~~~python

def type_check(type_a, type_b):
    def real_decorator(func):
        def wrapper(a, b):
            if isinstance(a, type_a) and isinstance(b, type_b):
                return func(a, b)
            else:
                raise RuntimeError('자료형이 올바르지 않습니다.')
        return wrapper
    return real_decorator

~~~




### 예제2
<br>
<br>
표준 입력으로 HTML 태그 이름 두 개가 입력됩니다. 다음 소스 코드에서 함수의 반환값을 HTML 태그로 감싸는 데코레이터를 만드세요. HTML 태그는 웹 페이지에 사용하는 문법이며 <span>문자열</span>, <p>문자열</p>처럼 <태그이름>으로 시작하며 </태그이름>으로 끝납니다.

~~~python

________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
a, b = input().split()
 
@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'
 
print(hello())

# 입력
p span
# 결과
<p><span>Hello, world!</span></p>
# 입력
b i
# 결과
<b><i>Hello, world!</i></b>

~~~

답

~~~python

def html_tag(tag):
    def real_decorator(func):
        def wrapper():
            result = '<{0}>{1}</{2}>'.format(tag, func(), tag)
            return result
        return wrapper
    return real_decorator

~~~



