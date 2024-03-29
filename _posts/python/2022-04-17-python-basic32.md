---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 클래스 사용하기
date: 2022-04-17 15:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 클래스 사용하기

<br>
<br>
클래스는 객체를 표현하기 위한 문법이다. 예를들어 게임을 만든다고 한다면 기사, 마법사, 궁수, 사제등 직업별로 클래스를 만들어 표현할 수 있다. 이처럼 특정한 개념이나 모양으로 존재하는 것을 객체(object)라고 부른다. 그리고 프로그래밍으로 객체를 만들때 사용하는 것이 클래스이다. 게임의 기사 캐릭터를 클래스로 표현해보자. 일단 게임 캐릭터는 체력, 마나, 물리 공격력, 주문력 등이 필요합니다. 그리고 기사 캐릭터는 칼로 베기, 찌르기 등의 스킬이 있어야 한다. 여기서 체력, 마나, 물리 공격력, 주문력 등의 데이터를 클래스의 속성(attribute)이라 부르고, 베기, 찌르기 등의 기능을 메서드(method)라고 부른다.

<br>
이런 식의 프로그래밍을 객체지향(object oriented) 프로그래밍이라고 한다. 객체지향 프로그래밍은 복잡한 문제를 잘게 나누어 객체로 만들고, 객체를 조합해서 문제를 해결한다. 따라서 현실 세계의 복잡한 문제를 처리하는데 유용하며 기능을 개선하고 발전시킬 때도 해당 클래스만 수정하면 되므로 유지 보수에도 효율적이다.


---

## 1. 클래스와 메서드 만들기
<br>
<br>
클래스는 class에 클래스 이름을 지정하고:(콜론)을 붙인 뒤 다음 줄부터 def로 메서드를 작성한다. 여기서 메서드는 클래스 안에 들어있는 함수를 뜻한다.
<br>
클래스 이름을 짓는 방법은 변수와 같다. 보통 파이썬에서 클래스의 이름은 대문자로 시작한다. 그리고 메서드 작성 방법은 함수와 같으며 코드는 반드시 들여쓰기를 해야한다. 특히 메서드의 첫 번째 매개변수는 반드시 self를 지정해야 한다.

 
~~~python

class 클래스이름:
    def 메서드(self):
        코드

# 메서드의 첫 번째 매개변수를 self로 지정하지 않았을때.
TypeError: ... takes 0 positional arguments but 1 was given: self

간단한 사람 클래스를 작성했다.

~~~python

class Person:
     def greeting(self):
         print('Hello')
         
~~~

이렇게 만든 클래스를 사용하려면 클래스에 ()를 붙인 뒤 변수에 할당한다. Person으로 변수 james를 만들었는데 이 james가 Person의 인스턴스(instance)다. 클래스는 특정 개념을 표현만 할뿐 사용을 하려면 인스턴스를 생성해야 한다.

~~~python

james = Person()

~~~


### 메서드 호출하기
<br>
<br>
메서드는 클래스가 아니라 인스턴트를 통해 호출한다. 다음과 같이 이스턴스 뒤에 .을 붙이고 메서드를 호출하면 된다. james.greeting()을 호출하니 'Hello'가 출력되었다. 이렇게 인스턴트를 통해 호출하는 메서드를 인스턴트 메서드라고 부른다.

~~~python

james.greeting()
Hello

~~~

### 파이썬에서 흔히 볼 수 있는 클래스
<br>
<br>

지금까지 사용한 int, list, dict 등도 사실 클래스다. 우리는 이 클래스로 인스턴스를 만들고 메서드를 사용했다. int 클래스에 10을 넣어서 인스턴스 a를 만들었다. 마찬가지로 list 클래스에 range(10)을 넣어서 인스턴스 b를 만들고, dict 클래스에 x=10, y=20을 넣어서 인스턴스 c를 만들었다. 잘 보면 Person으로 인스턴스를 만드는 방법과 똑같다. 물론 정수는 매우 자주 사용하므로 int를 생략하고 10을 바로 넣는다. 그리고 리스트와 딕셔너리도 자주 사용하므로 축약된 문법인 [ ]과 { }를 제공하지만 클래스인 것은 같다.

~~~python

a = int(10)
a
10
b = list(range(10))
b
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = dict(x=10, y=20)
c
{'x': 10, 'y': 20}

~~~

인스턴스 b에서 메서드 append를 호출해서 값을 추가한다. 이 부분도 지금까지 메서드를 만들고 사용한 것과 같은 방식이다.

~~~python

b = list(range(10))
b.append(20)
b
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 20]

~~~

즉, 파이썬에서는 자료형도 클래스이다. 다음과 같이 type을 사용하면 객체(인스턴스)가 어떤 클래스인지 확인할 수 있다.

- type(객체)

~~~python

a = 10
type(a)
<class 'int'>
b = [0, 1, 2]
type(b)
<class 'list'>
c = {'x':10, 'y':20}
type(c)
<class 'dict'>
maria = Person()
type(maria)
<class '__main__.Person'>

~~~

### 인스턴스와 객체의 차이점?
<br>
<br>
클래스는 객체를 표현하는 문법이라고 했는데, 클래스로 인스턴스를 만든다고 하니 좀 헷갈린다. 사실 인스턴스와 객체는 같은 것을 뜻한다. 보통 객체만 지칭할 때는 그냥 객체(object)라고 부른다. 하지만 클래스와 연관지어서 말할 때는 인스턴스(instance)라고 부른다. 그래서 다음과 같이 리스트 변수 a, b가 있으면 a, b는 객체이다. 그리고 a와 b는 list클래스의 인스턴스이다.

~~~python

a = list(range(10))
b = list(range(20))

~~~

### 빈 클래스 만들기
<br>
<br>
내용이 없는 빈 클래스를 만들 때는 코드 부분에 pass를 넣어준다.

~~~python

class Person:
    pass

~~~

### 메서드 안에서 메서드 호출하기
<br>
<br>
메서드 안에서 메서드를 호출할 때는 다음과 같이 self.메서드() 형식으로 호출해야 한다. self 없이 메서드 이름만 사용하면 클래스 바깥쪽에 있는 함수를 호출한다는 뜻이 되므로 주의해야 한다.

~~~python

class Person:
    def greeting(self):
        print('Hello')
 
    def hello(self):
        self.greeting()    # self.메서드() 형식으로 클래스 안의 메서드를 호출
 
james = Person()
james.hello()    # Hello

~~~

### 특정 클래스의 인스턴스인지 확인하기
<br>
<br>
현재 인스턴스가 특정 클래스의 인스턴스인지 확인할 때는 isinstance 함수를 사용한다. 특정 클래스의 인스턴스가 맞으면 True, 아니면 False를 반환한다.

- isinstance(인스턴스, 클래스)

~~~python

class Person:
     pass

james = Person()
isinstance(james, Person)
True

~~~

isinstance는 주로 객체의 자료형을 판단할 때 사용한다. 예를 들어 팩토리얼 함수는 1부터 n까지 양의 정수를 차례대로 곱해야 하는데, 실수와 음의 정수는 계산할 수 없다. 이런 경우에 isinstance를 사용하여 숫자(객체)가 정수일 때만 계산하도록 만들 수 있다.

~~~python

def factorial(n):
    if not isinstance(n, int) or n < 0:    # n이 정수가 아니거나 음수이면 함수를 끝냄
        return None
    if n == 1:
        return 1
    return n * factorial(n - 1)

~~~


---

## 2. 속성 사용하기
<br>
<br>
지금까지 클래스에서 메서드를 만들고 호출해봤다. 이번엔 클래스에서 속성을 만들고 사용해보자. 속성(attribute)을 만들 때는 \__init__ 메서드 안에서 self.속성에 값을 할당한다.

~~~python

class 클래스이름:
    def __init__(self):
        self.속성 = 값

~~~

다음 코드를 실행해 보자.

~~~python

class Person:
    def __init__(self):
        self.hello = '안녕하세요.'
 
    def greeting(self):
        print(self.hello)
 
james = Person()
james.greeting()

#실행결과
안녕하세요.

~~~

Person 클래스의 \__init__ 메서드에서 self.hello에 '안녕하세요.' 인사말을 넣었다. \__init__ 메서드는 james = Person()처럼 클래스에 ( )(괄호)를 붙여서 인스턴스를 만들 때 호출되는 특별한 메서드다. 즉, \__init__(initialize)이라는 이름 그대로 인스턴스(객체)를 초기화한다. 특히 이렇게 앞 뒤로 __(밑줄 두 개)가 붙은 메서드는 파이썬이 자동으로 호출해주는 메서드인데 스페셜 메서드(special method) 또는 매직 메서드(magic method)라고 부른다. 앞으로 파이썬의 여러 가지 기능을 사용할 때 이 스페셜 메서드를 채우는 식으로 사용하게 된다.


~~~python

class Person:
    def __init__(self):
        self.hello = '안녕하세요.'

~~~

이제 greeting 메서드를 살펴보자. greeting 메서드에서는 print로 self.hello를 출력하게 만들었다. 그다음에 Person 클래스로 인스턴스를 만들고, greeting 메서드를 호출해보면 self.hello에 저장된 '안녕하세요.'가 출력된다.

~~~python

    def greeting(self):
        print(self.hello)

james = Person()
james.greeting()    # 안녕하세요.

~~~

### self의 의미
<br>
<br>
self는 인스턴스 자기 자신을 의미한다. 우리는 인스턴스가 생성될 때 self.hello = '안녕하세요.'처럼 자기 자신에 속성을 추가했다. 여기서 __init의 매개변수 self에 들어가는 값은 person()이라 할 수 있다. 그리고 self가 완성된 뒤 james에 할당된다. 이후 메서드를 호출하면 현재 인스턴스가 자동으로 매개변수 self에 들어오게 된다. 그래서 greeting메서드에서 print(self.hello)처럼 속성을 출력할 수 있었던 것이다.

### 인스턴스를 만들 때 값 받기
<br>
<br>
이번에는 클래스로 인스턴스를 만들 때 값을 받는 방법을 알아보겠습니다. 다음과 같이 __init__ 메서드에서 self 다음에 값을 받을 매개변수를 지정합니다. 그리고 매개변수를 self.속성에 넣어줍니다.

~~~python

class 클래스이름:
    def __init__(self, 매개변수1, 매개변수2):
        self.속성1 = 매개변수1
        self.속성2 = 매개변수2


~~~

그럼 Person 클래스로 인스턴스를 만들 때 이름, 나이, 주소를 받아보자.

~~~python

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address
 
    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
 
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()    # 안녕하세요. 저는 마리아입니다.
 
print('이름:', maria.name)       # 마리아
print('나이:', maria.age)        # 20
print('주소:', maria.address)    # 서울시 서초구 반포동

#실행 결과
안녕하세요. 저는 마리아입니다.
이름: 마리아
나이: 20
주소: 서울시 서초구 반포동

~~~

\__init__ 메서드를 보면 self 다음에 name, age, address를 지정했습니다. 그리고 메서드 안에서는 self.name = name처럼 매개변수를 그대로 self에 넣어서 속성으로 만들었다.

~~~python

    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

~~~

greeting 메서드는 인사를 하고 이름을 출력하도록 수정했다. 물론 name 속성에 접근할 때는 self.name처럼 사용해야한다.

~~~python

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

~~~

이제 Person의 ( )(괄호) 안에 이름, 나이, 주소를 콤마로 구분해서 넣은 뒤에 변수에 할당한다. 이렇게 하면 이름은 '마리아', 나이는 20, 주소는 '서울시 서초구 반포동'인 maria 인스턴스가 만들어진다.

~~~python

maria = Person('마리아', 20, '서울시 서초구 반포동')

~~~

maria 인스턴스의 greeting 메서드를 호출해보면 '안녕하세요. 저는 마리아입니다.'처럼 인삿말과 함께 이름도 출력된다.

~~~python

maria.greeting()    # 안녕하세요. 저는 마리아입니다.

~~~

클래스 안에서 속성에 접근할 때는 self.속성 형식이 있었다. 클래스 바깥에서 속성에 접근할 때는 인스턴스.속성 형식으로 접근한다. 다음과 같이 maria.name, maria.age, maria.address의 값을 출력해보면 Person으로 인스턴스를 만들 때 넣었던 값이 출력된다.

~~~python

print('이름:', maria.name)       # 마리아
print('나이:', maria.age)        # 20
print('주소:', maria.address)    # 서울시 서초구 반포동

~~~

### 클래스의 위치 인수, 키워드 인수
<br>
<br>
클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수를 사용할 수 있다. 규칙은 함수와 같다. 위치 인수와 리스트 언패킹을 사용하려면 다음과 같이 *args를 사용하면 됩니다. 이때 매개변수에서 값을 가져오려면 args[0]처럼 사용해야 한다.

~~~python

class Person:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]
 
maria = Person(*['마리아', 20, '서울시 서초구 반포동'])

~~~

키워드 인수와 딕셔너리 언패킹을 사용하려면 다음과 같이 **kwargs를 사용하면 됩니다. 이때 매개변수에서 값을 가져오려면 kwargs['name']처럼 사용해야 한다.

~~~python

class Person:
    def __init__(self, **kwargs):    # 키워드 인수
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']
 
maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})

~~~


### 인스턴스를 생성한 뒤에 속성 추가하기, 특정 속성만 허용하기
<br>
<br>
지금까지 클래스의 인스턴스 속성은 __init__ 메서드에서 추가한 뒤 사용했다. 하지만 클래스로 인스턴스를 만든 뒤에도 인스턴스.속성 = 값 형식으로 속성을 계속 추가할 수 있다. 다음 Person 클래스는 빈 클래스이지만 인스턴스를 만든 뒤 name 속성을 추가한다.

~~~python

class Person:
     pass

maria = Person()         # 인스턴스 생성
maria.name = '마리아'    # 인스턴스를 만든 뒤 속성 추가
maria.name
'마리아'

~~~

이렇게 추가한 속성은 해당 인스턴스에만 생성된다. 따라서 클래스로 다른 인스턴스를 만들었을 때는 추가한 속성이 생성되지 않는다.

~~~python

james = Person()    # james 인스턴스 생성
james.name    # maria 인스턴스에만 name 속성을 추가했으므로 james 인스턴스에는 name 속성이 없음
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    james.name
AttributeError: 'Person' object has no attribute 'name'

~~~

인스턴스는 생성한 뒤에 속성을 추가할 수 있으므로 __init__ 메서드가 아닌 다른 메서드에서도 속성을 추가할 수 있다. 단, 이때는 메서드를 호출해야 속성이 생성된다.

~~~python

class Person:
     def greeting(self):
         self.hello = '안녕하세요'    # greeting 메서드에서 hello 속성 추가

maria = Person()
maria.hello    # 아직 hello 속성이 없음
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    maria.hello
AttributeError: 'Person' object has no attribute 'hello'
maria.greeting()    # greeting 메서드를 호출해야
maria.hello         # hello 속성이 생성됨
'안녕하세요'

~~~

인스턴스는 자유롭게 속성을 추가할 수 있지만 특정 속성만 허용하고 다른 속성은 제한하고 싶을 수도 있다. 이때는 클래스에서 __slots__에 허용할 속성 이름을 리스트로 넣어주면 된다. 특히 속성 이름은 반드시 문자열로 지정해준다.

- \__slots__ = ['속성이름1, '속성이름2']

~~~python

class Person:
     __slots__ = ['name', 'age']    # name, age만 허용(다른 속성은 생성 제한)

maria = Person()
maria.name = '마리아'                     # 허용된 속성
maria.age = 20                            # 허용된 속성
maria.address = '서울시 서초구 반포동'    # 허용되지 않은 속성은 추가할 때 에러가 발생함
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    maria.address = '서울시 서초구 반포동'
AttributeError: 'Person' object has no attribute 'address'

~~~

---

## 3. 비공개 속성 사용하기
<br>
<br>
위에서 만든 person클래스에는 hello, name, age, address 속성이 있었다.

~~~python

class Person:
    def __init__(self, name, age, address):
        self.hello = '안녕하세요.'
        self.name = name
        self.age = age
        self.address = address

~~~

이 속성들은 메서드에서 self로 접근할 수 있고, **인스턴스.속성** 형식으로 클래스 바깥에서도 접근할 수 있다.

~~~python

maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.name
'마리아'

~~~

이번에는 클래스 바깥에서는 접근할 수 없고 클래스 안에서만 사용할 수 있는 비공개 속성(private attribute)을 사용해보자.

비공개 속성은 **__속성**과 같이 이름이 __(밑줄 두 개)로 시작해야 한다. 단, **__속성__**처럼 밑줄 두 개가 양 옆에 왔을 때는 비공개 속성이 아니므로 주의해야 한다.


~~~python

class 클래스이름:
    def __init__(self, 매개변수)
        self.__속성 = 값

~~~

Person 클래스에 지갑 속성 __wallet을 넣어 봤다. 다음 내용을 IDLE의 소스 코드 편집 창에 입력한 뒤 실행해보자. 실행을 해보면 에러가 발생한다. self.__wallet처럼 앞에 밑줄 두 개를 붙여서 비공개 속성으로 만들었으므로 클래스 바깥에서 maria.__wallet으로는 접근할 수 없다.

~~~python

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.__wallet -= 10000    # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함

#실행결과
Traceback (most recent call last):
  File "C:\project\class_private_attribute_error.py", line 9, in <module>
    maria.__wallet -= 10000    # 클래스 바깥에서 비공개 속성에 접근하면 에러가 발생함
AttributeError: 'Person' object has no attribute '__wallet' 

~~~

비공개 속성은 클래스 안의 메서드에서만 접근할 수 있다. 다음과 같이 돈을 내는 pay 메서드를 만들어보자. pay는 돈을 내면 해당 금액을 지갑에서 빼도록 만들었다.

~~~python

class Person:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet    # 변수 앞에 __를 붙여서 비공개 속성으로 만듦
 
    def pay(self, amount):
        self.__wallet -= amount   # 비공개 속성은 클래스 안의 메서드에서만 접근할 수 있음
        print('이제 {0}원 남았네요.'.format(self.__wallet))
 
maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
maria.pay(3000)

# 실행결과

이제 7000원 남았네요.

~~~

물론 지갑에 든 돈은 굳이 밝힐 필요가 없으므로 print로 출력하지 않아도 된다. 보통은 다음과 같이 지갑에 든 돈이 얼마인지 확인하고 돈이 모자라면 쓰지 못하는 식으로 만든다.

~~~python

    def pay(self, amount):
        if amount > self.__wallet:    # 사용하려고 하는 금액보다 지갑에 든 돈이 적을 때
            print('돈이 모자라네...')
            return
        self.__wallet -= amount

~~~

이처럼 비공개 속성은 클래스 바깥으로 드러내고 싶지 않은 값에 사용한다. 즉, 중요한 값인데 바깥에서 함부로 바꾸면 안될 때 비공개 속성을 주로 사용한다. 비공개 속성을 바꾸는 경우는 클래스의 메서드로 한정한다.


### 공개 속성과 비공개 속성
<br>
<br>
클래스 바깥에서 접근할 수 있는 속성을 공개 속성(public attribute)이라 부르고, 클래스 안에서만 접근할 수 있는 속성을 비공개 속성(private attribute)이라 부른다.

### 비공개 메서드 사용하기
<br>
<br>
속성뿐만 아니라 메서드도 이름이 __(밑줄 두 개)로 시작하면 클래스 안에서만 호출할 수 있는 비공개 메서드가 된다. 비공개 메서드도 메서드를 클래스 바깥으로 드러내고 싶지 않을 때 사용한다. 보통 내부에서만 호출되어야 하는 메서드를 비공개 메서드로 만든다. 예를 들어 게임 캐릭터가 마나를 소비해서 스킬을 쓴다고 치면 마나 소비량을 계산해서 차감하는 메서드는 비공개 메서드로 만들고, 스킬을 쓰는 메서드는 공개 메서드로 만든다. 만약 마나를 차감하는 메서드가 공개되어 있다면 마음대로 마나를 차감시킬 수 있으므로 잘못된 클래스 설계가 된다.

~~~python

class Person:
    def __greeting(self):
        print('Hello')
 
    def hello(self):
        self.__greeting()    # 클래스 안에서는 비공개 메서드를 호출할 수 있음
 
james = Person()
james.__greeting()    # 에러: 클래스 바깥에서는 비공개 메서드를 호출할 수 없음

~~~



---

### 예제1
<br>
<br>
다음 소스 코드에서 클래스를 작성하여 게임 캐릭터의 능력치와 '베기'가 출력되게 만드세요.

~~~python

 ______________                                           
...
 ______________                                          
 
x = Knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

#결과
542.4 210.3 38
베기

~~~


답

~~~python

class Knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor
 
    def slash(self):
        print('베기')

~~~

x = Knight(health=542.4, mana=210.3, armor=38)와 같이 클래스에 값을 넣어서 인스턴스를 생성하고, print(x.health, x.mana, x.armor)와 같이 인스턴스 속성을 출력하고 있다. 따라서 class로 Knight 클래스를 만들고 \__init__ 메서드에 매개변수로 self, health, mana, armor를 지정한다. 이때 반드시 첫 번째 매개변수는 self어야 한다. 함수 안에서는 self.health = health처럼 모든 매개변수를 그대로 속성으로 만들어준다.

그다음에 x.slash()와 같이 인스턴스로 메서드를 호출하고 있으므로 Knight 클래스 안에 slash 메서드를 만들고 print로 '베기'를 출력하도록 만들면 되겠다.

### 예제2
<br>
<br>
표준 입력으로 게임 캐릭터 능력치(체력, 마나, AP)가 입력됩니다. 다음 소스 코드에서 애니(Annie) 클래스를 작성하여 티버(tibbers) 스킬의 피해량이 출력되게 만드세요. 티버의 피해량은 AP * 0.65 + 400이며 AP(Ability Power, 주문력)는 마법 능력치를 뜻합니다.

~~~python

________________
________________
________________
________________
________________
________________

health, mana, ability_power = map(float, input().split())
 
x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()

#입력
511.68 334.0 298

#결과
티버: 피해량 593.7

#입력
1803.68 1184.0 645

#결과
티버: 피해량 819.25

~~~

내가 쓴 답

~~~python

class Annie:
    def __init__(self,**kwargs):
        self.health = kwargs['health']
        self.mana = kwargs['mana']
        self.ability_power = kwargs['ability_power']
    def tibbers(self):
        print("티버: 피해량", (self.ability_power * 0.65 + 400))

~~~

코딩도장 풀이

~~~python

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power
    def tibbers(self):
        print("티버: 피해량 {0} ".format(self.ability_power * 0.65 + 400))

~~~

