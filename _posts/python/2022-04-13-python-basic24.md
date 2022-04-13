---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 세트 사용하기
date: 2022-04-13 11:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 세트 사용하기

<br>
<br>
파이썬은 집합을 표현하는 세트(set)라는 자료형을 제공한다. 집합을 영어로 하면 세트인데 수학에서 배우는 집합과 같다. 따라서 세트는 합집합, 교집합, 차집합 등의 연산이 가능하다.

---

## 1. 세트 만들기
<br>
<br>
세트는 {} 안에 값을 저장하며 각 값은 ,(콤마)로 구분한다. 세트는 요소의 순서가 정해져 있지 않다. 따라서 세트를 출력해보면 매번 요소의 순서가 다르게 나온다.

- 세트 = {값1, 값2, 값3}
~~~python

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
fruits
{'pineapple', 'orange', 'grape', 'strawberry', 'cherry'}

~~~

또한, 세트에 들어가는 요소는 중복될 수 없다. 다음과 같이 세트에 'orange'를 두개 넣어도 하나의 값만 들어간다.

~~~python

fruits = {'orange', 'orange', 'cherry'}
fruits
{'cherry', 'orange'}

~~~

세트는 리스트, 튜플, 딕셔너리와 달리 [](대괄호)로 특정 요소만 출력할 수 없다.

~~~python

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits[0])
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(fruits[0])
TypeError: 'set' object does not support indexing
fruits['strawberry']
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    fruits['strawberry']
TypeError: 'set' object is not subscriptable

~~~

###  세트에 특정 값이 있는지 확인하기
<br>
<br>
세트에 특정 값이 있는지 확인하려면 in연산자를 사용해야 한다.

- 값 in 세트

세트에 특정값이 있으면 True 없으면 Flase가 나온다. 세트 fruits에 orange가 있으므로 True peach가 없으므로 False가 나왔다.

~~~python

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
'orange' in fruits
True
'peach' in fruits
False

~~~

반대로 in앞에 not을 붙이면 특정 값이 없는지 확인한다.

~~~python

'peach' not in fruits
True
'orange' not in fruits
False

~~~

### set를 사용하여 세트 만들기
<br>
<br>
이번에는 set를 사용하여 세트를 만들어 보자.

**set(반복가능한객체)**와 같이 반복가능한 객체를 넣어 세트를 만든다. set('apple')과 같이 영문 문자열을 세트로 만들면 'apple'에서 유일한 문자인 a p l e만 세트로 만든다. 중복된 문자는 포함하지 않는다.


~~~python

a = set('apple')    # 유일한 문자만 세트로 만듦
a
{'e', 'l', 'a', 'p'}

~~~

set(range(5))와 같이 숫자를 만들어내는 range를 사용하면 0부터 4까지 숫자를 가진 세트를 만들 수 있다.

~~~python

b = set(range(5))
b
{0, 1, 2, 3, 4}

~~~

비어있는 세트는 c = set()과 같이 set에 아무것도 지정하지 않으면 된다.

~~~python

c = set()
c
set()

~~~

단 세트가 {}를 사용한다고 해서 c = {}와 같이 만들면 빈 딕셔너리가 만들어 짐으로 주의해야한다. 다음과 같이 type을 사용하면 자료형의 구조를 알 수 있다.

- type(객체)

~~~python

c = {}
type(c)
<class 'dict'>
c = set()
type(c)
<class 'set'>

~~~

### 한글 문자열을 세트로 만들기
<br>
<br>
set을 사용하여 한글 문자열을 세트로 만들면 다음과 같이 음절 단위로 세트가 만들어진다.

~~~python

set('안녕하세요')
{'녕', '요', '안', '세', '하'}

~~~

### 세트 안에 세트 넣기
<br>
<br>
세트는 리스트, 튜플, 딕셔너리와 달리 세트안에 세트를 넣을 수 없다.

~~~python

a = {% raw %}{{1, 2}, {3, 4}}{% endraw %} 
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a = {% raw %}{{1, 2}, {3, 4}}{% endraw %} 
TypeError: unhashable type: 'set'

~~~

### 세트 안에 세트 넣기
<br>
<br>
파이썬은 내용을 변경할 수 없는 세트도 제공한다.

**프로즌세트 = frozenset(반복가능한객체)**

frozenset(반복가능한객체)로 말그대로 얼어있는 세트를 만들 수 있다. 

~~~python

a = frozenset(range(10))
a
frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

~~~

frozenset는 뒤에서 설명할 집합 연산과 메서드에서 요소를 추가하거나 삭제하는 연산, 메서드는 사용할 수 없다. 다음과 같이 frozenset의 요소를 변경하려고 하면 에러가 발생한다.

~~~python

a = frozenset(range(10))
a |= 10
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a |= 10
TypeError: unsupported operand type(s) for |=: 'frozenset' and 'int'
a.update({10})
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    a.update({10})
AttributeError: 'frozenset' object has no attribute 'update'

~~~

frozenset는 세트 안에 세트를 넣고 싶을 때만 사용한다. 다음과 같이 frozenset는 중첩해서 넣을 수 있다. 단 frozenset만 넣을 수 있고, 일반 set는 넣을 수 없다.

~~~python

frozenset({frozenset({1, 2}), frozenset({3, 4})})
frozenset({frozenset({1, 2}), frozenset({3, 4})})

~~~

---

## 2. 집합 연산 사용하기
<br>
<br>
세트에서 집합 연산과 이에 대응하는 메서드를 사용해보자. 집합 연산은 파이썬의 산술 연산자와 논리 연산자를 활용한다.

**|**연산자는 합집합(union)을 구하며 OR연산자 |를 사용한다. set.union메서드와 작동이 같다. 다음은 세트 {1, 2, 3, 4}와 {3, 4, 5, 6}을 모두 포함하므로 {1, 2, 3, 4, 5, 6}이 나옵니다.

- 세트1 | 세트2
- set.union(세트1, 세트2)

~~~python

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a | b
{1, 2, 3, 4, 5, 6}
set.union(a, b)
{1, 2, 3, 4, 5, 6}

~~~

**&**연산자는 교집합(intersection)을 구하며 AND연산자 &를 사용한다. set.intersection메서드와 동작이 같다. 다음은 세트 {1, 2, 3, 4}와 {3, 4, 5, 6} 중에서 겹치는 부분을 구하므로 {3, 4}가 나온다.

- 세트1 & 세트2
- set.intersection(세트1, 세트2)

~~~python

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a & b
{3, 4}
set.intersection(a, b)
{3, 4}

~~~

**-**연산자는 차집합(difference)을 구하며 뺼셈 연산자 -를 사용한다. set.difference메서드와 동작이 같다. 다음은 {1, 2, 3, 4}에서 {3, 4, 5, 6}과 겹치는 3과 4를 뺐으므로 {1, 2}가 나온다.

~~~python

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a - b
{1, 2}
set.difference(a, b)
{1, 2}

~~~

**^**연산자는 대칭차집합(symmetric difference)을 구하며 XOR 연산자 ^를 사용한다. set.symmetric_difference 메서드와 동작이 같다. 대칭 차집합은 XOR연산자의 특성을 그대로 따르는데 XOR은 서로 다르면 참이다. 따라서 집합에서 두 집합 중 겹치지 않는 요소만 포함한다. 다음은 세트  {1, 2, 3, 4}와 {3, 4, 5, 6} 중에서 같은 값 3과 4를 제외한 다른 모든 요소를 구하므로 {1, 2, 5, 6}이 나온다.

- 세트1 ^ 세트2
- set.symmetric_difference(세트1, 세트2)

~~~python

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
a ^ b
{1, 2, 5, 6}
set.symmetric_difference(a, b)
{1, 2, 5, 6}

~~~

### 집합 연산 후 할당 연산자 사용하기
<br>
<br>
세트 자료형에 집합 연산 후 할당 연산자와 이에 대응하는 메서드를 사용해보자. 세트 자료형에 |, &, -, ^ 연산자와 할당 연산자 =을 함꼐 사용하면 집합 연산의 결과를 변수에 다시 저장한다.

**|=**은 현재 세트에 다른 세트를 더하며 update 메서드와 같다. 다음은 세트 {1, 2, 3, 4}에 {5}를 더하므로 {1, 2, 3, 4, 5}가 나온다.

- 세트1 |= 세트2
- 세트1.update(세트2)

~~~python

a = {1, 2, 3, 4}
a |= {5}
a
{1, 2, 3, 4, 5}
a = {1, 2, 3, 4}
a.update({5})
a
{1, 2, 3, 4, 5}

~~~

**&=**는 현재 세트와 다른 세트 중에서 겹치는 요소만 현재 세트에 저장한다. intersection_update 메서드와 같다. 다음은 세트 {1, 2, 3, 4}와 {0, 1, 2, 3, 4} 중에서 겹치는 요소만 a에 저장하므로 {1, 2, 3, 4}가 나온다.

- 세트1 &= 세트2
- 세트1.intersection_update(세트2)

~~~python

a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4}
a
{1, 2, 3, 4}
a = {1, 2, 3, 4}
a.intersection_update({0, 1, 2, 3, 4})
a
{1, 2, 3, 4}

~~~

**-=**는 현재 세트에서 다른 세트를 빼며 difference_update 메서드와 같다. 다음은 세트 {1, 2, 3, 4}에서 {3}을 빼므로 {1, 2, 4}가 나온다.

- 세트1 -= 세트2
- 세트1.difference_update(세트2)

~~~python

a = {1, 2, 3, 4}
a -= {3}
a
{1, 2, 4}
a = {1, 2, 3, 4}
a.difference_update({3})
a
{1, 2, 4}

~~~

**^=**는 현재 세트와 다른 세트중에서 겹치지 않는 요소만 현재 세트에 저장한다.symmetric_difference_update 메서드와 같다. 다음은 세트 {1, 2, 3, 4}와 {3, 4, 5, 6} 중에서 겹치지 않는 요소만 a에 저장하므로 {1, 3}이 나온다.

- 세트1 ^= 세트2
- 세트1.symmetric_difference_update(세트2)

~~~python

a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
a
{1, 2, 5, 6}
a = {1, 2, 3, 4}
a.symmetric_difference_update({3, 4, 5, 6})
a
{1, 2, 5, 6}

~~~

### 부분 집합과 상위집합 확인하기
<br>
<br>
세트는 부분집합, 진부분집합, 상위집합, 진상위집합과 같이 속하는 관계를 표현할 수도 있다. 현재 세트가 다른 세트의 (진)부분 집합 또는 (진)상위집합인지 확인할 때는 세트 자료형에 부등호와 등호를 사용한다.

**<=**는 현재 세트가 다른 세트의 부분집합(subset)인지 확인하며 issubset메서드와 같다. 다음은 세트 {1, 2, 3, 4}가 {1, 2, 3, 4}의 부분집합이므로 참이다.(등호가있어 두 세트가 같을 때도 참이다.)

- 현재세트 <= 다른세트
- 현재세트.issubset(다른세트)

~~~python

a = {1, 2, 3, 4}
a <= {1, 2, 3, 4}
True
a.issubset({1, 2, 3, 4, 5})
True

~~~

**>=**는 현재 세트가 다른 세트의 상위집합(superset)인지 확인하며 issuperset 메서드와 같다. 다음은 세트 {1, 2, 3, 4}가 {1, 2, 3, 4}의 상위집합이므로 참이다(등호가 있으므로 두 세트가 같을 때도 참이다).

- 현재세트 >= 다른세트
- 현재세트.issuperset(다른세트)

~~~python

a = {1, 2, 3, 4}
a >= {1, 2, 3, 4}
True
a.issuperset({1, 2, 3, 4})
True

~~~

**<**는 현재 세트가 다른 세트의 진부분집합(proper subset)인지 확인하며 메서드는 없다. 다음은 세트 {1, 2, 3, 4}가 {1, 2, 3, 4, 5}의 진부분집합이므로 참이다. 즉, 부분집합이지만 같지는 않을 때 참이다.

- 현재세트 < 다른세트


~~~python

a = {1, 2, 3, 4}
a < {1, 2, 3, 4, 5}
True

~~~

**>**는 현재 세트가 다른 세트의 진상위집합(proper superset)인지 확인하며 메서드는 없다. 다음은 세트 {1, 2, 3, 4}가 {1, 2, 3}의 진상위집합이므로 참이다. 즉, 상위집합이지만 같지는 않을 때 참이다.

- 현재세트 > 다른세트


~~~python

a = {1, 2, 3, 4}
a > {1, 2, 3}
True

~~~

[집합]!(https://user-images.githubusercontent.com/77658029/124087151-b6ad0100-da8c-11eb-9e33-0ae7406ed92f.png)

### 세트가 같은지 다른지 확인하기
<br>
<br>
세트는 == 연산자를 사용하여 서로 같은지 확인할 수 있다. 세트는 요소의 순서가 정해져 있지 않으므로 ==로 비교했을 때 각 요소만 같으면 참이다.

~~~python

a = {1, 2, 3, 4}
a == {1, 2, 3, 4}
True
a == {4, 2, 1, 3}
True

~~~

!=연산자는 세트가 다른지 확인한다.

~~~python

a = {1, 2, 3, 4}
a != {1, 2, 3}
True

~~~

### 세트가 같은지 다른지 확인하기
<br>
<br>
disjoint는 현재 세트가 다른 세트와 겹치지 않는지 확인한다. 겹치는 요소가 없으면 True, 있으면 False이다.

- 현재세트.isdisjoint(다른세트)

~~~python

a = {1, 2, 3, 4}
a.isdisjoint({5, 6, 7, 8})       # 겹치는 요소가 없음
True
a.isdisjoint({3, 4, 5, 6})    # a와 3, 4가 겹침
False

~~~

---

## 3.세트 조작하기
<br>
<br>
세트를 조작하는 메서드와 세트의 길이(요소 개수)를 구하는 방법을 알아보자.
<br>
<br>

### 세트에 요소 추가하기
<br>
<br>

**add(요소)**는 세트에 요소를 추가한다.

~~~python

a = {1, 2, 3, 4}
a.add(5)
a
{1, 2, 3, 4, 5}

~~~

### 세트에서 특정 요소를 삭제하기
<br>
<br>

**remove(요소)**는 세트에서 특정 요소를 삭제하고 요소가 없으면 에러를 발생시킨다.

~~~python

a = {1, 2, 3, 4}
a.remove(3)
a
{1, 2, 4, 5}

~~~

**discard(요소)**는 세트에서 특정 요소를 삭제하고 요소가 없으면 그냥 넘어간다. 다음은 세트 a에 2가 있으므로 2를 삭제하고, 3은 없으므로 그냥 넘어간다.

~~~python

a = {1, 2, 4, 5}
a.discard(2)
a
{1, 4, 5}
a.discard(3)
a
{1, 4, 5}

~~~

### 세트에서 임의의 요소 삭제하기
<br>
<br>

**pop()**은 세트에서 임의의 요소를 삭제하고 해당 요소를 반환한다. 만약 요소가 없으면 에러를 발생시킨다.

~~~python

a = {1, 2, 3, 4}
a.pop()
1
a
{2, 3, 4}
~~~


### 세트의 모든 요소를 삭제하기
<br>
<br>

**clear()**는 세트에서 모든 요소를 삭제한다.

~~~python

a = {1, 2, 3, 4}
a.clear()
a
set()

~~~

### 세트의 모든 요소를 삭제하기
<br>
<br>

**len(세트)**는 세트의 요소 개수 길이를 구한다.

~~~python

a = {1, 2, 3, 4}
len(a)
4

~~~

---

## 4.세트의 할당과 복사
<br>
<br>
세트도 리스트, 튜플, 딕셔너리처럼 할당과 복사의 차이점이 있다. 먼저 세트를 만든 뒤 다른 변수에 할당한다. b = a와 같이 세트를 다른 변수에 할당하면 세트는 두 개가 될 것 같지만 실제로는 세트가 한 개이다.

~~~python

a = {1, 2, 3, 4}
b = a

~~~

a와 b를 is 연산자로 비교해보면 True가 나온다. 즉, 변수 이름만 다를 뿐 세트 a와 b는 같은 객체이다.

~~~python

a is b
True

~~~

a와 b는 같으므로 b에 요소를 추가하면 세트 a와 b에 모두 반영된다.

~~~python

b.add(5)
a
{1, 2, 3, 4, 5}
b
{1, 2, 3, 4, 5}

~~~

세트 a와 b를 완전히 두 개로 만들려면 copy메서드로 모든 요소를 복사해야 한다.

~~~python

a = {1, 2, 3, 4}
b = a.copy()

~~~

이제 a와 b를 is 연산자로 비교해보면 False가 나온다. 즉, 두 세트는 다른 객체다. 그러나 복사한 요소는 같으므로 ==로 비교하면 True가 나온다.

~~~python

a is b
False
a == b
True

~~~

세트 a와 b는 별개이므로 한쪽의 값을 변경해도 다른 세트에 영향을 미치지 않는다. 다음과 같이 세트 b에 요소를 추가하면 세트 a는 그대로이고 세트 b만 바뀐다.

~~~python

a = {1, 2, 3, 4}
b = a.copy()
b.add(5)
a
{1, 2, 3, 4}
b
{1, 2, 3, 4, 5}

~~~

---

## 5.반복문으로 세트의 요소를 모두 출력하기
<br>
<br>
이번에는 세트와 for반복문을 사용하여 요소를 출력해보자. 간단하게 for in 뒤에 세트만 지정하면 된다.

~~~python

for 변수 in 세트:
     반복할 코드

~~~

다음은 for로 세트 a의 요소를 출력한다. for i in a:는 세트 a에서 요소를 꺼내서 i에 저장하고, 꺼낼 때마다 코드를 반복한다. 따라서 print i를 출력하면 요소를 모두 출력할 수 있다. 단, 세트의 요소는 순서가 없으므로 출력할 때마다 순서가 달라진다(숫자로만 이루어진 세트는 순서대로 출력됨).

~~~python

a = {1, 2, 3, 4}
for i in a:
     print(i)

1
2
3
4

# in 다음 세트를 직접 지정해도 상관 없다.

for i in {1, 2, 3, 4}:
    print(i)

~~~

---

## 6.세트 표현식 사용하기
<br>
<br>
세트는 for 반복문과 if조건문을 사용하여 세트를 생성할 수 있다. 다음과 같이 세트 안에 식과 for반복문을 지정하면 된다.

- {식 for 변수 in 반복가능한객체}
- set(식 for 변수 in 반복가능한객체)

{}또는 set()안에 식, for, 변수, in, 반복가능한 객체를 지정하여 세트를 생성한다. 여기서는 반복가능한 객체로 문자열 'apple'을 지정했다.

~~~python

a = {i for i in 'apple'}
a
{'l', 'p', 'e', 'a'}

~~~


### 세트 표현식에 if 조건문 사용하기
<br>
<br>
세트 표현식에서 if 조건문을 사용해 보자. 다음과 같이 if 조건문은 for반복문 뒤에 지정한다.

- {식 for 변수 in 세트 if 조건식}
- set(식 for 변수 in 세트 if 조건식)

{i for i in 'pineapple' if i not in 'apl'}은 문자열 'pineapple'에서 'a', 'p', 'l'을 제외한 문자들로 세트를 생성한다. 즉, 다음과 같이 for 반복문 뒤에 if 조건문을 지정하면 if 조건문에서 특정 요소를 제외한 뒤 세트를 생성한다.

~~~python

a = {i for i in 'pineapple' if i not in 'apl'}
a
{'e', 'i', 'n'}

~~~

if i not in 'apl'은 {i for i in 'pineapple' if i != 'a' and i != 'p' and i != 'l'}과 같이 문자를 하나씩 비교하고 and로 연결하는 if 조건문과 같다.

## 예제
<br>
<br>

표준 입력으로 양의 정수 두 개가 입력됩니다. 다음 소스 코드를 완성하여 두 숫자의 공약수를 세트 형태로 구하도록 만드세요. 단, 최종 결과는 공약수의 합으로 판단합니다.

~~~python

________________
________________
________________
 
divisor = a & b
 
result = 0
if type(divisor) == set:
    result = sum(divisor)
 
print(result)

#입력
10 20

#결과
18

#입력
100 200

#결과
217

~~~