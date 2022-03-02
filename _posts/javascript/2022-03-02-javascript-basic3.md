---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 변수, 비교
date: 2022-03-02 19:58 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 변수, 비교

<br>
<br>
<br>

# 변수

<br>
<br>

## 1. 변수의 사용법
<br>
<br>
변수(Variable)는 문자나 숫자같은 값을 담는 컨테이너로 값을 유지할 필요가 있을때 사용한다. 담겨진 값은 다른 값으로 바꿀수 있고 var로 변수를 선언할수 있다. 생략도 가능하지만 var의 의미를 명확하게 이해하기 전에는 var를 사용하는 것이 좋겠다. 예제를 보자.
<br>
<br>

~~~javascript

var a = 1;
alert(a+1);  //2
 
var a = 2;
alert(a+1);  //3

~~~
~~~javascript

var first = "coding";
alert(first+" everybody"); //coding everyday

~~~
~~~javascript

//변수 a에 coding ,변수 b에 everybody를 활당하는 방법은 아래와 같다.
var a = 'coding', b = 'everybody';
alert(a);
alert(b);
~~~
---

## 2. 변수의 효용
<br>
<br>
변수는 코드의 재활용성을 높여준다. 반복해서 100에서 10을 빼고 더하고 나누는 계산을 해야하는 코드가 있다고 가정해보고 변수가 없다면 100에관한 숫자 데이터를 모두 수정해야 할것이다. 여기서 변수를 적용하면 변수 값만 바꿔주면 된다.
<br>

~~~javascript

//변수를 쓰기 전

alert(100+10);
alert((100+10)/10);
alert(((100+10)/10)-10);
alert((((100+10)/10)-10)*10);

// 변수 사용 후

a = 100; //변할수 있는
a = a + 10; //변하지 않는
alert(a);
a = a / 10;
alert(a);
a = a - 10;
alert(a);
a = a * 10;      
alert(a);
~~~

변수를 쓰지 않은 코드보다 쓴 코드가 더 길기때문에 비효율 적으로 보일수 있으나 코드가 천줄 만줄이라고 생각하면 변수를 쓰는게 좋을것이다.<br>
코딩을 할때 위의 주석처럼 구획을 나누어 놓는게 좋다. 변할수 있는 부분이 군데군데 들어가 있다면 그것을 찾아서 수정해야한다. 그럴경우 유지보수가 힘들어진다.

---

# 비교

<br>
<br>


## 1.연산자
<br>
<br>

비교는 조건문을 쓸때 꼭 필요하다. 비교 기능 자체는 효용이 크지 않지만 조건문을 사용하기 위해 꼭 필요하다.<br>
연산자란 간단하게 말해 = 이다. 변수에 값을 대입할때 사용한다.

~~~javascript
a=1 //변수 대입연산자 값
~~~

---

## 2. 비교 연산자 (==과===)

<br>
<br>

비교 연산자는 말그대로 비교하고 판별할때 사용한다. 좌항과 우항중 뭐가 작고 큰지 또는 같은지 등을 판별한다. 비교연산자의 결과는 true나 false둘중 하나다. true와 false형식을 블린 데이터라고 부르고 역시 조건문에서 중요하게 사용한다.

<u>==</u> <br>
==는 동등연산자로 좌항과 우항의 값이 같다면 true 다르다면 false가 된다.=와 ==는 전혀 다르기 때문에 주의해야한다.

~~~javascript

alert(A==B)             //false
alert(A==A)             //true
alert("one"=="two")     //false 
alert("one"=="one")     //true

~~~

<u>===</u> <br>
=== 일치 연산자라고 하고 좌항과 우항이 정확하게 같을때 같다면 true 다르다면 false가 된다. 여기서 정확하게는 아래 코드처럼 형식까지 일치해야 한다는 말이다. 1과 '1'은 숫자와 숫자를 문자화시킨 데이터이다. 결론은 ==보다 ===를 쓰는것이 좋겠다.

~~~javascript

alert(1=='1');              //true
alert(1==='1');             //false

~~~

---

## 3.===를 사용하자
<br>
<br>
null과 undefined는 값이 없다는 의미의 데이터 형이다. var a; 라는 코드를 쓰고 alert(a); 를 하면 undefined라는 경고창이 나온다. 값이 정의되지 않았다는 뜻이다. 그리고 var a=null; alert(a);를 하면null이라는 경고창이 나온다. 이말은 작성한사람이 의도적으로 값이 없다는것을 지정한것이다.
이말은 프로그래밍에서 의도한것과 의도하지 않은것은 전혀 다른것이다. 

~~~javascript

alert(null == undefined);       //true
alert(null === undefined);      //false
alert(true == 1);               //true
alert(true === 1);              //false
alert(true == '1');             //true
alert(true === '1');            //false
 
alert(0 === -0);                //true
alert(NaN === NaN);             //false NaN(Not-a-Number)은 이값은 숫자가 아님을 의미한다.
                   //그래서 NaN생성의 가능성이 있는 코드는 비교 연산을 실행하면 안되겠다.

~~~

---

## 4.부정과 부등호

<br>
<br>

### !=

!는 부정을 의미한다. 1==2는 false다 하지만 1!=2는 true가 된다. 같지 않은게 사실이기 때문이다.

~~~javascript

alert(1!=2);            //true
alert(1!=1);            //false
alert("one"!="two");    //true
alert("one"!="one");    //false

~~~

### !==
!==는 ===에 부정을 부여한 것으로 정확하게 같지 않다는 의미이다.

<br>
<br>

### >
좌항과 우항을 비교해주는 연산자로 좌항이 더 크다는것을 의미한다. 더크면 true 작으면 false이다.<br>
<는 반대의 의미이다.

~~~javascript

alert(10>20);   //false
alert(10>1);    //true
alert(10>10);   //false
~~~

### >=

좌항이 우항보다 크거나 같다는 의미이다. <=는 반대의 의미이고 =>, =<식의 표현은 불가하다.

~~~javascript

alert(10>=20);      //false
alert(10>=1);       //true
alert(10>=10);      //true
~~~
