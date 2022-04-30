---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python break, continue로 반복문 제어하기
date: 2022-04-05 08:35 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# break, continue로 반복문 제어하기
<br>
<br>
break와 continue를 사용해 반복문을 제어하는 방법을 알아보자. break는 for와 while의 문법에서 제어흐름을 벗어나기 위해 사용한다. 즉, 루프를 중단한다. continue는 제어흐름을 유지한 상태에서 코드의 실행만 건너뛴다.

- break: 제어흐름 중단
- continue: 제어흐름 유지, 코드 실행만 건너뜀

---

## 1. break로 반복문 끝내기
<br>
<br>
break를 사용해 for와 while 에서 반복을 끝내는 방법을 알아보자.

<br>
<br>

### while에서 break로 반복문 끝내기

<br>
<br>
while 무한 루프에서 숫자를 증가시키다 변수 i가 100일 때 반복문을 끝내도록 만들었다. i값을 출력하고 증가시키므로 99까지 출력하고 반복을 멈추게 된다.

~~~python

i = 0
while True:    # 무한 루프
    print(i)
    i += 1          # i를 1씩 증가시킴
    if i == 100:    # i가 100일 때
        break       # 반복문을 끝냄. while의 제어흐름을 벗어남

#결과

0
1
2
... (생략)
97
98
99

~~~



### for에서 break로 반복문 끝내기
<br>
<br>
for에 range(10000)을 지정했다. 0부터 9999까지 반복하는데 i 가 100일때 break를 실행 함으로 0부터 100까지만 출력하고 반복문을 끝낸다. 100일때 100을 출력하고 반복을 멈추게 된다.

~~~python

for i in range(10000):    # 0부터 9999까지 반복
    print(i)
    if i == 100:    # i가 100일 때
        break       # 반복문을 끝냄. for의 제어흐름을 벗어남
#출력
0
1
2
... (생략)
98
99
100

~~~


---

## 2. continue로 코드 실행 건너뛰기
<br>
<br>
continue를 사용해 일부 코드를 실행하지 않고 건너 뛰어 보자.
<br>
<br>


### for에서 continue로 코드 실행 건너뛰기
<br>
<br>
for반복문에 range(100)를 사용해 0부터 99까지 반복한다. 그리고 if를 사용해 i가 짝수이면 continue를 실행한다. 마지막으로 print i의 값을 출력하고 99 까지 출력후 종료된다.


~~~python

for i in range(100):       # 0부터 99까지 증가하면서 100번 반복
    if i % 2 == 0:         # i를 2로 나누었을 때 나머지가 0면 짝수
        continue           # 아래 코드를 실행하지 않고 건너뜀
    print(i)

# 결과
1
3
5
... (생략)
95
97
99

~~~

### while 반복문에서 continue로 코드 실행 건너뛰기
<br>
<br>
while i < 100 : 으로 0부터 99까지 반복한다. i값을 1씩증가시킨뒤 if를 사용해 i가 짝수이면 continue를 실행한다. i의 초기값은 0이고 i +=1로 1로증가시킨 값부터 시작한다. 

~~~python

i = 0
while i < 100:        # i가 100보다 작을 때 반복. 0부터 99까지 증가하면서 100번 반복
    i += 1            # i를 1씩 증가시킴
    if i % 2 == 0:    # i를 2로 나누었을 때 나머지가 0이면 짝수
        continue      # 아래 코드를 실행하지 않고 건너뜀
    print(i)

~~~

만약 무한루프에서 continue를 사용하면 홀수만 계속 출려될 뿐 반복문은 끝나지 않는다.

### 반복문과 pass
<br>
<br>
for, while의 반복할 코드에서 아무 일도 하지 않지만, 반복문의 형태를 유지하고 싶다면 pass를 사용하면 된다.

~~~python

for i in range(10):    # 10번 반복
    pass               # 아무 일도 하지 않음

while True:    # 무한 루프
    pass       # 아무 일도 하지 않음

~~~

---


## 3. 입력한 횟수대로 반복하기
<br>
<br>
count에 input으로 입력을 받아 count변수에 저장하고 i에 0을 항당해 while True를 지정한 무한 루프로 만든다. 반복문 안에서는 i의 값을 출력하고, 변화식 에서는 i를 1씩증가시킨다. i의 값이 count의 값과 같으면 break를 실행한다.

~~~python

count = int(input('반복할 횟수를 입력하세요: '))
 
i = 0
while True:    # 무한 루프
    print(i)
    i += 1
    if i == count:    # i가 입력받은 값과 같을 때
        break         # 반복문을 끝냄

#출력
반복할 횟수를 입력하세요: 3 (입력)
0
1
2

~~~

### 입력한 숫자까지 홀수 출력하기
<br>
<br>
input으로 입력 값을 받아서 count 변수에 저장했다. 그리고 for의 range에 count + 1을 지정하여 count에 들어있는 값만큼 반복하도록 만들었다. 왜냐하면 range(count)는 0부터 시작하므로 count의 값은 반복에 포함되지 않기 때문이다.반복문 안에서는 if를 사용하여 i가 짝수이면 continue를 실행한다. 그다음에 print를 사용하여 i의 값을 출력한다.여기서는 9를 입력했으므로 0부터 9까지 반복하면서 i가 짝수이면 print를 실행하지 않고 건너뛰며 i가 홀수이면 print를 사용하여 숫자를 출력한다. 따라서 1 3 5 7 9가 출력된다.


~~~python

count = int(input('반복할 횟수를 입력하세요: '))
 
for i in range(count + 1):       # 0부터 증가하면서 count까지 반복(count + 1)
    if i % 2 == 0:               # i를 2로 나누었을 때 나머지가 0이면 짝수
        continue                 # 아래 코드를 실행하지 않고 건너뜀
    print(i)


# 결과 
반복할 횟수를 입력하세요: 9 (입력)
1
3
5
7
9
~~~


