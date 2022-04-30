---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 회문 판별과 N-gram 만들기
date: 2022-04-13 19:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 회문 판별과 N-gram 만들기

<br>
<br>
문자열을 응용해 회문을 판별하는 방법과 N-gram을 만드는 방법을 알아보자.<br>
회문은 유전자 염기서열 분석에서 많이 쓰고, N-gram은 빅 데이터 분석, 검색 엔진에서 많이 쓰인다. 특히 구글은 책들을 스캔해서 N-gram viewer를 만들었는데 사람들의 언어 패턴을 시대별로 분석하기도 했다.


---

## 1. 파일에 문자열 쓰기, 읽기
<br>
<br>

### 회문 판별하기
<br>
<br>
회문(palindrome)은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 단어와 문장을 말한다. 예를 들면 "level", "SOS", "rotator", "nurses run"과 같은 단어와 문장이 있다. 


### 반복문으로 문자 검사하기
<br>
<br>
이제 반복문으로 문자열의 각 문자를 검사해보자. 여기서 가장 중요한 부분은 문자열(단어)의 길이이다. 회문 판별은 문자열의 길이를 기준으로 하기 때문에 문자열을 절반으로 나누어서 왼쪽 문자와 오른쪽 문자가 같은지 판별해야한다. 그리고 if 판별문에서 첫번쨰 글자와 마지막 글자를 비교해준다. 마지막 글자는 -1을 넣어 인덱스 0일때 마지막의 첫번째 글자인 인덱스 -1의 글자를 비교하게 만들었다. word[-(1 + i)]와 같이 숫자를 i만큼 증가시킨 뒤 음수로 바꾸는 방식으로도 표현할 수 있다.


~~~python

word = input('단어를 입력하세요: ')
 
is_palindrome = True                 # 회문 판별값을 저장할 변수, 초깃값은 True
for i in range(len(word) // 2):      # 0부터 문자열 길이의 절반만큼 반복
    if word[i] != word[-1 - i]:      # 왼쪽 문자와 오른쪽 문자를 비교하여 문자가 다르면
        is_palindrome = False        # 회문이 아님
        break
 
print(is_palindrome)                 # 회문 판별값 출력

# 실행결과
단어를 입력하세요: level (입력)
True

# 실행결과
단어를 입력하세요: hello (입력)
False

~~~


###  시퀀스 뒤집기로 문자 검사하기
<br>
<br>
문자열을 반대로 뒤집어 판별할 수 있다. 객체 슬라이스를 활용해 간단하게 판별해 보자. word[::-1]은 문자열 전체에서 인덱스를 1씩 감소시키면서 요소를 가져오므로 문자열을 반대로 뒤집는다. 회문은 순서를 거꾸로 읽어도 제대로 읽은 것과 같은 문자열이므로 원래 문자열 word와 뒤집은 문자열 word[::-1]이 같으면 회문이다.

~~~python

word = input('단어를 입력하세요: ')
 
print(word == word[::-1])    # 원래 문자열과 반대로 뒤집은 문자열을 비교

#실행결과
단어를 입력하세요: level (입력)
True
단어를 입력하세요: hello (입력)
False

~~~

###  리스트와 reversed 사용하기
<br>
<br>
다음과 같이 반복 가능한 객체의 요소 순서를 반대로 뒤집는 reversed를 사용해도 된다. list에 문자열을 넣으면 문자 하나 하나가 리스트의 요소로 들어간다. 여기서 reversed로 문자열을 반대로 뒤집어서 list에 넣어 두 리스트를 ==로 비교하면 회문판별이 가능하다.

~~~python

word = 'level'
list(word) == list(reversed(word)) #reversed는 새로운 객체를 만들어 반환한다.
True

list(word)
['l', 'e', 'v', 'e', 'l']
list(reversed(word))
['l', 'e', 'v', 'e', 'l']

~~~

###  문자열의 join 메서드와 reversed 사용하기
<br>
<br>
문자열의 join메서드를 사용해서 회문을 판별할 수 있다. join은 구분자 문자열과 문자열 리스트의 요소를 연결한다. 여기서는 빈 문자열''에 reversed(word)의 요소를 연결했으므로 문자 순서가 반대로 된 문자열을 얻을 수 있다. 즉,  join은 요소 사이에 구분자를 넣지만 빈문자열 ''을 활용하여 각문자를 그대로 연결하는 방식이다.

~~~python

>>> word = 'level'
>>> word == ''.join(reversed(word))
True

>>> word
'level'
>>> ''.join(reversed(word))
'level'

~~~

---

## 2. N-gram 만들기
<br>
<br>
N-gram은 문자열에서 N개의 연속된 요소를 추출하는 방법이다. 만약 'Hello'라는 문자열을 문자(글자) 단위 2-gram으로 추출하면 다음과 같이 된다. 즉, 문자열의 처음부터 문자열 끝까지 한 글자씩 이동하면서 2글자를 추출한다. 3-gram은 3글자, 4-gram은 4글자를 추출하게 된다.

~~~python

He
el
ll
lo

~~~


### 반복문으로 N-gram 출력하기
<br>
<br>
이제 반복문으로 문자 단위 2-gram을 출력해보자. 만약 3-gram이라면 반복 횟수는 range(len(text) - 2))와 같이 되고, 문자열 끝에서 두 글자 앞까지 반복하면 된다. 문자열을 출력할 때는 print(text[i], text[i + 1], text[i + 2], sep='')가 된다. 여기서 문자열의 끝까지 반복하면 text[i + 1], text[i + 2]는 문자열의 범위를 벗어난 접근을 하게 되므로 주의해야 한다.

~~~python

text = 'Hello'
 
for i in range(len(text) - 1):             # 2-gram이므로 문자열의 끝에서 한 글자 앞까지만 반복함 range(4)
    print(text[i], text[i + 1], sep='')    # 현재 문자와 그다음 문자 출력 
    #인덱스 01,12,23,34를 반복

~~~

글자 단위 N-gram이 있다면 단어 단위 N-gram도 있다. 다음은 문자열을 공백으로 구분하여 단어 단위 2-gram을 출력한다. 예를 들어 'this is python script'는 'this is', 'is python', 'python script'가 된다. 단어 단위 2-gram도 간단하다. split을 사용하여 공백을 기준으로 문자열을 분리하여 리스트로 만든다. 그리고 2-gram이므로 words 리스트의 마지막에서 요소 한 개 앞까지만 반복하면서 현재 문자열과 그다음 문자열을 출력하면 된다.

~~~python

text = 'this is python script'
words = text.split()                 # 공백을 기준으로 문자열을 분리하여 리스트로 만듦
 
for i in range(len(words) - 1):      # 2-gram이므로 리스트의 마지막에서 요소 한 개 앞까지만 반복함
    print(words[i], words[i + 1])    # 현재 문자열과 그다음 문자열 출력

#실행 결과

this is
is python
python script

~~~

### zip으로 2-gram 만들기
<br>
<br>
zip함수로 2-gram을 만들수 있다. 지금까지 zip함수는 리스트 두 개를 딕셔너리로 만들 때 사용했는데, zip함수는 반복 가능한 객체의 각 요소를 튜플로 묶어준다. 

~~~python

text = 'hello'
 
two_gram = zip(text, text[1:])
for i in two_gram:
    print(i[0], i[1], sep='')

# 실행결과

He
el
ll
lo

~~~

zip(text, text[1:])은 문자열 text와 text[1:]의 각 요소를 묶어서 튜플로 만든다. text[1:]은 인덱스 1(두 번째 문자)부터 마지막 문자까지 가져온다. 따라서  text와 text[1:]을 zip으로 묶으면 문자 하나가 밀린 상태로 각 문자를 묶게 된다. zip()함수는 반복 가능한 객체의 길이가 다를경우 뒤에 부분은 생략되어 출력된다.

~~~python

text = 'hello'
list(zip(text, text[1:]))
[('h', 'e'), ('e', 'l'), ('l', 'l'), ('l', 'o')]

# 이 리스트를 출력할 때는 for i in two_gram:와 같이 for로 반복하면서 print(i[0], i[1], sep='')로 튜플의 요소를 출력해주면 된다.

~~~

단어 단위 2-gram도 같은 방법으로 만들면 된다. 문자열을 공백으로 분리하여 리스트로 만드는 것 말고는 앞과 같다.

~~~python

text = 'this is python script'
words = text.split()
list(zip(words, words[1:]))
[('this', 'is'), ('is', 'python'), ('python', 'script')]

~~~

### zip과 리스트 표현식으로 N-gram 만들기
<br>
<br>
N-gram을 만들때 일일이 슬라이스를 넣지않고 리스트 표현식을 사용해 만들어 보자. [text[i:] for i in range(3)]처럼 for로 3번 반복하면서 text[i:]로 리스트를 생성했다. 여기서 for i in range(3)은 0, 1, 2까지 반복하므로 text[i:]는 text[0:], text[1:], text[2:]가 된다. 3-gram에 필요한 슬라이스다. text[0:]은 text와 같으므로 지금까지 zip에 넣었던 모양이다.

~~~python

text = 'hello'
[text[i:] for i in range(3)]
['hello', 'ello', 'llo']

~~~

리스트['hello', 'ello', 'llo']를 zip에 넣어보자. 결과를 보면 원하는 3-gram이 아니다. zip은 반복 가능한 객체 여러 개를 콤마고 구분해서 넣어줘야 한다. 하지만 ['hello', 'ello', 'llo']는 요소가 3개 들어있는 리스트 1개이기 때문이다.

~~~python

list(zip(['hello', 'ello', 'llo']))
[('hello',), ('ello',), ('llo',)]

~~~

zip에 리스트의 각 요소를 콤마로 구분해서 넣어주려면 리스트 앞에 *를 붙여야 한다. 이제 3-gram 리스트가 만들어졌다. 

~~~python

list(zip(*['hello', 'ello', 'llo']))
[('h', 'e', 'l'), ('e', 'l', 'l'), ('l', 'l', 'o')]

~~~

물론 리스트 표현식을 바로 zip에 넣어주려면 리스트 표현식 앞에 *를 붙이면 된다.

~~~python

list(zip(*[text[i:] for i in range(3)]))
[('h', 'e', 'l'), ('e', 'l', 'l'), ('l', 'l', 'o')]

~~~



---


### 예제
<br>
<br>
단어가 줄 단위로 저장된 words.txt 파일이 주어집니다. words.txt 파일에서 회문인 단어를 각 줄에 출력하는 프로그램을 만드세요. 단어를 출력할 때는 등장한 순서대로 출력해야 합니다. 그리고 파일에서 읽은 단어는 \n이 붙어있으므로 \n을 제외한 뒤 회문인지 판단해야 하며 단어를 출력할 때도 \n이 출력되면 안 됩니다(단어 사이에 줄바꿈이 두 번 일어나면 안 됨).


~~~python

________________
________________
________________
________________
________________
________________

#words.txt

apache
decal
did
neep
noon
refer
river

#표준출력
did
noon
refer

~~~

내가 쓴 답

~~~python

with open('words.txt', 'r')as file:
    words = file.readlines()
    for word in words:
        if list(word.strip('\n')) == list(reversed(word.strip('\n'))) :
            print(word.strip('\n'))

~~~


더 좋은 답

~~~python

with open('words.txt', 'r')as file:
    words = file.readlines()
    for word in words:
        word = word.strip('\n')
        if word == word[::-1] :
            print(word)

~~~