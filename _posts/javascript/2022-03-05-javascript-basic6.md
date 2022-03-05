---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 함수
date: 2022-03-05 15:05 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 함수

<br>
<br>
<br>

## 1. 함수란?
<br>
<br>
함수(function)란 javascript에서 기본적인 구성 블록중 하나로, 작업을 수행하거나 값을 계산하는 문장 집합같은 절차이다. 함수는 하나의 로직을 재실행 할 수 있도록 하는것으로 코드의 재사용성을 높여준다.
<br>
<br>

### 함수의 형식
<br>
<br>
함수(function)의 형식은 아래와같다. 

~~~javascript

function 함수명( [인자...[,인자]] ){
   코드 내용
   return 반환값
}
~~~

### 함수의 정의와 호출
<br>
<br>
함수(function) 뒤에 함수의 이름이 오고, 소괄호가 따라온다. 우리가 변수를 호출하려면 변수를 정의하고 값을할당한후 그 변수를 호출해야한다. 함수도 마찬가지로 함수를 정의했으면 정의한 함수를 호출해야한다. 변수는 변수 이름만으로 호출하지만 함수는 함수명 뒤 (); 를 붙여줘야한다. ();를 붙이지 않으면 javascript는 변수로 인식하기 때문에 꼭 써줘야한다.

~~~javascript

function numbering() {
    document.write(1);
}
numbering();

~~~

다음 예제를 보자. 이 함수의 이름은 numbering이고, 내용은 0부터 9까지를 화면에 출력한다.

~~~javascript

function numbering(){
    i = 0;
    while(i < 10){
        document.write(i);
        i += 1; // i = i + 1; 과 같다
    }   
}
numbering();

~~~


---

## 2. 함수의 효용성
<br>
<br>
만약 함수가 없이 0~9까지의 코드를 출력하려고 하려고 하면 아래와 같이 하면 될것이다.

~~~javascript

var i = 0
while(i < 10>){
    document.write(i);
    i +=1;
}

var i = 0
while(i < 10>){
    document.write(i);
    i +=1;
}
var i = 0
while(i < 10>){
    document.write(i);
    i +=1;
}
var i = 0
while(i < 10>){
    document.write(i);
    i +=1;
}
var i = 0
while(i < 10>){
    document.write(i);
    i +=1;
}

~~~
그런데 위의 코드를 0에서19까지로 바꿔야한다면 while(i < 10>) 부분을 while(i < 20>)으로 바꿔줘야 한다. 5번만 호출한다면 어렵지 않겠지만 많은 횟수를 호출하는 상황에선 어려운 작업이 될것이다. 이럴때 함수를 쓰면 1에서19까지를 1000번을 호출해도 아래와 같이 간단히 바꿀수 있다.

~~~javascript

funtion numbering() {
    while(i < 20>){
    document.write(i);
    i +=1;
}
for(var i = 1; i < 1000; i++){
    numbering();
}

~~~

물론 함수를 사용하지 않고 for문과 while로도 호출이 가능하다.

~~~javascript

for(var i = 1; i < 1000; i++){
    var i = 0;
    while(i < 20>){
        document.write(i);
        i +=1;
    }
}

~~~

위의 두코드의 차이점은 반복문은 반복문 안에서만 실행이 되고 함수는 다른 여러곳에서도 호출하여 사용할 수 있다는 점이다. 핵심은 재사용성이고 이말은 이 함수를 사용하고 있는 여러곳 에서 이함수의 내용을 변경, 개선한다고 하면 함수만 변경하면 사용하는 여러곳 에서 변경이되기 때문에 유지보수가 용이하게 된다. 

---

## 3. 함수의 입력과 출력
<br>
<br>
함수의 핵심은 입력과 출력이다. 입력된 값을 연산해서 출력하는 것이 함수의 기본적인 역할이다. 다음은 함수에서 입력과 출력의 역할을 하는 구문들에 대한 설명이다.

### 함수의 출력
<br>
<br>

#### return
<br>
<br>
함수 내에서 사용한 return은 return 뒤에 따라오는 값을 함수의 결과로 반환한다. 동시에 함수를 종료시킨다. 아래 내용을 보자. 결과는 egoing과 k8805다.

~~~javascript

function get_member1(){
    return 'egoing';
}
 
function get_member2(){
    return 'k8805';
}
 
alert(get_member1());
alert(get_member2());

~~~
아래 함수를 실행시켜보면 'egoing'만 출력하고 함수가 종료된다. return뒤의 내용은 출력하지 않는다.
~~~javascript

function get_member(){
    return 'egoing';
    return 'k8805';
    return 'sorialgi';
}
alert(get_member());

~~~

<br>
<br>

#### 인자
<br>
<br>
인자(argument)는 함수로 유입되는 입력 값을 의미하는데, 어떤 값을 인자로 전달하느냐에 따라서 함수가 반환하는 값이나 메소드의 동작방법을 다르게 할 수 있다. 다음 예를보자.<br>
앞에서본 함수와는 다르게 함수명 뒤에 1과 2가 들어가있다. 이말은 get_argument라는 함수를 호출할때 숫자 1과2를 넣어준다는 말이 된다. 숫자가 들어가는 arg는 변수가된다. arg=1, arg=2라는 뜻이 되는것이다. return이지만 2번을 호출했기 떄문에 1000,2000 의 값이 출력 된다.

~~~javascript

function get_argument(arg){ //arg는 매개변수 또는 parameter라고 부른다.
    return arg*1000;
}
 
alert(get_argument(1)); // 1과 2를 인자 argument라고 한다.
alert(get_argument(2));

~~~

<br>
<br>

#### 복수의 인자
<br>
<br>
인자를 여러개의 사용할수도 있다. 첫번째 두번째 인자가 차례로 arg1와 arg2로 들어가게 되고 30 , 50의 값이 출력 되게 된다.

~~~javascript

function get_arguments(arg1, arg2){
    return arg1 + arg2
}
 
alert(get_arguments(10, 20));
alert(get_arguments(20, 30));

~~~

---

## 4. 다양한 함수 정의 방법
<br>
<br>
함수를 정의하는 다른 방법을 알아보자.
<br>
<br>
우리가 위에서 작성한 함수와는 조금 다르다. function내의 함수 내용이 numbering이라는 변수에 대입되어 변수가 함수를 가지게 된것이다.

~~~javascript

var numbering = function (){
    i = 0;
    while(i < 10){
        document.write(i);
        i += 1;
    }   
}
numbering();

~~~
아래의 함수와 위의 함수는 같다.
~~~javascript

function numbering() {
    var i = 0;
    while(1 < 10) {
        document.write(i);
        i += i;
    }
}

~~~

아래 함수는 이름을 정하지도 않고 변수도 붙이지 않았다. 함수를 정의하고 함수를 괄호로 묶었다. 그다음에 호출할때 사용하는 기호 ();로 호출하게 되면 정의와 호출을 하나의 문장으로 같이하는 함수로 <u>익명함수</u>라고 한다. 일회 성으로 호출할때 이런 함수를 사용한다.

~~~javascript

(function(){
    i = 0;
    while(i < 10){
        document.write(i);
        i += 1;
    }   
}) ();

~~~