---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 문자열 사용하기
date: 2022-03-28 20:20 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# Python 문자열 사용하기
<br>
<br>

---

## 1.문자열 사용하기
<br>
<br>
문자열은 영문 문자열뿐만 아니라 한글 문자열도 사용가능하다. 변수에 문자열을 담아보자.

~~~python

hello = '안녕하세요'

~~~

파이썬에선 문자열을 작은따옴표, 큰따옴표, 작은따옴표3개, 큰따옴표3개로 묶을 수 있다.

~~~python

hello = '안녕하세요'
hello = "안녕하세요"
hello = '''안녕하세요'''
hello = """안녕하세요"""

~~~


### 여러 줄로 된 문자열 사용하기

<br>
<br>

여러줄로 된 문자열을 표현하는 방법을 알아보자.


~~~python

hello = """안녕하세요
파이썬 입니다
작성하는 사람은
접니다."""

~~~

### 문자열 안에 작은따옴표나 큰따옴표 포함하기

<br>
<br>

문자열에 작은따옴표나 큰따옴표를 포함하고 싶다면 작은따옴표를 큰따옴표로 감싸주거나 큰따옴표를 작은따옴표로 묵어주면되고 작은따옴표에 작은따옴표를 넣거나 큰따옴표에 큰따옴표를 넣고싶다면 \를 사용하면 된다.

~~~python

single_quote = '''"안녕하세요."
'파이썬'입니다.'''

# "안녕하세요."
  '파이썬'입니다.
 
double_quote1 = """"Hello"
'Python'"""
 
#"Hello"
 'Python'

double_quote2 = """Hello, 'Python'""" 
# Hello, 'Python'

a = 'Python isn\'t difficult'
# "Python isn't difficult"


~~~

\n을 사용하면 여러개의 따옴표를 쓰지 않고도 여러 줄로된 문자열을 사용할 수 있다.

~~~python

print('Hello\nPython')
#결과
Hello
Python

~~~

