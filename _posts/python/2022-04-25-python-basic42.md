---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 정규표현식 사용하기
date: 2022-04-24 16:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 정규표현식 사용하기

<br>
<br>
파이썬 내장함수로는 할 수 있는게 별로없다. 그래서 좀 더 복잡한 프로그램을 만들려면 파이썬의 모듈과 패키지를 사용해야 한다. 중간에 사용했던 random, turtle, pickle 등이 바로 모듈과 패키지이다. 

모듈(module)은 각종 변수, 함수, 클래스를 담고 있는 파일이고, 패키지(package)는 여러 모듈을 묶은 것이다. 파이썬을 설치할 때 다양한 모듈과 패키지가 기본으로 설치된다. 만약 기본 모듈과 패키지로 부족하다면 다른 사람이 만든 유명 모듈과 패키지를 설치해서 쓸 수도 있다.


- 모듈: 특정 기능을 .py 파일 단위로 작성한 것입니다.

- 패키지: 특정 기능과 관련된 여러 모듈을 묶은 것입니다. 패키지는 모듈에 네임스페이스(namespace, 이름공간)를 제공합니다.

- 파이썬 표준 라이브러리: 파이썬에 기본으로 설치된 모듈과 패키지, 내장 함수를 묶어서 파이썬 표준 라이브러리(Python Standard Library, PSL)라 부릅니다.

---

## 1.import로 모듈 가져오기
<br>
<br>
모듈은 import 키워드로 가져올 수 있다. 

- import 모듈
- import 모듈1, 모듈2
- 모듈.변수
- 모듈.함수()
- 모듈.클래스()

그럼 간단한 파이썬 표준 라이브러리의 수학 모듈 math를 가져와 원주율을 출력해보자.
import에 모듈 이름을 지정하면 해당 모듈을 가져올 수 있으며 math.pi와 같이 모듈.변수 형식으로 모듈의 변수를 사용한다.


~~~python

import math
math.pi
3.141592653589793

~~~

이번에는 math 모듈의 제곱근 함수 sqrt를 사용해보자.
모듈의 함수는 math.sqrt(4.0)와 같이 모듈.함수() 형식으로 사용한다.

~~~python

import math
math.sqrt(4.0)
2.0
math.sqrt(2.0)
1.4142135623730951

~~~


### import as로 모듈 이름 지정하기
<br>
<br>

모듈의 함수를 사용할 때 매번 math를 입력하지 않아도 impor as로 모듈의 이름을 지정할 수 있다.

- import 모듈 as 이름

이제 math 모듈을 m으로 줄여보자. import math as m과 같이 모듈을 가져오면서 as 뒤에 이름을 지정해준다. 이후 math 모듈을 사용할 때 m으로 줄여서 사용할 수 있다.

~~~python

import math as m    # math 모듈을 가져오면서 이름을 m으로 지정
m.sqrt(4.0)         # m으로 제곱근 함수 사용
2.0
m.sqrt(2.0)         # m으로 제곱근 함수 사용
1.4142135623730951

~~~

### from import로 모듈의 일부만 가져오기
<br>
<br>
from math import pi와 같이 from 뒤에 모듈 이름을 지정하고 import 뒤에 가져올 변수를 입력한다. 이후 가져온 변수를 사용할 때는 pi와 같이 모듈 이름을 붙이지 않고 바로 사용하면된다.

- from 모듈 import 변수

다음은 math 모듈에서 변수 pi만 가져온다. from math import pi와 같이 from 뒤에 모듈 이름을 지정하고 import 뒤에 가져올 변수를 입력한다. 이후 가져온 변수를 사용할 때는 pi와 같이 모듈 이름을 붙이지 않고 바로 사용하면 된다.

~~~python

from math import pi    # math 모듈에서 변수 pi만 가져옴
pi                     # pi를 바로 사용하여 원주율 출력
3.141592653589793

~~~

이번에는 모듈의 함수를 가져와보자.

- from 모듈 import 함수
- from 모듈 import 클래스

다음은 math 모듈에서 sqrt 함수만 가져왔다. math 모듈에서 sqrt 함수만 가져왔으므로 sqrt(4.0)처럼 앞에 math를 붙이지 않고 함수를 바로 사용할 수 있다.

~~~python

from math import sqrt    # math 모듈에서 sqrt 함수만 가져옴
sqrt(4.0)                # sqrt 함수를 바로 사용
2.0
sqrt(2.0)                # sqrt 함수를 바로 사용
1.4142135623730951

~~~

변수나 함수 하나를 가져오는게 아닌 여러개를 import 뒤에 가져올 변수, 함수, 클래스를 콤마로 구분하여 한번에 불러올 수 있다.

- from 모듈 import 변수, 함수, 클래스

다음은 math 모듈에서 pi, sqrt를 가져온다. from math import pi, sqrt와 같이 pi와 sqrt 두 개를 가져왔다.

~~~python

from math import pi, sqrt    # math 모듈에서 pi, sqrt를 가져옴
pi                           # pi로 원주율 출력
3.141592653589793
sqrt(4.0)                    # sqrt 함수 사용
2.0
sqrt(2.0)                    # sqrt 함수 사용
1.4142135623730951

~~~

변수, 함수, 클래스가 수십가지라면 위의 방법으로 입력하기 불편하다. for import를 사용하면 모듈의 모든 변수, 함수, 클래스를 가져올 수 있다.

- from 모듈 import *

다음은 math 모듈의 모든 변수, 함수, 클래스를 가져온다. from math import *와 같이 지정하면 math 모듈의 모든 함수, 변수, 클래스를 가져온다.

~~~python

from math import *    # math 모듈의 모든 변수, 함수, 클래스를 가져옴
pi                    # pi로 원주율 출력
3.141592653589793
sqrt(4.0)             # sqrt 함수 사용
2.0
sqrt(2.0)             # sqrt 함수 사용
1.4142135623730951

~~~

### from import로 모듈의 일부만 가져오기
<br>
<br>
이번에는 from import로 변수, 함수, 클래스를 가져온 뒤 이름을 지정해보자.

- from 모듈 import 변수 as 이름
- from 모듈 import 함수 as 이름
- from 모듈 import 클래스 as 이름

다음은 math 모듈에서 sqrt 함수를 가져오면서 이름을 s로 지정한다. from import로 가져온 변수, 함수, 클래스 뒤에 as로 이름을 지정해주면 된다.

~~~python

from math import sqrt as s    # math 모듈에서 sqrt 함수를 가져오면서 이름을 s로 지정
s(4.0)                        # s로 sqrt 함수 사용
2.0
s(2.0)                        # s로 sqrt 함수 사용
1.4142135623730951

~~~

여러개를 가져올 경우 각 변수, 함수, 클래스 등을 콤마로 구분하여 as를 여러 개 지정하면 된다.

- from 모듈 import 변수 as 이름1, 함수 as 이름2, 클래스 as 이름3

다음은 math 모듈의 pi를 가져오면서 이름을 p로, sqrt를 가져오면서 이름을 s로 지정한다.

~~~python

from math import pi as p, sqrt as s
p         # p로 원주율 출력
3.141592653589793
s(4.0)    # s로 sqrt 함수 사용
2.0
s(2.0)    # s로 sqrt 함수 사용
1.4142135623730951

~~~

### 가져온 모듈 해제하기, 다시 가져오기
<br>
<br>
import로 가져온 모듈(변수, 함수, 클래스)은 del로 해제할 수 있다.

~~~python

import math
del math

~~~

모듈을 다시 가져오려면 importlib.reload를 사용한다.

~~~python

import importlib
import math
importlib.reload(math)

~~~

--

## 2.import로 패키지 가져오기
<br>
<br>
패키지는 특정 기능과 관련된 여러 모듈을 묶은 것인데, 패키지에 들어있는 모듈도 import를 사용하여 가져온다. 

- import 패키지.모듈
- import 패키지.모듈1, 패키지.모듈2
- 패키지.모듈.변수
- 패키지.모듈.함수()
- 패키지.모듈.클래스()

파이썬 표준 라이브러리에서 urllib 패키지의 request 모듈을 가져와 url주소의 응답을 받아왔다.
패키지에 들어있는 모듈은 import urllib.request와 같이 패키지.모듈 형식으로 가져온다. 마찬가지로 모듈의 함수를 사용할 때도 urllib.request.urlopen()과 같이 패키지.모듈.함수() 형식으로 패키지 이름과 모듈 이름을 모두 입력해준다.

~~~python

import urllib.request
response = urllib.request.urlopen('http://www.google.co.kr')
response.status
200

~~~


### import as로 패키지 모듈 이름 지정하기
<br>
<br>
패키지 안에 들어있는 모듈도 import as를 사용하여 이름을 지정할 수 있다.

- import 패키지.모듈 as 이름

다음은 urllib 패키지의 request 모듈을 가져오면서 이름을 r로 지정한다.

~~~python

import urllib.request as r    # urllib 패키지의 request 모듈을 가져오면서 이름을 r로 지정
response = r.urlopen('http://www.google.co.kr')    # r로 urlopen 함수 사용
response.status
200

~~~

### from import로 패키지의 모듈에서 일부만 가져오기
<br>
<br>
패키지도 from import를 사용하여 모듈에서 변수, 함수, 클래스를 가져올 수 있다.

- from 패키지.모듈 import 변수
- from 패키지.모듈 import 함수
- from 패키지.모듈 import 클래스
- from 패키지.모듈 import 변수, 함수, 클래스

다시 urllib 패키지의 request 모듈에서 urlopen 함수와 Request 클래스를 가져와 보겠자.

~~~python

from urllib.request import Request, urlopen    # urlopen 함수, Request 클래스를 가져옴
req = Request('http://www.google.co.kr')       # Request 클래스를 사용하여 req 생성
response = urlopen(req)                        # urlopen 함수 사용
response.status
200

~~~

참고로 urlopen 함수에 URL을 바로 넣어도 되고, Request('http://www.google.co.kr')와 같이 Request 클래스에 URL을 넣은 뒤에 req를 생성해서 urlopen 함수에 넣어도 된다.

패키지의 모듈에서 모든 변수, 함수, 클래스를 가져오는 방법은 다음과 같다.

- from 패키지.모듈 import *

다음은 urllib의 request 모듈에서 모든 변수, 함수, 클래스를 가져온다.

~~~python

from urllib.request import *     # urllib의 request 모듈에서 모든 변수, 함수, 클래스를 가져옴
req = Request('http://www.google.co.kr')    # Request를 사용하여 req 생성
response = urlopen(req)                     # urlopen 함수 사용
response.status
200

~~~

---

## 3. 파이썬 패키지 인덱스에서 패키지 설치하기
<br>
<br>
파이썬은 파이썬 표준 라이브러리(Python Standard Library, PSL) 이외에도 파이썬 패키지 인덱스(Python Package Index, PyPI)를 통해 다양한 패키지를 사용할 수 있다. 특히 명령만 입력하면 원하는 패키지를 인터넷에서 다운로드하여 설치해줄 뿐만 아니라 관련된 패키지(의존성)까지 자동으로 설치해주므로 매우 편리하다.


### pip 설치하기
<br>
<br>
pip는 파이썬 패키지 인덱스의 패키지 관리 명령어이며 Windows용 파이썬에는 기본으로 내장되어 있다. 리눅스와 macOS에서는 콘솔(터미널)에서 다음과 같은 방법으로 설치하면 된다.

~~~python

$ curl -O https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py

~~~                                                                                       

###  pip로 패키지 설치하기
<br>
<br>
이제 pip install 명령으로 패키지를 설치해보자.

- pip install 패키지

Windows에서는 명령 프롬프트를 실행(윈도우 키+R을 누른 뒤 cmd를 입력)하고, 리눅스와 macOS에서는 콘솔(터미널)을 실행한 뒤 pip install requests 명령을 입력한다(pip 명령은 파이썬 셸 >>>에 입력하면 안 된다. 반드시 명령 프롬프트, 콘솔, 터미널에 입력).

참고로 requests는 파이썬 표준 라이브러리의 urllib.request와 비슷한 역할을 하는 패키지인데 좀 더 기능이 많고 편리하다.
~~~python

C:\Users\dojang>pip install requests

~~~

리눅스, macOS에서는 앞에 sudo를 붙여서 관리자 권한으로 실행합니다.

~~~python

$ sudo pip install requests

~~~

또는, python에 -m 옵션을 지정해서 pip를 실행할 수도 있다. -m 옵션은 모듈을 실행하는 옵션이며 pip도 모듈이다.

~~~python

C:\Users\dojang>python -m pip install requests

~~~

리눅스, macOS에서는 python3으로 실행하고, 앞에 sudo를 붙여서 관리자 권한으로 실행한다.

~~~python

$ sudo python3 -m pip install requests

~~~

명령을 입력하면 패키지 다운로드 및 설치 상황이 표시되는데, 다음과 같이 출력되면 정상적으로 설치된 것이다.

~~~python

Collecting requests
  Downloading requests-2.9.1-py2.py3-none-any.whl (501kB)
    100% |################################| 503kB 974kB/s
Installing collected packages: requests
Successfully installed requests-2.9.1

~~~

###  import로 패키지 가져오기
<br>
<br>
이제 파이썬 코드에서 패키지를 사용해보자.

- import 패키지

보통 pip install 명령으로 설치한 패키지는 import 패키지 또는 import 패키지.모듈 형식으로 사용하면 된다. 단, 패키지마다 구성이 다를 수 있으므로 해당 패키지의 웹 사이트에서 사용 방법을 찾아봐야한다.

~~~python

import requests                                # pip로 설치한 requests 패키지를 가져옴
r = requests.get('http://www.google.co.kr')    # requests.get 함수 사용
r.status_code
200

~~~


---


### 예제1
<br>
<br>
다음 소스 코드를 완성하여 소수점 이하를 올림, 버림한 숫자가 출력되게 만드세요. 올림 함수는 math 모듈의 ceil, 버림 함수는 math 모듈의 floor 함수입니다.

~~~python

 _______________________                               
 
x = 1.5
 
print(ceil(x), floor(x))

#실행 결과
2 1

~~~


답

~~~python

from math import ceil, floor

~~~

### 예제2
<br>
<br>
표준 입력으로 URL 문자열이 입력 입력됩니다. 입력된 URL이 올바르면 True, 잘못되었으면 False를 출력하는 프로그램을 만드세요. 이 심사문제에서 판단해야 할 URL의 규칙은 다음과 같습니다.

- http:// 또는 https://로 시작
- 도메인은 도메인.최상위도메인 형식이며 영문 대소문자, 숫자, -로 되어 있어야 함
- 도메인 이하 경로는 /로 구분하고, 영문 대소문자, 숫자, -, _, ., ?, =을 사용함

~~~python

________________
________________
________________


# 입력
http://www.example.com/hello/world.do?key=python
# 결과
True
# 입력
https://example/hello/world.html
# 결과
False

~~~

내가 쓴 답

~~~python

import re

url = input()

p = re.compile('^[a-zA-Z0-9]+\:\/\/[a-zA-Z0-9.]+\.[a-zA-Z0-9.-_?=/]')

print(p.match(url) != None, end=' ')

~~~

답

~~~python

import re

p = re.compile('^(http?://)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/[a-zA-Z0-9-_/.?=]*')

print(p.match(input()) != None)


~~~


먼저 URL은 http:// 또는 https://로 시작한다고 했으므로 정규표현식은 ^https?://로 시작합니다. 여기서 맨 앞에 ^를 붙였으므로 http 또는 https로 시작하는지 판단합니다. 그리고 https?와 같이 만들면 s가 0개 또는 1개 있어야 합니다. 따라서 http와 https를 둘 다 판별할 수 있습니다.

이제 도메인을 판단합니다. 도메인 부분은 [a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+/와 같이 만들어줍니다. 먼저 [a-zA-Z0-9-]+와 같이 영문 대소문자, 숫자, -이면서 문자 1개 이상인지 판단합니다. 그리고 중간에 \.를 넣어서 도메인.최상위도메인 형식인지 판단합니다. 여기서 .은 정규표현식에 사용하는 특수 문자이므로 앞에 반드시 \를 붙여야 합니다. 특히 최상위 도메인은 여러 단계일 수도 있으므로 [a-zA-Z0-9-.]+/와 같이 범위에 .을 넣어줍니다. 그리고 도메인과 도메인 이하 경로를 구분할 수 있도록 /를 붙여줍니다.

도메인 이하 경로는 영문 대소문자, 숫자, -, \_, ., ?, =을 사용한다고 했으므로 [a-zA-Z0-9-_/.?=]\*와 같이 만들어줍니다. 특히 하위 경로가 더 나올 수 있으므로 범위 안에 /를 넣어야 합니다.

지금까지 만든 정규표현식을 차례대로 연결해서 re.match 함수로 url을 판단해주면 됩니다. 그리고 re.match 함수의 반환값이 있으면(None이 아니면) True를 출력하고, None이면 False를 출력하면 됩니다.