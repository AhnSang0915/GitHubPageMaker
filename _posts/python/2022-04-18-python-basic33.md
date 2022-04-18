---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 클래스 속성과 정적, 클래스 메서드 사용하기
date: 2022-04-18 18:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 클래스 속성과 정적, 클래스 메서드 사용하기

<br>
<br>
클래스에 속해 있는 클래스 속성에 대해 알아보자. 그리고 인스턴스를 만들지 않고 클래스로 호출하는 정적 메서드와 클래스 메서드도 사용해보자.


---

## 1. 클래스 속성과 인스턴스 속성 알아보기
<br>
<br>
속성에는 클래스 속성과 인스턴스 속성 두 가지 종류가 있다. __init__메서드에서 만들었던 속성은 인스턴스 속성이다.

### 클래스 속성 사용하기
<br>
<br>
클래스 속성을 사용해보자. 클래스 속성은 다음과 같이 클래스에 바로 속성을 만든다.


~~~python

class 클래스이름:
    속성 = 값
         
~~~

이제 간단하게 사람 클래스에 클래스 속성으로 가방 속성을 넣고 사용해보자. 다음과 같이 person클래스에 바로 bag을 넣고, put_bag메서드를 만든다. 그리고 인스턴스 두 개를 만든 뒤 각각 put_bag 메서드를 사용한다.

결과를 보면 james와 maria 인스턴스를 만들고 각자 put_bag 메서드로 물건을 넣었는데, james.bag과 maria.bag을 출력해보면 넣었던 물건이 합쳐져서 나온다. 즉, 클래스 속성은 클래스에 속해 있으며 모든 인스턴스에서 공유한다.

~~~python

class Person:
    bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)
print(maria.bag)

#실행 결과
['책', '열쇠']
['책', '열쇠']

~~~

put_bag 메서드에서 클래스 속성 bag에 접근할 때 self를 사용했다. 사실 self는 현재 인스턴스를 뜻하므로 클래스 속성을 지칭하기에는 조금 모호하다.

~~~python

class Person:
    bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)

~~~

그래서 클래스 속성에 접근할 때는 다음과 같이 클래스 이름으로 접근하면 좀 더 코드가 명확해진다.

- 클래스.속성

~~~python

class Person:
    bag = []
 
    def put_bag(self, stuff):
        Person.bag.append(stuff)    # 클래스 이름으로 클래스 속성에 접근

~~~

Person.bag이라고 하니 클래스 Person에 속한 bag 속성이라는 것을 바로 알 수 있다. 마찬가지로 클래스 바깥에서도 다음과 같이 클래스 이름으로 클래스 속성에 접근하면 된다.

~~~python

print(Person.bag)

~~~

### 속성, 메서드 이름을 찾는 순서
<br>
<br>
파이썬에서는 속성, 메서드 이름을 찾을 때 인스턴스, 클래스 순으로 찾는다. 그래서 인스턴스 속성이 없으면 클래스 속성을 찾게 되므로 james.bag, maria.bag도 문제 없이 동작한다. 겉보기에는 인스턴스 속성을 사용하는 것 같지만 실제로는 클래스 속성이다.

인스턴스와 클래스에서 \__dict__ 속성을 출력해보면 현재 인스턴스와 클래스의 속성을 딕셔너리로 확인할 수 있다.

- 인스턴스.\__dict__

- 클래스.\__dict__


~~~python

james.__dict__
{}
Person.__dict__
mappingproxy({'__module__': '__main__', 'bag': ['책', '열쇠'], 'put_bag': <function Person.put_bag at 0x028A32B8>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None})

~~~

### 인스턴스 속성 사용하기
<br>
<br>
그럼 bag을 여러 인스턴스가 공유하지 않으려면 어떻게 해야할까? 그냥 bag을 인스턴스 속성으로 만들면 된다.

~~~python

class Person:
    def __init__(self):
        self.bag = []
 
    def put_bag(self, stuff):
        self.bag.append(stuff)
 
james = Person()
james.put_bag('책')
 
maria = Person()
maria.put_bag('열쇠')
 
print(james.bag)
print(maria.bag)

#실행 결과
['책']
['열쇠']

~~~

james.bag과 maria.bag을 출력해보면 각자 넣은 물건만 출력된다. 즉, 인스턴스 속성은 인스턴스별로 독립되어 있으며 서로 영향을 주지 않는다.

- 클래스 속성: 모든 인스턴스가 공유. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
- 인스턴스 속성: 인스턴스별로 독립되어 있음. 각 인스턴스가 값을 따로 저장해야 할 때 사용

### 비공개 클래스 속성 사용하기
<br>
<br>

클래스 속성도 비공개 속성을 만들 수 있습니다. 클래스 속성을 만들 때 **\__속성** 과 같이 **\__(밑줄 두 개)**로 시작하면 비공개 속성이 됩니다. 따라서 클래스 안에서만 접근할 수 있고, 클래스 바깥에서는 접근할 수 없다.

~~~python

class 클래스이름:
    __속성 = 값    # 비공개 클래스 속성

~~~

즉, 클래스에서 공개하고 싶지 않은 속성이 있다면 비공개 클래스를 사용해야 한다. 예를 들어 기사 게임 캐릭터는 아이템을 최대 10개까지만 보유할 수 있다고 하자. 실행을 해보면 클래스 Knight의 비공개 클래스 속성 __item_limit는 클래스 안의 print_item_limit 메서드에서만 접근할 수 있고, 클래스 바깥에서 접근하면 에러가 발생한다. 아이템의 보유 제한이 10개인데, 이 클래스를 사용하는 사람이 마음대로 __item_limit = 1000으로 수정하는 경우를 방지한다.

~~~python

class Knight:
    __item_limit = 10    # 비공개 클래스 속성
 
    def print_item_limit(self):
        print(Knight.__item_limit)    # 클래스 안에서만 접근할 수 있음
 
 
x = Knight()
x.print_item_limit()    # 10
 
print(Knight.__item_limit)    # 클래스 바깥에서는 접근할 수 없음 에러발생

#실행 결과

10

Traceback (most recent call last):
  File "C:\project\class_private_class_attribute_error.py ", line 11, in <module>
    print(Knight.__item_limit)    # 클래스 바깥에서는 접근할 수 없음
AttributeError: type object 'Knight' has no attribute '__item_limit' 

~~~

### 클래스와 메서드의 독스트링 사용하기
<br>
<br>
함수와 마찬가지로 클래스와 메서드도 독스트링을 사용할 수 있다. 다음과 같이 클래스와 메서드를 만들 때 :(콜론) 바로 다음 줄에 """ """(큰따옴표 세 개) 또는 ''' '''(작은따옴표 세 개)로 문자열을 입력하면 된다. 그리고 클래스의 독스트링은 클래스.__doc__ 형식으로 사용하고, 메서드의 독스트링은 클래스.메서드.__doc__ 또는 인스턴스.메서드.__doc__ 형식으로 사용한다.

~~~python

class Person:
    '''사람 클래스입니다.'''
    
    def greeting(self):
        '''인사 메서드입니다.'''
        print('Hello')
 
print(Person.__doc__)             # 사람 클래스입니다.
print(Person.greeting.__doc__)    # 인사 메서드입니다.
 
maria = Person()
print(maria.greeting.__doc__)     # 인사 메서드입니다.

#실행결과

print(Person.__doc__)
사람 클래스입니다.
print(Person.greeting.__doc__)
인사 메서드입니다.
maria = Person()
print(maria.greeting.__doc__)
인사 메서드입니다.


~~~


---

## 2. 정적 메서드 사용하기
<br>
<br>
이번엔 인스턴스를 통하지 않고 클래스에서 바로 호출할 수 있는 정적 메서드와 클래스 메서드에 대해 알아보자.

먼저 정적 메서드이다. 정적 메서드는 다음과 같이 메서드 위에 @staticmethod를 붙인다. 이때 정적 메서드는 매개변수에 self를 지정하지 않는다.

~~~python

class 클래스이름:
    @staticmethod
    def 메서드(매개변수1, 매개변수2):
        코드

~~~

@staticmethod처럼 앞에 @이 붙은 것을 데코레이터라고 하며 메서드(함수)에 추가 기능을 구현할 때 사용한다.

그럼 간단하게 덧셈과 곱셈을 하는 클래스를 만들어보자.

~~~python

class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)
 
    @staticmethod
    def mul(a, b):
        print(a * b)
 
Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출

#실행 결과
30
200

~~~

Calc 클래스에서 @staticmethod를 붙여서 add 메서드와 mul 메서드를 만들었다. 정적 메서드를 호출할 때는 다음과 같이 클래스에서 바로 메서드를 호출하면 된다. 정적 메서드는 self를 받지 않으므로 인스턴스 속성에는 접근할 수 없다. 그래서 보통 정적 메서드는 인스턴스 속성, 인스턴스 메서드가 필요 없을 때 사용한다.

- 클래스.메서드()

~~~python

Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
Calc.mul(10, 20)    # 클래스에서 바로 메서드 호

~~~

여기서 만든 Calc 클래스에 들어있는 add, mul 메서드는 숫자 두개를 받아서 더하거나 곱할 뿐 인스턴스의 속성은 필요하지 않다. 정적 메서드는 메서드의 실행이 외부 상태에 영향을 끼치지 않는 순수 함수(pure function)를 만들 때 사용한다. 순수 함수는 부수 효과(side effect)가 없고 입력 값이 같으면 언제나 같은 출력 값을 반환한다. 즉, 정적 메서드는 인스턴스의 상태를 변화시키지 않는 메서드를 만들 때 사용한다.

### 파이썬 자료형의 인스턴스 메서드와 정적 메서드
<br>
<br>
파이썬의 자료형도 인스턴스 메서드와 정적, 클래스 메서드로 나뉘어져 있다. 예를 들어 세트에 요소를 더할 때는 인스턴스 메서드를 사용하고, 합집합을 구할 때는 정적 메서드를 사용하도록 만들어져 있다.

~~~python

a = {1, 2, 3, 4}
a.update({5})    # 인스턴스 메서드
a
{1, 2, 3, 4, 5}
set.union({1, 2, 3, 4}, {5})    # 정적(클래스) 메서드 합집합
{1, 2, 3, 4, 5}

~~~

이처럼 인스턴스의 내용을 변경해야 할 때는 update와 같이 인스턴스 메서드로 작성하면 되고, 인스턴스 내용과는 상관없이 결과만 구하면 될 때는 set.union과 같이 정적 메서드로 작성하면 된다.

---

## 3. 클래스 메서드 사용하기
<br>
<br>
이번에는 정적 메서드와 비슷하지만 약간의 차이점이 있는 클래스 메서드를 사용해보자. 

클래스 매서드는 다음과 같이 메서드 위에 @classmethod를 붙인다. 이때 클래스 메서드는 첫 번쨰 매개변수에 cls를 지정해야 한다.(cls는 class에서 따왔다).

~~~python

class 클래스이름:
    @classmethod
    def 메서드(cls, 매개변수1, 매개변수2):
        코드

~~~

그럼 사람 클래스 Person을 만들고 인스턴스가 몇 개 만들어졌는지 출력하는 메서드를 만들어보자.

~~~python

class Person:
    count = 0    # 클래스 속성
 
    def __init__(self):
        Person.count += 1    # 인스턴스가 만들어질 때
                             # 클래스 속성 count에 1을 더함
 
    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근
 
james = Person()
maria = Person()
 
Person.print_count()    # 2명 생성되었습니다.

#실행 결과
2명 생성되었습니다.

~~~

먼저 인스턴스가 만들어질 때마다 숫자를 세야 하므로 \__init__ 메서드에서 클래스 속성 count에 1을 더해줍니다. \__init__은 인스턴스가 만들어질 떄 마다 자동으로 호출된다. 물론 클래스 속성에 접근한다는 것을 명확하게 하기 위해 Person.count와 같이 만들어줍니다.

~~~python

class Person:
    count = 0    # 클래스 속성
 
    def __init__(self):
        Person.count += 1    # 인스턴스가 만들어질 때
                             # 클래스 속성 count에 1을 더함

~~~

이제 @classmethod를 붙여서 클래스 메서드를 만든다. 클래스 메서드는 첫 번째 매개변수가 cls인데 여기에는 현재 클래스가 들어오게된다. 따라서 cls.count처럼 cls로 클래스 속성 count에 접근할 수 있다.

~~~python

    @classmethod
    def print_count(cls):
        print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근

~~~

Person으로 인스턴스를 두 개 만들었으므로 print_count를 호출해보면 '2명 생성되었습니다.'가 출력된다. 물론 print_count는 클래스 메서드이므로 Person.print_count()처럼 클래스로 호출해준다.

~~~python

james = Person()
maria = Person()
 
Person.print_count()    # 2명 생성되었습니다.

~~~

클래스 메서드는 정적 메서드처럼 인스턴스 없이 호출할 수 있다는 점은 같다. 하지만 클래스 메서드는 메서드 안에서 클래스 속성, 클래스 메서드에 접근해야 할 때 사용한다.

특히 cls를 사용하면 메서드 안에서 현재 클래스의 인스턴스를 만들 수도 있다. 즉, cls는 클래스이므로 cls()는 Person()과 같다.

~~~python

    @classmethod
    def create(cls):
        p = cls()    # cls()로 인스턴스 생성 cls() = person()
        return p

~~~




---

### 예제1
<br>
<br>
다음 소스 코드에서 Date 클래스를 완성하세요. is_date_valid는 문자열이 올바른 날짜인지 검사하는 메서드입니다. 날짜에서 월은 12월까지 일은 31일까지 있어야 합니다.

~~~python

class Date:
 ______________                                           
...
 ______________                                          
 
if Date.is_date_valid('2000-10-31'):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')

~~~


답

~~~python

class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split('-'))
        return month <= 12 and day <= 31


~~~

is_date_valid 메서드는 Date.is_date_valid처럼 호출하고 있지만, 문자열이 올바른 날짜인지 검사만 하면 되고, 클래스에 접근할 필요는 없다. 그러므로 정적 메서드로 만든다. 먼저 메서드 위에 @staticmethod를 붙여준 뒤 첫 번째 매개변수로 날짜 문자열 date_string을 지정한다. 메서드 안에서는 year, month, day = map(int, date_string.split('-'))와 같이 '-'로 문자열을 분리한 뒤 int로 변환해서 각 변수에 넣어준다. 그다음에는 return month <= 12 and day <= 31과 같이 월이 12 이하이면서 일이 31일 이하인지 검사하고 결과를 반환하도록 만든다. 즉, 월, 일 모두 만족하면 True가 반환되고 하나라도 만족하지 않으면 False가 반환하게 된다.


### 예제2
<br>
<br>
표준 입력으로 시:분:초 형식의 시간이 입력됩니다. 다음 소스 코드에서 Time 클래스를 완성하여 시, 분, 초가 출력되게 만드세요. from_string은 문자열로 인스턴스를 만드는 메서드이며 is_time_valid는 문자열이 올바른 시간인지 검사하는 메서드입니다. 시간은 24시까지, 분은 59분까지, 초는 60초까지 있어야 합니다. 정답에 코드를 작성할 때는 class Time:에 맞춰서 들여쓰기를 해주세요.

~~~python

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

________________________________________________________
________________________________________________________
________________________________________________________
________________________________________________________
________________________________________________________
________________________________________________________

time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')

#입력
23:35:59

#결과
23 35 59

#입력
12:62:43

#결과
잘못된 시간 형식입니다.

~~~

답

~~~python


class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    @classmethod
    def from_string(cls, time_string):
        hour, minute, second = map(int, time_string.split(':'))
        time = cls(hour, minute, second)
        return time
    @staticmethod
    def is_time_valid(time_string):
        hour, minute, second = map(int, time_string.split(':'))
        return hour <=24 and minute <= 59 and second <=60


time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')


~~~




