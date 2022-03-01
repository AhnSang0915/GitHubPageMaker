---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript - 숫자와 문자
date: 2022-03-01 21:06 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 숫자와 문자

<br>
<br>
<br>

## 1. 수의 표현
<br>
<br> 
javascript는 큰따옴표나 작은 따옴표가 붙지 않은 숫자는 숫자로 인식한다.
<br>
정수, 자연수, 실수 모두 사용가능하고 모두 숫자로 인식한다.
<br>
javascript에선 포괄적으로 number라고 부르고 다른 프로그래밍 언어들 보다 덜 엄격한 편이다.
<br>
수식으로는 더하기는 + 빼기는 - 나누기는 / 곱셈은 * 으로 표현한다.
<br>

---

## 2. 수의 연산
<br>
<br>
javascript는 계산 기능이 있는데 우리가 흔히 쓰는 수식과는 조금 다르기 때문에 그 방법을 알아두는게 좋겠다.
<br>
<br>
아래 코드에 아직 배우지 않은 부분이 있는데 뒤에서 자세히 배워볼 예정이다.
<br>
<br>

~~~javascript

Math.pow(3,2);       // 9,   3의 2승 
Math.round(10.6);    // 11,  10.6을 반올림
Math.ceil(10.2);     // 11,  10.2를 올림
Math.floor(10.6);    // 10,  10.6을 내림
Math.sqrt(9);        // 3,   3의 제곱근
Math.random();       // 0부터 1.0 사이의 랜덤한 숫자

~~~

---

## 3. 문자
<br>
<br>

"",''내에 들어가는 내용은 javascript가 문자로 인식한다.<br>
데이터를 입력하면 javascript는 문자와 숫자를 인식하게 된다.<br>
숫자를 "A"나 'A'로 감싸면 문자로 인식하게 된다.<br>
우리가 작성한 데이터 값은 typeof 라는 명령을 사용하면 데이터의 형식을 알수있다.<br>
문자는 string 숫자는 number라는 결과가 나온다.<br>


~~~javascript
alert(typeof "1") //결과 : string 
~~~

<u>"내용' 이런식의 기입은 할수 없음을 알아두자.</u>
<br>
여러줄로 표시하기 위해서는 \n을 사용할 수 있다.<br>

~~~javascript

alert("왔냐.\n 코딩 연습장이다")

~~~

또한 데이터를 입력하다 보면 '이나 " ex)alert('egoing's coding everyday') 등을 사용 해야할 때가 이있는데 이럴땐 \뒤에 해당 기호를 넣어 문자로 인식하게 할수 있다.

~~~javascript

alert("egoing's coding everyday") // ""사이에 '가 들어 있기 때문에 사용 가능하다.

arlert('egoing\'s coding everyday')// 역슬래쉬 \뒤의 어떠한 기호는 문자로 해석된다. escape라고 한다.

~~~


---

## 4. 문자의 연산

<br>
<br>

1+1은 2이다 하지만 "1"+"1"은 "11"이된다. 숫자와 문자의 연산은 전혀 다르다.
문자를 더하는 표현은 아래와 같다.


~~~javascript

alert("Ahns"+" Coding Gym") //결과 : Ahns Coding Gym

~~~


문자의 길이를 구할때는 문자 뒤에 .length를 붙여준다.


~~~javascript

alert("Ahns Coding Gym".length) //결과 : 15 
~~~