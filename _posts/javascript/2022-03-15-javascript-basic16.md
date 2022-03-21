---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 함수지향 - 함수의 호출
date: 2022-03-15 21:39 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---
{% include javascript-table-of-contents.html %}


# JavaScript 함수지향 - 함수의 호출

<br>
<br>

---

## 1. apply 소개
<br>
<br>
Javascript에서 함수는 일종의 객체이다. 객체는 속성을 갖고있고 그 속성의 값을 가지고있으면 속성(property)라고 부르고 함수를 갖고있다면 메소드(method)라고 부른다.

~~~javascript
	
function func(){ 
}
func();
//func라는 함수는 객체이고 메소드를 갖고있다. func.apply func.call이라는 메소드에 접근할수 있다. 이것들이 하는역할은 func라는 객체를 호출하는 역할을 한다.

~~~

아래는 크롬 개발자 도구에서 실행한 코드이다. sum함수를 정의하고  arg1,arg2의 인자를 갖고있다. 여기서 특이한점은 sum(1,2), sum(4,2)를 실행한 결과와 sum.apply(null, \[1,2]); sum.apply(null, \[4,2]);를 한결과가 같다 이말은 .apply에 두번째 인자로 배열을 넣은 값들이 arg1, arg2가 되었다는 말이다. 다음 주제에서 왜 이렇게 복잡한 방법으로 함수를 호출하는지 그 이유를 배워보자.


~~~javascript
	
function sum(arg1, arg2) {
    return arg1+arg2 ; }
undefined
sum(1,2);
3
sum(4,2);
6
sum.apply
ƒ apply() { [native code] } // apply라고 하는 메소드가 브라우저에서 제공하는 메소드이기때문에 코드를 보여줄수 없다는 말이다. 내장된 코드는 네이티브 코드라는 메세지를 보여주게 되어있다.
sum.apply(null, [1,2]);
3
sum.apply(null, [4,2]);
6

~~~

---

## 2. apply 사용
<br>
<br>
apply를 사용하는 구체적인 이유를 알아보자. 우선 아래 코드는 함수를 정의하고 있다. _sum이라는 변수를 0으로 초기화 시켰고, for in 문으로 this라는 객체에 담겨있는 값들을 하나씩 꺼내 _sum이라는 지역변수에 하나씩 더해 바깥으로 리턴해주고있다. this가 무엇인지는 javascript에서 상당히 중요하다. 이맥락에서 this가 무엇인지는 정해져 있지 않다. 이전의 예제와는 다르게 sum.apply(o1), 그리고 o2를 주었다. 이말은 sum이라는 메소드를 호출할때의 대상을 o1, o2로 준것이다. sum.apply(o1)을 하게되면 o1이 sum이라고 하는 함수의 this가 된다. 독립되어있는 함수가 sum.apply를 하고 o1, o2를 인자로 전달하게되면 o1.sum, o2.sum이라는 메소드가 된다는 것이다.


~~~javascript

o1 = {val1:1, val2:2, val3:3}
o2 = {v1:10, v2:50, v3:100, v4:25}
function sum(){ // sum.apply(o1)을 하게되면 var this = o1; 이되는거라고 생각하자.
    var _sum = 0; 
    for(name in this){ //이 맥락에서 this는 정해져 있지 않다.
        _sum += this[name];
    }
    return _sum;
}
alert(sum.apply(o1)) // 6
alert(sum.apply(o2)) // 185

~~~

위 코드를 aaply를 사용하지 않으면 아래 코드처럼 될것이다. 이렇게 작성하고 출력하게 되면 6과 185이후에 sum함수의 내용도 같이 출력이 된다. 우리가 sum이라는 함수를 o1, o2의 속성으로 추가했기 때문이다.<br> sum : sum 의 왼쪽 sum은 o1, o2 객체의 속성(property)명이 되고 오른쪽 sum은 미리 만들어놓은 함수(function) sum이다. 그리고 객체를 호출하는데 객체의 접근방법은 속성명[property 또는 키값], 속성명.property 또는 키값으로 호출할수 있지만, 메서드의 경우 속성명.메소드명()로 접근한다. 따라서 o1.sum(),
o2.sum()로 호출하고 이렇게 호출하면 for in문이 this를 열거하는 과정에서 sum이라는 함수도 더하고 있기때문에 숫자열을 더하고 문자열까지 더해 출력하게 되는것이다. 

~~~javascript

function sum(){
    var _sum = 0;
    for(name in this){ 
        _sum += this[name];
    }
    return _sum;
}
o1 = {val1:1, val2:2, val3:3, sum:sum}
o2 = {v1:10, v2:50, v3:100, v4:25, sum:sum}
alert(o1.sum());
alert(o2.sum());

~~~

위 출력에서 함수내용을 출력하지 않으려면  if(typeof this\[name] !=== 'function' )를 사용해 출력에 제한을 주면 되겠다. 조건문을 사용해 typeof로 함수와 같지 않은경우만 더할것이라고 추가하면 함수의 차례가 오면 그부분을 스킵할 수 있게된다.

~~~javascript

function sum(){
    var _sum = 0;
    for(name in this){
        if(typeof this[name] !=== 'function' )
        _sum += this[name];
    }
    return _sum;
}
o1 = {val1:1, val2:2, val3:3, sum:sum}
o2 = {v1:10, v2:50, v3:100, v4:25, sum:sum}
alert(o1.sum());
alert(o2.sum());

~~~

물론 위의 방법대로 해도 사용할 수 있겠지만 복잡하기 때문에 apply를 사용하게되면 함수가 호출되는 시점에서 this값을 프로그래밍적으로 변경해 함수가 o1이라는 객체의 속성인것처럼 실행되게 할수있다.