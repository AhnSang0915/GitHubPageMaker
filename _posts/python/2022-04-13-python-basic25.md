---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 파일 사용하기
date: 2022-04-13 16:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 파일 사용하기

<br>
<br>
파이썬 에서 파일을 사용해 문자열을 읽고 쓰는 방법과 파이썬 객체를 파일에 읽고 쓰는 방법을 알아보자.

---

## 1. 파일에 문자열 쓰기, 읽기
<br>
<br>

### 파일에 문자열 쓰기
<br>
<br>
파일에 문자열을 쓸 때는 open함수로 파일을 열어서 파일 객체(file object)를 얻은 뒤에 write메서드를 사용한다.

- 파일객체 = open(파일이름, 파일모드)
- 파일객체.write('문자열')
- 파일객체.close()

파일을 사용하기 위해서는 먼저 open함수로 파일을 쓰기모드'w'( write)로 열고 파일에 문자열을 저장한후 파일을 닫고 실행해보면 우리가 지정한 위치에 hello.txt 파일이 저장되어 있을것이다.

~~~python

file = open('hello.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
file.write('Hello, world!')      # 파일에 문자열 저장
file.close()                     # 파일 객체 닫기

~~~

### 파일에 문자열 읽기
<br>
<br>
hello.txt파일의 문자열을 읽어보자. 파일을 읽을때도 open함수로 파일을 열어서 파일 객체를 얻은 뒤 read 메서드로 파일의 내용을 읽는다. 이때는 파일 모드를 읽기모드 'r'로 지정한다.

- 변수 = 파일객체.read()

open을 사용해 hello.txt파일을 읽기 모드 'r'로 연다. 여기서 'r'은 읽다(read)의 r이다. read의 반환값을 변수 s에 지정해주고 파일의 내용을 읽는다. 

~~~python

file = open('hello.txt', 'r')    # hello.txt 파일을 읽기 모드(r)로 열기. 파일 객체 반환
s = file.read()                  # 파일에서 문자열 읽기
print(s)                         # Hello, world!
file.close()                     # 파일 객체 닫기

~~~

그리고 print로 변수의 값을 출력하면 'Hello, world!'가 출력된다.

~~~python

# idle 소스코드창 출력
Hello, World!
s
'Hello, World!'

~~~

###  자동으로 파일 객체 닫기
<br>
<br>
파이썬 에서는 **with as** 를 사용하면 파일을 사용한 뒤 자동으로 파일 객체를 닫아준다. 다음과 같이 whith다음에 open으로 파일을 열고 as뒤에 파일 객체를 지정한다.

~~~python

with open(파일이름, 파일모드) as 파일객체:
    코드

~~~

hello.txt파일을 읽어보자.

~~~python

with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    s = file.read()                     # 파일에서 문자열 읽기
    print(s)                            # Hello, world!

# idle 소스코드창 출력
Hello, world!

~~~

---

## 2. 문자열 여러 줄을 파일에 쓰기, 읽기
<br>
<br>
문자열 여러 줄을 파일에 쓰고 읽는 방법을 알아보자.

### 반복문으로 문자열 여러 줄을 파일에 쓰기
<br>
<br>
반복문을 사용해 문자열 어려 줄을 써보자. 파일에 문자열 어려줄을 저장할 떄는 개행문자를 사용해야한다. 'Hello, world! {0}\n'와 같이 문자열 끝에 개행 문자 \n를 지정해주어야 줄바꿈이 된다. \n을 붙이지 않으면 문자열이 모두 한 줄로 붙어서 저장됨으로 주의한다.

~~~python

with open('hello.txt', 'w') as file:    # hello.txt 파일을 쓰기 모드(w)로 열기
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))

#hello.txt 의 내용
Hello, world! 0
Hello, world! 1
Hello, world! 2

~~~

### 리스트에 들어있는 문자열을 파일에 쓰기
<br>
<br>
리스트에 들어있는 문자열을 파일에 써보자.

- 파일객체.writelines(문자열리스트)

writelines는 리스트에 들어있는 문자열을 파일에 쓴다. 특히 writelines를 사용할 때는 반드시 리스트의 각 문자열 끝에 개행 문자 \n을 붙여주어야 한다. 그렇지 않으면 문자열이 모두 한 줄로 붙어서 저장되므로 주의해야 한다.

~~~python

lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
 
with open('hello.txt', 'w') as file:    # hello.txt 파일을 쓰기 모드(w)로 열기
    file.writelines(lines)

#hello.txt 의 내용
안녕하세요.
파이썬
코딩 도장입니다.

~~~


### 파일의 내용을 한 줄씩 리스트로 가져오기
<br>
<br>
앞에서 만든 hello.txt파일의 내용을 한 줄씩 읽어보자. read는 파일의 내용을 읽어서 문자열로 가져오지만 readlines는 파일의 내용을 한 줄씩 리스트 형태로 가져온다.

- 변수 = 파일객체.readlines()

~~~python

with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    lines = file.readlines()
    print(lines)

# idle 소스코드창 출력
['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']

~~~

### 파일의 내용을 한 줄씩 읽기
<br>
<br>
만약 파일의 내용을 한 줄씩 순차적으로 읽으려면 readline을 사용한다.

- 변수 = 파일객체.readline()

readline으로 파일을 읽을 때는 while 반복문을 활용한다. 왜냐면 파일에 문자열이 몇 줄이나 있는지 모르기 때문이다. while은 특정 조건이 만족할 때 계속 반복하므로 파일의 크기에 상관없이 문자열을 읽어올 수 있다. readline은 더 이상 읽을 줄이 없을 때는 빈 문자열을 반환하는데, while에는 이런 특성을 이용하여 조건식을 만들어준다. 즉, line != ''와 같이 빈 문자열이 아닐 때 계속 반복하도록 만든다. 그리고 반복문 안에서는 line = file.readline()과 같이 문자열 한 줄을 읽어서 변수 line에 저장해 준다.


~~~python

with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    line = None    # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline()
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

# idle 소스코드창 출력
안녕하세요.
파이썬
코딩 도장입니다.

~~~

특히 변수 line은 while로 반복하기전 None으로 초기화 해준다. 만약 변수 line을 만들지 않고 while을 실행하면 없는 변수와 빈 문자열 ''을 비교하게 되므로 에러가 발생한다. 또는, line을 None이 아닌 ''로 초기화하면 처음부터 line !=''는 거짓이 되므로 반복을 하지 않고 코드가 그냥 끝나버린다.
<br>
파일에서 읽어온 문자열에는 '안녕하세요.\n'와 같이 \n이 이미 들어있기 때문에 print(line.strip('\n')와 같이 strip 메서드로 \n을 삭제해줘야한다. strip('\n')을 생략하면 문자열 한 줄을 출력할 때마다 빈 줄이 계속 출력된다. 즉, 문자열 안에 든 \n과 print가 출력하는 \n 때문에 줄바꿈이 두 번 일어난다.


### for 반복문으로 파일의 내용을 줄 단위로 읽기
<br>
<br>
파이썬에서는 for 반복문으로 좀 더 간단하게 파일의 내용을 읽을 수 있다. 다음은 for반복문에 파일 객체를 지정하여 줄 단위로 파일의 내용을 읽는다. for line in file:로 간단하게 파일의 내용을 한줄 씩 읽었다. for 반복문에 파일 객체를 지정하면 반복을 할때마다 파일의 내용을 한 줄 씩 읽어 변수에 저장해준다.

~~~python

with open('hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    for line in file:    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

# idle 소스코드창 출력
안녕하세요.
파이썬
코딩 도장입니다.

~~~

### 파일 객체는 이터레이터
<br>
<br>
파일 객체는 이터레이터입니다. 따라서 변수 여러 개에 저장하는 언패킹(unpacking)도 가능하다.물론 a, b, c = file과 같이 사용하려면 hello.txt에는 문자열 3줄이 들어있어야 한다. 즉, 할당할 변수의 개수와 파일에 저장된 문자열의 줄 수가 일치해야 한다.

~~~python

>>> file = open('hello.txt', 'r')
>>> a, b, c = file
>>> a, b, c
('안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n')

~~~



---

## 3.파이썬 객체를 파일에 저장하기, 가져오기
<br>
<br>
파일에서 문자열만 읽고 쓴다면 조금 불편할 것이다. 파이썬은 객체를 파일에 저장하는 pickle모듈을 제공한다. 다음과 같이 파이썬 객체를 파일에 저장하는 과정을 피클링(pickling)이라고 하고, 파일에서 객체를 읽어오는 과정을 언피클링(unpickling)이라고 한다.


### 파이썬 객체를 파일에 저장하기
<br>
<br>
파이썬 객체를 파일에 저장하는 피클링을 해보자. 피클링은 pickle 모듈의 dump 메서드를 사용한다.
소스 코드를 실행하면 .py파일이 있는 폴더에 jame.p파일이 생성된다. 여기서는 확장자를 pickle의 p를 사용했지만 다른 확장자를 사용해도 상관없다. 특히 pickle.dump로 객체(값)를 저장할 때는 open('james.p', 'wb')와 같이 파일 모드를 **'wb'**로 지정해야 한다. b는 바이너리(binary)를 뜻하는데, 바이너리 파일은 컴퓨터가 처리하는 파일 형식이다. 따라서 메모장 같은 텍스트 편집기로 열어도 사람이 알아보기 어렵다.


~~~python

import pickle
 
name = 'james'
age = 17
address = '서울시 서초구 반포동'
scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
 
with open('james.p', 'wb') as file:    # james.p 파일을 바이너리 쓰기 모드(wb)로 열기
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)

~~~


### 파일에서 파이썬 객체 읽기
<br>
<br>
이제 파일에서 파이썬 객체를 읽어오는 언피클링을 해보자. 언피클링은 pickle 모듈의 load를 사용한다. 그리고 언피클링을 할 때는 반드시 파일 모드를 바이너리 읽기 모드 **'rb'**로 지정해야한다. 앞에서 james.p 파일을 저장할 때 pickle.dump를 네 번 사용했다. 마찬가지로 파일에서 객체(값)를 가져올 때도 pickle.load를 네 번 사용해야 한다. 즉, name, age, address, scores 순으로 저장했으므로 가져올 때도 같은 순서로 가져오면 된다.


~~~python

import pickle
 
with open('james.p', 'rb') as file:    # james.p 파일을 바이너리 읽기 모드(rb)로 열기
    name = pickle.load(file) #각각의 변수에 
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)

# 실행결과

james
17
서울시 서초구 반포동
{'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}

~~~

### 다른 파일 모드
<br>
<br>
사실 파일 모드는 조합에 따라 여러 종류가 있다. 읽기 'r', 쓰기 'w' 이외에 추가 'a', 배타적 생성 'x'도 있다. 추가 모드는 이미 있는 파일에서 끝에 새로운 내용을 추가할 때 사용하고, 배타적 생성 모드는 파일이 이미 있으면 에러(FileExistsError)를 발생시키고 없으면 파일을 만든다. 'x'는 베타적 생성(exclusive creation)의 x이다
<br>
또한, 파일의 형식도 함께 지정할 수 있는데, 텍스트 모드 't'와 바이너리 모드 'b'가 있다. 이 파일 형식과 읽기, 쓰기 모드를 조합한 텍스트 모드 'rt', 'wt'는 파일을 텍스트 모드로 연다. 특히 텍스트 모드는 생략할 수 있어서 그냥 'r', 'w'도 텍스트 모드이다. 그리고 바이너리 모드 'rb', 'wb' 등은 피클링을 사용하거나 바이너리 데이터를 직접 저장할 때 사용한다.
<br>
그다음에 '+'가 있는데 파일을 읽기/쓰기 모드로 연다. 이 모드는 'r+t', 'w+t', 'r+', 'w+', 'r+b', 'w+b' 등으로 조합할 수 있으며 읽기/쓰기 모드인 것은 같지만 파일 처리 방법이 조금씩 다르다.


---

### 예제
<br>
<br>
문자열이 저장된 words.txt 파일이 주어집니다(문자열은 한 줄로 저장되어 있습니다). words.txt 파일에서 문자 c가 포함된 단어를 각 줄에 출력하는 프로그램을 만드세요. 단어를 출력할 때는 등장한 순서대로 출력해야 하며 ,(콤마)와 .(점)은 출력하지 않아야 합니다.



~~~python

________________
________________
________________
________________
________________

#입력
Fortunately, however, for the reputation of Asteroid B-612, a Turkish dictator made a law that his subjects, under pain of death, should change to European costume. So in 1920 the astronomer gave his demonstration all over again, dressed with impressive style and elegance. And this time everybody accepted his report.

#출력
dictator
subjects
change
costume
elegance
accepted

~~~

내가 쓴답(왜 마지막 출력이 두번되는지 모르겠음)

~~~python

with open('words.txt', 'r')as file:
    x = file.readline()
    y = x.split()
    for word in y:
        for i in word:
            if i == 'c':
                print(word.strip(',.'))

# 출력
dictator
subjects
change
costume
elegance
accepted
accepted

~~~

정답

~~~python

with open('words.txt', 'r')as file:
    y = file.readline().split()
    for word in y:
        if 'c' in word:
            print(word.strip(',.'))

#출력
dictator
subjects
change
costume
elegance
accepted

~~~