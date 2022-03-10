---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 함수지향 - 유효범위
date: 2022-03-11 01:20 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 함수지향 - 유효범위

<br>
<br>


---

## 1. 전역변수와 지역변수
<br>
<br>
유효범위(Scope)는 변수의 수명을 의미한다. 아래의 예제를 보자. vscope라는 변수에 global이라는 데이터를 할당했다. fscope라는 함수는 함수 안에 선언되어 있지 않은, 함수 바깥쪽에 선언되어있는 vscope에 접근할 수 있다. 결과는 global이다. 

~~~javascript

var vscope = 'global';
function fscope(){
    alert(vscope);
}
fscope();

~~~

아래를 실행하게 되면 결과는 '함수안 local'과 '함수밖 global'이 출력된다. fscope 함수안에 vscope라는 변수가 할당되어 있기 때문에 vscope는 자기자신과 가까이에 있는 vscope를 가르키기 때문에 'local'이라는 값을 출력하게 된다. 함수안의 fscope 함수안에 정의 되어 있는 vscope는 지역변수(local variables) 이고, 함수밖에  정의되어 있는 vscope변수는 전역변수(global variables)라고 한다.즉 지역변수의 유효범위는 함수 안이고, 전역변수의 유효범위는 에플리케이션 전역인데, 같은 이름의 지역변수와 전역변수가 동시에 정의되어 있다면 지역변수가 우선한다는 것을 알 수 있다.

~~~javascript

var vscope = 'global';
function fscope(){
    var vscope = 'local';
    alert('함수안 '+vscope);
}
fscope();
alert('함수밖 '+vscope);

~~~

var을 쓴것과 쓰지않은것의 차이점을 알아보자. var을쓰면 전역변수를 호출하게되고 var을 쓰지않으면 vscope가 지역변수가 되어 global을 local로 변경하게된다. 즉,  var을 사용하지 않은 지역변수는 전역변수가 된다. fscope라는 함수에 var쓰고 변수를 지정하게 되면 fscope함수에 지역변수를 지정한것이다. 그렇기 때문에 전역 변수의 값이 local로 변경 된 것이다. 그렇기 때문에 출력은 local이 되게 된다.

~~~javascript

var vscope = 'global';
function fscope(){
    var vscope = 'local';
   
}
fscope();
alert(vscope);
// var을 쓸때 global
// var을 쓰지 않을때 local
~~~

아래 예제는 어떻게 될까? 마찬가지로 global을 출력하게 된다. 이유는 이미 var vscope으로 인해 지역변수가 생성이되었다. 그렇기 때문에 vscope를 사용해도 지역변수가 되는것이지 전역변수가 변경되지는 않는다.

~~~javascript

var vscope = 'global';
function fscope(){
    var vscope = 'local';
    vscope = 'local';   
}
fscope();
alert(vscope);
// global

~~~

---

## 2. 유효범위의 효용
<br>
<br>
아래 두개의 예제는 변수 i를 지역변수로 사용했을 때와 전역변수로 사용했을 때의 차이점을 보여준다. 전역변수는 각기 다른 로직에서 사용하는 같은 이름의 변수값을 변경시켜서 의도하지 않은 문제를 발생시킨다.
<br>
<br>
같은 이름을 사용했지만 var을 사용하는것과 사용하지 않는것의 차이가 있다. for문 안에들어있는 i의 값이 선언된것은 어떤 함수에 소속되지 않은 것이다. 그렇기 때문에 전역변수이고 함수 a를 호출하게 되면 변수 i의 값을 0으로 바꿔주고 있다. 그런데 var을 붙이지 않은것은 전역변수를 의미하게 된다. a함수와 for문이 가르키고 있는 i가 같기때문에 a가 실행될때마다 i의값이 매번 0으로 초기화된다. 따라서 무한반복하는 현상이 나타나고 같은이름의 변수를 중복해서 사용했지만 각각의 취지가 다를 때 이런현상이 일어난다.

~~~javascript

function a (){
    var i = 0; //결과 01234
    // i=0; // 결과 무한반복
}
for(var i = 0; i < 5; i++){
    a();
    document.write(i);
}

~~~

---

## 3. 전역변수를 사용하는 법
<br>
<br>
불가피하게 전역변수를 사용해야 하는 경우는 하나의 객체를 전역변수로 만들고 객체의 속성으로 변수를 관리하는 방법을 사용한다.

<br>
<br>
아래의 예제는 MYAPP이라는 전역변수 하나를 만들어서 속성을 지정해 만들었다. 이처럼 전역변수 하나만을 만들고 나머지 다른 전역변수들은 바로 그 전역변수의 소속에 해당되게 만들면 변수의 이름이 충돌할 가능성이 낮아진다.


~~~javascript

var MYAPP = {}
MYAPP.calculator = { //calculator 속성
    'left' : null,
    'right' : null
}
MYAPP.coordinate = {
    'left' : null,
    'right' : null
}
 
MYAPP.calculator.left = 10;
MYAPP.calculator.right = 20;
function sum(){
    return MYAPP.calculator.left + MYAPP.calculator.right;
}
document.write(sum());

~~~

아래의 예제는 함수안에 변수를 지정해 함수의 지역변수로 만들었다. 함수를 정의하고 바로 호출하는 기법을 익명함수라고 한다. 이러한 기법을 이용해 전역변수가 하나도 존재하지않는 방식을 사용할 수도있다.

~~~javascript

(function(){
    var MYAPP = {}
    MYAPP.calculator = {
        'left' : null,
        'right' : null
    }
    MYAPP.coordinate = {
        'left' : null,
        'right' : null
    }
    MYAPP.calculator.left = 10;
    MYAPP.calculator.right = 20;
    function sum(){
        return MYAPP.calculator.left + MYAPP.calculator.right;
    }
    document.write(sum());
}())

~~~

---


## 4. 유효범위의 대상
<br>
<br>
Javascript는 함수에 대한 유효범위만을 제공한다. 다시말해 Javascript 에선 for문이나 if문에서 중괄호 안에서 선언된 변수는 지역변수로서의 의미를 갖지 않는다. 많은 언어들이 블록(대체로 {,})에 대한 유효범위를 제공하는 것과 다른 점이다. 아래 예제의 결과는 coding everybody이다.

~~~javascript

for(var i = 0; i < 1; i++){
    var name = 'coding everybody';
}
alert(name);

~~~

자바에서는 아래의 코드는 허용되지 않는다. name은 지역변수로 for 문 안에서 선언 되었는데 이를 for문 밖에서 호출하고 있기 때문이다.


~~~javascript

for(int i = 0; i < 10; i++){
    String name = "egoing";
}
System.out.println(name);

~~~

---


## 5. 정적 유효범위
<br>
<br>
자바스크립트는 함수가 선언된 시점에서의 유효범위를 갖는다. 이러한 유효범위의 방식을 정적 유효범위(static scoping), 혹은 렉시컬(lexical scoping)이라고 한다. 이는 이후에 살펴볼 클로저와 연관되어 있다.
<br>
<br>
전역변수 var i = 5가 정의되어 있고 a 함수는 var i = 10이라는 지역변수를 정의하고 있다. a라고 하는 함수를 호출했을 때 함수의 내부적으로 i의 값이 10이 된다. 그 상태에서 b를 호출하게 되면 i는 b 함수 안에 i라고 하는 지역변수가 존재하는지 찾게 된다. 없다면 전역변수를 찾게 되는데 b를 호출하고 있는 함수는 a이다.그렇다면 a 함수에 정의된 변수 a를 호출하게 될까? 아니다. 왜냐하면, 함수 b가 선언된 시점에서 i의 전역변수가 사용되는 것이지 b가 호출된 시점에서 b가 담겨있는 함수의 지역변수가 사용되는 것이 아니다. 즉, 사용될 때 가 아니고 정의 될 때의 전역변수가 사용되게 된다는 말이다. 이러한 것을 정적 유효범위 또는 렉시컬(lexical scoping)유효범위라고 한다.

~~~javascript

var i = 5; // 전역변수
 
function a(){
    var i = 10; // 지역변수
    b();
}
 
function b(){
    document.write(i);
}
 
a();
 // 5
~~~

