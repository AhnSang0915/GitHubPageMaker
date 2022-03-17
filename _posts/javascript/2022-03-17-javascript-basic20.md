---
layout: post
current: post
cover:  assets/built/images/javascript-logo.png
navigation: True
title: Javascript - JavaScript 객체지향 - this
date: 2022-03-17 22:10 +0900
tags: [javascript]
class: post-template
subclass: 'post tag-javascript'
author: AhnSang0915
---

# JavaScript 객체지향 - this

## 1. 함수와 this
<br>
<br>
this는 함수 내에서 함수 호출 맥락(context 어떠한 의미가 고정되어 있지 않고 사용되는 상황에따라 그의미가 달라질 수 있따.)를 의미한다. 맥락이라는 것은 상황에 따라서 달라진다는 의미인데 즉 함수를 어떻게 호출하느냐에 따라서 this가 가리키는 대상이 달라진다는 뜻이다. 함수와 객체의 관계가 느슨한 자바스크립트에서 this는 이 둘을 연결시켜주는 실질적인 연결점의 역할을 한다.
<br>
<br>
아래 코드는 조건문에서 window(전역객체)와 함수안에서의 this가 정확하게 일치한다면 window === this를 출력하는 코드이다. 개발자 도구 콘솔에서 실행시 아래와 같이 나온다. 아래 예제처럼 함수안에서의 this는 전역객체를 의미하는 window를 의미하는 것이다.

~~~javascript

function func(){
    if(window === this){
        console.log("window === this");
    }
}
undefined
func();
// window === this

~~~


---

## 2. 메소드와 this
<br>
<br>
객체의 소속인 메소드의 this는 그 객체를 가르킨다.
<br>
 o라고 하는 변수에 객체를 정의해서 할당했다. 그객체엔 func라는 프로퍼티가 있고 함수이기 때문에 메소드 이다. 함수의 내용은 변수o와 this가 정확하게 같다면 o === this를 출력하는 함수이다. 출력값은 o === this 이다.

~~~javascript

var o = {
    func : function(){
        if(o === this){
            document.write("o === this");
        }
    }
}
o.func();   


~~~

## 3. 생성자 this
<br>
<br>
아래 코드는 함수를 호출했을 때와 new를 이용해서 생성자를 호출했을 때의 차이를 보여준다.<br>
function Func()의 funcThis = this;는 지역변수로 지정하지 않았기 때문에 전역변수인 funcThis의 값이 this가 된다. 그렇기 때문에 if(function === window)는 true가 된다. 이말은 우리가 함수와 this에서 본 예제와 같이 함수안에서의 this는 전역객체 window를 의미하는 것이다. 
<br>
그아래 var o2 = new Func();는 new를 사용해 javascript내부적으로 비어있는 객체를 만들었다. 그비어있는 객체는 o2가된다. 그리고 var o2 = new Func();를 실행하면 생성자 function Func()가 실행이되고 this의 값이 funcThis가 되고 그값은 var = funcThis가 된다. 자 정리하자. 우리가 new생성자를 통해 o2에 빈객체를 만들었고 그 new생성자는 function Func(){funcThis = this;}이고 여기서의 funcThis는 var funcThis를 의미한다. 즉 우리가 생성자를 통해 만든 객체는 o2에 들어있고 그 생성자가 가르키는것이 var funcThis이기 때문에 if(funcThis === o2)는 true가 된다. 이것을 통해 알수 있는것은 생성자의 맥락으로, 똑같은 함수지만 생성자로 사용될 때에는 this의 값이 생성될 객체를 의미한다.


~~~javascript

var funcThis = null; 
 
function Func(){
    funcThis = this;
}
var o1 = Func();
if(funcThis === window){
    document.write('window <br />');
}
 
var o2 = new Func();
if(funcThis === o2){
    document.write('o2 <br />');
}

~~~

위의 예제를 조금 바꿔봤다. if(o2 === this); 를 추가했는데 이렇게 되면 문제가 있다. 우리가 생성자를 호출하게 되면 생성자에대한 호출이 모두 끝나고난 뒤에 그때 비로소 o2라고하는 변수에 우리가 생성한 객체가 할당이 된다. 그전에 객체는 만들어져 있지만 o2라는 변수에 할당되어 있지 않기 때문에 우리는 객체를 할당할수 없다. 따라서 생성자 안에서 o2라는 변수와 this를 확인하면 o2라는 변수에 객체가 담겨있지 않기때문에 undefined이다. this라고 하는것은 객체에대한 초기화가 끝나서

~~~javascript

var funcThis = null; 
 
function Func(){
    if(o2 === this);
}
var o2 = new Func();
if(funcThis === o2){
    document.write('o2 <br />');
}
//undefined

~~~


---

## 4. 객체로서의 함수
<br>
<br>
이번엔 javascript가 얼마나 유연한지 극명하게 보여주는 주제를 알아보자.
<br>
아래 예제는 개발자도구에 입력한 내용이다. function sum(x,y) {return x+y;}는 sum이라고하는 함수 객체를 만든것이다. 그런데 우리가 new Function('x','y','return x+y;');로 함수객체를 만드는것은 함수의 본문이 복잡하면 굉장히 힘들다. 그래서 함수를 쉽게작성할 수 있도록 function sum(x,y) {return x+y;} 이런식으로 작성하면 javascript해석기는 함수객체를 만들어주고 이런식의 작성을 함수 리터럴(literal)이라고 한다. 그리고 객체를 만들때  var a = {} 이런식으로 만드는것을 객체 리터럴, var a = []; 이런식을 배열 리터럴이라고 한다. 우리가 명시적으로  new Object, new array등으로 만들수도 있지만 보다 편리하게 어떤 값을 만들수있도록 해주는 처리를 리터럴(literal)이라고 한다.


~~~javascript

function sum(x,y) { 
    return x+y;}
undefined
sum(1,2);
3
var sum2 = new Function('x','y','return x+y;'); // new를 통해서 function이라고하는 생성자함수를 호출한것이다. 앞의 두'x','y',는 함수를 정의할때 매개변수를 정의하는것과 같은 의미이고 마지막 'return x+y;' 가 본문{}에 해당되는 것이다.
undefined
sum2(1,2);
3

~~~

---

## 5. apply와this
<br>
<br>
함수가 가지고있는 프로퍼티중에 EcamaScript에서 정의하고있는 메소드중의 하나가 apply와 call이다.
<br>
<br>
switch는 괄호안의 어떤값이 들어가면 값과 같은 케이스 안에들어있는 구간이 break를 만날때까지 실행된다. if문과 대체제의 관계에 있고 이것은 for문과 while문이 대체제역할에 있는것과 같다.
<br>
<br>
함수를 apply를이용해 호출했을때 내부적으로 this의 값은 어떻게 변경되는지 알아보자. func();를 호출하게 되면 함수에서의 this의 값은 전역객체window를 의미하기 때문에 window를 실행하게 된다. func.apply(o);는 객체이기 때문에 프로퍼티를 가지고 있을수 있고 Ecmascript의 스펙으로 정의되어 있는 표준 메소드인 apply를 가지고있다. apply를 호출할때 첫번째 인자로 함수호출 컨테스트 o를 주게되면 func()함수가 실행되게 되면서 this의값이 o가된다. 그래서 o를실행하고 braek가되어 값을 반환하게된다. func.apply(p);도 마찬가지로 p를 반환할 것이다.

~~~javascript

var o = {}
var p = {}
function func(){
    switch(this){
        case o:
            document.write('o<br />');
            break;
        case p:
            document.write('p<br />');
            break;
        case window:
            document.write('window<br />');
            break;          
    }
}
func();
func.apply(o);
func.apply(p);

~~~

window, o, p라는 객체와 함수가 있었다. 함수를 어떻게 호출하느냐에 따라 즉 맥락에 따라 window에 소속되기도 하고 o와 p에 소속되기도 했다.