---
layout: post
current: post
cover:  assets/built/images/python-logo.png
navigation: True
title: Python - Python 문자열 응용하기
date: 2022-04-11 17:00 +0900
tags: [python]
class: post-template
subclass: 'post tag-python'
author: AhnSang0915
---

{% include python-table-of-contents.html %}

# 문자열 응용하기
<br>
<br>
---

## 1. 문자열 조작하기
<br>
<br>
문자열은 문자열을 조작하거나 정보를 얻는 다양한 메서드(method)를 제공한다. 파이썬에서 제공하는 문자열 메서드중 자주 쓰는 메서드를 알아보자.

<br>
<br>

### 문자열 바꾸기
<br>
<br>

문자열을 다른 문자열로 바꾸는 메서드를 알아보자. 다음 문자열 Hello, world!'에서 'world'를 'Python'으로 바꾸는 코드이다. 바뀐 결과를 유지하고 싶다면 문자열이 저장된 변수에 replace를 사용한 뒤 다시 변수에 할당한다.

- replace('바꿀문자열', '새문자열')

~~~python

'Hello, world!'.replace('world', 'Python')

#결과
'Hello, Python!

#결과를 유지하고 싶을때.

s = 'Hello, world!'
s = s.replace('world!', 'Python')
s
'Hello, Python'

~~~

### 문자 바꾸기
<br>
<br>
문자열 안의 문자를 다른 문자로 바꾸는 메서드를 알아보자. 먼저 **str.maketrans('바꿀문자', '새문자')**로 변환 테이블을 만든다. 그다음에 **translate(테이블)**을 사용하면 문자를 바꾼 뒤 결과를 반환한다.

~~~python

table = str.maketrans('aeiou', '12345')
'apple'.translate(table)
'1ppl2'

~~~

**splite('기준이되는문자열')**과 같이 기준이되는 문자열을 지정하면 기준 문자열로 문자열을 분리한다.
문자열에서 각 단어가,(콤마)와 공백으로 구분되어 있을때', '으로 문자열을 분리하면 단어만 따로 리스트로 처리된다.

~~~python

'apple, pear, grape, pineapple, orange'.split(', ') #기준이 되는 문자열에 split(', ')
['apple', 'pear', 'grape', 'pineapple', 'orange']

~~~

### 구분자 문자열과 문자열 리스트 연결하기
<br>
<br>

**join(리스트)**를 사용하면 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만든다. 다음은 공백 ' '에 join을 사용하여 각 문자열 사이에 공백이 들어가게 만든다. 공백이 아닌 다른 문자를 사용하면 사용된 문자가 문자열 사이에 들어가게 된다.

~~~python

['apple', 'pear', 'grape', 'pineapple', 'orange']

' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
         
'apple pear grape pineapple orange'

# - 를 넣었을때.

'-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
'apple-pear-grape-pineapple-orange'

~~~

### 소문자를 대문자로 바꾸기
<br>
<br>

**바꾸고싶은 문자열.upper()**은 바꾸고싶은 문자열을 모두 대문자로 바꿔준다. 문자열에 이미 대문자가 있는경우 그대로 유지된다.


~~~python

'python'.upper()
'PYTHON'

~~~

### 대문자를 소문자로 바꾸기
<br>
<br>

**바꾸고싶은 문자열.lower()**은 바꾸고싶은 문자열을 모두 소문자로 바꿔준다. 문자열에 이미 소문자가 있는경우 그대로 유지된다.

~~~python

'PYTHON'.lower()
'python'

~~~

### 왼쪽 공백 삭제하기
<br>
<br>

**lstrip, rstrip, strip** 메서드는 공백을 삭제해야 할 경우가 사용된다. lstrip()은 문자열에서 왼쪽에 있는 연속된 모든 공백을 삭제한니다(l은 왼쪽(left)을 의미).

~~~python

'   Python   '.strip() #양쪽에 있는 모든 연속된 공백 삭제
         
'Python'

'   Python   '.lstrip() #왼쪽 공백 삭제
'Python   '

'   Python   '.rstrip() #오른쪽 공백 삭제
         
'   Python'

~~~

### 왼쪽의 특정 문자 삭제하기
<br>
<br>

**lstrip('삭제할문자들'), rstrip('삭제할문자들'), strip('삭제할문자들')**을 사용하면 해당 방향의 '삭제할 문자들에' 들어있는 문자열을 삭제한다.

~~~python

', python.'.lstrip(',.') #왼쪽에 있는 ',.'문자열 삭제
' python.'

', python.'.rstrip(',.') #오른쪽에 있는 ',.'문자열 삭제
', python' '

', python.'.strip(',.') #양쪽의 ',.'문자열 삭제
' python'

~~~

### 구두점을 간단하게 삭제하기
<br>
<br>
**punctuation**을 사용하면 문자열의 양쪽 모든 구두점을 삭제할 수 있다.

~~~python

import string
', python.'.strip(string.punctuation)
' python'
string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

~~~

공백까지 삭제하고자 한다면 string.punctuation에 공백 ' '을 연결해서 넣어주면 된다.
~~~python

', python.'.strip(string.punctuation + ' ')
'python'

~~~

### 문자열을 왼쪽 정렬하기
<br>
<br>

**ljust(길이)**는 문자열을 지정된 길이로 만든 뒤 왼쪽으로 정렬하며 남는 공간을 공백으로 채운다.<br>

**rjust(길이)**는 문자열을 지정된 길이로 만든 뒤 오른쪽으로 정렬하며 남는 공간을 공백으로 채운다.
<br>

**center(길이)**는 문자열을 지정된 길이로 만든 뒤 가운데로 정렬하며 남는 공간을 공백으로 채운다.
만약 남는 공간이 홀수이면 왼쪽에 공백이 한칸 더 들어간다.

~~~python

'python'.ljust(10) #python을 왼쪽으로 정렬하고 남는 공간을 공백처리
'python    '

'python'.rjust(10) #python을 오른으로 정렬하고 남는 공간을 공백처리
'    python'

'python'.center(10) ##python을 가운데 정렬하고 양쪽의 남는 공간을 공백처리
'  python  '

~~~


### 메서드 체이닝
<br>
<br>
메서드 체이닝은 메서드를 줄줄이 연결 한다고 해서 메서드 체이닝(method chaining)이라 부른다. 메서드를 계속 연결해 호출하는 메서드 체이닝을 알아보자. input().split()도 input()이 반환한 문자열에 split을 호출하는 메서드 체이닝이다. 아래 코드는 문자열을 지정된 길이인 10개로 만들고 오른쪽정렬과 대문자 처리를 해줬다.

~~~python

'python'.rjust(10).upper()
'    PYTHON'

~~~

### 문자열 왼쪽에 0 채우기
<br>
<br>

**zfill(길이)**를 사용하면 지정된 길이에 맞춰 문자열의 왼쪽에 0을 채운다( zero fill을 의미). 문자열의 길이가 지정된 길이보자 작다면 아무것도 채우지 않는다. 보통 zfill은 숫자를 일정 자릿수로 맞추고 앞자리는 0으로 채울 때 사용한다.

~~~python

'35'.zfill(4)        # 숫자 앞에 0을 채움
'0035'
'3.5'.zfill(6)       # 숫자 앞에 0을 채움
'0003.5'
'hello'.zfill(10)    # 문자열 앞에 0을 채울 수도 있음
'00000hello'

~~~

### 문자열 위치 찾기
<br>
<br>

**find('찾을문자열')**은 문자열에서 특정 문자열을 찾아서 인덱스를 반환하고, 문자열이 없으면 -1을 반환한다. find는 왼쪽부터 문자열을 찾고, 같은 문자열이 여러개일 경우 처음 찾은 문자열의 인덱스를 반환한다. 아래에서는 'pl'이 2개 있지만 왼쪽에서 처음 찾은 'pl'의 인덱스 2를 반환한다.
<br>

**rfind('찾을문자열')**은 오른쪽에서부터 특정 문자열을 찾아서 인덱스를 반환하고, 문자열이 없으면 -1을 반환한다. 같은 문자열이 여러개일 경우 처음 찾은 문자열의 인덱스를 반환한다. 아래에서는 'pl'이 2개 있지만 오른쪽에서 처음 찾은 'pl'의 인덱스 12를 반환한다.


~~~python

'apple pineapple'.find('pl') #찾는 문자열이 인덱스 2번위치부터 위치한다.
2
'apple pineapple'.find('xy') #찾는 문자열이 없기때문에 -1을 반환
-1

'apple pineapple'.rfind('pl') #찾는 문자열이 인덱스 12번위치부터 위치한다.
12
'apple pineapple'.rfind('xy') #찾는 문자열이 없기때문에 -1을 반환
-1

~~~

### 문자열 위치 찾기
<br>
<br>
find, rfind 이외에도 index, rindex로 문자열의 위치를 찾을 수 있다.<br>

**index('찾을문자열')**은 왼쪽에서부터 특정 문자열을 찾아서 인덱스를 반환한다. 단, 문자열이 없으면 에러를 발생시킨다. index도 같은 문자열이 여러 개일 경우 처음 찾은 문자열의 인덱스를 반환한다. 
**rindex('찾을문자열')**은 오른쪽에서부터 특정 문자열을 찾아서 인덱스를 반환한다(r은 오른쪽(right)을 의미). 마찬가지로 문자열이 없으면 에러를 발생시키며 같은 문자열이 여러 개일 경우 처음 찾은 문자열의 인덱스를 반환한다.


~~~python

'apple pineapple'.index('pl')
2
'apple pineapple'.rindex('pl')
12

~~~

### 문자열 개수 세기
<br>
<br>

**count('문자열')**은 현재 문자열에서 특정 문자열이 몇 번 나오는지 알아낸다. 여기서는 'pl'이 2번 나오므로 2가 반환된다.

~~~python

'apple pineapple'.count('pl')
2

~~~

---

## 2. 문자열 서식 지정자와 포매팅 사용하기
<br>
<br>
서식 지정자(format specifier)로 문자열을 만드는 방법과 format 메서드로 문자열을 만드는 문자열 포매팅(string formatting)에 대해 알아보자.<br>
예를들어 학생의 이름과 평균 점수를 출력한다고하자. 두 문자열에서 '의 평균 점수는', '점입니다.'는 같지만 이름과 점수가 다르다. 이렇게 문자열 안에서 특정 부분을 원하는 값으로 바꿀 때 서식 지정자 또는 문자열 포매팅을 사용한다.

~~~python

제임스의 평균 점수는 85.3점입니다.

~~~

학생이 바뀌면 이름과 점수 부분도 바뀌게 된다.

~~~python

마리아의 평균 점수는 98.7점입니다.

~~~


### 서식 지정자로 문자열 넣기
<br>
<br>
서식 지정자(format specifier)로 문자열 중간에 다른 문자열을 넣어보자.

- '%s' % '문자열'

서식 지정자는 %로 시작하고 자료형을 뜻하는 문자가 붙는다. %s는 문자열이라는 뜻이고 string의 s이다. 문자열 안에 %s를 넣고 그 뒤에 %를 붙인 뒤 'james'를 지정해주면 %s부분이 'james'로 바뀐다. 문자열이 아닌 변수를 지정할 수도 있다.

~~~python

'I am %s.' % 'james'
'I am james.'

name = 'maria'
'I am %s.' % name
'I am maria.'

~~~

### 서식 지정자로 숫자 넣기
<br>
<br>
서식 지정자로 숫자형을 넣는 방식이다.

- '%d' % 숫자

숫자는 %d를 넣고 % 뒤에 숫자를 지정하면 된다. %d는 10진 정수 decimal integer의 d이다.

~~~python

'I am %d years old.' % 20
'I am 20 years old.'

~~~


### 서식 지정자로 소수점 표현하기
<br>
<br>
서식 지정자로 실수를 넣는 방법이다.

- '%f' % 숫자

실수를 넣을 때는 %f를 사용하며 고정 소수점 fixed point의 f이다. %f는 기본적으로 소수점 이하 6자리까지 표시하므로 2.3은 2.300000으로 표시된다. 소수점 이하 자릿수를 지정하고 싶다면 다음과 같이 f 앞에 .(점)과 자릿수를 지정해주면 된다.

- '%.자릿수f' % 숫자

~~~python

'%f' % 2.3
'2.300000'


'%.2f' % 2.3 #소숫점 이하 2자리까지 표시
'2.30'
'%.3f' % 2.3 #소숫점 이하 3자리까지 표시
'2.300'

~~~

### 서식 지정자로 문자열 정렬하기
<br>
<br>

서식 지정자와 숫자를 조합하여 문자열을 정렬하는 방법이다. 다음과 같이 % 뒤에 숫자를 붙이면 문자열을 지정된 길이로 만든 뒤 오른쪽으로 정렬하고 남는 공간을 공백으로 채운다. %10s는 문자열의 길이를 10으로 만든 뒤 지정된 문자열을 넣고 오른쪽으로 정렬한다. 따라서 문자열 'python'은 길이가 6이므로 왼쪽 공간을 공백 4칸으로 채운다.

- %길이s

~~~python

'%10s' % 'python'
'    python'

~~~

왼쪽 정렬은 아래와 같다. %-10s는 문자열의 길이를 10으로 만든 뒤 지정된 문자열을 넣고 왼쪽으로 정렬한다. 따라서 문자열 'python'은 길이가 6이므로 오른쪽 공간을 공백 4칸으로 채운다.

- %-길이s

~~~python

'%-10s' % 'python'
'python    '

~~~

### 자릿수가 다른 숫자 출력하기
<br>
<br>

문자열 오른쪽 정렬은 자릿수가 다른 숫자를 출력할 때 유용하다. %d와 %f도 숫자와 조합하여 오른쪽으로 정렬할 수 있다.

- %길이d

~~~python

'%10d' % 150
'       150'
'%10d' % 15000
'     15000'

~~~

- 길이.자릿수f

~~~python

'%10.2f' % 2.3
'      2.30'
'%10.2f' % 2000.3
'   2000.30'

~~~

### 서식 지정자로 문자열 안에 값 여러 개 넣기
<br>
<br>

서식지정자로 문자열 안에 값을 여러개 넣는 방법이다. 

- '%d %s' % (숫자, '문자열')

문자열 안에 값을 두개 이상 넣으려면 %를 붙이고 괄호 안에 값또는 변수를 콤마로 구분해서 넣어주면 된다. 특히 값을 괄호로 묶지 않으면 에러가 발생하니 주의해야 한다. 이처럼 서식 지정자가 여러 개면 괄호 안의 값(변수) 개수도 서식 지정자 개수와 똑같이 맞춰주어야 한다.

~~~python

'Today is %d %s.' % (3, 'April')
'Today is 3 April.'

~~~

### format 메서드 사용하기
<br>
<br>

파이썬은 문자열을 만들 때 서식 지정자 방식보다 더 간단한 문자열 포매팅(string formatting)을 제공한다. 문자열 포매팅은 { }(중괄호) 안에 포매팅을 지정하고 format 메서드로 값을 넣는다.

- '{인덱스}'.format(값)


~~~python

'Hello, {0}'.format('world!')
'Hello, world!'
'Hello, {0}'.format(100)
'Hello, 100'

~~~

### format 메서드로 값을 여러 개 넣기
<br>
<br>

값을 여러개 넣으려면 인덱스 값을 지정하고 format에는 인덱스가 증가하는 순서대로 값을 넣으면 된다.

- '{인덱스}'.format(값)


~~~python
                                0       1       2
'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)
'Hello, Python 3.6 Script'

~~~

### format 메서드로 같은 값을 여러 개 넣기
<br>
<br>

특히 같은 인덱스가 지정된 { }를 여러 개 넣으면 같은 값이 여러 개 들어간다. 다음은 문자열에 'Python'이 두 개, 'Script'가 두 개 들어간다.


~~~python

'{0} {0} {1} {1}'.format('Python', 'Script')
'Python Python Script Script'

~~~

### format 메서드에서 인덱스 생략하기
<br>
<br>

만약 { }에서 인덱스를 생략하면 format에 지정한 순서대로 값이 들어간다.

~~~python

'Hello, {} {} {}'.format('Python', 'Script', 3.6)
'Hello, Python Script 3.6'

~~~

### format 메서드에서 인덱스 대신 이름 지정하기
<br>
<br>

{ }에 인덱스 대신 이름을 지정해 값을 할당할 수 있다.

~~~python

'Hello, {language} {version}'.format(language='Python', version=3.6)
'Hello, Python 3.6'

~~~

### 문자열 포매팅에 변수를 그대로 사용하기
<br>
<br>

파이썬 3.6부터는 변수에 값을 넣고 { }에 변수 이름을 지정해 변수를 그대로 사용할 수 있다. 이때 문자열 앞에 포매팅(formatting)이라는 뜻으로 f를 붙인다.

~~~python

language = 'Python'
version = 3.6
f'Hello, {language} {version}'
'Hello, Python 3.6'

# 중괄호 출력하기

'{\{ {0} }\}'.format('Python')
'{ Python }'

~~~

### format 메서드로 문자열 정렬하기
<br>
<br>

문자열 포매팅도 문자열을 정렬할 수 있다. 다음과 같이 인덱스 뒤에 :(콜론)을 붙이고 정렬할 방향과 길이를지정해준다. 

- '{인덱스:<길이}'.format(값)
'{0:<10}'은 부등호 방향이 왼쪽을 가리키고있다. 따라서 문자열을 지정된 길이로 만든 뒤 왼쪽으로 정렬하고 남는 공간을 공백으로 채운다.

~~~python

'{0:<10}'.format('python')
'python    '

~~~

다음과 같이 >을 넣어서 오른쪽을 가리키도록 만들면 문자열을 지정된 길이로 만든 뒤 오른쪽으로 정렬하고 남는 공간을 공백으로 채운다.

- '{인덱스:>길이}'.format(값)

~~~python

'{0:>10}'.format('python')
'    python'

~~~

인덱스를 사용하지 않는다면 :(콜론)과 정렬 방법만 지정해도 된다.

~~~python

'{:>10}'.format('python')
'    python'

~~~

### 숫자 개수 맞추기
<br>
<br>
d는 다음과 같이 %와 d 사이에 0과 숫자 개수를 넣어주면 자릿수에 맞춰서 앞에 0이 들어간다. 즉, %03d로 지정하면 1은 '001', 35는 '035'가 된다. { }를 사용할 때는 인덱스나 이름 뒤에 :(콜론)를 붙이고 03d처럼 0과 숫자 개수를 지정하면 된다.

- '%0개수d' % 숫자
- '{인덱스:0개수d'}'.format(숫자)

~~~python

'%03d' % 1
'001'
'{0:03d}'.format(35)
'035'

~~~

실수도 숫자 개수를 맞출 수 있다. 특히 소수점 이하 자릿수를 지정하고 싶으면 %08.2f처럼 .(점) 뒤에 자릿수를 지정헤준다. 여기서 주의할 점은 '%08.2f' % 3.6을 출력했을 때 '00003.60'이 나온다는 점이다. 실수는 숫자 개수에 정수 부분, 소수점, 소수점 이하 자릿수가 모두 포함된다. 따라서 '00003' 5개, '.' 1개, '60' 2개 총 8개가된다.

- '%0개수.자릿수f' % 숫자
- '{인덱스:0개수.자릿수f'}.format(숫자)

~~~python

'%08.2f' % 3.6
'00003.60'
'{0:08.2f}'.format(150.37)
'00150.37'
~~~

### 채우기와 정렬을 조합해서 사용하기
<br>
<br>
문자열 포매팅은 채우기와 정렬을 조합해서 사용할 수 있다. 다음과 같이 { }에 인덱스, 채우기, 정렬, 길이, 자릿수, 자료형 순으로 지정해 준다. 길이를 10으로 만들고 왼쪽, 오른쪽으로 정렬하고 남는 공간은 0으로 채워보자.

- '{인덱스:[[채우기]정렬][길이][.자릿수][자료형]}'

~~~python

'{0:0<10}'.format(15)    # 길이 10, 왼쪽으로 정렬하고 남는 공간은 0으로 채움
'1500000000'
'{0:0>10}'.format(15)    # 길이 10, 오른쪽으로 정렬하고 남는 공간은 0으로 채움
'0000000015'

~~~

실수로 만들고 싶다면 다음과 같이 소수점 자릿수와 실수 자료형 f를 지정해주면 된다.

~~~python

'{0:0>10.2f}'.format(15)    # 길이 10, 오른쪽으로 정렬하고 소수점 자릿수는 2자리
'0000015.00'

~~~

채우기 부분에 0이 아닌 다른 문자를 넣어도 된다. 공백을 넣어도 되고, 문자를 넣어도 된다. 채우기 부분을 생략하면 공백이 들어가게된다.

~~~python

'{0: >10}'.format(15)    # 남는 공간을 공백으로 채움
'        15'
'{0:>10}'.format(15)     # 채우기 부분을 생략하면 공백이 들어감
'        15'
'{0:x>10}'.format(15)    # 남는 공간을 문자 x로 채움
'xxxxxxxx15'

~~~

### 금액에서 천단위로 콤마 넣기
<br>
<br>
숫자 중에서 금액은 천단위로 콤마를 넣는다. 파이썬에서 간단하게 천단위로 콤마를 넣을수 있다. \ format 내장 함수를 사용하는 방법입니다. 다음과 같이 format 함수에 숫자와 ','를 넣어준다.

- format(숫자, ',')

~~~python

format(1493500, ',')
'1,493,500'

~~~

format 함수는 서식 지정자와 함께 사용할 수 있습니다. 다음은 콤마를 넣은 숫자를 오른쪽 정렬한다.

~~~python

'%20s' % format(1493500, ',')    # 길이 20, 오른쪽으로 정렬
'           1,493,500'

~~~

포매팅에서 콤마를 넣으려면 다음과 같이 :(콜론)뒤에 ,(콤마)를 지정하면 된다.

~~~python

'{0:,}'.format(1493500)
'1,493,500'

~~~

만약 정렬을 하고 싶다면 정렬 방향과 길이 뒤에 콤마를 지정해준다.

~~~python

 '{0:>20,}'.format(1493500)     # 길이 20, 오른쪽으로 정렬
'           1,493,500'
'{0:0>20,}'.format(1493500)    # 길이 20, 오른쪽으로 정렬하고 남는 공간은 0으로 채움
'000000000001,493,500'

~~~


### 예제1
<br>
<br>
표준 입력으로 문자열이 입력됩니다. 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 단, 모든 문자가 소문자인 'the'만 찾으면 되며 'them', 'there', 'their' 등은 포함하지 않아야 합니다.

~~~python

# 입력
the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.

#결과
6

~~~

내가 쓴답

~~~python

paragraph = str(input())
words = paragraph.split()
count = 0
for i in words:
    if i.strip(",.'") == 'the':
         count += 1
         
print(count)

~~~

### 예제2
<br>
<br>
표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 각 가격은 ;(세미콜론)으로 구분되어 있습니다. 입력된 가격을 높은 가격순으로 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 이때 가격은 길이를 9로 만든 뒤 오른쪽으로 정렬하고 천단위로 ,(콤마)를 넣으세요.

~~~python

# 입력
51900;83000;158000;367500;250000;59200;128500;1304000

#결과
1,304,000
  367,500
  250,000
  158,000
  128,500
   83,000
   59,200
   51,900

~~~

내가 쓴 답. 지저분하다.

~~~python

price = str(input())
x = price.replace(';',' ')
x = x.split()
x = list(map(int, x))
x = sorted(x, reverse = True)
for i in x:
    print('{0:>9,}'.format(i))

~~~

다른 방식

~~~python

price = list(map(int,input().split(';')))
price.sort(reverse=True) # 기존 리스트의 값들을 역순으로 정렬해준다
for i in price:
    print('{0:>9,}'.format(i))

~~~