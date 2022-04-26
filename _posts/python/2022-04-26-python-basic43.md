---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 모듈과 패키지 만들기
date: 2022-04-26 16:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 모듈과 패키지 만들기

<br>
<br>
파이썬 스크립트를 작성할 때마다 매번 비슷한 클래스와 함수를 작성한다면 코드도 길어지고 중복되는 부분이 생긴다. 이런 경우 공통되는 부분을 빼내 모듈과 패키지로 만든다. 이후 코드를 다시 만들지 않고 모듈과 패키지만 가져와서 사용하면 편리하다.

모듈(module)은 변수, 함수, 클래스 등을 모아 놓은 스크립트 파일이고, 패키지(package)는 여러 모듈을 묶은 것이다. 모듈은 간단한 기능을 담을 때 사용하고, 패키지는 코드가 많고 복잡할 때 사용한다. 즉, 패키지는 기능들이 모듈 여러 개로 잘게 나누어져 있고, 관련된 모듈끼리 폴더에 모여 있는 형태이다.

---

## 1.모듈 만들기
<br>
<br>

그럼 간단하게 2의 거듭제곱을 구하는 모듈을 만들어보자. 다음 내용을 작업환경에 저장한다. square2로 저장한다.


~~~python

base = 2          # 변수
 
def square(n):    # 함수
    return base ** n

~~~

### 모듈 사용하기
<br>
<br>

위에서 만든 모듈과 같은 폴더에 파일을 저장하고 실행해보자.

- import 모듈
- 모듈.변수
- 모듈.함수()


~~~python

import square2               # import로 square2 모듈을 가져옴
 
print(square2.base)          # 모듈.변수 형식으로 모듈의 변수 사용
print(square2.square(10))    # 모듈.함수() 형식으로 모듈의 함수 사용 2의10승

실행 결과
2
1024

~~~


### from import로 변수, 함수 가져오기
<br>
<br>

모듈에서 from import로 변수와 함수를 가져온 뒤 모듈 이름을 붙이지 않고 사용할 수도 있다.

- from 모듈 import 변수, 함수

~~~python

from square2 import base, square
print(base)
2
square(10)
1024

~~~

### 모듈에 클래스 작성하기
<br>
<br>

그럼 이번에는 모듈에 클래스를 작성하고 사용해보자. 다음 내용을 작업 폴더 안에 person.py 파일로 저장한다.

~~~python

class Person:    # 클래스
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
 
    def greeting(self):
        print('안녕하세요. 저는 {0}입니다.'.format(self.name))

~~~

이제 main2 파일을 다음과 같이 작성해 실행한다.

- import 모듈
- 모듈.클래스()

모듈의 클래스를 사용하는 방법도 변수, 함수와 같다. 즉, 모듈.클래스()형식으로 모듈의 클래스를 사용하며, 클래스로 인스턴스를 만들 때는 person.Person('마리아', 20, '서울시 서초구 반포동')와 같이 사용하면 된다.

### from import로 클래스 가져오기
<br>
<br>

물론 모듈에서 from import로 클래스를 가져온 뒤 모듈 이름을 붙이지 않고 사용할 수도 있다.

- from 모듈 import 클래스

~~~python

from person import Person
maria = Person('마리아', 20, '서울시 서초구 반포동')
maria.greeting()
안녕하세요. 저는 마리아입니다.

~~~

--

## 2.모듈과 시작점 알아보기
<br>
<br>
인터넷에 있는 파이썬 코드를 보다 보면 if __name__ == '__main__':으로 시작하는 부분을 자주본다.

~~~python

if __name__ == '__main__':
    코드

~~~

위 코드는 현재 스크립트 파일이 실행되는 상태를 파악하기 위해 사용한다.
먼저 __name__부터 알아보자. 다음 내용을 작업폴더에 hello파일로 저장한다.

~~~python

print('hello 모듈 시작')
print('hello.py __name__:', __name__)    # __name__ 변수 출력
print('hello 모듈 끝')

~~~

그리고 hello파일의 내용을 main3에 저장한뒤 실행해보자.

실행을 해보면 hello.py 파일과 main3.py 파일의 \__name__ 변수 값이 출력된다.

파이썬에서 import로 모듈을 가져오면 해당 스크립트 파일이 한 번 실행된다. 따라서 hello 모듈을 가져오면 hello.py 안의 코드가 실행된다. 따라서 hello.py의 \__name__ 변수에는 'hello'가 들어가고, main3.py의 \__name__ 변수에는 '\__main3__'이 들어간다.

~~~python

import hello    # hello 모듈을 가져옴
 
print('main.py __name__:', __name__)    # __name__ 변수 출력

# 실행 결과
hello 모듈 시작
hello.py __name__: hello
hello 모듈 끝
main.py __name__: __main3__

~~~

즉, \__name__은 모듈의 이름이 저장되는 변수이며 import로 모듈을 가져왔을 때 모듈의 이름이 들어간다. 하지만 파이썬 파이썬 인터프리터로 스크립트 파일을 직접 실행했을 때는 모듈의 이름이 아니라 '\__main__'이 들어간다.

좀 더 정확하게 알아보기 위해 콘솔에서 실행해보자. python main.py와 같이 파이썬으로 스크립트 파일을 직접 실행했다. 여기서도 hello.py 파일의 \__name__ 변수에는 'hello' 그리고 main.py 파일의 \__name__ 변수에는 '\__main__'이 들어간다

~~~python

C:\project>python main.py
hello 모듈 시작
hello.py __name__: hello
hello 모듈 끝
main.py __name__: __main__

~~~

하지만 다음과 같이 python으로 hello.py파일을 실행해보면 결과가 달라진다. hello.py파일의 \__name__ 변수에는 'hello'가 아니라 '\__main__'이 들어간다. 즉, 어떤 스크립트 파일이든 파이썬 인터프리터가 최초로 실행한 스크립트 파일의 __name__에는 '\__main__'이 들어간다. 이는 프로그램의 시작점(entry point)이라는 뜻이다.

~~~python

C:\project>python hello.py
hello 모듈 시작
hello.py __name__: __main__
hello 모듈 끝

~~~

파이썬은 최초로 시작하는 스크립트 파일과 모듈의 차이가 없다. 어떤 스크립트 파일이든 시작점도 될 수 있고, 모듈도 될 수 있다. 그래서 \__name__ 변수를 통해 현재 스크립트 파일이 시작점인지 모듈인지 판단한다.

if \__name__ == '\__main__':처럼 \__name__ 변수의 값이 '\__main__'인지 확인하는 코드는 현재 스크립트 파일이 프로그램의 시작점이 맞는지 판단하는 작업이다. 즉, 스크립트 파일이 메인 프로그램으로 사용될 때와 모듈로 사용될 때를 구분하기 위한 용도이다.

### 스크립트 파일로 실행하거나 모듈로 사용하는 코드 만들기
<br>
<br>
그럼 스크립트 파일을 그대로 실행할 수도 있고, 모듈로도 사용할 수 있는 코드를 만들어보자. 다음 내용을 프로젝트 폴더(C:\project) 안에 calc.py 파일로 저장한 뒤 실행해보자.

~~~python

def add(a, b):
    return a + b
 
def mul(a, b):
    return a * b
 
if __name__ == '__main__':    # 프로그램의 시작점일 때만 아래 코드 실행
    print(add(10, 20))
    print(mul(10, 20))

# 실행 결과
30
200

~~~

IDLE에서 실행하거나 python calc.py와 같이 파이썬 인터프리터로 실행하면 10, 20의 합과 곱이 출력된다. 즉, 프로그램의 시작점일 때는 if __name__ == '__main__': 아래의 코드가 실행된다.

그럼 calc.py를 모듈로 사용하면 어떻게 될까요? 다음과 같이 import로 calc를 가져와보자.

~~~python

import calc

#실행 결과

~~~

모듈로 가져왔을때는 아무것도 출력되지 않는다. 왜냐하면 \__name__ 변수 값이 '\__main__'일 때만 10, 20의 합과 곱을 출력하도록 만들었기 때문이다. 즉, 스크립트 파일을 모듈로 사용할 때는 calc.add, calc.mul처럼 함수만 사용하는 것이 목적임으로 10,20의 합과 곱을 출력하지 않는다.

모듈로 사용하려면 다음과 같이 calc.add와 calc.mul함수에 원하는 값을 넣어서 사용하면 된다.

~~~python

calc.add(50, 60)
110
calc.mul(50, 60)
3000

~~~

---

## 3. 패키지 만들기
<br>
<br>
이번에는 패키지를 만들어보자. 모듈은 스크립트 파일이 한 개지만 패키지는 폴더(디렉토리)로 구성되어 있다.

지금부터 만들 패키지의 폴더 구성은 다음과 같다.

project > main.py calcpkg
calcpkg> \__init__, operation.py, geometry.py

먼저 프로젝트 폴더(C:\project) 안에 calcpkg 폴더를 만들고 다음 내용을 calcpkg 폴더 안에 \__init__.py 파일로 저장한다.
폴더(디렉터리) 안에 __init__.py 파일이 있으면 해당 폴더는 패키지로 인식됩니다. 그리고 기본적으로 __init__.py 파일의 내용은 비워 둘 수 있다.

~~~python

# __init__.py 파일은 내용을 비워 둘 수 있음

~~~
                                                                                    

###  패키지에 모듈 만들기
<br>
<br>
이제 calcpkg 패키지에 모듈을 두 개를 만들어야한다. 첫 번째 모듈은 덧셈, 곱셈 함수가 들어있는 operation 모듈이고, 두 번째 모듈은 삼각형, 사각형의 넓이 계산 함수가 들어있는 geometry 모듈이다.

먼저 다음 내용을 calcpkg 폴더 안에 operation.py 파일로 저장한다.

~~~python

def add(a, b):
    return a + b
 
def mul(a, b):
    return a * b

~~~

그리고 다음 내용을 calcpkg 폴더 안에 geometry 파일로 저장한다.

~~~python

def triangle_area(base, height):
    return base * height / 2
 
def rectangle_area(width, height):
    return width * height

~~~

### 패키지 사용하기
<br>
<br>
이제 스크립트 파일에서 패키지의 모듈을 사용해보자. 다음 내용을 프로젝트 폴더(C:\project) 안에 main.py 파일로 저장한 뒤 실행한다(main.py 파일을 calcpkg 패키지 폴더 안에 넣으면 안 된다).

- import 패키지.모듈
- 패키지.모듈.변수
- 패키지.모듈.함수()
- 패키지.모듈.클래스()

calcpkg 패키지의 operation 모듈과 geometry 모듈을 가져와서 안에 들어있는 함수를 호출했다.

이처럼 패키지의 모듈을 가져올 때는 import 패키지.모듈 형식으로 가져온다. 그리고 패키지.모듈.함수() 형식으로 모듈의 함수를 사용한다(변수와 클래스도 같은 형식).

~~~python

import calcpkg.operation    # calcpkg 패키지의 operation 모듈을 가져옴
import calcpkg.geometry     # calcpkg 패키지의 geometry 모듈을 가져옴
 
print(calcpkg.operation.add(10, 20))    # operation 모듈의 add 함수 사용
print(calcpkg.operation.mul(10, 20))    # operation 모듈의 mul 함수 사용
 
print(calcpkg.geometry.triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(calcpkg.geometry.rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용

# 실행 결과
30
200
600.0
1200

~~~

### from import로 패키지의 모듈에서 변수, 함수, 클래스 가져오기
<br>
<br>
물론 패키지의 모듈에서 from import로 함수(변수, 클래스)를 가져온 뒤 패키지와 모듈 이름을 붙이지 않고 사용할 수도 있다.

- from 패키지.모듈 import 변수
- from 패키지.모듈 import 함수
- from 패키지.모듈 import 클래스

다음은 calcpkg 패키지의 operation 모듈에서 add, mul 함수를 가져온다.

~~~python

from calcpkg.operation import add, mul
add(10, 20)
30
mul(10, 20)
200

~~~

### 패키지의 모듈과 __name__
<br>
<br>
패키지의 모듈에서는 __name__ 변수에 패키지.모듈 형식으로 이름이 들어간다. 즉, calcpkg 패키지의 geometry.py에서 __name__의 값을 출력하도록 만들고, import로 가져오면 'calcpkg.geometry'가 나온다.

---

## 4. 패키지에서 from import 응용하기
<br>
<br>
지금까지 calcpkg 패키지의 모듈을 가져올 때 import calcpkg.operation처럼 import 패키지.모듈 형식으로 가져왔다. 그러면 그러면 import calcpkg처럼 import 패키지 형식으로 패키지만 가져와서 모듈을 사용할 수는 없을까? 이때는 calcpkg 패키지의 __init__.py 파일을 다음과 같이 수정한다.

~~~python

from . import operation    # 현재 패키지에서 operation 모듈을 가져옴
from . import geometry     # 현재 패키지에서 geometry 모듈을 가져옴

~~~

파이썬 에서 \__init__.py파일은 폴더가 패키지로 인식되도록 하는 역할도 하고, 이름 그대로 패키지를 초기화하는 역할도 한다. 즉, import로 패키지를 가져오면 \__init__.py 파일이 실행되므로 이 파일에서 from.import 모듈 형식으로 현재 패키지에서 모듈을 가져오게 만들어야 한다. 참고로 .(점)은 현재 패키지라는 뜻이다.

이제 main.py에서 import calcpkg와 같이 패키지만 가져오도록 수정한 뒤 실행해보자.

~~~python

import calcpkg    # calcpkg 패키지만 가져옴
 
print(calcpkg.operation.add(10, 20))    # operation 모듈의 add 함수 사용
print(calcpkg.operation.mul(10, 20))    # operation 모듈의 mul 함수 사용
 
print(calcpkg.geometry.triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(calcpkg.geometry.rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용

~~~

calcpkg의 \__init__.py에서 하위 모듈을 함께 가져오게 만들었으므로 import calcpkg로 패키지만 가져와도 calcpkg.operation.add(10, 20)처럼 사용할 수 있다.

### from import로 패키지에 속한 모든 변수, 함수, 클래스 가져오기
<br>
<br>
앞에서 form import 문법 중에  *(애스터리스크)를 지정하여 모든 변수, 함수, 클래스를 가져오는 방법이 있었다. 패키지에 속한 모든 변수, 함수, 클래스를 가져오려면 먼저 main.py에서 import calcpkg를 from calcpkg import *와 같이 수정하고, 각 함수들도 앞에 붙은 calcpkg.operation, calcpkg.geometry를 삭제한 뒤 실행해보자.

- from 패키지 import *

~~~python

from calcpkg import *    # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴
 
print(add(10, 20))    # operation 모듈의 add 함수 사용
print(mul(10, 20))    # operation 모듈의 mul 함수 사용
 
print(triangle_area(30, 40))    # geometry 모듈의 triangle_area 함수 사용
print(rectangle_area(30, 40))   # geometry 모듈의 rectangle_area 함수 사용

# 실행 결과
Traceback (most recent call last):
  File "C:\project\main.py", line 3, in <module>
    print(add(10, 20))    # operation 모듈의 add 함수 사용
NameError: name 'add' is not defined 

~~~

실행을 해보면 add가 정의되지 않았다면서 에러가 발생한다. 왜냐하면 __init__.py에서 모듈만 가져왔을 뿐 모듈 안의 함수는 가져오지 않았기 때문이다.

IDLE의 파이썬 프롬프트에서 dir 함수를 호출하여 현재 네임스페이스(namespace, 이름공간)를 확인해보자(main.py 안에서 print(dir())을 호출하고 main.py를 실행해도 됨).

~~~python

>>> dir()
['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'geometry', 'operation']

~~~

현재 네임스페이스에는 operation, geometry만 들어있어서 add, mul처럼 함수 이름만으로는 호출할 수가 없다.

이때는 \__init__.py에서 모듈 안의 함수를 가져오게 만들어야 한다. 특히 현재 패키지(calcpkg)라는 것을 명확하게 나타내기 위해 모듈 앞에 .(점)을 붙인다.

- from .모듈 import 변수, 함수, 클래스

이제 main.py 파일을 실행해보면 결과도 잘 출력되고 add, mul, triangle_area, rectangle_area처럼 함수 이름 그대로 호출할 수 있다.

~~~python

# 현재 패키지의 operation, geometry 모듈에서 각 함수를 가져옴
from .operation import add, mul
from .geometry import triangle_area, rectangle_area

# 실행 결과
30
200
600.0
1200

~~~

물론 __init__.py 파일에서 특정 함수(변수, 클래스)를 지정하지 않고 *을 사용해서 모든 함수(변수, 클래스)를 가져와도 상관없다.

- from .모듈 import *

~~~python

from .operation import *    # 현재 패키지의 operation 모듈에서 모든 변수, 함수, 클래스를 가져옴
from .geometry import *     # 현재 패키지의 geometry 모듈에서 모든 변수, 함수, 클래스를 가져옴

~~~

이렇게 패키지의 \__init__.py에서 from .모듈 import 변수, 함수, 클래스 또는 from .모듈 import * 형식으로 작성했다면 패키지를 가져오는 스크립트에서는 패키지.함수() 형식으로 사용할 수 있습니다(변수, 클래스도 같은 형식). 이때는 import calcpkg와 같이 패키지만 가져오면 됩니다.

- import 패키지
- 패키지.변수
- 패키지.함수()
- 패키지.클래스()

\__init__.py에서 from .모듈 import 변수, 함수, 클래스 또는 from .모듈 import * 형식으로 모듈을 가져오면 calcpkg 패키지의 네임스페이스에는 add, mul, triangle_area, rectangle_area가 들어간다. 따라서 모듈을 거치지 않고 calcpkg.add처럼 패키지에서 함수를 바로 사용할 수 있다.

~~~python

import calcpkg    # calcpkg 패키지만 가져옴
 
print(calcpkg.add(10, 20))   # 패키지.함수 형식으로 operation 모듈의 add 함수 사용
print(calcpkg.mul(10, 20))   # 패키지.함수 형식으로 operation 모듈의 mul 함수 사용
 
print(calcpkg.triangle_area(30, 40)) # 패키지.함수 형식으로 geometry 모듈의 triangle_area 함수 사용
print(calcpkg.rectangle_area(30, 40))# 패키지.함수 형식으로 geometry 모듈의 rectangle_area 함수 사용

# 실행 결과
30
200
600.0
1200

~~~

### __all__로 필요한 것만 공개하기
<br>
<br>
패키지의 __init__.py에서 from .모듈 import *로 모든 변수, 함수, 클래스를 가져오면 패키지 외부에 공개하고 싶지 않은 것까지 공개하게 된다. 이때는 __all__에 공개할 모듈, 변수, 함수, 클래스를 리스트 형태로 지정해주면 된다. __all__이라는 이름 그대로 모든 것(*)을 가져갈 때의 목록을 정한다.

~~~python

__all__ = ['add', 'triangle_area']    # calcpkg 패키지에서 add, triangle_area 함수만 공개
 
from .operation import *    # 현재 패키지의 operation 모듈에서 모든 변수, 함수, 클래스를 가져옴
from .geometry import *     # 현재 패키지의 geometry 모듈에서 모든 변수, 함수, 클래스를 가져옴

~~~

~~~python

from calcpkg import *    # calcpkg 패키지의 모든 변수, 함수, 클래스를 가져옴
 
print(add(10, 20))    # add 함수는 공개되어 있으므로 사용할 수 있음
print(mul(10, 20))    # 에러: mul 함수는 공개되어 있지 않으므로 사용할 수 없음
 
print(triangle_area(30, 40))    # triangle_area 함수는 공개되어 있으므로 사용할 수 있음
print(rectangle_area(30, 40))   # 에러: rectangle_area 함수는 공개되어 있으므로 사용할 수 있음

~~~

main.py에서 from calcpkg import *로 패키지의 모든 변수, 함수, 클래스를 가져온다 하더라도 __all__에 지정된 add, triangle_area 함수만 사용할 수 있다.

~~~python

30
Traceback (most recent call last):
  File "C:\project\main.py", line 4, in <module>
    print(mul(10, 20))    # 에러: mul 함수는 공개되어 있지 않으므로 사용할 수 없음
NameError: name 'mul' is not defined

~~~

### 하위 패키지 사용하기
<br>
<br>
파이썬의 패키지는 패키지 안에 하위 패키지를 만들 수 있다. 즉, 패키지 안에 폴더(디렉터리)를 만들고 __init__.py와 모듈을 넣으면 하위 패키지가 된다.

예를 들어서 다음과 같이 calcpkg 안에 operation과 geometry 하위 패키지가 있고, 그 아래에 모듈이 들어있다.

import로 하위 패키지의 모듈을 가져올 때는 계층 순서대로 .(점)을 붙여서 가져오면 됩니다.

- import 패키지.하위패키지.모듈

즉, import calcpkg.operation.element와 같은 식입니다. 함수를 사용할 때는 calcpkg.operation.element.add(10, 20)이 되겠다.

만약, import calcpkg처럼 패키지만 가져와서 사용하고 싶다면 calcpkg/\__init__.py에서 하위 패키지의 모듈에 들어있는 변수, 함수, 클래스를 모두 가져오게 만들면 된다.

~~~python

from .operation.element import *
from .operation.logic import *
from .geometry.shape import *
from .geometry.vector import *

~~~

이렇게 하면 calcpkg.add(10, 20), calcpkg.triangle_area(30, 40) 또는, add(10, 20), triangle_area(30, 40)처럼 사용할 수 있다.

참고로 하위 패키지 안에서 옆에 있는 패키지의 요소를 가져와서 사용하려면 ..을 사용해야 합니다. ..은 상위 폴더(디렉터리)라는 뜻이며 ..패키지 또는 ..모듈은 상위 폴더에 있는 패키지, 모듈이라는 뜻이다. 즉, 현재 패키지와 같은 계층의 패키지 또는 모듈이다. 그리고 ...은 상위 폴더의 상위 폴더라는 뜻이며 위로 갈 수록 .이 하나씩 늘어난다.

- from ..패키지 import 모듈

- from ..패키지.모듈 import 클래스, 변수, 함수

- from ..패키지.모듈 import *

예를 들어 calcpkg/geometry/shape.py에서 옆에 있는 calcpkg/operation 패키지의 element 모듈을 사용한다면 다음과 같이 from ..operation import element로 지정해준다. 또는, from ..operation.element import mul과 같이 지정하면 mul을 함수 그대로 사용할 수 있다.

~~~python

from ..operation import element             # from ..operation.element import mul로도 가능
 
def triangle_area(base, height):
    return element.mul(base, height) / 2    # mul(base, height)로도 가능
 
def rectangle_area(width, height):
    return element.mul(width, height)       # mul(width, height)로도 가능

~~~

### 모듈과 패키지의 독스트링
<br>
<br>
모듈의 독스트링은 모듈 파일의 첫 줄에 """ """(큰따옴표 세 개) 또는 ''' '''(작은따옴표 세 개)를 사용하여 문자열을 넣는다.

~~~python

'''모듈의 독스트링'''

~~~

패키지의 독스트링은 \__init__.py 파일의 첫 줄에 """ """(큰따옴표 세 개) 또는 ''' '''(작은따옴표 세 개)를 사용하여 문자열을 넣는다.

~~~python

'''패키지의 독스트링'''

~~~

모듈과 패키지의 독스트링을 출력하려면 모듈 또는 패키지의 \__doc__를 출력하면 된다.

~~~python

모듈.__doc__
패키지.__doc__

~~~

---


### 예제1
<br>
<br>
다음 소스 코드를 완성하여 소수점 이하를 올림, 버림한 숫자가 출력되게 만드세요. 올림 함수는 math 모듈의 ceil, 버림 함수는 math 모듈의 floor 함수입니다.

~~~python

 _______________________                               
 
x = 1.5
 
print(ceil(x), floor(x))

#실행 결과
2 1

~~~


답

~~~python

from math import ceil, floor

~~~

### 예제2
<br>
<br>
표준 입력으로 URL 문자열이 입력 입력됩니다. 입력된 URL이 올바르면 True, 잘못되었으면 False를 출력하는 프로그램을 만드세요. 이 심사문제에서 판단해야 할 URL의 규칙은 다음과 같습니다.

- http:// 또는 https://로 시작
- 도메인은 도메인.최상위도메인 형식이며 영문 대소문자, 숫자, -로 되어 있어야 함
- 도메인 이하 경로는 /로 구분하고, 영문 대소문자, 숫자, -, _, ., ?, =을 사용함

~~~python

________________
________________
________________


# 입력
http://www.example.com/hello/world.do?key=python
# 결과
True
# 입력
https://example/hello/world.html
# 결과
False

~~~

내가 쓴 답

~~~python

import re

url = input()

p = re.compile('^[a-zA-Z0-9]+\:\/\/[a-zA-Z0-9.]+\.[a-zA-Z0-9.-_?=/]')

print(p.match(url) != None, end=' ')

~~~

답

~~~python

import re

p = re.compile('^(http?://)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]*')

print(p.match(input()) != None)


~~~


먼저 URL은 http:// 또는 https://로 시작한다고 했으므로 정규표현식은 ^https?://로 시작합니다. 여기서 맨 앞에 ^를 붙였으므로 http 또는 https로 시작하는지 판단합니다. 그리고 https?와 같이 만들면 s가 0개 또는 1개 있어야 합니다. 따라서 http와 https를 둘 다 판별할 수 있습니다.

이제 도메인을 판단합니다. 도메인 부분은 [a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/와 같이 만들어줍니다. 먼저 [a-zA-Z0-9-]+와 같이 영문 대소문자, 숫자, -이면서 문자 1개 이상인지 판단합니다. 그리고 중간에 \.를 넣어서 도메인.최상위도메인 형식인지 판단합니다. 여기서 .은 정규표현식에 사용하는 특수 문자이므로 앞에 반드시 \를 붙여야 합니다. 특히 최상위 도메인은 여러 단계일 수도 있으므로 [a-zA-Z0-9-.]+/와 같이 범위에 .을 넣어줍니다. 그리고 도메인과 도메인 이하 경로를 구분할 수 있도록 /를 붙여줍니다.

도메인 이하 경로는 영문 대소문자, 숫자, -, \_, ., ?, =을 사용한다고 했으므로 [a-zA-Z0-9-_/.?=]\*와 같이 만들어줍니다. 특히 하위 경로가 더 나올 수 있으므로 범위 안에 /를 넣어야 합니다.

지금까지 만든 정규표현식을 차례대로 연결해서 re.match 함수로 url을 판단해주면 됩니다. 그리고 re.match 함수의 반환값이 있으면(None이 아니면) True를 출력하고, None이면 False를 출력하면 됩니다.