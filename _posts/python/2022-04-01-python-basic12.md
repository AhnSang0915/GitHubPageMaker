---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python  elif를 사용하여 여러 방향으로 분기하기
date: 2022-04-01 10:20 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# Python elif를 사용하여 여러 방향으로 분기하기
<br>
<br>
elif는 조건식을 여러 개 지정하여 각 조건 마다 다른 코드를 실행할 수 있다.

~~~python

if 콜라 버튼을 눌렀다면:
    콜라를 내보냄
elif 사이다 버튼을 눌렀다면:
    사이다를 내보냄
elif 환타 버튼을 눌렀다면:
    환타를 내보냄:
else:
    제공하지 않는 메뉴

~~~

---

## 1. elif 사용하기
<br>
<br>
elif는 else인 상태에서 조건식을 지정할 때 사용하며 else if라는 뜻이다. 물론 if, else와 마찬가지로 조건식 끝에 :(콜론)을 붙여야 하고, elif 단독으로 사용할 수 없다.

~~~python

if 조건식:
     코드1
elif:
     코드2

~~~

~~~python

x = 20
if x == 10:
    print('10이다.')
elif x == 20:
    print('20이다.')
    
# 20이다.

~~~

### if, elif, else를 모두 사용하기

<br>
<br>
elif와 else는 단독으로 사용할 수 없으며 if, else 형태로 사용하거나, if, elif, else 형태로 사용한다. 이번에는 if, elif, else를 모두 사용해보자.

~~~python

if 조건식:
    코드1
elif 조건식:
    코드2
else:
    코드3  

~~~

아래 코드는 if, elif의 조건식이 모두 거짓일 때만 else의 코드가 실행된다. 여기서는 x가 30이라 if, elif의 조건식에 모두 만족하지 않는다. 따라서 마지막 else의 '10도 20도 아닙니다.'가 출력된다.

~~~python

x = 30
 
if x == 10:             # x가 10일 때
    print('10입니다.')
elif x == 20:           # x가 20일 때
    print('20입니다.')
else:                   # 앞의 조건식에 모두 만족하지 않을 때
    print('10도 20도 아닙니다.') 

# 10도 20도 아닙니다.

~~~


### 음료수 자판기 만들기

<br>
<br>

버튼 1번은 '콜라', 2번은 '사이다', 3번은 '환타'이고 각 버튼에 따라 음료수 이름을 출력한다고 하자(1, 2, 3이외의 숫자는 '제공하지 않는 메뉴' 출력).

~~~python

button = int(input())
 
if button == 1:
    print('콜라')
elif button == 2:
    print('사이다')
elif button == 3:
    print('환타')
else:
    print('제공하지 않는 메뉴')

# 1 (입력)
# 콜라

~~~

