---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 딕셔너리 사용하기
date: 2022-03-30 10:20 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# Python 딕셔너리 사용하기
<br>
<br>
파이썬은 연관된 값을 묶어 저장하는 용도로 딕셔너리라는 자료형을 제공한다. 게임 캐릭터의 능력치를 딕셔너리에 저장해봤다.

~~~python

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

~~~

이제 딕셔너리만 봐도 lux라는 캐릭터의 체력(health)은 490, 마나(mana)는 334, 사거리(melee)는 550, 방어력(armor)은 18.72라는 것을 쉽게 알 수 있다.

---

## 1. 딕셔너리 만들기
<br>
<br>
딕셔너리는 {}안에 키 : 값 의 형식으로 저장하며 각 키와 값은 ,(콤마)로 구분해 준다. 키를 먼저 지정하고 :(콜론)을 붙여서 값을 표현한다. 특히 키에는 값을 하나만 지정할 수 있으며 이런 특성을 따서 키 - 값 쌍(key-value pair)이라 부른다(키-값은 1:1 대응).

~~~python

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

~~~

### 키 이름이 중복되면?

<br>
<br>
딕셔너리의 키값이 중복되면 가장 뒤에있는 값만 사용한다. 중복된 키는 저장되지 않는다. 딕셔너리 lux를 만들 때 'health': 490이 있고 그 뒤에 'health': 800을 넣었다. lux['health']를 출력해보면 800이 나오는걸 알 수 있다.

~~~python

lux = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health']    # 키가 중복되면 가장 뒤에 있는 값만 사용함
800
lux    # 중복되는 키는 저장되지 않음
{'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}

~~~



### 딕셔너리 키의 자료형

<br>
<br>

딕셔너리의 키는 문자열뿐만 아니라 정수, 실수, 불 도 사용할 수 있으며 자료형을 섞어서 사용해도 된다. 그리고 값에는 리스트, 딕셔너리 등을 포함하여 모든 자료형을 사용할 수 있다. 단, 키에는 리스트와 딕셔너리를 사용할 수 없다.

~~~python

x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
x
{100: 'hundred', False: 0, 3.5: [3.5, 3.5]}

x = {100 : 20, 100 : {100: 800}}
x
{100: {100: 800}}

# 키에는 리스트와 딕셔너리를 사용할 수 없다.

x = {[10, 20]: 100}
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    x = {[10, 20]: 100}
TypeError: unhashable type: 'list'

x = \{\{'a': 10}: 100\}
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x = \{\{'a': 10\}: 100\}
TypeError: unhashable type: 'dict'

~~~


### 빈 딕셔너리 만들기

<br>
<br>
비어있는 딕셔너리를 만들때는 {}만 지정하거나 dict을 사용하면 된다. 보통 {}를 주로 사용한다.
<br>

- 딕셔너리 = {}
- 딕셔너리 = dict()

~~~python

x = {}
x
# {}
y = dict()
y
# {}

~~~

### dict로 딕셔너리 만들기
<br>
<br>
dict는 다음과 같이 키와 값을 연결하거나, 리스트, 튜플, 딕셔너리로 딕셔너리를 만들때 사용한다.
<br>

- 딕셔너리 = dict(키1=값1, 키2=값2)
- 딕셔너리 = dict(zip([키1, 키2], [값1, 값2]))
- 딕셔너리 = dict([(키1, 값1), (키2, 값2)])
- 딕셔너리 = dict({키1: 값1, 키2: 값2})
<br>
<br>
다음과 같이 dict에서 키=값 형식으로 딕셔너리를 만들 수 있다. 이때는 키에 ' '(작은따옴표)나 " "(큰따옴표)를 사용하지 않아야 한다. 키는 딕셔너리를 만들고 나면 문자열로 바뀐다.

~~~python

lux1 = dict(health=490, mana=334, melee=550, armor=18.72)    
# 키=값 형식으로 딕셔너리를 만듦
lux1
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

~~~

두 번째 방법은 dict에서 zip 함수를 이용하는 방법이다. 다음과 같이 키가 들어있는 리스트와 값이 들어있는 리스트를 차례대로 zip에 넣은 뒤 다시 dict에 넣어주면 된다. 물론 키와 값을 리스트가 아닌 튜플에 저장해서 zip에 넣어도 된다.

~~~python

lux2 = dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))     # zip 함수로
lux2      # 키 리스트와 값 리스트를 묶음
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

~~~

세 번째 방법은 리스트 안에 (키, 값) 형식의 튜플을 나열하는 방법이다.

~~~python

lux3 = dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
lux3    # (키, 값) 형식의 튜플로 딕셔너리를 만듦
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72} 

~~~

네 번째 방법은 dict 안에서 중괄호로 딕셔너리를 생성하는 방법이다.

~~~python

lux4 = dict({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})     # dict 안에서
lux4  # 중괄호로 딕셔너리를 만듦
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

~~~

---

## 2. 딕셔너리의 키에 접근하고 값 할당하기
<br>
<br>
딕셔너리의 키에 접근할 때는 딕셔너리 뒤에 [ ](대괄호)를 사용하며 [ ] 안에 키를 지정해주면 된다.

~~~python

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health']
490
lux['armor']
18.72

#딕셔너리에 키를 지정하지 않은상태는 해당 딕셔너리 전체를 뜻한다.
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux    # 딕셔너리에 키를 지정하지 않으면 딕셔너리 전체를 뜻함
{'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}

~~~

### 딕셔너리의 키에 값 할당하기
<br>
<br>
딕셔너리는 []로 키에 접근한 뒤 값을 할당할 수 있다.

~~~python

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['health'] = 2037
lux['mana'] = 1184
lux
{'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72}

~~~

딕셔너리에 없는 키에 값을 할당하면 해당 키와 값이 추가된다.

~~~python

lux['mana_regen'] = 3.28
lux
{'health': 2037, 'mana': 1184, 'melee': 550, 'armor': 18.72, 'mana_regen': 3.28}

~~~

딕셔너리에 없는 키값을 가져오려고 하면 에러가 발생한다.\

~~~python

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
lux['attack_speed']    # lux에는 'attack_speed' 키가 없음
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    lux['attack_speed']
KeyError: 'attack_speed'

~~~



### 딕셔너리에 키가 있는지 확인하기
<br>
<br>
딕셔너리 안에 키가 있는지 확인하려면 in연산자를 사용한다.
<br>

- 키 in 딕셔너리

딕셔너리에 특정 키가 있으면 True 없으면 Fasle가 나온다. 
~~~python

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
'health' in lux
True
'attack_speed' in lux
False

~~~

반대로 not in을 하면 특정 키가 없는지 확인한다. 없으면 True 있으면 False가 나온다.

~~~python

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
>>> 'attack_speed' not in lux
True
>>> 'health' not in lux
False

~~~

- 해시 : 딕셔너리는 해시(Hash) 기법을 이용해서 데이터를 저장한다. 보통 딕셔너리와 같은 키-값 형태의 자료형을 해시, 해시 맵, 해시테이블 등으로 부르기도 한다.



### 딕셔너리의 키 개수 구하기
<br>
<br>
딕셔너리를 사용하다 보면 딕셔너리의 키 개수를 구할 필요가 있다. 딕셔너리의 키와 값을 직접 타이핑 할 때는 키의 개수를 알기가 쉽다. 하지만 실무에서는 함수 등을 사용해서 딕셔너리를 생성하거나 키를 추가하기 때문에 키의 개수가 눈에 보이지 않는다. 따라서 다음과 같이 키의 개수는 len함수를 사용하여 구한다.
<br>

- len(딕셔너리)

len에 딕셔너리 변수를 넣어도 되고 딕셔너리를 그대로 넣어도 된다.

~~~python

lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
len(lux)
4
len({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72})
4

~~~

