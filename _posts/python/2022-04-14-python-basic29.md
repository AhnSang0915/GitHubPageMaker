---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 함수에서 재귀호출 사용하기
date: 2022-04-14 19:50 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 함수에서 재귀호출 사용하기

<br>
<br>
함수 안에서 함수 자기자신을 호출하는 방식을 재귀호출(recursive call)이라고 한다. 재귀 호출은 일반적인 상황에서는 잘 사용하지 않지만 알고리즘을 구현할 때 매우 유용하다. 보통 알고리즘에 따라서 반복문으로 구현한 코드보다 재귀호출로 구현한 코드가 좀 더 직관적이고 이해하기 쉬운 경우가 많다.

---

## 1. 재귀호출 사용하기
<br>
<br>
먼저 간단한 재귀호출 함수를 만들어보자. 다음 내용을 IDLE의 소스 코드 편집 창에 입력한 뒤 실행해보자.
 
~~~python

def hello():
    print('Hello, world!')
    hello()
 
hello()

~~~

hello 함수 안에서 다시 hello 함수를 호출하고 있다. 소스 코드를 실행해보면 'Hello, world!' 문자열이 계속 출력되다가 에러가 발생한다. 왜냐하면 파이썬에서는 최대 재귀 깊이(maximum recursion depth)가 1,000으로 정해져 있어서 그렇다. 즉, hello 함수가 자기자신을 계속 호출하다가 최대 재귀 깊이를 초과하면 RecursionError가 발생한다.

~~~python

Hello, world!
Hello, world!
Hello, world!
...(생략)
Traceback (most recent call last):
  File "C:\project\recursive_function_error.py", line 5, in <module>
    hello()
  File "C:\project\recursive_function_error.py", line 3, in hello
    hello()
  File "C:\project\recursive_function_error.py", line 3, in hello
    hello()
  File "C:\project\recursive_function_error.py", line 3, in hello
    hello()
  [Previous line repeated 974 more times]
  File "C:\project\recursive_function_error.py", line 2, in hello
    print('Hello, world!')
RecursionError: maximum recursion depth exceeded while pickling an object 

~~~


### 재귀호출에 종료 조건 만들기
<br>
<br>
재귀호출을 사용하려면 반드시 다음과 같이 종료 조건을 만들어주어야 한다. 먼저 hello 함수의 반복 횟수를 계산하기 위해 매개변수 count를 지정다. 그리고 count가 0이면 hello 함수를 호출하지 않고 끝낸다. 만약 0이 아니면 'Hello, world!'를 출력하고, count의 값을 1씩 감소시킨 뒤 hello 함수를 호출할 때 넣어준다.

~~~python

def hello(count):
    if count == 0:    # 종료 조건을 만듦. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄
        return
    
    print('Hello, world!', count)
    
    count -= 1      # count를 1 감소시킨 뒤
    hello(count)    # 다시 hello에 넣음 처음 5를 넣었다고 하면 hello(4)가 되고 점차 줄어든다.
 
hello(5)    # hello 함수 호출

#결과

Hello, world! 5
Hello, world! 4
Hello, world! 3
Hello, world! 2
Hello, world! 1

~~~

---

## 2. 재귀호출로 팩토리얼 구하기
<br>
<br>
팩토리얼은 1부터 n까지 양의 정수를 차례대로 곱한 값이다. !(느낌표) 기호로 표기한다. 예를 들어 5!은 5 * 4 * 3 * 2 * 1이며 결과는 120이다. 재귀함수를 사용해 팩토리얼을 구현해 보자.

~~~python

def factorial(n):
    if n == 1:      # n이 1일 때
        return 1    # 1을 반환하고 재귀호출을 끝냄
    return n * factorial(n - 1)    # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함
 
print(factorial(5))

# 실행 결과
120

~~~

먼저 factorial 함수를 만들 때 매개변수 n을 지정해준다. 팩토리얼은 1부터 n까지의 곱을 구하는 문제인데 여기서는 n부터 역순으로 1씩 감소하면서 재귀호출을 하고 n이 1이 되었을때 재귀호출을 중단한다.

~~~python

def factorial(n):
    if n == 1:      # n이 1일 때
        return 1    # 1을 반환하고 재귀호출을 끝냄

~~~

factorial 함수의 핵심은 반환값 부분이다. 계산 결과가 즉시 구해지는 것이 아니라 재귀호출로 n - 1을 계속 전달하다가 n이 1일 때 비로소 1을 반환하면서 n과 곱하고 다시 결괏값을 반환한다. 그 뒤 n과 반환된 결괏값을 곱하여 다시 반환하는 과정을 반복한다.

~~~python

return n * factorial(n - 1)    # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함

~~~

factorial(5)를 호출해서 n이 1이 될 때까지 재귀호출하면 다음과 같은 모양이 된다. 왼쪽에서 오른쪽 순서이다.

| 5 * factorial | 5 * factorial | 5 * factorial | 5 * factorial | 5 * factorial         |
|---------------|---------------|---------------|---------------|-----------------------|
|               | 4 * factorial | 4 * factorial | 4 * factorial | 4 * factorial         |
|               |               | 3 * factorial | 3 * factorial | 3 * factorial         |
|               |               |               | 2 * factorial | 2 * factorial         |
|               |               |               |               | factorial(1) return 1 |

이제 if n == 1:을 만나서 factorial 함수가 1을 반환한다. 그 뒤 1과 2를 곱해서 2를 반환하고, 3과 2를 곱해서 6을 반환하고, 4와 6을 곱해서 24를 반환하고, 5와 24를 곱해서 120을 반환하게 된다.

| 5 * factorial         | 5 * factorial | 5 * factorial | 5 * factorial | 5 * factorial |
|-----------------------|---------------|---------------|---------------|---------------|
| 4 * factorial         | 4 * factorial | 4 * factorial | 4 * factorial |               |
| 3 * factorial         | 3 * factorial | 3 * factorial |               |               |
| 2 * factorial         | 2 * factorial |               |               |               |
| factorial(1) return 1 |               |               |               |               |


---

### 예제1
<br>
<br>
다음 소스 코드를 완성하여 문자열이 회문인지 판별하고 결과를 True, False로 출력되게 만드세요. 여기서는 재귀호출을 사용해야 합니다.

~~~python

def is_palindrome(word):
    _________________________                                
    ...
    _________________________                                
 
print(is_palindrome('hello'))
print(is_palindrome('level'))

# 실행결과

False
True

~~~


답

~~~python

    if len(word) < 2:      # 문자열의 길이가 2미만이면 True를 반환하고 재귀함수를 종료시킨다. 
        return True
    if word[0] != word[-1]: # 첫 문자와 마지막 문자가 다르면 False를 출력하고 아니면 다음 줄로 이동
        return False
    return is_palindrome(word[1:-1]) #문자열의 1번인덱스 부터 -2인덱스 까지 넣어서 다시 함수에 넣는다. (문자열 슬라이싱에서  1:-1이면 마지막 인덱스의 전까지 가져온다.)

~~~

### 예제2
<br>
<br>
표준 입력으로 정수 한 개가 입력됩니다(입력 값의 범위는 10~30). 다음 소스 코드를 완성하여 입력된 정수에 해당하는 피보나치 수가 출력되게 만드세요.

피보나치 수는 0과 1로 시작하며, 다음 번 피보나치 수는 바로 앞의 두 피보나치 수의 합입니다.

~~~python

# n

0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21...

# 결과

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946...

________________
________________
________________
________________
________________

n = int(input())
print(fib(n))

#예
10
#결과
55

#예
20
#결과
6765

~~~

답

~~~python

def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)

#또는 

def fib(n):
    if n < 3: # 피보나치 수열의 2번쨰 까지 값이 1로 첫번째 값은 0이지만 영향을 주지 않아 값은 그대로 나옴
        return 1
    return fib(n-1)+fib(n-2)

#재귀함수를 사용하지 않은 코드

# 0 1 1 2 3 5 8 13 21 34 55 89
# fib(1) = [1], fib(2) = [1, 1] fib(3) = [1, 1, 2]
def fib(num):
    result = []    
    first = 1
    second = 1
    if(num > 1):
        result.append(first)
        
    result.append(second)    
    for i in range(2, num):
        third = first + second
        result.append(third)
        first = second
        second = third   
    return result.pop()
    
print(fib(num))




~~~

피보나치 수열을 재귀함수로 해결하려면 결과와 정의를 잘 봐야한다. 재귀함수를 풀때는 역순으로 생각하는게 편하며 지문에서 말했듯이 '바로앞의 두 피보나치 수의 합이 다음 번 피보나치 수가 된다.'를 코드로 작성하면 fib(n) = fib(n-1)+fib(n-2) 이라는 것이다. 이 예제는 트리 형태를 띄고 있으며 10을 호출했을 경우를 풀어서 작성해보자. 각 함수 fib(n) 안에 다시 fib함수가 들어있는 형태이다.

- fib(10) = fib(9) + fib(8)  (34+21 = 55)
- fib(9) = fib(8) + fib(7)   (21+13 = 34)
- fib(8) = fib(7) + fib(6)   (13+8 = 21)
- fib(7) = fib(6) + fib(5)   (8+5 = 13)
- fib(6) = fib(5) + fib(4)   (5+3 = 8)
- fib(5) = fib(4) + fib(3)   (3+2 = 5)
- fib(4) = fib(3) + fib(2)   (2+1 = 3)
- fib(3) = fib(2) + fib(1)   (1+1 = 2)
- fib(2) = fib(1) + fib(0)   (1+0 = 1)
- fib(1) = 1

