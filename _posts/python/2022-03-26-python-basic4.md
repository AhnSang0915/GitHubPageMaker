---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 출력 방법 알아보기
date: 2022-03-26 10:20 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# Python 출력 방법 알아보기
<br>
<br>

---

## 1.값을 여러 개 출력하기
<br>
<br>

print 하나로 여러개의 값을 출력하는 방법을 알아보자.
<br>
<br>
print에 변수나 값 여러개를 ,(콤마)로 구분하여 여러개를 넣을 수 있다.

~~~python

print(1, 2, 3)
# 1 2 3

print('Hello', 'python')
# Hello python

a=20
b=30
c=40
print(a,b,c)
# 20 30 40

~~~


### sep로 값 사이에 문자 넣기

<br>
<br>

그런데 값 사이에 공백이 아닌 다른 문자를 넣고 싶을 수도 있다. 이때는 다음과 같이 print의 sep에 문자 또는 문자열을 지정해주면 된다.


~~~python

print(1, 2, 3, sep=', ')    # sep에 콤마와 공백을 지정
# 1, 2, 3
print(4, 5, 6, sep=',')    # sep에 콤마만 지정
# 4,5,6
print('Hello', 'Python', sep='')    # sep에 빈 문자열을 지정
# HelloPython
print(1920, 1080, sep='x')    # sep에 x를 지정
# 1920x1080

~~~


---

## 2. 줄바꿈 활용하기
<br>
<br>
출력되는 값을 줄바꿈 해 출력하는 방법을 알아보자. print의 sep에 개행 문자(\n)라는 특별한 문자를 지정하면 값을 한 줄에 하나씩 출력할 수 있다.

~~~python

print(1, 2, 3, sep='\n')
1
2
3

~~~

print에서도 여러줄로 출력이 가능하다.다음과 같이 문자열 안에 \n를 넣으면 1 2 3은 세 줄로 출력이 된다.

~~~python

print('1\n2\n3')
1
2
3

~~~

### 제어 문자
<br>
<br>
제어 문자는 화면에 출력되지 않지만 출력 결과를 제어한다고해서 제어 문자라고 부른다. 제어 문자는 \로 시작하는 이스케이프 시퀀스 이다.

- \n: 다음 줄로 이동하며 개행이라고도 부릅니다.
- \t: 탭 문자, 키보드의 Tab 키와 같으며 여러 칸을 띄웁니다.
- \\\: \ 문자 자체를 출력할 때는 \를 두 번 써야 합니다.

### end 사용하기
<br>
<br>
print는 기본적으로 출력하는 값 끝에 \n을 붙인다. 그래서 print를 여러 번 사용하면 값이 여러 줄에 출력된다. 

~~~python

print(1)
print(2)
print(3)
# 결과
1
2
3

~~~

print를 여러 번 사용해서 print(1, 2, 3)처럼 한 줄에 여러 개의 값을 출력할 수 있다. 이때는 print의 end에 빈 문자열을 지정해주면 된다.

~~~python

print(1, end='')    # end에 빈 문자열을 지정하면 다음 번 출력이 바로 뒤에 오게 됨
print(2, end='')
print(3)
#결과
123

~~~

즉, end는 현재 print가 끝난 뒤 그 다음에 오는 print 함수에 영향을 준다. 만약 1 2 3 사이를 띄워주고 싶다면 end에 공백 한 칸을 지정하면 된다.


~~~python

print(1, end=' ')    # end에 공백 한 칸 지정
print(2, end=' ')
print(3)
# 결과
1 2 3

~~~
