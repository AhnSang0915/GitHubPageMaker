---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 함수지향 - arguments
date: 2022-03-13 22:10 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 함수지향 - arguments

## 1. arguments 소개
<br>
<br>
arguments객체는 배열과 유사하다. arguments는 함수안에서 사용할 수 있도록 그 이름이나 특성이 약속되어 있는 일종의 배열이다. 몇개의 인자가 들어올지 모를떄 인자를 정의하지 않고 그함수 안에 arguments를 사용하여 결과를 알아내면 되겠다.
<br>
<br>
아래의 예제는 매개변수가 없는 sum이라는 함수가 있다. javacsript는 관대한 언어이다. 매개변수가 없거나, 인자의 수와 매개변수의 수가 다르더라도 문제가 생기지 않는다.아래 for문에서의 arguments는 Javascript와 약속되어있는 특수한 이름의 변수명이다. arguments라는 배열이 담겨져 있다. 이 배열의 역할을 사용자가 전달한 인자(1,2,3,4)를 담는것이다. 그래서arguments.length는 4가되고 4만큼 for문이 반복되게된다. 
 document.write(i+' : '+arguments[i]+'<br />');는 0 : 1(인덱스0) 부터 차례로 표시하게되고, 그후 _sum의 변수에 +=(a+=1;는a=a+1;과 같다) arguments[i];를 담았다. 이말은 (1,2,3,4)의 값을 
_sum = _sum + arguments[i]이다. 즉, sum_에 1234를 차례로 더한다는 것이다. _sum의 초기값은 0이기 때문에 10이된다. 

~~~javascript
	
function sum(){
    var i, _sum = 0;     // i 루프를 위한 변수 _sum 출력할 결과를 담아낼 변수
    for(i = 0; i < arguments.length; i++){ 
      //arguments javascript와 약속되어있는 특수한 이름의 변수명
        document.write(i+' : '+arguments[i]+'<br />');
        _sum += arguments[i];
    }   
    return _sum;
}
document.write('result : ' + sum(1,2,3,4)); 

~~~


---

## 2. 매개변수의 수 - function length
<br>
<br>
함수명.length는 몇개의 매개변수를 갖고있는지 알려주고, arguments.length는 함수를 호출할때 몇개의 인자, 몇개의 arguments를 담고있는지의 정보를 담고있다.
<br>
<br>



~~~javascript

function zero(){
    console.log(
        'zero.length', zero.length,
        'arguments', arguments.length
    );
}
function one(arg1){
    console.log(
        'one.length', one.length,
        'arguments', arguments.length
    );
}
function two(arg1, arg2){
    console.log(
        'two.length', two.length,
        'arguments', arguments.length
    );
}
zero(); // zero.length 0 arguments 0 
one('val1', 'val2');  // one.length 1 arguments 2 
two('val1');  // two.length 2 arguments 1

~~~

