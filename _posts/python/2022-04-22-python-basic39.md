---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 코루틴 사용하기
date: 2022-04-21 16:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 코루틴 사용하기

<br>
<br>
다음과 같이 calc 함수 안에서 add 함수를 호출했을 때 add 함수가 끝나면 다시 calc 함수로 돌아온다. 특히 add 함수가 끝나면 이 함수에 들어있던 변수와 계산식은 모두 사라진다. 아래 소스 코드에서 calc 함수와 add함수의 관계를 살펴보자. calc가 메인루틴(main routine)이면 add는 calc의 서브루틴(sub routine)이다. 

~~~python

def add(a, b):
    c = a + b    # add 함수가 끝나면 변수와 계산식은 사라짐
    print(c)
    print('add 함수')
 
def calc():
    add(1, 2)    # add 함수가 끝나면 다시 calc 함수로 돌아옴
    print('calc 함수')
 
calc()

~~~

메인 루틴에서 서브 루틴을 호출하면 서브 루틴의 코드를 실행한 뒤 다시 메인 루틴으로 돌아온다. 특히 서브 루틴이 끝나면 서브 루틴의 내용은 모두 사라진다. 즉, 서브 루틴은 메인 루틴에 종속된 관계이다. 

코루틴은 방식이 위와는 조금 다르다. 코루틴(coroutine)은 cooperative routine을 의미하는데 서로 협력하는 루틴이라는 뜻이다. 즉, 메인루틴과 서브 루틴처럼 종속된 관계가 아니고 서로 대등한 관계이며 특정 시점에 상대방의 코드를 실행한다. 코루틴은 함수가 종료되지 않은 상태에서 메인 루틴의 코드를 실행한 뒤 다시 돌아와서 코루틴의 코드를 실행한다. 따라서 코루틴이 종료되지 않았으므로 코루틴의 내용도 계속 유지된다.

일반 함수를 호출하면 코드를 한 번만 실행할 수 있지만, 코루틴은 코드를 여러 번 실행할 수 있다. 참고로 함수의 코드를 실행하는 지점을 진입점(entry point)이라고 하는데, 코루틴은 진입점이 여러 개인 함수이다.

---

## 1.코루틴에 값 보내기
<br>
<br>
코루틴은 제너레이터의 특별한 형태이다. 제너레이터는 yield로 값을 발생시켰지만 코루틴은 yield로 값을 받아올 수 있다. 다음과 같이 코루틴에 값을 보내면서 코드를 실행할 때는 send 메서드를 사용한다. sand 메서드가 보낸 값을 받아오려면(yield) 형식으로 yield를 괄호로 묶어준 뒤 변수에 저장한다.

- 코루틴객체.send(값)
- 변수 = (yield)

그럼 코루틴에 숫자 1, 2, 3을 보내서 출력해보겠다.

~~~python

def number_coroutine():
    while True:        # 코루틴을 계속 유지하기 위해 무한 루프 사용
        x = (yield)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
        print(x)
 
co = number_coroutine()
next(co)      # 코루틴 안의 yield까지 코드 실행(최초 실행)
 
co.send(1)    # 코루틴에 숫자 1을 보냄
co.send(2)    # 코루틴에 숫자 2을 보냄
co.send(3)    # 코루틴에 숫자 3을 보냄
# 실행 결과
1
2
3

~~~

코루틴 number_coroutine은 while True:로 무한히 반복하도록 만든다. 왜냐하면 코루틴을 종료하지 않고 계속 유지시키기 위해 무한 루프를 사용한다. 그리고 x = (yield)와 같이 코루틴 바깥에서 보낸 값을 받아서 x에 저장하고, print로 x의 값을 출력한다.

~~~python

def number_coroutine():
    while True:        # 코루틴을 계속 유지하기 위해 무한 루프 사용
        x = (yield)    # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
        print(x)

~~~

코루틴 바깥에서는 co = number_coroutine()과 같이 코루틴 객체를 생성한 뒤 next(co)로 코루틴 안의 코드를 최초로 실행하여 yield까지 코드를 실행한다.

- next(코루틴객체)

~~~python

co = number_coroutine()
next(co)      # 코루틴 안의 yield까지 코드 실행(최초 실행)

~~~

그다음에 co.send로 숫자 1, 2, 3을 보내면 코루틴 안에서 숫자를 받은 뒤 print로 출력한다.

~~~python

co.send(1)    # 코루틴에 숫자 1을 보냄
co.send(2)    # 코루틴에 숫자 2을 보냄
co.send(3)    # 코루틴에 숫자 3을 보냄

~~~

먼저 next(co)로 코루틴의 코드를 최초로 실행하면 x = (yield)의 yield에서 대기하고 다시 메인 루틴으로 돌아온다. 그다음에 메인 루틴에서 co.send(1)로 1을 보내면 코루틴은 대기 상태에서 풀리고 x = (yield)의 x = 부분이 실행된 뒤 print(x)로 숫자를 출력한다. 이 코루틴은 while True:로 반복하는 구조이므로 다시 x = (yield)의 yield에서 대기한다. 그러고 나서 메인 루틴으로 돌아옵니다. 이런 과정으로 send가 보낸 값을 (yield)가 받게 된다. 계속 같은 과정으로 send를 사용하여 값을 보내면 코루틴에서 값을 받아서 출력한다.

정리하자면 next 함수(\__next__ 메서드)로 코루틴의 코드를 최초로 실행하고, send 메서드로 코루틴에 값을 보내면서 대기하고 있던 코루틴의 코드를 다시 실행한다.

### send로 코루틴의 코드를 최초로 실행하기
<br>
<br>
지금까지 코루틴의 코드를 최초로 실행할 때 next 함수(__next__ 메서드)를 사용했지만, 코루틴객체.send(None)과 같이 send 메서드에 None을 지정해도 코루틴의 코드를 최초로 실행할 수 있다.

---

## 2.코루틴 바깥으로 값 전달하기
<br>
<br>
코루틴에서 바깥으로 값을 전달해보자. 다음과 같이 (yield 변수) 형식으로 yield에 변수를 지정한 뒤 괄호로 묶어주면 값을 받아오면서 바깥으로 값을 전달한다. 그리고 yield를 사용하여 바깥으로 전달한 값은 next 함수(__next__ 메서드)와 send 메서드의 반환값으로 나온다.

- 변수 = (yield 변수)
- 변수 = next(코루틴객체)
- 변수 = 코루틴객체.send(값)

그럼 코루틴에 숫자를 보내고, 코루틴은 받은 숫자를 누적해서 바깥에 전달해보자.

~~~python

def sum_coroutine():
    total = 0
    while True:
        x = (yield total)    # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x
 
co = sum_coroutine()
print(next(co))      # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력
 
print(co.send(1))    # 1: 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
print(co.send(2))    # 3: 코루틴에 숫자 2를 보내고 코루틴에서 나온 값 출력
print(co.send(3))    # 6: 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력

# 실행 결과
0
1
3
6

~~~

코루틴에서 값을 누적할 변수 total을 만들고 0을 할당한다. 그리고 x = (yield total)과 같이 값을 받아오면서 바깥으로 값을 전달하도록 만든다. 즉, 바깥에서 send가 보낸 값은 x에 저장되고, 코루틴 바깥으로 보낼 값은 total이다. 그 다음에 total += x 와 같이 받은 값을 누적해 준다.

~~~python

def sum_coroutine():
    total = 0
    while True:
        x  = (yield total)    # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        total += x

~~~

코루틴 바깥에서는 co = sum_coroutine()과 같이 코루틴 객체를 생성한 뒤 next(co)로 코루틴 안의 코드를 최초로 실행하여 yield까지 코드를 실행하고, print로 next(co)에서 변환된 값을 출력한다. 그다음에 co.send로 숫자 1, 2, 3을 보내고 print로 co.send에서 반환된 값을 출력한다.

~~~python

co = sum_coroutine()
print(next(co))      # 0: 코루틴 안의 yield까지 코드를 실행하고 코루틴에서 나온 값 출력
 
print(co.send(1))    # 1: 코루틴에 숫자 1을 보내고 코루틴에서 나온 값 출력
print(co.send(2))    # 3: 코루틴에 숫자 2를 보내고 코루틴에서 나온 값 출력
print(co.send(3))    # 6: 코루틴에 숫자 3을 보내고 코루틴에서 나온 값 출력

~~~

next와 send의 차이를 살펴보면 next는 코루틴의 코드를 실행하지만 값을 보내지 않을 때 사용하고, send는 값을 보내면서 코루틴의 코드를 실행할 때 사용한다.

먼저 next(co)로 코루틴의 코드를 최초로 실행하면 x = (yield total)의 yield에서 total을 메인 루틴으로 전달하고 대기한다. 그다음에 메인 루틴에서 print(next(co))와 같이 코루틴에서 나온 값을 출력한다. 여기서는 total에 0이 들어있으므로 0을 받아와서 출력한다.

그리고 co.send(1)로 1을 보내면 코루틴은 대기 상태에서 풀리고 x = (yield total)의 x = 부분이 실행된뒤 total += x로 숫자를 누적한다. 이 코루틴은 while True:로 반복하는 구조이므로 다시 x=(yield total)의 yield에서 total을 메인 루틴으로 전달하고 대기한다. 그다음에 메인 루틴에서 print(co.send(1))과 같이 코루틴에서 나온 값을 출력한다. 여기서는 total에 1이들어가 있으므로 1을 받아와서 출력한다.

이런 과정으로 (yield total)이 바깥으로 전달한 값을 next와 send의 반환값으로 받고, send가 보낸 값을 x = (yield total)의 x가 받게 된다.

제너레이터와 코루틴의 차이점을 정리해보자.

- 제너레이터는 next 함수(\__next__ 메서드)를 반복 호출하여 값을 얻어내는 방식
- 코루틴은 next 함수(\__next__ 메서드)를 한 번만 호출한 뒤 send로 값을 주고 받는 방식

### 값을 보내지 않고 코루틴의 코드 실행하기
<br>
<br>
값을 보내지 않으면서 코루틴의 코드를 실행할 때는 next 함수(__next__ 메서드)만 사용하면 된다. 잘 생각해보면 이 방식이 일반적인 제너레이터이다.


---

## 3. 코루틴을 종료하고 예외 처리하기
<br>
<br>
보통 코루틴은 실행 상태를 유지하기 위해 while:True:를 사용해서 끝나지 않는 무한 루프로 동작한다. 만약 코루틴을 강제로 종료하고 싶다면 close메서드를 사용한다.

- 코루틴객체.close()

다음은 코루틴에 숫자를 20개 보낸 뒤 코루틴을 종료한다. 코루틴 객체에서 close 메서드를 사용하면 코루틴이 종료된다. 사실 파이썬 스크립트가 끝나면 코루틴도 끝나기 때문에 close를 사용하지 않은 것과 별 차이가 없다. 하지만 close는 코루틴의 종료 시점을 아아야 할 때 사용하면 편리하다.

~~~python

def number_coroutine():
    while True:
        x = (yield)
        print(x, end=' ')
 
co = number_coroutine()
next(co)
 
for i in range(20):
    co.send(i)
 
co.close()    # 코루틴 종료

# 실행 결과
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19

~~~

### GeneratorExit 예외 처리하기

코루틴 객체에서 close 메서드를 호출하면 코루틴이 종료될 때 GeneratorExit 예외가 발생한다. 따라서 이 예외를 처리하면 코루틴의 종료 시점을 알 수 있다.

~~~python

def number_coroutine():
    try:
        while True:
            x = (yield)
            print(x, end=' ')
    except GeneratorExit:    # 코루틴이 종료 될 때 GeneratorExit 예외 발생
        print()
        print('코루틴 종료')
 
co = number_coroutine()
next(co)
 
for i in range(20):
    co.send(i)
 
co.close()

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 
코루틴 종료

~~~

코루틴 안에서 try except로 GeneratorExit 예외가 발생하면 '코루틴 종료'가 출력되도록 만들었다. 이렇게 하면 close 메서드로 코루틴을 종료할 때 원하는 코드를 실행할 수 있다.

~~~python

    except GeneratorExit:    # 코루틴이 종료 될 때 GeneratorExit 예외 발생
        print()
        print('코루틴 종료')

~~~

### 코루틴 안에서 예외 발생시키기
<br>
<br>
이번에는 코루틴 안에 예외를 발생시켜서 코루틴을 종료해보자.

코루틴 안에 예외를 발생 시킬 때는 throw 메서드를 사용합니다. throw는 말그대로 던지다라는 뜻인데 예외를 코루틴 안으로 던진다. 이때 throw 메서드에 지정한 에러 메시지는 except as의 변수에 들어간다.

- 코루틴객체.throw(예외이름, 에러메시지)

다음은 코루틴에 숫자를 보내서 누적하다가 RuntimeError 예외가 발생하면 에러 메시지를 출력하고 누적된 값을 코루틴 바깥으로 전달한다.
~~~python

def sum_coroutine():
    try:
        total = 0
        while True:
            x = (yield)
            total += x
    except RuntimeError as e:
        print(e)
        yield total    # 코루틴 바깥으로 값 전달
 
co = sum_coroutine()
next(co)
 
for i in range(20):
    co.send(i)
 
print(co.throw(RuntimeError, '예외로 코루틴 끝내기')) # 190
                                                      # 코루틴의 except에서 yield로 전달받은 값


# 실행 결과
예외로 코루틴 끝내기
190

~~~

코루틴 안에서 try except로 RuntimeError 예외가 발생하면 print로 에러 메시지를 출력하고 yield를 사용하여 total을 바깥으로 전달하도록 만들었다.

~~~python

    except RuntimeError as e:
        print(e)
        yield total    # 코루틴 바깥으로 값 전달

~~~

코루틴 바깥에서는 co.throw(RuntimeError, '에외로 코루틴 끝내기')와 같이 throw 메서드에 RuntimeError 예외와 에러 메시지를 지정하면 코루틴 안에서 예외가 발생한다. 그리고 코루틴 안의 except에서 yield를 사용하여 바깥으로 전달한 값은 throw 메서드의 반환 값으로 나온다.

여기서는 코루틴 안에서 예외 처리를 했으므로 '예외로 코루틴 끝내기'가 출력되고, 코루틴 바깥에서는 누적된 값 190이 출력된다.


## 4. 하위 코루틴의 반환값 가져오기
<br>
<br>
제너레이터에서 yield from을 사용하면 값을 바깥으로 여러 번 전달한다고 했습니다('40.3 yield from으로 값을 여러 번 바깥으로 전달하기' 참조). 하지만 코루틴에서는 조금 다르게 사용한다. yield from에 코루틴를 지정하면 해당 코루틴에서 return으로 반환한 값을 가져온다(yield from은 파이썬 3.3 이상부터 사용 가능) 

- 변수 = yield from 코루틴()

다음은 코루틴에서 숫자를 누적한 뒤 합계를 yield from으로 가져온다.

코루틴에 1부터 10까지 보내서 합계 55를 구하고, 다시 1부터 100까지 보내서 합계 5050을 구했다.


~~~python

def accumulate():
    total = 0
    while True:
        x = (yield)         # 코루틴 바깥에서 값을 받아옴
        if x is None:       # 받아온 값이 None이면
            return total    # 합계 total을 반환
        total += x
 
def sum_coroutine():
    while True:
        total = yield from accumulate()    # accumulate의 반환값을 가져옴
        print(total)
 
co = sum_coroutine()
next(co)
 
for i in range(1, 11):    # 1부터 10까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄
 
for i in range(1, 101):   # 1부터 100까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄

# 실행 결과
55
5050

~~~

먼저 숫자를 받아서 누적할 코루틴을 만든다. x = (yield)와 같이 코루틴 바깥에서 값을 받아온 뒤 total에 계속 더한다. 특히 이 코루틴은 while True:로 무한히 반복하지만 코루틴을 끝낼 방법이 필요하다. 여기서는 코루틴 바깥에서 받아온 값이 None이면 return으로 total을 반환하고 코루틴을 끝낸다.


~~~python

def accumulate():
    total = 0
    while True:
        x = (yield)         # 코루틴 바깥에서 값을 받아옴
        if x is None:       # 받아온 값이 None이면
            return total    # 합계 total을 반환, 코루틴을 끝냄
        total += x

~~~

이제 합계를 출력할 코루틴을 만든다. 먼저 while True:로 무한히 반복한다. 그리고 total = yield from accumulate()와 같이 yield from을 사용하여 코루틴 accumulate의 반환값을 가져온다.

~~~python

co = sum_coroutine()
next(co)
 
for i in range(1, 11):    # 1부터 10까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄

~~~

코루틴에서 yield from을 사용하면 코루틴 바깥에서 send로 하위 코루틴까지 값을 보낼 수 있다. 따라서 co = sum_coroutine()으로 코루틴 객체를 만든 뒤 co.send로 값을 보내면 accumulate에서 값을 받는다.

~~~python

co = sum_coroutine()
next(co)
 
for i in range(1, 11):    # 1부터 10까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄

~~~

co.send로 숫자를 계속 내보내다가 누적을 끝내고 싶으면 None을 보내면 된다.


~~~python

co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄

~~~

이때 accumulate는 None을 받으면 코루틴이 완전히 끝나지만 sum_coroutine에서 무한 루프로 반복하고 있으므로 print로 total을 출력한 뒤 다시 yield from accumulate()로 accumulate를 실행하게 된다.

~~~python

def sum_coroutine():
    while True:
        total = yield from accumulate()    # accumulate가 끝나면 yield from으로 다시 실행
        print(total)

~~~

### StopIteration 예외 발생시키기
<br>
<br>
코루틴도 제너레이터이므로 return을 사용하면 StopIteration이 발생한다. 그래서 코루틴에서 return 값은 raise StopIteration(값)처럼 사용할 수도 있다(파이썬 3.6 이하). 이렇게 raise로 StopIteration 예외를 직접 발생시키고 값을 지정하면 yield from으로 값을 가져올 수 있다(단, 파이썬 3.7부터는 제너레이터 안에서 raise로 StopIteration 예외를 직접 발생시키면 RuntimeError로 바뀌므로 이 방법은 사용할 수 없다. 파이썬 3.7부터는 그냥 return 값을 사용하자)

- raise StopIteration(값)

~~~python

def accumulate():
    total = 0
    while True:
        x = (yield)                       # 코루틴 바깥에서 값을 받아옴
        if x is None:                     # 받아온 값이 None이면
            raise StopIteration(total)    # StopIteration에 반환할 값을 지정(파이썬 3.6 이하)
        total += x
 
def sum_coroutine():
    while True:
        total = yield from accumulate()    # accumulate의 반환값을 가져옴
        print(total)
 
co = sum_coroutine()
next(co)
 
for i in range(1, 11):    # 1부터 10까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄
 
for i in range(1, 101):   # 1부터 100까지 반복
    co.send(i)            # 코루틴 accumulate에 숫자를 보냄
co.send(None)             # 코루틴 accumulate에 None을 보내서 숫자 누적을 끝냄

# 실행 결과
55
5050

~~~

accumulate에서 return total 대신 raise StopIteration(total)을 사용했다. 이때도 yield from은 accumulate의 total을 가져오게 된다.

### 코루틴의 yield from으로 값을 발생시키기
<br>
<br>
아래 예제에서는  x = (yield)와 같이 코루틴 바깥에서 보낸 값만 받아왔다. 하지만 코루틴에서 yield에 값을 지정해서 바깥으로 전달했다면 yield from은 해당 값을 다시 바깥으로 전달된다.

~~~python

def number_coroutine():
    x = None
    while True:
        x = (yield x)    # 코루틴 바깥에서 값을 받아오면서 바깥으로 값을 전달
        if x == 3:
            return x
 
def print_coroutine():
    while True:
        x = yield from number_coroutine()   # 하위 코루틴의 yield에 지정된 값을 다시 바깥으로 전달
        print('print_coroutine:', x)
 
co = print_coroutine()
next(co)
 
x = co.send(1)    # number_coroutine으로 1을 보냄
print(x)          # 1: number_coroutine의 yield에서 바깥으로 전달한 값
x = co.send(2)    # number_coroutine으로 2를 보냄
print(x)          # 2: number_coroutine의 yield에서 바깥으로 전달한 값
co.send(3)        # 3을 보내서 반환값을 출력하도록 만듦

# 실행 결과
1
2
print_coroutine: 3

~~~



---


### 예제1
<br>
<br>
다음 소스 코드를 완성하여 문자열에서 특정 단어가 있으면 True, 없으면 False가 출력되게 만드세요. find 함수는 코루틴으로 작성해야 합니다.

~~~python

_________________________________
...
_________________________________
 
f = find('Python')
next(f)
 
print(f.send('Hello, Python!'))
print(f.send('Hello, world!'))
print(f.send('Python Script'))
 
f.close()
                                                     
 

실행 결과
True
False
True

~~~


답

~~~python

def find(word):
    result = False
    while True:
        line = (yield result)
        result = word in lineㅇ

~~~




### 예제2
<br>
<br>
표준 입력으로 정수 두 개가 입력됩니다(첫 번째 입력 값의 범위는 10~1000, 두 번째 입력 값의 범위는 100~1000이며 첫 번째 입력 값은 두 번째 입력 값보다 항상 작습니다). 다음 소스 코드에서 첫 번째 정수부터 두 번째 정수 사이의 소수(prime number)를 생성하는 제너레이터를 만드세요. 소수는 1과 자기자신만으로 나누어 떨어지는 1보다 큰 양의 정수입니다.

~~~python

________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________
________________

start, stop = map(int, input().split())
 
g = prime_number_generator(start, stop)
print(type(g))
for i in g:
    print(i, end=' ')

#입력
50 100
#결과
<class 'generator'>
53 59 61 67 71 73 79 83 89 97 
#입력
950 1000
#결과
<class 'generator'>
953 967 971 977 983 991 997 

~~~

답

~~~python

def isPrime(number): # 아래 prime_number_generator함수에서 i의 값이 매개변수로 들어간다.
    if number == 1:
        return False #소수는 1보다 큰 자연수 중 1과 자기자신만을 약수로 가지는 수이다. 
                     #1은 1보다 크지 않기 때문에 소수가 아니다.
    for i in range(2, number): # 2부터 전달된 number의 값까지 i에 전달하고 
        if number % i == 0: # 전달된 number를 number전의 수까지로 나누어 0이 되면 소수가 아니다.
            return False
    return True

def prime_number_generator(start, stop):
    for i in range(start, stop+1):
        if isPrime(i):
            yield i

~~~



