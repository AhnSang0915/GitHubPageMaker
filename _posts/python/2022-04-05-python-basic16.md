---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 중첩루프
date: 2022-04-05 12:35 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 중첩루프
<br>
<br>
이번에는 지금까지 배운 for 반복문과 if 조건문을 사용하여 계단식으로 별(*)을 출력해보자.

~~~python

*
**
***
****
*****

~~~

---

## 1. 중첩 루프 사용하기
<br>
<br>
콘솔(터미널, 명령 프롬프트)은 2차원 평면이므로 별을 일정한 모양으로 출력하려면 반복문을 두 개 사용하는 것이 편리하다. i를 사용하는 바깥루프는 세로방향을 처리하고, j를 사용하는 안쪽 루프는 가로 방향을 처리한다.
<br>
<br>
첫번째 for문 i가 0일때 두번째 for문 j는 0부터 4까지의 j를 출력한다. 출력후 다음 print문에서 줄바꿈을 출력하게되고 다시 i = 1로 시작해 두번쨰 for문을 돈다.


~~~python

for i in range(5):          # 5번 반복. 바깥쪽 루프는 세로 방향
    for j in range(5):      # 5번 반복. 안쪽 루프는 가로 방향
        print('j:', j, sep='', end=' ')    # j값 출력. end에 ' '를 지정하여 줄바꿈 대신 한 칸 띄움
    print('i:', i, '\\n', sep='')    # i값 출력, 개행 문자 모양도 출력
                                     # 가로 방향으로 숫자를 모두 출력한 뒤 다음 줄로 넘어감
                                     # (print는 기본적으로 출력 후 다음 줄로 넘어감)

# 출력
j 0 j 1 j 2 j 3 j 4 I 0 //n
j 0 j 1 j 2 j 3 j 4 I 1 //n
j 0 j 1 j 2 j 3 j 4 I 2 //n
j 0 j 1 j 2 j 3 j 4 I 3 //n
j 0 j 1 j 2 j 3 j 4 I 4 //n

~~~
중첩 루프는 2차원 평면을 다룰 수 있다. 영상처리, 이미지 처리, 좌표계 처리 등에 주로 쓰인다.

---

## 2. 사각형으로 별 출력하기
<br>
<br>
중첩 반복문으로 5x5 사각형 별을 그려보자. 안쪽의 for문을 실행하면 가로방향으로 *이5개 출력된다. 5번 반복해 print(*)를 하는데 끝에 end=''를 사용해 줄바꿈을 하지 않기 때문이다. 바깥쪽의 for i in range(5):의 경우 안쪽의 for j in range(5):를 5번 반복한다. 마지막 print()는 기본적으로 end='\n' 상태이므로 아무것도 기입하지 않아도 \n은 출력되어 줄바꿈을 해주게 된다.

~~~python

for i in range(5) :
    for j in range(5):
        print('*', end='')
    print()

# 출력    
*****
*****
*****
*****
*****

~~~

### 사각형 모양 바꾸기
<br>
<br>
이제 for 반복문의 조건식을 수정하여 사각형의 모양을 바꿔보자.


~~~python

for i in range(3):            # 3번 반복. 세로 방향
    for j in range(7):        # 7번 반복. 가로 방향
        print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
               # (print는 출력 후 기본적으로 다음 줄로 넘어감)

#출력
*******
*******
*******

~~~


---


## 3. 계단식으로 별 출력하기
<br>
<br>
계단식으로 별을 출력해 보자. 계단식으로 출력하려면 출력하지 않는 부분이 있기 때문에 if문을 사용한다. j <= i로 i가 1일때 j는 1보다 작거나 같아야만 출력이된다.

~~~python

for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
    for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
        if j <= i:                # 세로 방향 변수 i만큼
            print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
               # (print는 출력 후 기본적으로 다음 줄로 넘어감)

#출력
*
**
***
****
*****
~~~

### 대각선으로 별 출력하기
<br>
<br>
별을 대각선으로 출력해 보자. i = 1일때 *출력 이후 else부분의 공백이 4개 들어가게 된다.

~~~python

for i in range(5):        # 0부터 4까지 5번 반복. 세로 방향
    for j in range(5):    # 0부터 4까지 5번 반복. 가로 방향
        if j == i:                # 세로 방향 변수와 같을 때
            print('*', end='')    # 별 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
        else:                     # 세로 방향 변수와 다를 때
            print(' ', end='')    # 공백 출력. end에 ''를 지정하여 줄바꿈을 하지 않음
    print()    # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
               # (print는 출력 후 기본적으로 다음 줄로 넘어감)

# 결과 
*
 *
  *
   *
    *
~~~


### 예제
<br>
<br>
표준 입력으로 삼각형의 높이가 입력됩니다. 입력된 높이만큼 산 모양으로 별을 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 이때 출력 결과는 예제와 정확히 일치해야 합니다. 모양이 같더라도 공백이나 빈 줄이 더 들어가면 틀린 것으로 처리됩니다.

~~~python

count = int(input())
for i in range(count): # 0~4
    for j in reversed(range(count)): #4~0
        if j > i:
            print(' ', end='')
        else :
            print('*', end='')
    print('*'*i)

~~~