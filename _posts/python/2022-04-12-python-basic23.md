---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 딕셔너리 응용하기
date: 2022-04-12 17:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 딕셔너리 응용하기
<br>
<br>
딕셔너리의 키-값 쌍을 조작하는 메서드 정보를 조회하는 메서드를 사용해보자. 그리고 for 반복문을 사용하여 키와 값에 접근하는 방법, 딕셔너리 표현식, 중첩 딕셔너리를 알아보자.

---

## 1. 딕셔너리 조작하기
<br>
<br>
딕셔너리를 조작하는 메서드와 정보를 얻는 메서드를 알아보자.

<br>
<br>

### 딕셔너리에 키-값 쌍 추가하기
<br>
<br>

딕셔너리의 중요한 기능중 하나는 키-값 쌍 추가이다. 두가지 메서드를 사용하는 방법으로 키-값 쌍을 추가할 수 있다.

- setdefault: 키-값 쌍 추가
- update: 키의 값 수정, 키가 없으면 키-값 쌍 추가

### 딕셔너리에 키와 기본값 저장하기
<br>
<br>

**setdefault(키)**는 딕셔너리에 키-값 쌍을 추가한다. setdefault에 키만 지정하면 값에 None을 저장한다. 키 'e'를 추가하고 값에 None을 저장하는 코드다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
x
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': None}

~~~

키 'f'를 추가하고 값에 100을 저장한뒤 100을 반환한다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('f',100)
100
x
{'a': 10, 'b': 20, 'c': 30, 'd': 40, 'f': 100}

~~~


### 딕셔너리에서 키의 값 수정하기
<br>
<br>

**update(키=값)**는 키-값 쌍을 수정하는 메서드이다. 예를 들어 x = {'a' : 10}이라면 x.update(a=90)과 같이 키에서 작은 따옴표 또는 큰따옴표를 빼고 키 이름과 값을 지정한다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=90)
x
{'a': 90, 'b': 20, 'c': 30, 'd': 40}

~~~

만약 딕셔너리에 키가 없으면 키-값 쌍을 추가한다. 딕셔너리 x에는 키 'e'가 없기떄문에 x.update(e=50)을 실행하면 'e' : 50을 추가한다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(e=50)
x
{'a': 90, 'b': 20, 'c': 30, 'd': 40, 'e': 50}

~~~

키-값 쌍 여러 개를 콤마로 구분해서 넣어주면 값을 한꺼번에 수정할 수 있다. 이때도 키가 있으면 해당 키의 값을 수정하고 없으면 키-값 쌍을 추가한다. 다음은 키 'a'의 값을 900으로 수정하고 'f':60을 추가한다. 

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=900, f=60)
x
{'a': 900, 'b': 20, 'c': 30, 'd': 40, 'e': 50, 'f': 60}

~~~

update(키=값)은 키가 문자열일 때만 사용할 수 있다. 만약 키가 숫자일 경우에는 **update(딕셔너리)**처럼 딕셔너리를 넣어서 값을 수정할 수 있다.

~~~python

y = {1: 'one', 2: 'two'}
y.update({1: 'ONE', 3: 'THREE'})
y
{1: 'ONE', 2: 'two', 3: 'THREE'}

~~~

다른 방법으로는 리슽트와 튜플을 이용하는 방법도 있다. update(리스트), update(튜플)은 리스트와 튜플로 값을 수정한다. 여기서 리스트는 [[키1, 값1]], [[키2, 값2]] 형식으로 키와 값을 리스트로 만들고 이 리스트를 다시 리스트 안에 넣어서 키-값 쌍을 나열해준다.

~~~python

y = {1: 'ONE', 2: 'two', 3: 'THREE'}
y.update([[2, 'TWO'], [4, 'FOUR']])
y
{1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR'}

~~~

특히 **update(반복가능한객체)**는 키-값 쌍으로 된 반복 가능한 객체로 값을 수정한다. 즉, 다음과 같이 키 리스트와 값 리스트를 묶은 zip 객체로 값을 수정할 수 있다.

~~~python

y = {1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR'}
y.update(zip([1, 2], ['one', 'two']))
y
{1: 'one', 2: 'two', 3: 'THREE', 4: 'FOUR'}

~~~

### setdefault와 update의 차이
<br>
<br>
setdefault는 키-값 쌍 추가만 할 수 있고, 이미 들어있는 키의 값은 수정할 수 없다. 하지만 update는 키-값 쌍 추가와 값 수정이 모두 가능하다. 다음과 같이 setdefault로 이미 들어있는 키'a'를 90으로 저장해도 'a'의 값은 바뀌지 않는다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('a', 90)
10
x
{'a': 10, 'b': 20, 'c': 30, 'd': 40} # a의 값이 바뀌지 않음

~~~

### 딕셔너리에서 키-값 쌍 삭제하기
<br>
<br>

**pop(키)**는 딕셔너리에서 특정 키-값 쌍을 삭제한 뒤 삭제한 값을 반환한다. 다음은 딕셔러니 x에서 키'a'를 삭제한 뒤 10을 반환한다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.pop('a')
10
x
{'b': 20, 'c': 30, 'd': 40}

~~~

**pop(키, 기본값)**처럼 기본값을 지정하면 딕셔너리에 키가 있을 때는 해당 키-값 쌍을 삭제한뒤 삭제한 값을 반환하지만 키가 없을 때는 기본값만 반환한다. 딕셔러니 x에는 키'z'가 없으므로 기본값으로 지정한 0을 반환한다.

~~~python

x.pop('z', 0)
0

~~~

pop 대신 del로 특정 키-값 쌍을 삭제할 수도 있다. 이때는 [ ]에 키를 지정하여 del을 사용한다. 다음은 딕셔너리 x의 키 'a'를 삭제한다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
del x['a']
x
{'b': 20, 'c': 30, 'd': 40}

~~~

### 딕셔너리에서 임의의 키-값 쌍 삭제하기
<br>
<br>

**popitem()**은 딕셔너리에서 <임의의 키-값 쌍을 삭제한 뒤 삭제한 키-값 쌍을 튜플로 반환한다. 이 메서드는 파이썬 버전에 따라 동작이 달라지는데, 파이썬 3.6 이상에서는 마지막 키-값 쌍을 삭제하며 3.5 이하에서는 임의의 키-값 쌍을 삭제한다. 아래 코드는 3.6이상 기준이다.


~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.popitem()
('d', 40)
x
{'a': 10, 'b': 20, 'c': 30}

~~~

### 딕셔너리의 모든 키-값 쌍을 삭제하기
<br>
<br>

**clear()**는 딕셔너리의 모든 키-값 쌍을 삭제한다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.clear() #모두 삭제
x
{}

~~~

### 딕셔너리에서 키의 값을 가져오기
<br>
<br>

**get(키)**는 딕셔너리의 특정 키 값을 가져온다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.get('a') # 키 'a'의 값을 가져온다. 
10

~~~

**get(키, 기본값)**처럼 기본값을 지정하면 딕셔너리에 키가 있을 때는 해당 키의 값을 반환하지만 키가 없을때는 기본값을 반환한다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.get('z', 0) # x딕셔너리에 없는 키'z'와 기본값 0을 지정
0 # 기본값 반환.

~~~


### 딕셔너리에서 키-값 쌍을 모두 가져오기
<br>
<br>
딕셔너리는 기와 값을 가져오는 다양한 메서드를 제공한다.

- items: 키-값 쌍을 모두 가져옴
- keys: 키를 모두 가져옴
- values: 값을 모두 가져옴

**items()**는 딕셔너리의 키-값 쌍을 모두 가져온다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.items()
dict_items([('a', 10), ('b', 20), ('c', 30), ('d', 40)])

~~~

**keys()**는 키를 모두 가져옵니다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.keys()
dict_keys(['a', 'b', 'c', 'd']) # 모든 키


~~~

**values()**는 값을 모두 가져옵니다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.values()
dict_values([10, 20, 30, 40]) # 모든 값

~~~

### 리스트와 튜플로 딕셔너리 만들기
<br>
<br>
이번에는 리스트(튜플)로 딕셔너리를 만들어 보자.<br>
keys = ['a', 'b', 'c', 'd']처럼 키가 들어있는 리스트를 준비한다(튜플도 가능). 그리고 dict.fromkeys에 키가 들어있는 리스트를 넣으면 딕셔너리를 생성한다.<br>

**dict.fromkeys(키리스트)**는 키 리스트로 딕셔너리를 생성하며 값은 모두 None으로 저장한다.

~~~python

keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
x
{'a': None, 'b': None, 'c': None, 'd': None} # 키 리스트로 딕셔너리 생성후 값을 모두 None으로 저장.

~~~

**dict.fromkeys(키리스트, 값)**처럼 키 리스트와 값을 지정하면 해당 값이 키의 값으로 저장된다.

~~~python

keys = ['a', 'b', 'c', 'd']
x = dict.fromkeys(keys)
x
{'a': None, 'b': None, 'c': None, 'd': None}
y = dict.fromkeys(keys, 100) # 키리스트에 값 100을 지정
y
{'a': 100, 'b': 100, 'c': 100, 'd': 100}

~~~

### defaultdict 사용하기
<br>
<br>
딕셔너리(dict)는 없는 키에 접근했을 경우 에러가 발생한다.

~~~python

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
x['z']    # 키 'z'는 없음
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    x['z']
KeyError: 'z'

~~~

**defaultdict(기본값생성함수)**를 사용하면 없는 키에 접근하더라도 에러가 발생하지 않고 기본값을 반환한다. defaultdict는 collections 모듈에 들어있으며 기본값 생성 함수를 넣는다. 아래와 같이 기본 값에 int를 지정하게 되면 0이 나오는데 int()를 하고 호출하면 0이 나오기 때문이다.

~~~python

from collections import defaultdict
y = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = defaultdict(int)

int() #int()호출
0

y['z'] # 없는 키를 에 접근했지만 기본값을 int로 지정해놨다.
0

~~~

0이 아닌 다른 값을 기본 값으로 설정할 수도 있다.

~~~python

from collections import defaultdict
z = defaultdict(lambda: 'python')
z['a']
'python'
z[0]
'python'

~~~

---

## 2. 반복문으로 딕셔너리의 키-값 쌍을 모두 출력하기
<br>
<br>
딕셔너리와 for반복문을 사용해 간단하게 모든 키-값 쌍을 출력해 보자. for i in x 처럼 for 반복문에 딕셔너리를 지정한 뒤에 print로 변수 i를 출력해보면 값을 출력되지 않고 키만 출력된다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
     print(i, end=' ')

a b c d

~~~

키와 값을 모두 출력하려면 for in 뒤에 딕셔너리를 지정하고 items(키-값 쌍을 모두 가져옴)를 사용해야 한다.

~~~python

for 키, 값 in 딕셔너리.items():
     반복할 코드

~~~

다음은 for로 리스트 a의 모든 키와 값을 출력한다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(key, value)

    
a 10
b 20
c 30
d 40

~~~


### 딕셔너리의 키만 출력하기
<br>
<br>
for 반복문에서 keys로 키를 가져오면서 반복해보자.

- items: 키-값 쌍을 모두 가져옴
- keys: 키를 모두 가져옴
- values: 값을 모두 가져옴

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key in x.keys(): #딕셔너리 x에 있는 key를 모두 가져와 key에 대입한다.
    print(key, end = ' ')

    
a b c d 

~~~

### 딕셔너리의 값만 출력하기
<br>
<br>
for 반복문에서 values를 사용해 값만 가져오며 반복한다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for value in x.values():
    print(value, end = ' ')

    
10 20 30 40 

~~~

---

## 3.딕셔너리 표현식 사용하기
<br>
<br>
리스트와 마찬가지로 딕셔너리도 for 반복문과 if 조건문을 사용해 딕셔너리를 생성할 수 있다. 다음과 같이 딕셔너리 안에 키와 값, for 반복문을 지정하면 된다.

- {키: 값 for 키, 값 in 딕셔너리}
- dict({키: 값 for 키, 값 in 딕셔너리})

딕셔너리 표현식을 사용할 때는 for in 다음에 딕셔너리를 지정하고 items를 사용한다. 그리고 키, 값을 가져온뒤에는 키 : 값 형식으로 변수나 값을 배치하여 딕셔너리를 생성한다.

~~~python

keys = ['a', 'b', 'c', 'd']
x = {key : value for key, value in dict.fromkeys(keys).items()} # 키리스트로 딕셔너리를 생성하고 값은 모두 None으로 저장한 키와 값모두를 가져와 변수 key, value에 지정하고 그걸 다시 key : value 에 대입해 딕셔너리로 만든다.
x
{'a': None, 'b': None, 'c': None, 'd': None}

~~~

다음과 같이 keys로 킴만 가져온 뒤 특정 값을 넣거나, values로 값을 가져온뒤 값을 키로 사용할 수도 있다. 또는, 키와 값의 자리를 바꾸는 등 여러 가지로 응용할 수 있다.

~~~python

keys = ['a', 'b', 'c', 'd']
y = {key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()} # 키리스트로 딕셔너리를 생성하고 키만 가져온후 변수key에 대입후 key: 0 에 키를 대입해 딕셔너리로 만든다. 값을 0으로 지정했다.
y
{'a': 0, 'b': 0, 'c': 0, 'd': 0}


keys = ['a', 'b', 'c', 'd']
z = {value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()} # 딕셔너리의 값만 추출해 value에 대입후 value: 0를 값을 키로 만들고 값을 0으로 지정한다.
z
{10: 0, 20: 0, 30: 0, 40: 0}

keys = ['a', 'b', 'c', 'd']
t = {value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()} 
t
{10: 'a', 20: 'b', 30: 'c', 40: 'd'}

~~~


### 딕셔너리 표현식에서 if 조건문 사용하기
<br>
<br>
표현식이 복잡하고 dict.fromkeys함수만 사용한 결과와 큰차이점이 없어 보이지만 딕셔너리에서 특정값을 찾아 삭제할때 유용하다. 딕셔너리는 특정키를 삭제하는 pop 메서드만 제공할 뿐 특정 값을 삭제하는 메서드는 제공하지 않는다. for 반복문으로 반복하면서 del로 삭제하는 방식은 딕셔너리의 크기가 바뀌어 에러가 발생한다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
 
for key, value in x.items():
    if value == 20:    # 값이 20이면
        del x[key]     # 키-값 쌍 삭제
 
print(x)

#결과

Traceback (most recent call last):
  File "C:\project\dict_del_by_value_error.py", line 3, in <module>
    for key, value in x.items():
RuntimeError: dictionary changed size during iteration 

~~~

특정 값을 삭제하려면 딕셔너리 표현식에 if조건문을 사용해 삭제할 값을 제외해야한다. 표현식에 if value != 20과 같이 if 조건문을 지정하면 값이 20이 아닌 키-값 쌍으로 다시 딕셔너리를 만든다. 직접 키-값 쌍을 삭제하는 방식이 아니라 삭제할 키-값 쌍을 제외하고 남은 키-값 쌍으로 딕셔너리를 새로 만드는 것이다.

~~~python

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x = {key: value for key, value in x.items() if value != 20}
x
{'a': 10, 'c': 30, 'd': 40}

~~~

---

## 4.딕셔너리 안에서 딕셔너리 사용하기
<br>
<br>
이번에는 딕셔너리 안에서 딕셔너리를 사용하는 중첩 딕셔너리를 알아보자. 다음과 같이 딕셔너리는 값 부분에 다시 딕셔너리가 계속 들어갈 수 있다.

- 딕셔너리 = {키1: {키A: 값A}, 키2: {키B: 값B}}

아래는 지구형 행성의 반지름, 질량, 공전주기를 딕셔너리로 표현한 것이다.

~~~python

terrestrial_planet = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}
 
print(terrestrial_planet['Venus']['mean_radius'])    # 6051.8

~~~

딕셔너리 terrestrial_planet에 키 'Mercury', 'Venus', 'Earth', 'Mars'가 들어있고, 이 키들은 다시 값 부분에 딕셔너리를 가지고 있다. 즉, 중첩 딕셔너리는 계층형 데이터를 지정할 때 유용하다.
<br>
딕셔너리 안에 들어있는 딕셔너리에 접근하려면 딕셔너리 뒤에 []를 단계만큼 붙이고 키를 지정해주면 된다.

- 딕셔너리[키][키]
- 딕셔너리[키][키] = 값

딕셔너리 terrestrial_planet는 딕셔너리가 두 단계로 구성되어 있으므로 대괄호를 두 번 사용한다. 금성(Venus)의 반지름(mean radius)를 출력하려면 다음과 같이 먼저 'Venus'를 찾아가고 다시 'mean_radius'의 값을 가져오면 된다.

~~~python

print(terrestrial_planet['Venus']['mean_radius'])    # 6051.8

~~~

---

## 5.딕셔너리의 할당과 복사
<br>
<br>
리스트와 마찬가지로 딕셔너리도 할당과 복사는 큰차이점이 있다. 먼저 딕셔너리를 만든 뒤 변수에 할당한다. y = x와 같이 딕셔너리를 다른 변수에 할당하면 딕셔너리는 두 개가 될 것 같지만 실제로는 딕셔너리가 한개이다. x와 y를 is연산자로 비교하면 True가 나온다. 즉, 변수 이름만 다를 뿐 딕셔너리 x와 y는 같은 객체이다.

~~~python

x is y
True

~~~

x와 y는 같으므로 y['a']=99와 같이 키'a'의 값을 변경하면 딕셔너리 x와 y모두 반영된다.

~~~python

y['a'] = 99
x
{'a': 99, 'b': 0, 'c': 0, 'd': 0}
y
{'a': 99, 'b': 0, 'c': 0, 'd': 0}

~~~

딕셔너리 x와 y를 완전이 분리한 두개의 딕셔너리로 만드려면 copy메서드로 모든 키-값 쌍을 복사해야한다. 복사후 x와 y를 is 연산자로 비교해보면 False가 나온다. 즉, 두 딕셔너리는 이제 다른 객체이다. 그러나 복사한 키-값 쌍은 같음으로 ==로 비교하면 True가 나온다. 딕셔너리 x와 y는 별개 이므로 한쪽의 값을 변경해도 다른 딕셔너리에 영향을 미치지 않는다. 다음과 같이 딕셔너리 y에서 키 'a'의 값을 변경하면 딕셔너리 x는 그대로이고 딕셔너리 y만 바뀐다.

~~~python

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x.copy()

x is y
False
x == y
True

y['a'] = 99
x
{'a': 0, 'b': 0, 'c': 0, 'd': 0}
y
{'a': 99, 'b': 0, 'c': 0, 'd': 0}

~~~


### 중첩 딕셔너리의 할당과 복사 알아보기
<br>
<br>
딕셔너리 안에 딕셔너리가 들어있는 중첩 딕셔너리는 copy메서드를 사용할 경우 값을 복사하면 두 딕셔너리의 값이 모두 바뀌게된다.

~~~python

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy() # 중첩 딕셔너리를 copy메서드로 복사

y['a']['python'] = '2.7.15' # 딕셔너리 y의 a키의 값 python키 의 값 변경
x
{'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}
y
{'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}} 
# 두 딕셔너리 모두 값이 변경됨.

~~~

중첩 딕셔너리를 완전히 복사하려면 copy메서드 대신 deepcopy 함수를 사용해야한다. 이제 딕셔너리y의 값을 변경해도 딕셔너리 x에 영향을 미치지 않는다. copy.deepcopy 함수는 중첩된 딕셔너리에 들어있는 모든 딕셔너리를 복사하는 깊은 복사(deep copy)를 해준다.

~~~python

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
import copy             # copy 모듈을 가져옴
y = copy.deepcopy(x)    # copy.deepcopy 함수를 사용하여 깊은 복사
y['a']['python'] = '2.7.15'
x
{'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y
{'a': {'python': '2.7.15'}, 'b': {'python': '3.6'}}   '

~~~

---

## 예제
<br>
<br>
표준 입력으로 문자열 여러 개와 숫자 여러 개가 두 줄로 입력되고, 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성합니다. 다음 코드를 완성하여 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 30인 키-값 쌍을 삭제하도록 만드세요.


~~~python

keys = input().split()
values = map(int, input().split())
 
x = dict(zip(keys, values))

__________________________
__________________________

print(x)


#입력
alpha bravo charlie delta
10 20 30 40

#결과
{'alpha': 10, 'bravo': 20}

#입력
alpha bravo charlie delta echo foxtrot golf
30 40 50 60 70 80 90

#결과
{'bravo': 40, 'charlie': 50, 'echo': 70, 'foxtrot': 80, 'golf': 90}

~~~

답


~~~python

x = {key: value for key, value in x.items() if value != 30 and key != 'delta'}

~~~