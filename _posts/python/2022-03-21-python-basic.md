---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 기본 
date: 2022-03-21 18:27 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# Python 기본
<br>
<br>

---

## Python은 세미콜론(;)을 안붙여도 된다.
<br>
<br>

파이썬은 세미콜론이 없어도 된다. 세미콜론을 붙여도 문법적 오류가 발생하지 않는다. 하지만 필요없는 내용을 코드에 작성할 필요는 없을것 같다.
## Python의 주석
<br>
<br>
파이썬에서 사람만 알아볼 수 있도록 작성하는 부분을 주석(comment)라고 한다. 즉, 주석은 파이썬 인터프리터가 처리하지 않으므로 프로그램의 실행에는 영향을 주지 않는다. 아래는 파이썬의 주석처리 방법이다.
<br>
<br>
한줄 주석의 경우 주석의 내용 앞에 #를 붙여준다. 일반적으로 #뒤에 한칸을 띄어쓰기하고 사용한다.

~~~python

# print("파이썬 공부하자")

~~~

파이썬의 여러줄 주석은 '''이나 """을 앞뒤로 붙여주면 된다.

~~~python

'''
print("파이썬 공부하자")
print("파이썬 공부하자")
print("파이썬 공부하자")
'''

"""
print("파이썬 공부하자")
print("파이썬 공부하자")
print("파이썬 공부하자")
"""

~~~



## 들여쓰기
<br>
<br>

들여쓰기란 코드의 가독성을 높이기 위해 일정한 간격을 띄워서 작성하는 방법이다. 파이썬은 들여쓰기가 문법으로 되어있어 들여쓰기를 하지 않으면 문법 오류가 나오게 된다.


~~~python

if a == 10:
print('10입니다.')    # 들여쓰기 문법 에러

#IndentationError: expected an indented block

if a == 10:
   print('10입니다.')  

~~~

## 코드블록
<br>
<br>

특정한 동작을 위해 코드가 모여있는 상태를 코드블록 이라고 한다. 주의할 점은 같은 블록은 들여쓰기 칸수가 같아야고 공백과 tap을 같이 사용하면 안된다.


~~~python

if a == 10:
      print('10')
      print('입니다.')

~~~

![코드블록(코딩도장)](https://dojang.io/pluginfile.php/13388/mod_page/content/3/004002.png)