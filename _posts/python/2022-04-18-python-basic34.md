---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 클래스 상속 사용하기
date: 2022-04-18 23:50 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 클래스 상속 사용하기

<br>
<br>
지금까지 클래스의 기본적인 사용 방법을 알아보았다. 이번에는 클래스 상속(inheritance)을 사용해보자. 

상속은 무언가를 물려 받는다는 뜻이다. 클래스 상속은 물려받은 기능을 유지한채로 다른 기능을 추가할 때 사용한다. 여기서 기능을 물려주는  클래스를 기반 클래스(base class), 상속을 받아 새롭게 만드는 클래스를 파생 클래스(derived class)라고 한다.

보통 기반 클래스는 부모클래스(parent class), 슈퍼 클래스(super class)라고 부르고, 파생 클래스는 자식 클래스(child class), 서브 클래스(subclass)라고도 부른다.

새로운 기능이 필효할때 계속 클래스를 만든다면 중복되는 부분을 반복해서 만들어야 한다. 이럴 때 상속을 사용하면 중복되는 기능을 만들지 않아도 된다. 따라서 상속은 기존 기능을 재사용할 수 있어서 효율적이다.


---

## 1. 사람 클래스로 학생 클래스 만들기
<br>
<br>
클래스 상속은 다음과 같이 클래스를 만들 때()괄호 를 붙이고 안에 기반 클래스 이름을 넣는다.

 
~~~python

class 기반클래스이름:
    코드
 
class 파생클래스이름(기반클래스이름):
    코드

~~~

그럼 간단하게 사람 클래스를 만들고 사람 클래스를 상속받아 학생 클래스를 만들어보자.

student클래스를 만들 때 class student(Person):과 같이 ()괄호 안에 기반 클래스인 person클래스를 넣었다. 이렇게 하면 person클래스의 기능을 불려받은 Student클래스가 된다. Student 클래스에는 greeting 메서드가 없지만 Person 클래스를 상속받았으므로 greeting 메서드를 호출할 수 있다.

~~~python

class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def study(self):
        print('공부하기')
 
james = Student()
james.greeting()    # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.study()       # 공부하기: 파생 클래스 Student에 추가한 study 메서드

#실행 결과
안녕하세요.
공부하기

~~~

이처럼 클래스 상속은 기반 클래스의 기능을 유지하면서 새로운 기능을 추가할 수 있다. 특히 클래스 상속은 연관되면서 동등한 기능일 때 사용한다. 즉, 학생은 사람이므로 연관된 개념이고, 학생은 사람에서 역할만 확장되었을 뿐 동등한 개념이다.

### 상속 관계 확인하기
<br>
<br>
클래스의 상속 관계를 확인하고 싶을 때는 issubclass 함수를 사용한다. 즉, 클래스가 기반 클래스의 파생 클래스인지 확인한다. 기반 클래스의 파생 클래스가 맞으면 True, 아니면 False를 반환한다.

- issubclass(파생클래스, 기반클래스)

Student가 Person의 파생 클래스이므로 issubclass는 True가 나오게된다.

~~~python

class Person:
     pass

class Student(Person):
     pass

issubclass(Student, Person)
True

~~~


---

## 2. 상속 관계와 포함 관계 알아보기
<br>
<br>
클래스 상속을 어디에 사용하는지 알아보자.

### 상속 관계
<br>
<br>
위에서 만든 Student 클래스는 Person 클래스를 상속받아서 만들었다. 여기서 학생 Student는 사람 Person이므로 같은 종류다. 이처럼 상속은 명확하게 같은 종류이며 동등한 관계일 때 사용한다. 즉, "학생은 사람이다."라고 했을 때 말이 되면 동등한 관계다. 그래서 상속 관계를 영어로 is-a 관계라고 부른다(Student is a Person).

~~~python

class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def study(self):
        print('공부하기')

~~~

### 포함 관계
<br>
<br>

하지만 학생 클래스가 아니라 사람 목록을 관리하는 클래스를 만든다면 어떻게 할까? 다음과 같이 리스트 속성에 Person인스턴스를 넣어서 관리하면 된다.

여기서는 상속을 사용하지 않고 속성에 인스턴스를 넣어서 관리하므로 PersonList가 Person을 포함하고 있다. 이러면 사람 목록 PersonList와 사람 Person은 동등한 관계가 아니라 포함 관계다. 즉, "사람 목록은 사람을 가지고 있다."라고 말할 수 있다. 그래서 포함 관계를 영어로 has-a 관계라고 부른다(PersonList has a Person).

정리하자면 같은 종류에 동등한 관계일 때는 상속을 사용하고, 그 이외에는 속성에 인스턴스를 넣는 포함 방식을 사용하면 되겠다.

~~~python

class Person:
    def greeting(self):
        print('안녕하세요.')
 
class PersonList:
    def __init__(self):
        self.person_list = []    # 리스트 속성에 Person 인스턴스를 넣어서 관리
 
    def append_person(self, person):    # 리스트 속성에 Person 인스턴스를 추가하는 함수
        self.person_list.append(person)
~~~



---

## 3. 기반 클래스의 속성 사용하기
<br>
<br>
기반 클래스에 들어있는 인스턴스 속성을 사용해보자. 다음과 같이 Person 클래스에 hello속성이 있고, Person클래스를 상속받아 Student 클래스를 만든다. 그다음에 Student로 인스턴스를 만들고 hello 속성에 접근해본다.

실행해보면 에러가 발생한다. 왜냐하면 기반 클래스 Person의 \__init__ 메서드가 호출되지 않았기 때문이다. 실행 결과를 잘 보면 'Student \__init__'만 출력되었다. 즉, Person의 \__init__ 메서드가 호출되지 않으면 self.hello = '안녕하세요.'도 실행되지 않아서 속성이 만들어지지 않는다.


~~~python

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        self.school = '파이썬 코딩 도장'
 
james = Student()
print(james.school)
print(james.hello)    # 기반 클래스의 속성을 출력하려고 하면 에러가 발생함

~~~

~~~python

Student __init__
파이썬 코딩 도장
Traceback (most recent call last):
  File "C:\project\class_inheritance_attribute_error.py", line 14, in <module>
    print(james.hello)
AttributeError: 'Student' object has no attribute 'hello' 

~~~

### super()로 기반 클래스 초기화하기
<br>
<br>
이때는 super()를 사용해서 기반 클래스의 __init__ 메서드를 호출해준다. 다음과 같이 super() 뒤에 .(점)을 붙여서 메서드를 호출하는 방식이다.

- super().메서드()

실행을 해보면 기반 클래스 Person의 속성인 hello가 잘 출력된다. super().\__init__()와 같이 기반 클래스 Person의 \__init__ 메서드를 호출해주면 기반 클래스가 초기화되어서 속성이 만들어진다. 실행 결과를 보면 'Student \__init__'과 'Person \__init__'이 모두 출력되었다.


~~~python

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    def __init__(self):
        print('Student __init__')
        super().__init__()                # super()로 기반 클래스의 __init__ 메서드 호출
        self.school = '파이썬 코딩 도장'
 
james = Student()
print(james.school)
print(james.hello)

~~~

### 기반 클래스를 초기화하지 않아도 되는 경우
<br>
<br>

만약 파생클래스에서 \__init__ 메서드를 생략한다면 기반 클래스의 \__init__이 자동으로 호출되므로 super()는 사용하지 않아도 된다. 이처럼 파생 클래스에 \__init__ 메서드가 없다면 기반 클래스의 \__init__이 자동으로 호출되므로 기반 클래스의 속성을 사용할 수 있다.


~~~python

class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = '안녕하세요.'
 
class Student(Person):
    pass
 
james = Student()
print(james.hello)

#실행 결과
Person __init__
안녕하세요.

~~~

### 좀 더 명확하게 super 사용하기
<br>
<br>
super는 다음과 같이 파생 클래스와 self를 넣어서 현재 클래스가 어떤 클래스인지 명확하게 표시하는 방법도 있다. 물론 super()와 기능은 같다.


- super(파생클래스, self).메서드
~~~python

class Student(Person):
    def __init__(self):
        print('Student __init__')
        super(Student, self).__init__()     # super(파생클래스, self)로 기반 클래스의 메서드 호출
        self.school = '파이썬 코딩 도장'

~~~

---

## 4. 메서드 오버라이딩 사용하기
<br>
<br>
이번에는 파생 클래스에서 기반 클래스의 메서드를 새로 정의하는 메서드 오버라이딩에 대해 알아보자. 다음과 같이 Person의 greeting메서드가 있는 상태에서 Student에도 greeting 메서드를 만든다. james.greeting()처럼 Student의 greeting 메서드를 호출하니 '안녕하세요. 저는 학생입니다.'가 출력되었다. 

~~~python

class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
        print('안녕하세요. 저는 학생입니다.')
 
james = Student()
james.greeting()

#실행 결과
안녕하세요. 저는 학생입니다.

~~~

오버라이딩(overriding)은 무시하다, 우선하다라는 뜻을 가지고 있는데 말 그대로 기반 클래스의 메서드를 무시하고 새로운 메서드를 만든다는 뜻이다. 여기서는 Person 클래스의 greeting 메서드를 무시하고 Student 클래스에서 새로운 greeting 메서드를 만들었다.

오버라이딩은 프로그램에서 어떤 기능이 같은 메서드 이름으로 계속 사용되어야 할 때 메서드 오버라이딩을 활용한다. 만약 Student클래스에서 인사하는 메서드를 greeting2로 만들어야 한다면 모든 소스 코드에서 메서드 호출 부분을 greeting2로 수정해야한다.

다시 Person 클래스의 greeting 메서드와 Student 클래스의 greeting 메서드를 보면 '안녕하세요.'라는 문구가 중복된다.

~~~python

    def greeting(self):
        print('안녕하세요.')


    def greeting(self):
        print('안녕하세요. 저는 학생입니다.')

~~~

이럴 때는 기반 클래스의 메서드를 재활용하면 중복을 줄일 수 있다. 다음과 같이 오버라이딩된 메서드에서 super()로 기반 클래스의 메서드를 호출해보자.

~~~python

class Person:
    def greeting(self):
        print('안녕하세요.')
 
class Student(Person):
    def greeting(self):
        super().greeting()    # 기반 클래스의 메서드 호출하여 중복을 줄임
        print('저는 학생입니다.')
 
james = Student()
james.greeting()

#실행 결과
안녕하세요.
저는 학생입니다.

~~~

Student의 greeting에서 super().greeting()으로 Person의 greeting을 호출했다. 즉, 중복되는 기능은 파생 클래스에서 다시 만들지 않고, 기반 클래스의 기능을 사용하면 된다.

이처럼 메서드 오버라이딩은 원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용한다.

---

## 5.다중 상속 사용하기
<br>
<br>
다중 상속은 여러 기반 클래스로부터 상속을 받아서 파생 클래스를 만드는 방법이다. 다음과 같이 클래스를 만들 때 ( )(괄호) 안에 클래스 이름을 ,(콤마)로 구분해서 넣는다.

~~~python

class 기반클래스이름1:
    코드
 
class 기반클래스이름2:
    코드
 
class 파생클래스이름(기반클래스이름1, 기반클래스이름2):
    코드

~~~

그럼 사람 클래스와 대학교 클래스를 만든 뒤 다중 상속으로 대학생 클래스를 만들어보자.

~~~python

class Person:
    def greeting(self):
        print('안녕하세요.')
 
class University:
    def manage_credit(self):
        print('학점 관리')
 
class Undergraduate(Person, University):
    def study(self):
        print('공부하기')
 
james = Undergraduate()
james.greeting()         # 안녕하세요.: 기반 클래스 Person의 메서드 호출
james.manage_credit()    # 학점 관리: 기반 클래스 University의 메서드 호출
james.study()            # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드

#실행 결과
안녕하세요.
학점 관리
공부하기

~~~

먼저 기반 클래스 Person과 University를 만들었다. 그다음에 파생 클래스 Undergraduate를 만들 때 class Undergraduate(Person, University):와 같이 괄호 안에 Person과 University를 콤마로 구분해서 넣었다. 이렇게 하면 두 기반 클래스의 기능을 모두 상속받을 수 있다.

###  다이아몬드 상속
<br>
<br>
다이아몬드 상속에 대해 알아보자. 여기서는 편의상 클래스 이름을 A, B, C, D로 만들었다. 클래스 간의 관계가 다이아몬드 같이 생겼다 그래서 객체지향 프로그래밍에서는 이런 상속 관계를 다이아몬드 상속이라 부른다.


~~~python

class A:
    def greeting(self):
        print('안녕하세요. A입니다.')
 
class B(A):
    def greeting(self):
        print('안녕하세요. B입니다.')
 
class C(A):
    def greeting(self):
        print('안녕하세요. C입니다.')
 
class D(B, C):
    pass
 
x = D()
x.greeting()    # 안녕하세요. B입니다.

#실행 결과
안녕하세요. B입니다.

~~~

기반 클래스 A가 있고, B, C는 A를 상속받는다. 그리고 다시 D는 B, C를 상속받는다. 이 관계를 그림으로 나타내면 다음과 같은 모양이 된다.

![다이아몬드 상속](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wikiwand.com%2Fko%2F%25EB%258B%25A4%25EC%25A4%2591_%25EC%2583%2581%25EC%2586%258D&psig=AOvVaw2FlkA_Qu8QVDgMwbr3qY9b&ust=1650376151092000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCOjX0bbgnfcCFQAAAAAdAAAAABAD)

여기서는 클래스 A를 상속받아서 B, C를 만들고, 클래스 B와 C를 상속받아서 D를 만들었다. 그리고 A, B, C 모두 greeting이라는 같은 메서드를 가지고 있다면 D는 어떤 클래스의 메서드를 호출해야 할지 조금 애매하다. 프로그래밍에서는 이렇게 명확하지 않고 애매한 상태를 좋아하지 않는다. 프로그램이 어떨 때는 A의 메서드를 호출하고, 또 어떨 때는 B 또는 C의 메서드를 호출한다면 큰 문제가 생긴다. 그래서 다이아몬드 상속은 문제가 많다고 해서 죽음의 다이아몬드라고도 부른다.


### 메서드 탐색 순서 확인하기
<br>
<br>
많은 프로그래밍 언어들이 다이아몬드 상속에 대한 해결책을 제시하고 있는데 파이썬에서는 메서드 탐색 순서(Method Resolution Order, MRO)를 따른다. 다음과 같이 클래스 D에 메서드 mro를 사용해보면 메서드 탐색 순서가 나온다(클래스.__mro__ 형식도 같은 내용)


- 클래스.mro()
~~~python

D.mro()
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]

~~~

MRO에 따르면 D의 메서드 호출 순서는 자기 자신 D, 그 다음이 B다. 따라서 D로 인스턴스를 만들고 greeting을 호출하면 B의 greeting이 호출된다( D는 greeting 메서드가 없으므로).

~~~python

x = D()
x.greeting()    # 안녕하세요. B입니다.

~~~

파이썬은 다중 상속을 한다면 class D(B, C):의 클래스 목록 중 왼쪽에서 오른쪽 순서로 메서드를 찾는다. 그러므로 같은 메서드가 있다면 B가 우선한다. 만약 상속 관계가 복잡하게 얽혀 있다면 MRO를 살펴보는 것이 편리하다.

### object 클래스
<br>
<br>
파이썬에서 object는 모든 클래스의 조상이다. 그래서 int의 MRO를 출력해보면 int 자기 자신과 object가 출력된다.

~~~python

>>> int.mro()
[<class 'int'>, <class 'object'>]

~~~

파이썬 3에서 모든 클래스는 object 클래스를 상속받으므로 기본적으로 object를 생략한다. 다음과 같이 클래스를 정의한다면

~~~python

class X:
    pass

~~~

괄호 안에 object를 넣은 것과 같다.

~~~python

class X(object):
    pass
    
~~~

파이썬 3에서는 괄호 안에 object를 넣어도 되고 넣지 않아도 된다.

---

## 6.추상 클래스 사용하기
<br>
<br>
파이썬은 추상 클래스(abstract class)라는 기능을 제공한다. 추상 클래스는 메서드의 목록만 가진 클래스이며 상속받는 클래스에서 메서드 구현을 강제하기 위해 사용된다.

먼저 추상 클래스를 만들려면 import로 abc 모듈을 가져와야 한다( abc는 abstract base class의 약자입니다). 그리고 클래스의 ( )(괄호) 안에 metaclass=ABCMeta를 지정하고, 메서드를 만들 때 위에 @abstractmethod를 붙여서 추상 메서드로 지정한다.

여기서는 from abc import *로 abc 모듈의 모든 클래스와 메서드를 가져왔다. 만약 import abc로 모듈을 가져왔다면 abc.ABCMeta, @abc.abstractmethod로 사용해야 한다.

~~~python

from abc import *
 
class 추상클래스이름(metaclass=ABCMeta):
    @abstractmethod
    def 메서드이름(self):
        코드

import abc
class 클래스이름(metaclass=abc.ABCMeta):

~~~

그럼 학생 추상 클래스 StudentBase를 만들고, 이 추상 클래스를 상속받아 학생 클래스 Student를 만들어보자.

~~~python

from abc import *
 
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
 
    @abstractmethod
    def go_to_school(self):
        pass
 
class Student(StudentBase):
    def study(self):
        print('공부하기')
 
james = Student()
james.study()

#실행 결과
Traceback (most recent call last):
  File "C:\project\class_abc_error.py", line 16, in <module>
    james = Student()
TypeError: Can't instantiate abstract class Student with abstract methods go_to_school 

~~~

실행을 해보면 에러가 발생한다. 왜냐하면 추상 클래스 StudentBase에서는 추상 메서드로 study와 go_to_school을 정의했다. 하지만 StudentBase를 상속받은 Student에서는 study 메서드만 구현하고, go_to_school 메서드는 구현하지 않았으므로 에러가 발생한다.

따라서 추상 클래스를 상속받았다면 @abstractmethod가 붙은 추상 메서드를 모두 구현해야 한다. 다음과 같이 Student에서 go_to_school 메서드도 구현해준다.

~~~python

from abc import *
 
class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
 
    @abstractmethod
    def go_to_school(self):
        pass
 
class Student(StudentBase):
    def study(self):
        print('공부하기')
 
    def go_to_school(self):
        print('학교가기')
 
james = Student() # 추상클래스의 추상 매서드를 모두 구현했는지 확인하는 시점
james.study()
james.go_to_school()


#실행 결과
공부하기
학교가기

~~~

모든 추상 메서드를 구현하니 실행이 잘 된다.

StudentBase는 학생이 반드시 해야 하는 일들을 추상 메서드로 만들었습니다. 그리고 Student에는 추상 클래스 StudentBase의 모든 추상 메서드를 구현하여 학생 클래스를 작성했다. 이처럼 추상 클래스는 파생 클래스가 반드시 구현해야 하는 메서드를 정해줄 수 있다.

참고로 추상 클래스의 추상 메서드를 모두 구현했는지 확인하는 시점은 파생 클래스가 인스턴스를 만들 때 이다. 따라서 james = Student()에서 확인한다(구현하지 않았다면 TypeError 발생).

### 추상 메서드를 빈 메서드로 만드는 이유
<br>
<br>
그리고 또 한 가지 중요한 점이 있는데 추상 클래스는 인스턴스로 만들 수가 없다는 점이다. 다음과 같이 추상 클래스 StudentBase로 인스턴스를 만들면 에러가 발생한다.

~~~python

>>> james = StudentBase()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    james = StudentBase()
TypeError: Can't instantiate abstract class StudentBase with abstract methods go_to_school, study

~~~

그래서 지금까지 추상 메서드를 만들 때 pass만 넣어서 빈 메서드로 만든 것이다. 왜냐하면 추상 클래스는 인스턴스를 만들 수 없으니 추상 메서드도 호출할 일이 없기 때이다.

~~~python

    @abstractmethod
    def study(self):
        pass    # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦
 
    @abstractmethod
    def go_to_school(self):
        pass    # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦

~~~

정리하자면 추상 클래스는 인스턴스로 만들 때는 사용하지 않으며 오로지 상속에만 사용한다. 그리고 파생 클래스에서 반드시 구현해야 할 메서드를 정해 줄 때 사용한다.


---


### 예제1
<br>
<br>
다음 소스 코드에서 리스트(list)에 replace 메서드를 추가한 AdvancedList 클래스를 작성하세요. AdvancedList는 list를 상속받아서 만들고, replace 메서드는 리스트에서 특정 값으로 된 요소를 찾아서 다른 값으로 바꾸도록 만드세요.

~~~python

 ______________                                           
...
 ______________                                          
 
x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)

# 실행 결과
[100, 2, 3, 100, 2, 3, 100, 2, 3]

~~~


답

~~~python

class AdvancedList(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new

~~~

list를 상속받아서 AdvancedList를 만들라고 했으므로 클래스는 class AdvancedList(list):와 같이 만듭니다.

replace 메서드는 리스트에서 특정 값으로 된 요소를 찾아서 다른 값으로 바꾼다고 했습니다. 먼저 클래스의 메서드 안에서 현재 객체를 조작하려면 self를 이용해야 합니다. 여기서는 AdvancedList가 list를 상속받았으므로 self로 리스트의 모든 메서드를 사용할 수 있습니다.

특정 값을 찾을 때는 리스트의 index 메서드를 사용하고, index로 찾은 인덱스를 self에 지정해준 뒤 새 값을 할당하면 값을 바꿀 수 있습니다. 이때 리스트에서 같은 값이 여러 개 들어있을 수도 있으므로 모든 값을 바꿔주어야 합니다.

즉, while로 반복하면서 self에 특정 요소가 있을 때 계속 반복하도록 만든 뒤 요소를 바꿔주면 됩니다. 물론 리스트에서 특정 요소가 있는지 확인할 때는 in 연산자를 사용합니다. 이 방식을 사용하면 리스트에서 요소를 계속 바꾸다가 바꿀 값이 없으면 반복을 끝냅니다.

while self.count(찾을값) != 0:처럼 count 메서드를 사용해서 요소 개수가 0이 아닐 때 계속 반복하는 방식도 가능합니다.

### 예제2
<br>
<br>
다음 소스 코드에서 동물 클래스 Animal과 날개 클래스 Wing을 상속받아 새 클래스 Bird를 작성하여 '먹다', '파닥거리다', '날다', True, True가 각 줄에 출력되게 만드세요.

~~~python

class Animal:
    def eat(self):
        print('먹다')
 
class Wing:
    def flap(self):
        print('파닥거리다')
________________
________________
________________
________________

b = Bird()
b.eat()
b.flap()
b.fly()
print(issubclass(Bird, Animal))
print(issubclass(Bird, Wing))

#결과
먹다
파닥거리다
날다
True
True

~~~

내가 쓴 답

~~~python

class Bird(Animal, Wing):
    def fly(self):
        print('날다')

~~~



