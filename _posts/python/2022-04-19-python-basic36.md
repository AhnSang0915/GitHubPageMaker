---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 예외 처리 사용하기
date: 2022-04-19 17:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 예외 처리 사용하기

<br>
<br>
예외(exception)란 코드를 실행하는 중에 발생한 에러를 뜻한다. 다음과 같이 10을 어떤 값으로 나누는 함수 ten_div가 있을 때 인수에 따라 정상으로 동작하기도 하고 에러가 나기도 한다.

~~~python

def ten_div(x):
     return 10 / x

~~~

이 함수에 2를 넣으면 5.0이 나온다.

~~~python

def ten_div(x):
     return 10 / x

ten_div(2)
5.0

~~~

하지만 0을 넣으면 실행하는 중에 에러가 발생한다. 이런 상황을 예외라고 하는데 여기서는 어떤 숫자를 0으로 나누어서 ZeroDivisionError 예외가 발생했다.

~~~python

def ten_div(x):
     return 10 / x

ten_div(0)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    ten_div(0)
  File "<pyshell#119>", line 2, in ten_div
    return 10 / x
ZeroDivisionError: division by zero 

~~~

ZeroDivisionError뿐만 아니라 지금까지 만난 AttributeError, NameError, TypeError 등 다양한 에러들도 모두 예외다.

예외가 발생했을 때도 스크립트 실행을 중단하지 않고 계속 실행하게 해주는 예외 처리 방법에 대해 알아보자.

---

## 1. try except로 사용하기
<br>
<br>
예외 처리를 하려면 다음과 같이 try에 실행할 코드를 넣고 except에 예외가 발생했을 때 처리하는 코드를 넣는다

~~~python

try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드

~~~

이제 숫자를 0으로 나누었을 때 발생하는 예외를 처리해보자.

~~~python

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
    print(y)
except:    # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.')

~~~

소스 코드를 실행한 뒤 0을 입력하고 엔터를 누르면 eroDivisionError 예외가 발생한다. 여기서는 except에서 예외 처리를 하도록 만들었으므로 '예외가 발생했습니다.'가 출력된다.

~~~python

나눌 숫자를 입력하세요: 0 (입력)
예외가 발생했습니다.

~~~

특히 예외가 발생하면 해당 줄에서 코드 실행을 중단하고 바로 except로 가서 코드를 실행한다. 즉, try의 y = 10 / x 를 비롯하여 그 아래줄에 있는 print(y)도 실행되지 않는다.

다시 소스 코드를 실행한 뒤 2를 입력하면 예외가 발생하지 않고 계산 결과가 잘 출력된다. 이처럼 try의 코드가 에러 없이 잘 실행 되면 except의 코드는 실행되지 않고 그냥 넘어간다. 즉, try의 코드에서 에러가 발생했을 때만 except의 코드가 실행된다.

~~~python

나눌 숫자를 입력하세요: 2 (입력)
5.0

~~~

### 특정 예외만 처리하기
<br>
<br>
이번에는 except에 예외 이름을 지정해서 특정 예외가 발생했을 때만 처리 코드를 실행하도록 만들어보겠다.

~~~python

try:
    실행할 코드
except 예외이름:
    예외가 발생했을 때 처리하는 코드

~~~

다음과 같이 정수 두 개를 입력받아서 하나는 리스트의 인덱스로 사용하고, 하나는 나누는 값으로 사용한다. 그리고 except를 두 개 사용하고 각각 ZeroDivisionError와 IndexError를 지정한다.

~~~python

y = [10, 20, 30]
 
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
except IndexError:           # 범위를 벗어난 인덱스에 접근하여 에러가 발생했을 때 실행됨
    print('잘못된 인덱스입니다.')

~~~

소스 코드를 실행한 뒤 2와 0을 입력하고 엔터 키를 눌러 실행한다. 2 0을 입력하면 30 / 0이 되므로 숫자를 0으로 나누게 된다. 이때는 except ZeroDivisionError:의 처리 코드가 실행된다.

~~~python

인덱스와 나눌 숫자를 입력하세요: 2 0 (입력)
숫자를 0으로 나눌 수 없습니다.

~~~

다시 소스 코드를 실행한 뒤 3 5를 입력하고 엔터 키를 누른다. y = [10, 20, 30]은 요소가 3개 들어있는 리스트다. 따라서 인덱스에 3을 지정하면 범위를 벗어나게 된다. 이때는 except IndexError:의 처리 코드가 실행된다.

~~~python

인덱스와 나눌 숫자를 입력하세요: 3 5 (입력)
잘못된 인덱스입니다.

~~~

### 예외의 에러 메시지 받아오기
<br>
<br>
특히 except에서 as 뒤에 변수를 지정하면 발생한 예외의 에러 메시지를 받아올 수 있다.

~~~python

try:
    실행할 코드
except 예외 as 변수:
    예외가 발생했을 때 처리하는 코드

~~~

앞에서 만든 코드의 except에 as e를 넣는다. 보통 예외( exception)의 e를 따서 변수 이름을 e로 짓는다. 2 와0, 3 과5처럼 예외가 발생하는 숫자를 넣어보면 해당 예외에 해당하는 에러 메시지가 출력된다. 단, 예외가 여러 개 발생하더라도 먼저 발생한 예외의 처리 코드만 실행됩니다(또는, 예외 중에서 높은 계층의 예외부터 처리. 기반 클래스 > 파생 클래스 순).

~~~python

y = [10, 20, 30]
 
try:
    index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요: ').split())
    print(y[index] / x)
except ZeroDivisionError as e:                    # as 뒤에 변수를 지정하면 에러를 받아옴
    print('숫자를 0으로 나눌 수 없습니다.', e)    # e에 저장된 에러 메시지 출력
except IndexError as e:
    print('잘못된 인덱스입니다.', e)

#실행 결과
인덱스와 나눌 숫자를 입력하세요: 2 0 (입력)
숫자를 0으로 나눌 수 없습니다. division by zero
#실행 결과
인덱스와 나눌 숫자를 입력하세요: 3 5 (입력)
잘못된 인덱스입니다. list index out of range

~~~

참고로 모든 예외의 에러 메시지를 출력하고 싶다면 다음과 같이 except에 Exception을 지정하고 as 뒤에 변수를 넣으면 된다.

~~~python

except Exception as e:    # 모든 예외의 에러 메시지를 출력할 때는 Exception을 사용
    print('예외가 발생했습니다.', e)

~~~

이처럼 예외 처리는 에러가 발생하더라도 스크립트의 실행을 중단시키지 않고 계속 실행하고자 할 때 사용한다.

---

## 2.else와 finally 사용하기
<br>
<br>
이번에는 예외가 발생하지 않았을 때 코드를 실행하는 else를 사용해보자. 다음과 같이 else는 except바로 다음에 와야 하며 except를 생략할 수 없다.

~~~python

try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드

~~~

그럼 10을 입력된 숫자로 나누고 예외가 발생하지 않으면 계산 결과를 출력해보자.

~~~python

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)

~~~

소스 코드를 실행한 뒤 2를 입력하고 엔터 키를 눌러 실행하면 2를 입력했으므로 y = 10 / x에서 예외가 발생하지 않았다. 따라서 else의 코드가 실행되고 계산 결과가 출력된다.

~~~python

나눌 숫자를 입력하세요: 2 (입력)
5.0

~~~

물론 0을 입력해서 예외가 발생하면 except의 코드만 실행되고 else의 코드는 실행되지 않는다.

~~~python

나눌 숫자를 입력하세요: 0 (입력)
숫자를 0으로 나눌 수 없습니다.

~~~

### 예외와는 상관없이 항상 코드 실행하기
<br>
<br>
이번에는 예외 발생 여부와 상관없이 항상 코드를 실행하는 finally를 사용해보겠다. 특히 finally는 except와 else를 생략할 수 있다.

~~~python

try:
    실행할 코드
except:
    예외가 발생했을 때 처리하는 코드
else:
    예외가 발생하지 않았을 때 실행할 코드
finally:
    예외 발생 여부와 상관없이 항상 실행할 코드

~~~

다음은 try의 코드가 끝나면 항상 '코드 실행이 끝났습니다.'를 출력한다.

~~~python

try:
    x = int(input('나눌 숫자를 입력하세요: '))
    y = 10 / x
except ZeroDivisionError:    # 숫자를 0으로 나눠서 에러가 발생했을 때 실행됨
    print('숫자를 0으로 나눌 수 없습니다.')
else:                        # try의 코드에서 예외가 발생하지 않았을 때 실행됨
    print(y)
finally:                     # 예외 발생 여부와 상관없이 항상 실행됨
    print('코드 실행이 끝났습니다.')

~~~

소스 코드를 실행한 뒤 2를 입력하고 실행하면 예외가 발생하지 않았으므로 계산 결과가 출력되고, '코드 실행이 끝났습니다.'도 출력된다.

~~~python

나눌 숫자를 입력하세요: 2 (입력)
5.0
코드 실행이 끝났습니다.

~~~

다시 소스 코드를 실행한 뒤 0을 입력하고 실행하면 숫자를 0으로 나눠서 예외가 발생했지만 finally는 항상 실행되므로 '코드 실행이 끝났습니다.'가 출력된다.

~~~python

나눌 숫자를 입력하세요: 0 (입력)
숫자를 0으로 나눌 수 없습니다.
코드 실행이 끝났습니다.

~~~

---

## 3.예외 발생시키기
<br>
<br>
위에서 숫자를 0으로 나눴을때 에러, 리스트의 범위를 벗어난 인덱스에 접근했을 때 에러 등 파이썬에서 정해진 예외만 처리했다. 이번에는 직접 예외를 발생시켜 보자.

예외를 발생시킬 때는 raise에 예외를 지정하고 에러 메시지를 넣는다(에러 메시지는 생략 할 수 있음).

- raise 예외('에러메시지')

그럼 3의 배수를 입력받은 뒤 숫자가 3의 배수가 아니면 예외를 발생시켜보자.

~~~python

try:
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
    print(x)
except Exception as e:                             # 예외가 발생했을 때 실행됨
    print('예외가 발생했습니다.', e)

~~~

소스 코드를 실행하고 5를 입력한뒤 실행하면 5는 3의 배수가 아니므로 raise Exception('3의 배수가 아닙니다.')로 예외를 발생시켰다. 이때 Exception에 넣은 에러 메시지는 except Exception as e:의 e에 들어가게된다. 그리고 raise로 예외를 발생시키면 raise 아래에 있는 코드는 실행되지 않고 바로 except로 넘어간다. 따라서 try의 print(x)는 실행되지 않는다.

~~~python

3의 배수를 입력하세요: 5 (입력)
예외가 발생했습니다. 3의 배수가 아닙니다.

~~~

참고로 이 예제에서는 예외로 Exception을 사용했는데 RuntimeError, NotImplementedError 등 다른 예외를 사용해도 상관없다.

### raise의 처리 과정
<br>
<br>
raise의 처리 과정을 알아보자. 다음은 함수 안에서 raise를 사용하지만 함수 안에서는 try except가 없는 상환이다.

~~~python

def three_multiple():
    x = int(input('3의 배수를 입력하세요: '))
    if x % 3 != 0:                                 # x가 3의 배수가 아니면
        raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
    print(x)                                       # 현재 함수 안에는 except가 없으므로
                                                   # 예외를 상위 코드 블록으로 넘김
 
try:
    three_multiple()
except Exception as e:                             # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('예외가 발생했습니다.', e)

~~~

소스 코드를 실행한 뒤 5를 입력하고 실행하면 three_multiple 함수는 안에 try except가 없는 상태에서 raise로 예외를 발생시키게 되어 함수 바깥에 있는 except에서 예외가 처리가 된다. 즉, 예외가 발생하더라도 현재 코드 블록에서 처리해줄 except가 없다면 except가 나올 때까지 계속 상위 코드 블록으로 올라간다.

~~~python

3의 배수를 입력하세요: 5 (입력)
예외가 발생했습니다. 3의 배수가 아닙니다.

~~~

만약 함수 바깥에도 처리해줄 except가 없다면 코드 실행은 중지되고 에러가 표시된다. 다음은 파이썬 셸에서 직접 three_multiple 함수를 호출했으므로 except가 없는 상태다.\

~~~python

three_multiple()
3의 배수를 입력하세요: 5 (입력)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    three_multiple()
  File "C:\project\try_except_function_raise.py", line 4, in three_multiple
    raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
Exception: 3의 배수가 아닙니다.

~~~

### 현재 예외를 다시 발생시키기
<br>
<br>
try except에서 처리한 예외를 다시 발생시키는 방법이다. except 안에서 raise를 사용하면 현재 예외를 다시 발생시킨다(re-raise).

- raise
다음은 three_multiple 코드 블록의 예외를 다시 발생시킨 뒤 상위 코드 블록에서 예외를 처리한다.

~~~python

def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:                                 # x가 3의 배수가 아니면
            raise Exception('3의 배수가 아닙니다.')    # 예외를 발생시킴
        print(x)
    except Exception as e:                             # 함수 안에서 예외를 처리함
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise    # raise로 현재 예외를 다시 발생시켜서 상위 코드 블록으로 넘김
 
try:
    three_multiple()
except Exception as e:             1             # 하위 코드 블록에서 예외가 발생해도 실행됨
    print('스크립트 파일에서 예외가 발생했습니다.', e)

~~~

소스 코드를 실행한 뒤 5를 입력하고 실행하면 three_multiple 함수 안에서 발생한 예외를 함수 안의 except에서 한 번 처리하고, raise로 예외를 다시 발생시켜서 상위 코드 블록으로 넘겼다. 그다음에 함수 바깥의 except에서 예외를 처리했다. 이런 방식으로 같은 예외를 계속 처리해줄 수 있다.

~~~python

        if x % 3 != 0:
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    except Exception as e:
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise RuntimeError('three_multiple 함수에서 예외가 발생했습니다.')

~~~

참고로 raise만 사용하면 같은 예외를 상위 코드 블록으로 넘기지만 raise에 다른 예외를 지정하고 에러 메시지를 넣을 수도 있다.

- raise 예외('에러메시지')

~~~python

        if x % 3 != 0:
            raise Exception('3의 배수가 아닙니다.')
        print(x)
    except Exception as e:
        print('three_multiple 함수에서 예외가 발생했습니다.', e)
        raise RuntimeError('three_multiple 함수에서 예외가 발생했습니다.')

~~~

### assert로 예외 발생시키기
<br>
<br>
발생시키는 방법 중에는 assert를 사용하는 방법도 있다. assert는 지정된 조건식이 거짓일 때 AssertionError 예외를 발생시키며 조건식이 참이면 그냥 넘어간다. 보통 assert는 나와서는 안 되는 조건을 검사할 때 사용한다.

다음은 3의 배수가 아니면 예외 발생, 3의 배수이면 그냥 넘어가게 된다.

- assert 조건식
- assert 조건식, 에러메시지

~~~python

x = int(input('3의 배수를 입력하세요: '))
assert x % 3 == 0, '3의 배수가 아닙니다.'    # 3의 배수가 아니면 예외 발생, 3의 배수이면 그냥 넘어감
print(x)

~~~


~~~python

3의 배수를 입력하세요: 5 (입력)
Traceback (most recent call last):
  File "C:\project\assertion.py", line 2, in <module>
    assert x % 3 == 0, '3의 배수가 아닙니다.'
AssertionError: 3의 배수가 아닙니다.

~~~

---

## 4.예외 만들기
<br>
<br>
지금까지 파이썬에 내장된 예외를 처리했는데, 이번에는 예외를 직접 만들어서 발생시켜보자. 프로그래머가 직접 만든 예외를 사용자 정의 예외라고 한다.

예외를 만드는 방법은 간단하다. 그냥 Exception을 상속받아서 새로운 클래스를 만들면 된다. 그리고 \__init__ 메서드에서 기반 클래스의 \__init__ 메서드를 호출하면서 에러 메시지를 넣어주면 된다.

~~~python

class 예외이름(Exception):
    def __init__(self):
        super().__init__('에러메시지')

~~~

그럼 입력된 숫자가 3의 배수가 아닐 때 발생시킬 예외를 만들어보자.

~~~python

class NotThreeMultipleError(Exception):    # Exception을 상속받아서 새로운 예외를 만듦
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')
 
def three_multiple():
    try:
        x = int(input('3의 배수를 입력하세요: '))
        if x % 3 != 0:                     # x가 3의 배수가 아니면
            raise NotThreeMultipleError    # NotThreeMultipleError 예외를 발생시킴
        print(x)
    except Exception as e:
        print('예외가 발생했습니다.', e)
 
three_multiple()

~~~

5를 입력하면 3의 배수가 아니므로 NotThreeMultipleError 예외가 발생한다.

~~~python

3의 배수를 입력하세요: 5 (입력)
예외가 발생했습니다. 3의 배수가 아닙니다.

~~~

먼저 Exception을 상속받아서 NotThreeMultipleError 예외를 만들었다. 그리고 \__init__ 메서드 안에서 기반 클래스의 \__init__ 메서드를 호출하면서 에러 메시지를 넣었다.

~~~python

class NotThreeMultipleError(Exception):    # Exception을 상속받아서 새로운 예외를 만듦
    def __init__(self):
        super().__init__('3의 배수가 아닙니다.')

~~~

예외를 발생시킬 때는 raise NotThreeMultipleError와 같이 raise에 새로 만든 예외를 지정해주면 된다.

참고로 다음과 같이 Exception만 상속받고 pass를 넣어서 아무것도 구현하지 않아도 된다.

~~~python

class NotThreeMultipleError(Exception):    # Exception만 상속받고
    pass                                   # 아무것도 구현하지 않음

~~~

이때는 예외를 발생시킬 때 에러 메시지를 넣어주면 됩니다.

~~~python

raise NotThreeMultipleError('3의 배수가 아닙니다.')    # 예외를 발생시킬 때 에러 메시지를 넣음

~~~

지금까지 예외 처리에 대해 배웠다. 예외 처리는 에러가 발생하더라도 스크립트의 실행을 중단하지 않고 계속 실행하고자 할 때 사용한다는 점 꼭 기억하자.



---


### 예제1
<br>
<br>
다음 소스 코드를 완성하여 maria.txt 파일이 있으면 파일의 내용을 읽어서 출력하고, 파일이 없으면 '파일이 없습니다.'를 출력하도록 만드세요. 파일이 없을 때 발생하는 예외는 FileNotFoundError입니다.

~~~python

①     
    file = open('maria.txt', 'r')
②                          
    print('파일이 없습니다.')
③     
    s = file.read()
    file.close()

~~~


답

~~~python

① try:
② except FileNotFoundError:
③ else:

~~~


### 예제2
<br>
<br>
표준 입력으로 문자열이 입력됩니다. 다음 소스 코드를 완성하여 입력된 문자열이 회문이면 문자열을 그대로 출력하고, 회문이 아니면 '회문이 아닙니다.'를 출력하도록 만드세요. palindrome 함수와 NotPalindromeError 예외를 작성해야 합니다.

~~~python

________________
________________
________________
________________
________________
________________
________________
try:
    word = input()
    palindrome(word)
except NotPalindromeError as e:
    print(e)

#입력
level
#결과
level
#입력
hello
#결과
회문이 아닙니다.

~~~

내가 쓴 답

~~~python

class NotPalindromeError(Exception):
    def __init__(self):
        super().__init__('회문이 아닙니다.')
        
def palindrome(word):
    if word != word[::-1]:
        raise NotPalindromeError
    print(word)

~~~



